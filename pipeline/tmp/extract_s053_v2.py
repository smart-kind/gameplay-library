#!/usr/bin/env python3
"""Extract games from S053 Pocket Gamer page 6."""
import re
import json

with open("/data/games/gameplay-library/pipeline/tmp/page6.html", "r") as f:
    html = f.read()

# Remove all the scripts and styles first
html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)

# Find all game-simple entries
# Pattern: <a href="/slug/" class="game-simple"> ... <h2>Name</h2> ... <div class="formats"><span>Platform</span></div>
entries = re.findall(
    r'<a[^>]*href="(/[^"]+)"[^>]*class="game-simple"[^>]*>.*?<h2>(.*?)</h2>.*?<div class="formats">(.*?)</div>',
    html, re.DOTALL
)

games = []
for slug, name_html, formats_html in entries:
    # Clean name
    name = re.sub(r'<[^>]+>', '', name_html).strip()
    # Clean platforms
    platforms = re.sub(r'<[^>]+>', '', formats_html).strip()
    platforms = platforms.replace('\n', '').replace('\t', '')
    platforms = re.sub(r'\s+', ' ', platforms)
    
    # Find stars
    stars_on = formats_html.count('icon-blue-star-on')
    stars_half = 1 if 'icon-blue-star-half' in formats_html else 0
    
    url = f'https://www.pocketgamer.com{slug}'
    
    games.append({
        'name': name,
        'platform': platforms,
        'url': url,
        'slug': slug,
        'stars': stars_on + (0.5 if stars_half else 0)
    })

print(f"Found {len(games)} games from S053:")
for g in games:
    print(f"  [{g['stars']}] {g['name']} | {g['platform']} | {g['slug']}")

# Save for later use
with open("/data/games/gameplay-library/pipeline/tmp/s053_games.json", "w") as f:
    json.dump(games, f, indent=2, ensure_ascii=False)
print(f"\nSaved {len(games)} games")
