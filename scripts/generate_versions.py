#!/usr/bin/env python3
"""Generate per-plugin version pages from GitHub Releases."""

import json
import os
import urllib.request

PLUGINS = {
    "mytrip": "ChafficPlugins/MyTrip",
    "mininglevels": "ChafficPlugins/MiningLevels",
    "cruciallib": "ChafficPlugins/CrucialLib",
}

DOCS_DIR = "docs"


def fetch_releases(repo):
    """Fetch all releases for a GitHub repo."""
    url = f"https://api.github.com/repos/{repo}/releases?per_page=100"
    headers = {"Accept": "application/vnd.github.v3+json"}

    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        headers["Authorization"] = f"token {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except Exception as exc:
        print(f"  Warning: could not fetch releases for {repo}: {exc}")
        return []


def generate_page(plugin_name, repo, releases):
    """Build the Markdown content for a plugin's versions page."""
    lines = [f"# {plugin_name} Versions\n"]

    if not releases:
        lines.append("No releases published yet.\n")
        return "\n".join(lines)

    # Latest badge
    latest = releases[0]
    tag = latest["tag_name"]
    date = latest["published_at"][:10]
    lines.append(
        f'!!! success "Latest &mdash; {tag} ({date})"\n'
        f"    [Download {tag}]({latest['html_url']}){{ .md-button }}\n"
    )

    # Table of all releases
    lines.append("## All Releases\n")
    lines.append("| Version | Date | Downloads |")
    lines.append("|---------|------|----------:|")

    for rel in releases:
        t = rel["tag_name"]
        d = rel["published_at"][:10]
        url = rel["html_url"]
        downloads = sum(a["download_count"] for a in rel.get("assets", []))
        lines.append(f"| [{t}]({url}) | {d} | {downloads:,} |")

    lines.append("")

    # Detailed changelogs
    lines.append("## Changelog\n")
    for rel in releases:
        t = rel["tag_name"]
        d = rel["published_at"][:10]
        name = rel.get("name") or t
        body = (rel.get("body") or "").strip()

        lines.append(f"### {name} ({d})\n")
        if body:
            lines.append(f"{body}\n")
        else:
            lines.append("*No release notes.*\n")

    return "\n".join(lines)


def main():
    for plugin_dir, repo in PLUGINS.items():
        plugin_name = repo.split("/")[1]
        print(f"Fetching releases for {plugin_name} ({repo})...")

        releases = fetch_releases(repo)
        print(f"  Found {len(releases)} release(s)")

        content = generate_page(plugin_name, repo, releases)

        out = os.path.join(DOCS_DIR, plugin_dir, "versions.md")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w") as f:
            f.write(content)
        print(f"  Wrote {out}")


if __name__ == "__main__":
    main()
