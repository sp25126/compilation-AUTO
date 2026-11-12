import { NICHE_GRAPH, getNextSubCategory } from './src/pipeline/NicheGraph';

// Test 1: Count total sub-categories
let totalSubCategories = 0;
NICHE_GRAPH.forEach(niche => {
  totalSubCategories += niche.subCategories.length;
});
console.log(`Total Niches: ${NICHE_GRAPH.length}`);
console.log(`Total Sub-Categories: ${totalSubCategories}`);

// Test 2: Test Round-Robin State tracking
const firstRun = getNextSubCategory();
console.log(`First Run ID: ${firstRun.id}`);

const secondRun = getNextSubCategory();
console.log(`Second Run ID: ${secondRun.id}`);

