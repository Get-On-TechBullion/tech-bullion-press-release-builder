#!/usr/bin/env node

interface PRInput {
  pressRelease: string;
  contentType: string;
  prQuality: number;
  publicationReadiness: number;
  seoOptimization: number;
  techKeywords: number;
  mediaDistribution: number;
  newsworthiness: number;
}

interface PROutput {
  pressRelease: string;
  contentType: string;
  prQualityScore: number;
  publicationReadinessScore: number;
  seoOptimizationScore: number;
  techKeywordsScore: number;
  mediaDistributionScore: number;
  newsworthinessScore: number;
  overallPRScore: number;
  priorityAction: string;
  platformVisibility: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    prQuality: "Press Release Quality",
    publicationReadiness: "Publication Readiness",
    seoOptimization: "SEO Optimization",
    techKeywords: "Tech Keywords",
    mediaDistribution: "Media Distribution",
    newsworthiness: "Newsworthiness",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getPlatformVisibility(seo: number, media: number, quality: number): Record<string, number> {
  return {
    "TechBullion": Math.min(100, Math.round(quality * 1.02)),
    "Google News": Math.min(100, Math.round(seo * 1.0)),
    "Yahoo Finance": Math.min(100, Math.round(media * 0.97)),
    "PR Newswire": Math.min(100, Math.round(media * 1.0)),
  };
}

export function buildPressRelease(input: PRInput): PROutput {
  const scores = {
    prQuality: input.prQuality,
    publicationReadiness: input.publicationReadiness,
    seoOptimization: input.seoOptimization,
    techKeywords: input.techKeywords,
    mediaDistribution: input.mediaDistribution,
    newsworthiness: input.newsworthiness,
  };
  const overallPRScore = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    pressRelease: input.pressRelease,
    contentType: input.contentType,
    prQualityScore: input.prQuality,
    publicationReadinessScore: input.publicationReadiness,
    seoOptimizationScore: input.seoOptimization,
    techKeywordsScore: input.techKeywords,
    mediaDistributionScore: input.mediaDistribution,
    newsworthinessScore: input.newsworthiness,
    overallPRScore,
    priorityAction: getPriorityAction(scores),
    platformVisibility: getPlatformVisibility(
      input.seoOptimization, input.mediaDistribution, input.prQuality
    ),
  };
}

const args = process.argv.slice(2);
const pressRelease = args[0] || "my-press-release";
const contentType = args[1] || "tech-announcement";
const prQuality = parseInt(args[2]) || 88;
const publicationReadiness = parseInt(args[3]) || 82;
const seoOptimization = parseInt(args[4]) || 85;
const techKeywords = parseInt(args[5]) || 78;
const mediaDistribution = parseInt(args[6]) || 90;
const newsworthiness = parseInt(args[7]) || 80;

const result = buildPressRelease({
  pressRelease, contentType, prQuality, publicationReadiness,
  seoOptimization, techKeywords, mediaDistribution, newsworthiness,
});

console.log(`Press Release: ${result.pressRelease}`);
console.log(`Content Type: ${result.contentType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Press Release Quality Score:   ${result.prQualityScore}/100  [${getStatus(result.prQualityScore)}]`);
console.log(`Publication Readiness Score:   ${result.publicationReadinessScore}/100  [${getStatus(result.publicationReadinessScore)}]`);
console.log(`SEO Optimization Score:        ${result.seoOptimizationScore}/100  [${getStatus(result.seoOptimizationScore)}]`);
console.log(`Tech Keywords Score:           ${result.techKeywordsScore}/100  [${getStatus(result.techKeywordsScore)}]`);
console.log(`Media Distribution Score:      ${result.mediaDistributionScore}/100  [${getStatus(result.mediaDistributionScore)}]`);
console.log(`Newsworthiness Score:          ${result.newsworthinessScore}/100  [${getStatus(result.newsworthinessScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall PR Score:              ${result.overallPRScore}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nPlatform Visibility:");
Object.entries(result.platformVisibility).forEach(([platform, score]) => {
  console.log(`  ${platform.padEnd(20)} ${score}/100`);
});
