#!/usr/bin/env python3
"""
TechBullion Press Release Builder
Helps businesses create professional press releases, technology announcements,
startup news, fintech updates, AI stories, and blockchain content
ready for publication.
https://getontechbullion.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "pr_quality": "Press Release Quality",
        "publication_readiness": "Publication Readiness",
        "seo_optimization": "SEO Optimization",
        "tech_keywords": "Tech Keywords",
        "media_distribution": "Media Distribution",
        "newsworthiness": "Newsworthiness",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_platform_visibility(seo: int, media: int, quality: int) -> dict:
    return {
        "TechBullion": min(100, round(quality * 1.02)),
        "Google News": min(100, round(seo * 1.0)),
        "Yahoo Finance": min(100, round(media * 0.97)),
        "PR Newswire": min(100, round(media * 1.0)),
    }


def build_press_release(
    press_release: str,
    content_type: str = "tech-announcement",
    pr_quality: int = 88,
    publication_readiness: int = 82,
    seo_optimization: int = 85,
    tech_keywords: int = 78,
    media_distribution: int = 90,
    newsworthiness: int = 80,
) -> dict:
    """
    Build and score press releases for tech media distribution.

    Args:
        press_release: Press release title or identifier
        content_type: Type of content
        pr_quality: Press release quality score (0-100)
        publication_readiness: Publication readiness score (0-100)
        seo_optimization: SEO optimization score (0-100)
        tech_keywords: Tech keyword score (0-100)
        media_distribution: Media distribution score (0-100)
        newsworthiness: Newsworthiness score (0-100)

    Returns:
        dict with individual signal scores, overall PR score, and platform visibility
    """
    scores = {
        "pr_quality": pr_quality,
        "publication_readiness": publication_readiness,
        "seo_optimization": seo_optimization,
        "tech_keywords": tech_keywords,
        "media_distribution": media_distribution,
        "newsworthiness": newsworthiness,
    }
    overall_pr_score = round(sum(scores.values()) / 6)

    return {
        "press_release": press_release,
        "content_type": content_type,
        "pr_quality_score": pr_quality,
        "publication_readiness_score": publication_readiness,
        "seo_optimization_score": seo_optimization,
        "tech_keywords_score": tech_keywords,
        "media_distribution_score": media_distribution,
        "newsworthiness_score": newsworthiness,
        "overall_pr_score": overall_pr_score,
        "priority_action": get_priority_action(scores),
        "platform_visibility": get_platform_visibility(seo_optimization, media_distribution, pr_quality),
    }


if __name__ == "__main__":
    press_release = sys.argv[1] if len(sys.argv) > 1 else "my-press-release"
    content_type = sys.argv[2] if len(sys.argv) > 2 else "tech-announcement"
    pr_quality = int(sys.argv[3]) if len(sys.argv) > 3 else 88
    publication_readiness = int(sys.argv[4]) if len(sys.argv) > 4 else 82
    seo_optimization = int(sys.argv[5]) if len(sys.argv) > 5 else 85
    tech_keywords = int(sys.argv[6]) if len(sys.argv) > 6 else 78
    media_distribution = int(sys.argv[7]) if len(sys.argv) > 7 else 90
    newsworthiness = int(sys.argv[8]) if len(sys.argv) > 8 else 80

    result = build_press_release(
        press_release, content_type, pr_quality, publication_readiness,
        seo_optimization, tech_keywords, media_distribution, newsworthiness
    )

    print(f"Press Release: {result['press_release']}")
    print(f"Content Type: {result['content_type']}")
    print("=" * 45)
    print(f"Press Release Quality Score:   {result['pr_quality_score']}/100  [{get_status(result['pr_quality_score'])}]")
    print(f"Publication Readiness Score:   {result['publication_readiness_score']}/100  [{get_status(result['publication_readiness_score'])}]")
    print(f"SEO Optimization Score:        {result['seo_optimization_score']}/100  [{get_status(result['seo_optimization_score'])}]")
    print(f"Tech Keywords Score:           {result['tech_keywords_score']}/100  [{get_status(result['tech_keywords_score'])}]")
    print(f"Media Distribution Score:      {result['media_distribution_score']}/100  [{get_status(result['media_distribution_score'])}]")
    print(f"Newsworthiness Score:          {result['newsworthiness_score']}/100  [{get_status(result['newsworthiness_score'])}]")
    print("=" * 45)
    print(f"Overall PR Score:              {result['overall_pr_score']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nPlatform Visibility:")
    for platform, score in result['platform_visibility'].items():
        print(f"  {platform:<22} {score}/100")


def main():
    """Entry point for PyPI CLI."""
    import sys as _sys
    args = _sys.argv[1:]
    press_release = args[0] if len(args) > 0 else "my-press-release"
    content_type = args[1] if len(args) > 1 else "tech-announcement"
    pr_quality = int(args[2]) if len(args) > 2 else 88
    publication_readiness = int(args[3]) if len(args) > 3 else 82
    seo_optimization = int(args[4]) if len(args) > 4 else 85
    tech_keywords = int(args[5]) if len(args) > 5 else 78
    media_distribution = int(args[6]) if len(args) > 6 else 90
    newsworthiness = int(args[7]) if len(args) > 7 else 80

    result = build_press_release(
        press_release, content_type, pr_quality, publication_readiness,
        seo_optimization, tech_keywords, media_distribution, newsworthiness
    )

    print(f"Press Release: {result['press_release']}")
    print(f"Content Type: {result['content_type']}")
    print("=" * 45)
    print(f"Press Release Quality Score:   {result['pr_quality_score']}/100  [{get_status(result['pr_quality_score'])}]")
    print(f"Publication Readiness Score:   {result['publication_readiness_score']}/100  [{get_status(result['publication_readiness_score'])}]")
    print(f"SEO Optimization Score:        {result['seo_optimization_score']}/100  [{get_status(result['seo_optimization_score'])}]")
    print(f"Tech Keywords Score:           {result['tech_keywords_score']}/100  [{get_status(result['tech_keywords_score'])}]")
    print(f"Media Distribution Score:      {result['media_distribution_score']}/100  [{get_status(result['media_distribution_score'])}]")
    print(f"Newsworthiness Score:          {result['newsworthiness_score']}/100  [{get_status(result['newsworthiness_score'])}]")
    print("=" * 45)
    print(f"Overall PR Score:              {result['overall_pr_score']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nPlatform Visibility:")
    for platform, score in result['platform_visibility'].items():
        print(f"  {platform:<22} {score}/100")
