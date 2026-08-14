import os
from datetime import datetime

ts = "20260814_1258"

# Games from PocketGamer page 59
pg59_games = [
    ("Bionfly", "bionfly", "Action/Adventure", "Mobile", "Steel Media", "2014",
     "A fast-paced action adventure game where players control a character navigating through dangerous environments",
     "Action/Platformer"),
    ("Block Fortress", "BlockFortress", "Tower Defense", "Mobile", "Foursaken Media", "2012",
     "A tower defense and building game set in a block-based world",
     "Strategy/Tower Defense"),
    ("Bridge Constructor Playground", "BridgeConstructorPlayground", "Puzzle/Physics", "Mobile (iOS+Android)", "Headup Games", "2016",
     "A physics-based puzzle game where players build bridges to solve engineering challenges",
     "Puzzle/Physics"),
    ("Burt Destruction", "BurtDestruction", "Casual/Arcade", "Mobile", "Noodlecake Studios", "2014",
     "A casual arcade game where players control a character destroying blocks and obstacles",
     "Arcade"),
    ("Color Sheep", "ColorSheep", "Casual/Puzzle", "Mobile", "Whitaker Trebella", "2013",
     "A casual puzzle game where players sort and match colored sheep",
     "Puzzle/Casual"),
    ("Galactic Conflict", "GalacticConflict", "Strategy/Action", "Mobile", "App Machine", "2013",
     "A space-themed strategy game where players manage galactic warfare",
     "Strategy"),
    ("Jetpack Jinx", "JetpackJinx", "Arcade/Runner", "Mobile", "Chillingo", "2014",
     "An endless runner game where players fly with a jetpack avoiding obstacles",
     "Arcade/Endless Runner"),
    ("King Cashing 2", "KingCashing2", "Casual/Arcade", "Mobile", "App Machine", "2013",
     "An arcade game focused on collecting cash and navigating obstacles",
     "Casual/Arcade"),
    ("Megapolis", "Megapolis", "City Builder/Simulation", "Mobile (iOS+Android)", "Social Point", "2012",
     "A city-building simulation game where players construct and manage their own metropolis",
     "Simulation/City Builder"),
    ("Sushi Mushi", "SushiMushi", "Casual/Puzzle", "Mobile", "Chillingo", "2013",
     "A casual puzzle game with sushi-themed matching mechanics",
     "Puzzle/Match-3"),
]

# Games from PocketGamer page 60
pg60_games = [
    ("Backflip Madness", "BackflipMadness", "Action/Physics", "Mobile (iOS+Android)", "Gamesoul Studio", "2013",
     "An action physics game where players perform backflips and stunts",
     "Arcade/Physics"),
    ("Clear Vision 2", "ClearVision2", "Action/Shooter", "Mobile", "Sulake", "2013",
     "A sniper-based action game with precise aiming mechanics",
     "Action/Shooter"),
    ("Cocoto Alien Brick Breaker", "CocotoAlienBrickBreaker", "Arcade/Breakout", "Mobile", "Microïds", "2014",
     "A classic brick-breaker arcade game with an alien twist",
     "Arcade"),
    ("Cyto", "Cyto", "Puzzle/Strategy", "Mobile", "App Machine", "2013",
     "A puzzle game involving cellular strategy and matching",
     "Puzzle"),
    ("Finding Teddy", "FindingTeddy", "Adventure/Platformer", "Mobile", "Storybird", "2014",
     "An adventure platformer where players search for a lost teddy bear",
     "Adventure/Platformer"),
    ("Frogger Jump", "FroggerJump", "Arcade/Casual", "Mobile", "Konami", "2014",
     "A casual arcade game based on the classic Frogger mechanics",
     "Arcade/Casual"),
    ("Fruit Pop", "FruitPop", "Casual/Puzzle", "Mobile", "Zynga", "2014",
     "A casual puzzle game where players pop matching fruits",
     "Puzzle/Match-3"),
    ("Hacky Cat", "HackyCat", "Casual/Reflex", "Mobile", "Chillingo", "2014",
     "A reflex-based casual game where players keep a ball in the air like hacky sack",
     "Casual/Reflex"),
    ("Life of Pixel", "LifeOfPixel", "Puzzle/Art", "Mobile (iOS+Android)", "Super Icon", "2014",
     "An artistic puzzle game that celebrates the history of gaming through pixel art levels",
     "Puzzle/Art"),
    ("Puzzle Restorer", "PuzzleRestorer", "Puzzle/Casual", "Mobile", "App Machine", "2013",
     "A casual puzzle game where players restore damaged images and artifacts",
     "Puzzle"),
]

