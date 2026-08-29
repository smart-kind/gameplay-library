import urllib.request
import json
import os

urls = [
    ("S614", "casual puzzle game match relaxing", "https://itunes.apple.com/search?term=casual+puzzle+game+match+relaxing&media=software&limit=10"),
    ("S615", "best mini games mobile casual 2024 2025", "https://itunes.apple.com/search?term=best+mini+games+mobile+casual+2024+2025&media=software&limit=10"),
    ("S616", "viral hyper casual games list gameplay mechanics", "https://itunes.apple.com/search?term=viral+hyper+casual+games+list+gameplay+mechanics&media=software&limit=10"),
]

for sid, keyword, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
        results = data.get('results', [])
        print(f"=== {sid} | {keyword} | {len(results)} games ===")
        for r in results:
            name = r.get('trackName', r.get('collectionName', 'Unknown'))
            artist = r.get('artistName', '')
            genres = r.get('genres', [])
            desc = r.get('description', '')[:500]
            release = r.get('releaseDate', '')[:4]
            bundle = r.get('bundleId', '')
            primary = r.get('primaryGenreName', '')
            price = r.get('formattedPrice', 'Free')
            print(f"  NAME: {name}")
            print(f"  ARTIST: {artist}")
            print(f"  GENRE: {primary} / {','.join(genres[:3])}")
            print(f"  RELEASED: {release}")
            print(f"  PRICE: {price}")
            print(f"  BUNDLE: {bundle}")
            print(f"  DESC: {desc[:200]}...")
            print(f"  ---")
        print()
    except Exception as e:
        print(f"=== {sid} | ERROR: {e} ===")
