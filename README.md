# TechBullion Press Release Builder 📰🚀

[![npm](https://img.shields.io/npm/v/@get-on-techbullion/press-release-builder)](https://npmjs.com/package/@get-on-techbullion/press-release-builder)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21632743.svg)](https://doi.org/10.5281/zenodo.21632743)

TechBullion Press Release Builder helps businesses create professional press releases, technology announcements, startup news, fintech updates, AI stories, and blockchain content ready for publication. Built by [GetOnTechBullion.com](https://getontechbullion.com).

## Features

- Press Release Quality Score — evaluates structure, clarity, and journalistic standards
- Publication Readiness Score — checks formatting and editorial compliance
- SEO Optimization Score — measures keyword density and search visibility
- Tech Keyword Score — tracks relevant technology, fintech, AI, and blockchain terms
- Media Distribution Score — evaluates suitability for tech news platforms
- Newsworthiness Score — predicts media pickup and editorial interest
- Content Types — tech announcements, startup news, fintech updates, AI stories, blockchain content
- CLI support in Node.js and Python
- Benchmark dataset included (20 press release cases)
- Lightweight, publish-ready, minimal dependencies

## Quick Start

### Node.js

```bash
npm install @get-on-techbullion/press-release-builder
npx techbullion-pr-builder "my-press-release" tech-announcement 88 82 85 78 90 80
```

### Python

```bash
pip install techbullion-press-release-builder
python -m builder "my-press-release" tech-announcement 88 82 85 78 90 80
```

## Output

```
Press Release: my-press-release
Content Type: Tech Announcement
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Press Release Quality Score:   88 / 100  [Excellent]
Publication Readiness Score:   82 / 100  [Healthy]
SEO Optimization Score:        85 / 100  [Excellent]
Tech Keyword Score:            78 / 100  [Healthy]
Media Distribution Score:      90 / 100  [Excellent]
Newsworthiness Score:          80 / 100  [Healthy]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall PR Score:              84 / 100
Priority Action:               Tech Keywords (lowest — act first)

Platform Visibility:
  TechBullion:          90 / 100
  Google News:          85 / 100
  Yahoo Finance:        82 / 100
  PR Newswire:          88 / 100
```

## Content Types

| Type | Description |
|------|-------------|
| tech-announcement | Technology product and feature announcements |
| startup-news | Startup launches, funding, and milestones |
| fintech-update | Fintech product and regulatory updates |
| ai-story | AI and machine learning developments |
| blockchain-content | Blockchain, Web3, and crypto news |
| product-launch | New product and service launches |
| funding-round | Investment and funding announcements |
| partnership | Strategic partnership announcements |
| executive-news | Leadership and executive announcements |
| award-recognition | Awards, rankings, and recognitions |

## Project Structure

```
tech-bullion-press-release-builder/
├── index.ts              # TypeScript PR builder
├── builder.py            # Python PR builder
├── package.json          # NPM package config
├── package-lock.json     # NPM lock file
├── tsconfig.json         # TypeScript config
├── schema.json           # JSON-LD structured data
├── zenodo.json           # Zenodo metadata
├── heartbeat.txt         # Auto-updated daily
├── mkdocs.yml            # ReadTheDocs config
├── .readthedocs.yaml     # ReadTheDocs build config
├── docs/
│   ├── index.md          # Documentation
│   └── requirements.txt
├── dataset/
│   └── press_release_benchmarks.csv
├── kaggle/
│   └── notebook.ipynb
├── .github/workflows/
│   ├── heartbeat.yml
│   └── npm-publish.yml
├── README.md
└── LICENSE
```

## PR Signal Scores

| Signal | Description | Score Range |
|--------|-------------|-------------|
| Press Release Quality | Structure, clarity, journalistic standards | 0–100 |
| Publication Readiness | Formatting and editorial compliance | 0–100 |
| SEO Optimization | Keyword density and search visibility | 0–100 |
| Tech Keywords | Technology, fintech, AI, blockchain terms | 0–100 |
| Media Distribution | Suitability for tech news platforms | 0–100 |
| Newsworthiness | Media pickup and editorial interest | 0–100 |

## Score Interpretation

| Score | Status | Action |
|-------|--------|--------|
| 0–30 | Critical | Major revision required |
| 31–60 | At Risk | Significant improvements needed |
| 61–80 | Healthy | Minor optimizations recommended |
| 81–100 | Excellent | Ready for distribution |

## Keywords

TechBullion Press Release · Tech Announcement Builder · Startup News Generator · Fintech PR · AI Story Builder · Blockchain Content · Press Release Optimization · Tech Media Distribution

## Links

| Platform | URL |
|----------|-----|
| Website | https://getontechbullion.com |
| GitHub | https://github.com/Get-On-TechBullion/tech-bullion-press-release-builder |
| GitHub Pages | https://get-on-techbullion.github.io/tech-bullion-press-release-builder/ |
| NPM | https://npmjs.com/package/@get-on-techbullion/press-release-builder |
| PyPI | https://pypi.org/project/techbullion-press-release-builder |
| Hugging Face | https://huggingface.co/datasets/get-on-techbullion/press-release-benchmarks |
| Kaggle | https://kaggle.com/datasets/getontechbullion/press-release-benchmarks |
| Zenodo | https://zenodo.org/records/21632743 |
| Docs | https://techbullion-press-release-builder.readthedocs.io |
| Quora | https://www.quora.com/profile/Get-On-Techbullion |
| SlideShare | https://www.slideshare.net/slideshow/get-on-techbullion-fast-editorial-coverage-for-tech-brands/288837590 |

## About GetOnTechBullion.com

GetOnTechBullion.com helps businesses create professional press releases, technology announcements, startup news, fintech updates, AI stories, and blockchain content ready for publication on TechBullion and leading tech media platforms.

## License

MIT — [GetOnTechBullion.com](https://getontechbullion.com)
