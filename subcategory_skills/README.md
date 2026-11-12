# Sub-Category Production Skills (`subcategory_skills/`)

This directory contains **execution-ready production skill files** for each of the 50 sub-categories in [`src/pipeline/master_category_registry.json`](../src/pipeline/master_category_registry.json).

- **Master 7-Stage Pipeline SOP & Template:** [`PIPELINE_ARCHITECTURE.md`](./PIPELINE_ARCHITECTURE.md)

## How the AI Pipeline Uses These Files
Before sourcing, trimming, or rendering any compilation for a `subCategoryId`, the pipeline **MUST**:
1. Read `subcategory_skills/<subCategoryId>.md` first.
2. Follow its **Reference Channels**, **Strict Sourcing & Rejection Rules**, **2-Stage Frame Inspection Protocol**, **Cause-Before-Freeze Timing Formula**, **Compositor Spec**, and **QA Gates** without substituting hardcoded or guessed offsets.

## Available Sub-Category Skills
| Sub-Category ID | Display Name | Niche | Skill File | Status |
| :--- | :--- | :--- | :--- | :--- |
| `people_accepting_fate` | THIS IS THE END | `human_fails` | [`people_accepting_fate.md`](./people_accepting_fate.md) | Verified & Production-Proven |
| `instant_karma` | INSTANT KARMA | `instant_karma` | [`instant_karma.md`](./instant_karma.md) | Verified & Production-Proven |
| `pets_being_dumb` | PETS BEING DUMB | `funny_animals` | [`pets_being_dumb.md`](./pets_being_dumb.md) | Verified & Production-Proven |
| `overconfident_humbled` | OVERCONFIDENT HUMBLED | `human_fails` | [`overconfident_humbled.md`](./overconfident_humbled.md) | Verified & Production-Proven |
| `athletes_celebrating_too_early` | CELEBRATING TOO EARLY | `sports_bloopers` | [`athletes_celebrating_too_early.md`](./athletes_celebrating_too_early.md) | Verified & Production-Proven |
| `defying_warning_signs` | IGNORING WARNING SIGNS | `instant_karma` | [`defying_warning_signs.md`](./defying_warning_signs.md) | Verified & Production-Proven |
| `pets_being_smart` | 200 IQ SMART PETS | `funny_animals` | [`pets_being_smart.md`](./pets_being_smart.md) | Verified & Production-Proven |
| `one_million_aura_loss` | -1,000,000 AURA MOMENTS | `aura_debt` | [`one_million_aura_loss.md`](./one_million_aura_loss.md) | Verified & Production-Proven |
| `used_all_luck_for_life` | USED ALL LUCK MOMENTS | `extreme_luck` | [`used_all_luck_for_life.md`](./used_all_luck_for_life.md) | Verified & Production-Proven |
| `unrendered_game_npcs` | REAL-LIFE NPC GLITCHES | `npc_glitches` | [`unrendered_game_npcs.md`](./unrendered_game_npcs.md) | Verified & Production-Proven |
| `worst_shift_ever` | WORST SHIFT MOMENTS | `workplace_disasters` | [`worst_shift_ever.md`](./worst_shift_ever.md) | Verified & Production-Proven |
| `treadmill_slingshots` | GYM & TREADMILL FAILS | `gym_bloopers` | [`treadmill_slingshots.md`](./treadmill_slingshots.md) | Verified & Production-Proven |
| `pranks_backfired` | PRANKS GONE WRONG | `instant_karma` | [`pranks_backfired.md`](./pranks_backfired.md) | Verified & Production-Proven |
| `ice_driveway_slides` | ICE SLIPPING MOMENTS | `nature_weather` | [`ice_driveway_slides.md`](./ice_driveway_slides.md) | Verified & Production-Proven |
