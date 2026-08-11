#!/usr/bin/env python3
"""Extract games from S053 Pocket Gamer page 6."""
import re
import sys
import os
import json
import time
from urllib.request import urlopen, Request
from html.parser import HTMLParser

TMP = "/data/games/gameplay-library/pipeline/tmp"

with open(f"{TMP}/page6.html", "r") as f:
    html = f.read()

# Find all game-simple entries
entries = re.split(r'<a\s[^>]*class="game-simple"', html)[1:]

games = []
for entry in entries:
    slug_m = re.search(r'href="(/[^"]+)"', entry)
    name_m = re.search(r'<h2>(.*?)</h2>', entry, re.DOTALL)
    platform_m = re.search(r'<div class="formats">(.*?)</div>', entry, re.DOTALL)
    score_m = re.findall(r'icon-blue-star-on.svg', entry)
    score_half = len(re.findall(r'icon-blue-star-half.svg', entry))
    
    if slug_m and name_m:
        slug = slug_m.group(1)
        name = re.sub(r'<[^>]+>', '', name_m.group(1)).strip()
        
        if platform_m:
            platform_raw = re.sub(r'<[^>]+>', '', platform_m.group(1)).strip()
            platform = platform_raw.replace('</span> + <span>', ' + ')
        else:
            platform = 'Unknown'
        
        stars = len(score_m) + (0.5 if score_half else 0)
        url = f'https://www.pocketgamer.com{slug}'
        
        games.append({
            'name': name,
            'platform': platform,
            'url': url,
            'slug': slug,
            'stars': stars
        })

print(f"Found {len(games)} games from S053:")
for g in games:
    print(f"  [{g['stars']}] {g['name']} | {g['platform']} | {g['slug']}")

# Save for later use
with open(f"{TMP}/s053_games.json", "w") as f:
    json.dump(games, f, indent=2, ensure_ascii=False)
print(f"\nSaved to {TMP}/s053_games.json")
