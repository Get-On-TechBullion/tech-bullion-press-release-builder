from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="techbullion-press-release-builder",
    version="1.0.0",
    author="GetOnTechBullion.com",
    author_email="info@getontechbullion.com",
    description="TechBullion Press Release Builder helps businesses create professional press releases, technology announcements, startup news, fintech updates, AI stories, and blockchain content ready for publication.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://getontechbullion.com",
    project_urls={
        "Homepage": "https://getontechbullion.com",
        "GitHub": "https://github.com/Get-On-TechBullion/tech-bullion-press-release-builder",
        "Documentation": "https://techbullion-press-release-builder.readthedocs.io",
        "PyPI": "https://pypi.org/project/techbullion-press-release-builder",
    },
    py_modules=["builder"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Text Processing",
    ],
    keywords=[
        "press-release-builder",
        "tech-announcement",
        "startup-news",
        "fintech-pr",
        "ai-story-builder",
        "blockchain-content",
        "techbullion",
        "getontechbullion",
        "tech-press-release",
    ],
    entry_points={
        "console_scripts": [
            "techbullion-pr-builder=builder:main",
        ],
    },
)
