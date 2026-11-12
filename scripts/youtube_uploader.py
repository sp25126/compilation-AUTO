import argparse
import os
import sys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Required scopes for uploading and managing YouTube videos
SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]


def get_authenticated_service(client_secrets_file: str = "client_secrets.json", token_file: str = "token.json"):
    creds = None
    if os.path.exists(token_file):
        try:
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        except Exception as e:
            print(f"[YouTube Uploader] Warning: Could not load token file: {e}", file=sys.stderr)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(client_secrets_file):
                raise FileNotFoundError(
                    f"Client secrets file '{client_secrets_file}' not found. Please place your Google OAuth credentials there."
                )
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_file, "w", encoding="utf-8") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)


def upload_video(
    file_path: str,
    title: str,
    description: str,
    tags: list[str],
    publish_at: str | None = None,
):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Video file not found: {file_path}")

    youtube = get_authenticated_service()

    # Determine privacy and schedule
    if publish_at:
        privacy_status = "private"
        status_body = {
            "privacyStatus": privacy_status,
            "publishAt": publish_at,
            "selfDeclaredMadeForKids": False,
        }
    else:
        privacy_status = "public"
        status_body = {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": False,
        }

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "23",  # Comedy / Entertainment
        },
        "status": status_body,
    }

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True, mimetype="video/mp4")

    print(f"[YouTube Uploader] Uploading '{file_path}' (status: {privacy_status}, publishAt: {publish_at})...")
    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"[YouTube Uploader] Upload progress: {int(status.progress() * 100)}%")

    print(f"[YouTube Uploader] Video uploaded successfully! Video ID: {response.get('id')}")
    return response


def main():
    parser = argparse.ArgumentParser(description="YouTube Video Uploader & Scheduler")
    parser.add_argument("--file", required=True, help="Path to video file to upload")
    parser.add_argument("--title", required=True, help="Video title")
    parser.add_argument("--description", default="", help="Video description")
    parser.add_argument("--tags", default="", help="Comma-separated list of tags")
    parser.add_argument("--publish-at", default=None, help="ISO 8601 UTC timestamp for scheduled publish")

    args = parser.parse_args()

    tag_list = [t.strip() for t in args.tags.split(",") if t.strip()]

    try:
        upload_video(
            file_path=args.file,
            title=args.title,
            description=args.description,
            tags=tag_list,
            publish_at=args.publish_at,
        )
    except Exception as e:
        print(f"[YouTube Uploader] Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