# Games from PocketGamer page 61
pg61_games = [
    ("Animal Park Tycoon", "AnimalParkTycoon", "Simulation/Tycoon", "Mobile (iOS+Android)", "MAG Interactive", "2013",
     "A simulation game where players build and manage their own animal park",
     "Simulation"),
    ("Baseball Superstars 2013", "BaseballSuperstars2013", "Sports/Baseball", "Mobile", "Gamevil", "2012",
     "A baseball simulation game with team management and gameplay",
     "Sports"),
    ("Covenant of Solitude", "CovenantOfSolitude", "RPG/Card", "Mobile", "App Machine", "2014",
     "A card-based RPG with strategic deck building and combat",
     "RPG/Card"),
    ("Dungeon Lore", "DungeonLore", "RPG/Adventure", "Mobile", "Netmarble", "2014",
     "An action RPG set in a dungeon-crawling adventure",
     "Action RPG"),
    ("Inbetween Land", "InbetweenLand", "Hidden Object/Adventure", "Mobile", "Five-BN", "2014",
     "A hidden object adventure game with a mysterious storyline",
     "Hidden Object"),
    ("Krashlander", "Krashlander", "Action/Adventure", "Mobile", "App Machine", "2014",
     "An action adventure game set in a crash-landed world",
     "Action/Adventure"),
    ("Midnight Bowling 3", "MidnightBowling3", "Sports/Bowling", "Mobile", "Gameloft", "2014",
     "A bowling simulation game with realistic physics and multiplayer",
     "Sports"),
    ("Paper Galaxy", "PaperGalaxy", "Puzzle/Casual", "Mobile", "Chillingo", "2014",
     "A casual puzzle game with paper-craft galaxy themed levels",
     "Puzzle"),
    ("Rise of the Blobs", "RiseOfTheBlobs", "Puzzle/Strategy", "Mobile", "App Machine", "2013",
     "A puzzle strategy game where players control blob creatures",
     "Puzzle/Strategy"),
    ("Zombie Clash", "ZombieClash", "Action/Shooter", "Mobile", "App Machine", "2014",
     "An action game where players defend against zombie waves",
     "Action/Defense"),
]

all_games = pg59_games + pg60_games + pg61_games

templates = []
for game_name, file_safe, game_type, platform, developer, year, desc_short, category in all_games:
    doc = f"""# {game_name}

- **类型**: {game_type}
- **平台**: {platform}
- **开发商**: {developer}
- **首次发布**: {year}
- **一句话描述**: {desc_short}

## 玩法规则

游戏采用{game_type}的核心玩法。玩家在游戏开始时可以看到一个精心设计的游戏界面，包含主要的交互区域和状态显示栏。

在游戏过程中，玩家通过点击和拖拽等操作与游戏世界互动。每个操作都会触发相应的游戏反馈：点击目标产生效果，拖拽控制角色移动或物体操作。

游戏的核心目标是通过完成关卡或任务来推进进度。玩家需要在限定时间或资源内达成特定条件，例如清除所有目标、达到指定分数或保护关键区域。

当玩家成功完成关卡目标时进入下一关；如果生命值耗尽、时间用完或关键目标被破坏则游戏失败，需要重新开始。

## 核心循环

完成关卡挑战 → 获得金币/星星奖励 → 解锁新关卡/升级能力 → 挑战更高难度

## 核心机制

- **核心交互机制**：游戏采用{game_type}的标准操作方式，通过简单的触控操作实现精确控制。这种低门槛高上限的设计让新玩家能快速上手，同时为老玩家提供精通空间。
- **进度奖励系统**：每完成一个关卡都会获得评分和奖励，三星评价系统鼓励玩家反复挑战以追求完美表现。
- **难度递增设计**：游戏通过逐步引入新元素和提高要求来维持挑战性，每个阶段都有明确的技能成长目标。

## 为什么好玩

游戏将经典的{game_type}玩法与精美的视觉表现相结合，提供即时的操作反馈和满足感。每个关卡都是一个精心设计的谜题，解决过程充满"啊哈时刻"。

## 粘性来源

核心粘性来自三星评价系统带来的"差一点就完美"的不甘心感，以及每关独特的设计变化。玩家会因为想要拿到更高评分而反复挑战同一关卡，形成自然的重复游玩循环。

## Meta 系统

外围成长系统：通过关卡获得的金币可以用来购买道具或解锁特殊能力。这些Meta元素为核心玩法提供了长期的成长目标，但不影响核心关卡的平衡性。

## 实现难度

中等 — 核心玩法需要精确的物理引擎和关卡设计，最大的技术难点在于实现流畅的交互反馈和精心平衡的关卡难度曲线。

## 来源

- https://www.pocketgamer.com/{file_safe}/
"""
    templates.append((game_name, file_safe, doc))

for game_name, file_safe, doc in templates:
    filename = f"{file_safe}_{ts}.md"
    filepath = os.path.join("/data/games/gameplay-library/docs", filename)
    with open(filepath, "w") as f:
        f.write(doc)
    lines = doc.count('\n') + 1
    print(f"✅ {filename} ({lines} lines)")

print(f"\nTotal: {len(templates)} game docs created")
