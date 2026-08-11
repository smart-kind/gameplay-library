#!/usr/bin/env python3
"""Process pending games with real data fetching."""
import subprocess
import re
import os
import json
import time
from datetime import datetime

DOCS_DIR = "/data/games/gameplay-library/docs"
TMP = "/data/games/gameplay-library/pipeline/tmp"

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def run_cmd(cmd, timeout=20):
    """Run a shell command."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip(), r.returncode
    except:
        return "", 1

def fetch_url(url, filename):
    """Fetch URL to file."""
    path = os.path.join(TMP, f"{filename}.html")
    _, rc = run_cmd(f'curl -s -L -A "{UA}" -m 15 -o "{path}" "{url}"')
    size = os.path.getsize(path) if os.path.exists(path) else 0
    return path, size

def fetch_json(url, filename):
    """Fetch JSON URL."""
    path = os.path.join(TMP, f"{filename}.json")
    _, rc = run_cmd(f'curl -s -L -A "{UA}" -m 15 -o "{path}" "{url}"')
    size = os.path.getsize(path) if os.path.exists(path) else 0
    if size > 0:
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except:
            return None
    return None

def search_wikipedia(game_name):
    """Get info from Wikipedia."""
    safe = game_name.replace(' ', '_')
    data = fetch_json(
        f"https://en.wikipedia.org/api/rest_v1/page/summary/{safe}",
        f"wiki_{safe}"
    )
    if data and 'extract' in data:
        return {
            'title': data.get('title', ''),
            'extract': data.get('extract', ''),
            'desc': data.get('description', ''),
            'url': data.get('content_urls', {}).get('desktop', {}).get('page', '')
        }
    return None

def search_mobygames(game_name):
    """Search MobyGames for game info."""
    safe = game_name.replace(' ', '+')
    # Search API
    data = fetch_json(
        f"https://api.mobygames.com/api/v1/mobygames/search?q={safe}&api_key=demo",
        f"moby_search_{safe}"
    )
    # MobyGames free API may not work, return None
    return None

def fetch_igdb_info(game_name):
    """IGDB requires API key, skip."""
    return None

def extract_paragraphs(html_path, max_count=10):
    """Extract text paragraphs from HTML."""
    if not os.path.exists(html_path):
        return []
    with open(html_path, 'r', errors='ignore') as f:
        html = f.read()
    # Remove scripts, styles, nav, footer, header
    for tag in ['script', 'style', 'nav', 'footer', 'header', 'aside', 'form', 'noscript']:
        html = re.sub(f'<{tag}[^>]*>.*?</{tag}>', '', html, flags=re.DOTALL)
    # Get paragraphs
    paras = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
    texts = []
    for p in paras:
        text = re.sub(r'<[^>]+>', '', p).strip()
        text = re.sub(r'\s+', ' ', text)
        if len(text) > 50:
            texts.append(text)
    return texts[:max_count]

def generate_doc(game, wiki_info, paragraphs, source_url):
    """Generate a proper markdown doc based on real data."""
    now = datetime.now().strftime("%Y%m%d_%H%M")
    name = game['name']
    
    # Clean filename
    safe_name = re.sub(r'[^a-zA-Z0-9_]', '', name.replace(' ', '_'))
    safe_name = re.sub(r'_+', '_', safe_name).strip('_')
    filename = f"{safe_name}_{now}.md"
    filepath = os.path.join(DOCS_DIR, filename)
    
    # Determine game type from data
    game_type = "休闲/解谜"  # default fallback
    developer = "待确认"
    platform = "Mobile (iOS+Android)"
    release_year = "待确认"
    
    desc = "待补充"
    wiki_extract = ""
    
    if wiki_info:
        wiki_extract = wiki_info.get('extract', '')
        if wiki_info.get('desc'):
            desc = wiki_info['desc']
        
        # Try to determine type from description
        d = wiki_info.get('desc', '').lower()
        if 'puzzle' in d:
            game_type = "解谜"
        elif 'platform' in d or 'platformer' in d:
            game_type = "平台跳跃"
        elif 'racing' in d:
            game_type = "竞速"
        elif 'strategy' in d:
            game_type = "策略"
        elif 'roguelike' in d or 'roguelite' in d:
            game_type = "Roguelike"
        elif 'card' in d:
            game_type = "卡牌"
        elif 'action' in d:
            game_type = "动作"
        elif 'rpg' in d:
            game_type = "RPG"
        elif 'simulation' in d:
            game_type = "模拟经营"
        elif 'adventure' in d:
            game_type = "冒险"
    
    # Try to extract more info from paragraphs
    para_text = '\n'.join(paragraphs) if paragraphs else ""
    
    # Build doc
    doc_lines = []
    doc_lines.append(f"# {game['name']}")
    doc_lines.append("")
    doc_lines.append(f"- **类型**: {game_type}")
    doc_lines.append(f"- **平台**: {platform}")
    doc_lines.append(f"- **开发商**: {developer}")
    doc_lines.append(f"- **首次发布**: {release_year}")
    doc_lines.append(f"- **一句话描述**: {desc}")
    doc_lines.append("")
    
    if wiki_extract:
        doc_lines.append("## 玩法规则")
        doc_lines.append("")
        doc_lines.append(wiki_extract)
        doc_lines.append("")
    elif paragraphs:
        doc_lines.append("## 玩法规则")
        doc_lines.append("")
        for p in paragraphs:
            doc_lines.append(p)
            doc_lines.append("")
    else:
        doc_lines.append("## 玩法规则")
        doc_lines.append("")
        doc_lines.append("（待补充 — 需要更多来源数据）")
        doc_lines.append("")
    
    doc_lines.append("## 核心循环")
    doc_lines.append("")
    doc_lines.append("待补充 — 需要详细游玩数据")
    doc_lines.append("")
    
    doc_lines.append("## 核心机制")
    doc_lines.append("")
    doc_lines.append("- 待补充")
    doc_lines.append("")
    
    doc_lines.append("## 为什么好玩")
    doc_lines.append("")
    doc_lines.append("待补充")
    doc_lines.append("")
    
    doc_lines.append("## 粘性来源")
    doc_lines.append("")
    doc_lines.append("待补充")
    doc_lines.append("")
    
    doc_lines.append("## Meta 系统")
    doc_lines.append("")
    doc_lines.append("待补充")
    doc_lines.append("")
    
    doc_lines.append("## 实现难度")
    doc_lines.append("")
    doc_lines.append("待确认")
    doc_lines.append("")
    
    doc_lines.append("## 来源")
    doc_lines.append("")
    if wiki_info and wiki_info.get('url'):
        doc_lines.append(f"- Wikipedia: {wiki_info['url']}")
    if source_url:
        doc_lines.append(f"- {game['source']}: {source_url}")
    doc_lines.append("")
    
    doc = '\n'.join(doc_lines)
    
    with open(filepath, 'w') as f:
        f.write(doc)
    
    return filename, len(doc_lines)

# Process pending games
GAMES = [
    {"id": "G102", "name": "Graine", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/graine/"},
    {"id": "G103", "name": "Crunchyroll: Kawaii Kitchen", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/crunchyroll-kawaii-kitchen/"},
    {"id": "G104", "name": "Arkanoid vs Space Invaders+", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/arkanoid-vs-space-invaders-plus/"},
    {"id": "G105", "name": "Drive Ahead!", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/drive-ahead/"},
    {"id": "G106", "name": "Hidden in my Paradise", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/hidden-in-my-paradise/"},
    {"id": "G107", "name": "Choice of Life: Wild Islands", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/choice-of-life-wild-islands/"},
    {"id": "G108", "name": "Sokobond Express", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/sokobond-express/"},
    {"id": "G109", "name": "Crystal Knights", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/crystal-knights/"},
    {"id": "G110", "name": "Color Flow: Physics Puzzles", "source": "Pocket Gamer", "url": "https://www.pocketgamer.com/color-flow/"},
    {"id": "G121", "name": "City Guesser", "source": "S038 Beebom", "url": ""},
]

results = []
for i, game in enumerate(GAMES):
    print(f"\n{'='*60}")
    print(f"[{i+1}/{len(GAMES)}] {game['id']}: {game['name']}")
    
    # Step 1: Wikipedia
    wiki_info = search_wikipedia(game['name'])
    if wiki_info:
        print(f"  ✅ Wiki: {wiki_info['title']} - {wiki_info.get('desc', '')[:80]}")
    
    # Step 2: Fetch source page if available
    paragraphs = []
    if game['url']:
        path, size = fetch_url(game['url'], f"src_{game['id'].lower()}")
        if size > 1000:
            paragraphs = extract_paragraphs(path)
            if paragraphs:
                print(f"  ✅ Source: {len(paragraphs)} paragraphs extracted")
    
    # Step 3: Generate doc
    filename, lines = generate_doc(game, wiki_info, paragraphs, game['url'])
    print(f"  📝 Doc: {filename} ({lines} lines)")
    
    results.append({
        'id': game['id'],
        'name': game['name'],
        'filename': filename,
        'lines': lines,
        'has_wiki': bool(wiki_info),
        'has_source': len(paragraphs) > 0,
        'source': game['source']
    })
    
    if i < len(GAMES) - 1:
        time.sleep(3)

# Summary
print(f"\n{'='*60}")
print(f"PROCESSED: {len(results)} games")
for r in results:
    status = "✅" if r['has_wiki'] or r['has_source'] else "⚠️"
    print(f"  {status} {r['id']} {r['name']} -> {r['filename']} ({r['lines']} lines)")

with open(os.path.join(TMP, "run_results.json"), "w") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
