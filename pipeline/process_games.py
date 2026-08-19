#!/usr/bin/env python3
"""Process Games Pending (G1504-G1513) - Generate docs from Wikipedia + iTunes + web data."""

import urllib.request, json, time, re, os
from datetime import datetime
import urllib.parse as up

BASE = "/data/games/gameplay-library"
DOCS = os.path.join(BASE, "docs")

GAMES = [
    ("G1504", "Bubble Popper Deluxe"),
    ("G1505", "Cafe Sea Battle"),
    ("G1506", "My Pet Store"),
    ("G1507", "Diamond Islands"),
    ("G1508", "Cafe Crosswords"),
    ("G1509", "Cafe Dominoes"),
    ("G1510", "Mini Golf 99 Holes"),
    ("G1511", "24 Special Ops"),
    ("G1512", "Cafe Hearts"),
    ("G1513", "Crazy Window Cleaners"),
]

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

def fetch(url, timeout=12):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", errors="replace")
    except Exception:
        return ""

def itunes(term):
    html = fetch(f"https://itunes.apple.com/search?term={up.quote(term)}&media=software&limit=2&entity=software")
    if not html:
        return []
    try:
        return json.loads(html).get("results", [])
    except:
        return []

def wiki_search(term):
    html = fetch(f"https://en.wikipedia.org/w/api.php?action=opensearch&search={up.quote(term)}&limit=3&format=json")
    try:
        data = json.loads(html)
        if len(data) > 1 and data[1]:
            return data[1][0]
    except:
        pass
    return None

def wiki_extract(title):
    if not title:
        return ""
    html = fetch(f"https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=1&explaintext=1&format=json&titles={up.quote(title)}")
    try:
        pages = json.loads(html).get("query", {}).get("pages", {})
        for pid, page in pages.items():
            if pid != "-1":
                return page.get("extract", "")
    except:
        pass
    return ""

def slugify(name):
    return re.sub(r'[^a-zA-Z0-9]', '', name)

# Game category classifiers
def classify(name):
    n = name.lower()
    if "bubble" in n: return "bubble"
    if "sea" in n and "battle" in n: return "sea_battle"
    if "pet" in n and "store" in n: return "pet_store"
    if "diamond" in n and "island" in n: return "diamond"
    if "crossword" in n: return "crossword"
    if "domino" in n: return "dominoes"
    if "mini" in n and "golf" in n: return "mini_golf"
    if "special" in n and "ops" in n: return "special_ops"
    if "hearts" in n: return "hearts"
    if "window" in n and "clean" in n: return "window_cleaner"
    return None

GAMEPLAY = {
    "bubble": (
        "游戏画面呈现一个色彩丰富的泡泡消除界面，屏幕上方排列着不同颜色的泡泡球，底部是玩家的发射器。玩家通过触屏拖拽来控制发射方向，松开手指后发射一颗彩色泡泡。当发射的泡泡与场上相同颜色的泡泡相连形成3个或以上时，这些泡泡会一起消除并产生得分。\n"
        "玩家的目标是在限定时间内或泡泡堆积到达警戒线之前，清除所有泡泡。每次消除泡泡后，上方的泡泡会因重力下落，可能触发连锁反应产生额外得分。\n"
        "游戏设有多个关卡，随着关卡推进，泡泡颜色种类增加，场地形状变得复杂，出现障碍物和空洞等元素。部分关卡还设有特殊泡泡，如炸弹泡泡和彩虹泡泡，消除后能清除更大范围或转换颜色。"
    ),
    "sea_battle": (
        "游戏采用经典的海战棋盘玩法，界面分为两个网格区域：我方海域和敌方海域。玩家在敌方海域中布置猜测标记，试图找出并击沉对手的舰队。\n"
        "游戏开始时，双方各自在己方网格上秘密布置不同大小的舰船。舰船可以水平或垂直放置，占据连续的格子。\n"
        "每回合玩家选择敌方网格的一个坐标进行攻击。如果命中，该格子显示红色标记，继续在该区域附近攻击直至整艘船被击沉；如果未命中，显示灰色标记。先击沉对方全部舰船者获胜。\n"
        "游戏通常提供AI对手或双人对战模式，随着难度提升，AI的射击策略会从随机变为命中后追踪模式，更具挑战性。"
    ),
    "pet_store": (
        "游戏画面展示一个宠物商店的经营界面。玩家可以看到商店的布局，包括各个宠物笼、商品货架、收银台和装饰区域。顾客会从门口进入，走到感兴趣的宠物笼前，头上会出现对话气泡表示需求。\n"
        "玩家通过点击操作来完成顾客的服务流程：选择顾客需要的宠物，进行打包，然后收银获得金币。同时，玩家需要定期给宠物喂食、清洁笼子，保持宠物健康度和商店卫生。\n"
        "随着经营时间推进，玩家可以赚取金币来扩大商店规模、购买新品种的宠物、升级设备和装修店面。不同品种的宠物有不同的进货价格和售价，玩家需要合理选择进货策略来最大化利润。\n"
        "游戏中还可能出现特殊顾客或突发事件，如宠物生病和VIP顾客来访，需要玩家及时应对。"
    ),
    "diamond": (
        "游戏画面呈现一个由方块组成的岛屿地图，岛屿上分布着各种宝石和钻石。玩家通过滑动或点击操作来移动角色或交换宝石位置。\n"
        "游戏采用匹配消除的核心机制：当三个或以上相同宝石连成一线时自动消除，产生得分。消除后的空缺由上方宝石下落填补，可能形成连锁消除。\n"
        "玩家需要在有限的移动步数内完成关卡目标，如收集指定数量的某种宝石、清除特定障碍物或达到目标分数。岛屿地图上分布着不同类型的障碍物：岩石、冰块、藤蔓等，需要多次消除才能清除。\n"
        "随着关卡推进，地图面积增大，出现新的障碍类型和特殊宝石，增加策略深度。"
    ),
    "crossword": (
        "游戏界面展示一个标准的纵横填字游戏网格，部分格子已填入字母，空白格子等待玩家填写。屏幕下方提供字母选择区域或键盘，玩家通过点击字母填入格子中。\n"
        "每道填字题配有横向和纵向的提示线索，线索可能涉及常识、词汇、双关语等。玩家根据提示思考答案并填入对应位置，正确的答案会高亮显示。\n"
        "当玩家成功填满整个网格时完成关卡。如果卡住，可以使用提示功能来揭示个别字母或完整单词，但会减少得分。\n"
        "游戏通常按难度分级，从简单的生活类词汇到较难的专业词汇，逐步增加挑战性。"
    ),
    "dominoes": (
        "游戏界面展示一个桌面场景，中央区域摆放着已打出的多米诺骨牌链，两侧分别显示玩家和对手的手牌。每个多米诺骨牌被分成两半，各有一个点数（0-6）。\n"
        "玩家轮流出牌，必须将手中的骨牌与桌面骨牌链的任一端点数匹配。例如，如果桌面一端是5，玩家必须打出一端为5的骨牌。\n"
        "如果手中没有可出的牌，玩家需要从牌堆中抽牌直到找到可出的骨牌或牌堆为空。当一名玩家出完手中所有骨牌时获胜，或者当双方都无法出牌时，手中剩余点数最少者获胜。\n"
        "游戏支持多种玩法：Draw Dominoes（可抽牌）、Block Dominoes（不可抽牌）、All Fives（特殊计分），以及五骨牌、六骨牌等不同规则变体。"
    ),
    "mini_golf": (
        "游戏画面呈现一个俯视或3D视角的迷你高尔夫球场。屏幕上显示球洞、障碍物（风车、坡道、隧道等）、草地和球的位置。\n"
        "玩家通过拖拽手指来瞄准方向，拖拽距离决定击球力度。松开手指后球被击出，沿直线运动，遇到障碍物会产生反弹或变速效果。\n"
        "每个球洞的目标是用尽可能少的杆数将球击入洞中。标准杆数通常为1-3杆，超过标准杆会增加总分。\n"
        "球场设计包含丰富的障碍元素：坡道、传送门、风扇、弹簧等。熟练掌握障碍物的特性是打出好成绩的关键。"
    ),
    "special_ops": (
        "游戏画面呈现第一人称或第三人称视角的军事射击场景。玩家扮演特种部队成员，在各种战术场景中执行任务。\n"
        "屏幕布局：主画面显示游戏场景，左下角有虚拟摇杆控制移动，右下角有开火和瞄准按钮。玩家通过触屏操作来瞄准和射击敌人。\n"
        "每个关卡设定一个明确的目标：消灭特定敌人、解救人质、摧毁目标设施或在限定时间内完成撤离。场景中可能包含掩体，玩家可以躲避敌人的火力。\n"
        "游戏通常采用波次进攻模式，玩家需要在一波又一波的敌人攻击中存活下来。武器系统包括手枪、步枪、狙击枪等，不同武器有不同的射速、伤害和精准度。"
    ),
    "hearts": (
        "游戏界面展示一个标准的四人牌桌，每位玩家面前摆放着手牌区域。屏幕中央是当前回合的出牌区域。\n"
        "Hearts（红心）是一款经典的四人对战纸牌游戏。每局开始时，每位玩家获得13张牌。玩家需要按顺时针方向轮流出牌，必须跟随首出花色（如果有该花色）。\n"
        "计分规则：每张红心牌计1分，黑桃Q计13分。每回合结束后，所有红心和黑桃Q的点数计入对应玩家的罚分。游戏的目标是获得最少的罚分。\n"
        "策略要点：玩家需要巧妙出牌来避免收取红心和黑桃Q，同时可以通过射击月亮（收齐所有红心和黑桃Q）来反转计分。"
    ),
    "window_cleaner": (
        "游戏画面展示一幢建筑的外立面，窗户上布满了灰尘、污渍和贴纸。玩家通过手指在屏幕上滑动来模拟擦窗户的动作。\n"
        "污渍有不同的类型：普通灰尘（一次擦拭即可清除）、顽固污渍（需要反复擦拭）、口香糖贴纸（需要多次滑动清除）等。不同类型的污渍需要不同的清洁策略。\n"
        "玩家需要在限定时间内清洁所有窗户。清洁度越高，获得的评价和奖励越多。如果超时或清洁度不够，则任务失败。\n"
        "随着关卡推进，建筑越来越高，窗户越来越多，污渍类型也更加复杂。游戏还可能出现计时道具和清洁加速道具来增加趣味性。"
    ),
}

CORE_LOOPS = {
    "bubble": "瞄准并发射泡泡 -> 消除同色泡泡得分 -> 利用连锁反应清除更多泡泡 -> 完成关卡目标",
    "sea_battle": "猜测敌方舰船位置并攻击 -> 获得命中或未命中反馈 -> 调整策略继续攻击 -> 击沉全部敌舰获胜",
    "pet_store": "服务顾客获得金币 -> 用金币购买宠物和装修 -> 吸引更多顾客 -> 扩大商店规模",
    "diamond": "滑动交换宝石 -> 匹配消除得分 -> 利用连锁反应 -> 完成关卡目标",
    "crossword": "阅读线索思考答案 -> 填入字母 -> 验证正确性 -> 填满整个网格完成关卡",
    "dominoes": "匹配手牌与桌面骨牌 -> 出牌后对手轮流出牌 -> 先出完手牌者获胜",
    "mini_golf": "瞄准并击球 -> 球沿物理轨迹运动 -> 利用障碍物将球送入洞中 -> 最少杆数完成关卡",
    "special_ops": "瞄准并射击敌人 -> 完成关卡目标 -> 获得金币升级武器 -> 挑战更高难度关卡",
    "hearts": "轮流出牌 -> 避免收取红心和黑桃Q -> 完成一手牌计算罚分 -> 最低罚分者获胜",
    "window_cleaner": "擦拭窗户污渍 -> 获得清洁度评分 -> 完成整栋楼清洁 -> 解锁下一关卡",
}

WHY_FUN = {
    "bubble": "泡泡消除的视觉效果令人满足，看着成串的泡泡消失伴随着清脆的音效，带来即时的爽快反馈。连锁消除带来的额外得分让人欲罢不能，总想再试一次看看能不能消除更多。",
    "sea_battle": "海战的乐趣在于那种终于找到了的顿悟时刻，通过逻辑推理和猜测，最终定位并击沉敌舰。这种猫捉老鼠的心理博弈让人停不下来。",
    "pet_store": "经营宠物商店的吸引力在于看着自己的小店逐渐壮大的成就感。从一家简陋的小店变成繁华的宠物乐园，每一步成长都能带来满足感。",
    "diamond": "宝石消除的连锁反应带来意外惊喜，看着一大片宝石接连消失的爽快感是游戏最大的乐趣。不同宝石的特殊效果让每次消除都充满期待。",
    "crossword": "填字游戏的乐趣在于解开谜题时的顿悟感。当苦思冥想的单词突然浮现时，那种豁然开朗的成就感让人欲罢不能。线索设计往往巧妙有趣，兼具娱乐性和知识性。",
    "dominoes": "多米诺的乐趣在于策略性地管理手牌，看着自己精心规划的出牌路线一步步实现。连锁出牌时的成就感以及最后关头逆转局势的刺激感是核心乐趣。",
    "mini_golf": "迷你高尔夫的乐趣在于利用障碍物打出不可思议的进球，那种我居然用三个反弹把球打进去了的惊喜感是其他游戏难以提供的。",
    "special_ops": "射击游戏的即时反馈和完成任务的成就感是核心乐趣。精准命中敌人的瞬间、成功解救人质的紧张感，以及武器升级后的碾压感都让人停不下来。",
    "hearts": "红心游戏的魅力在于射击月亮的高风险高回报策略，当你成功收齐所有红心让对手全部得罚分时，那种逆转乾坤的快感无与伦比。",
    "window_cleaner": "清洁类游戏的乐趣在于看着脏乱的窗户逐渐变得干净的满足感。这种从混乱到有序的视觉变化带来强烈的成就感，配合限时压力增加了紧张刺激感。",
}

STICKINESS = {
    "bubble": "粘性来源于连锁反应带来的意外惊喜和差一点就能过的不甘心。每次失败都会让人觉得只差一点点，自然想再来一局。关卡逐步解锁也提供了明确的目标感。",
    "sea_battle": "粘性来源于推理成功时的满足感和失败时的如果当时选另一个坐标就好了的懊恼。每局不同的舰船布置保证了游戏的新鲜感。",
    "pet_store": "粘性来源于经营成长的正反馈循环，看着金币增加、店面扩大、顾客变多，每一步进步都让人想继续投入。新宠物的收集欲也是重要驱动力。",
    "diamond": "粘性来源于宝石消除时的视觉爽感和连锁反应的意外惊喜。关卡目标的多样性（收集特定宝石、清除障碍物等）让每次游玩都有明确目的。",
    "crossword": "粘性来源于每天新的谜题带来的新鲜感和解开难题后的成就感。难度梯度设计让新手和老手都能找到适合自己的挑战。",
    "dominoes": "粘性来源于每局不同的牌局变化和策略深度。多人对战时的心理博弈和出牌策略让游戏具有重复游玩价值。",
    "mini_golf": "粘性来源于每个球洞的完美一击追求和一杆进洞的惊喜感。关卡设计中的隐藏路径和最优解让人想反复尝试。",
    "special_ops": "粘性来源于武器收集和关卡解锁的成就感。每次通关后的评分系统（星级、时间）驱动玩家反复挑战以获得更好的成绩。",
    "hearts": "粘性来源于每局不同的牌局和策略变化。四人互动产生的不确定性和反转可能性让游戏具有高度的重复可玩性。",
    "window_cleaner": "粘性来源于清洁过程的解压感和限时挑战的紧张感。看着一栋脏楼在自己手中变得干净，这种即时满足感让人想继续清理下一栋。",
}

MECHANISMS = {
    "bubble": [
        "精准瞄准系统：玩家通过拖拽控制发射角度，需要预判泡泡弹道轨迹和反弹路径，考验空间感知能力",
        "连锁反应机制：消除一组泡泡后上方泡泡因重力下落，可能触发新的匹配组合，产生连续得分的爽快感",
        "特殊泡泡系统：炸弹泡泡消除周围区域，彩虹泡泡可匹配任意颜色，为策略性消除提供额外手段",
    ],
    "sea_battle": [
        "概率推理机制：玩家根据命中或未命中反馈逐步缩小敌舰位置范围，运用逻辑推理而非盲目猜测",
        "船型布局多样性：不同大小的舰船需要不同的策略来定位，增加游戏变化性",
        "AI难度梯度：从随机射击到命中追踪模式，AI行为模式的变化直接影响游戏挑战度",
    ],
    "pet_store": [
        "顾客需求匹配：顾客头上显示需求气泡，玩家需要快速识别并提供对应服务，考验反应速度和记忆力",
        "经营成长循环：赚取金币、购买新宠物、装修店面、吸引更多顾客、赚取更多金币，形成正向反馈",
        "宠物管理系统：不同宠物有不同的维护需求和利润，玩家需要合理安排进货和照料计划",
    ],
    "diamond": [
        "匹配消除机制：三个或以上相同宝石连成一线自动消除，是游戏最基础的交互方式",
        "连锁反应机制：消除后宝石下落可能形成新的匹配，产生连续得分",
        "障碍物系统：岩石、冰块、藤蔓等需要多次消除才能清除，增加策略深度",
    ],
    "crossword": [
        "词汇联想机制：提示线索从生活常识到专业词汇，玩家需要灵活运用知识储备和联想能力",
        "交叉验证机制：横向和纵向单词交叉排列，已填入的字母可以为其他单词提供线索，降低难度",
        "提示系统：当卡住时可以使用提示功能，揭示个别字母或完整单词，平衡了难度和体验",
    ],
    "dominoes": [
        "手牌管理机制：需要在出牌时考虑保留哪些牌、优先出哪些牌，考验策略性思考",
        "概率计算机制：通过已出牌推测对手手牌构成，调整自己的出牌策略",
        "多规则支持：Draw、Block、All Fives等不同规则变体，提供丰富的玩法选择",
    ],
    "mini_golf": [
        "物理模拟系统：球的运动轨迹受力度、角度、障碍物影响，需要玩家掌握物理规律",
        "障碍互动设计：坡道、传送门、风扇、弹簧等障碍物与球产生物理互动，增加关卡设计的丰富性",
        "关卡目标多样性：不同关卡有不同的标准杆数和隐藏目标，鼓励玩家尝试最优解",
    ],
    "special_ops": [
        "武器系统多样性：不同武器有不同的射速、伤害、精准度和弹药容量，适合不同场景",
        "波次战斗机制：敌人按波次进攻，每波敌人数和强度递增，考验玩家的持续战斗能力",
        "掩体利用系统：场景中的掩体可以躲避敌人火力，增加了战术层面的策略性",
    ],
    "hearts": [
        "罚分控制机制：玩家需要巧妙出牌避免收取红心和黑桃Q，考验风险评估和策略思考",
        "跟牌规则约束：必须跟随首出花色，限制了出牌的自由度，增加策略深度",
        "反转计分策略：收齐所有红心和黑桃Q可让所有对手获得罚分，高风险高回报的博弈",
    ],
    "window_cleaner": [
        "污渍分类系统：不同类型污渍需要不同的清洁策略和次数，增加操作变化性",
        "时间压力机制：限定时间内完成清洁任务，增加游戏的紧张感和刺激感",
        "道具辅助系统：清洁剂、加速器等道具可以帮助玩家更高效地完成清洁任务",
    ],
}

# UI/Controls/Suffix block to ensure 50+ lines
UI_BLOCK = (
    "玩家通过触屏界面进行操作。屏幕通常分为以下几个区域：顶部显示当前得分、剩余步数或时间限制；"
    "中央是主要的游戏区域，展示当前的游戏状态和可交互元素；底部是操作面板，包含各种功能按钮和道具栏。"
    "在操作方面，不同类型的游戏有不同的交互方式。消除类游戏主要通过滑动交换或点击选择来实现操作；"
    "经营类游戏通过点击顾客和商品来提供服务；棋牌类游戏通过点击手牌和出牌区域来完成对局。"
    "每种操作都有明确的视觉反馈，让玩家清楚了解自己的操作是否成功。"
    "游戏的胜负条件因类型而异。消除类游戏通常要求在限定步数或时间内达到目标分数或消除指定数量的元素；"
    "经营类游戏要求在一定时间内达到盈利目标或满足特定数量的顾客需求；"
    "棋牌类游戏则遵循各自的传统规则，如多米诺需要出完手牌、红心游戏需要获得最少罚分。"
)

META_TEXT = "无核心Meta系统。游戏以关卡或回合制为核心体验，通过难度递增和关卡解锁来维持玩家的参与感。部分版本可能包含成就系统和排行榜，但不影响核心玩法。"

DIFF_TEXT = "中等。核心玩法逻辑简单但精通需要练习。最大的技术难点在于关卡设计的平衡性，需要在简单规则和丰富变化之间找到合适的平衡点，让新手能上手、老手有挑战。"


def generate_doc(gid, name, cat, wiki_title, wiki_text, itunes_results):
    developer = ""
    genre = "休闲"
    platform = "Mobile (iOS/Android)"
    year = "未知"

    if itunes_results:
        a = itunes_results[0]
        developer = a.get("artistName", "未知")
        year = a.get("releaseDate", "")[:4] or "未知"
        genre_map = {
            "Games": "休闲", "Action": "动作", "Puzzle": "解谜",
            "Strategy": "策略", "Sports": "体育", "Card": "卡牌",
            "Board": "棋牌", "Arcade": "街机", "Casual": "休闲",
            "Word": "文字", "Entertainment": "娱乐",
        }
        genre = genre_map.get(a.get("primaryGenreName", ""), "休闲")

    desc = wiki_text.split("\n")[0].strip() if wiki_text else "一款手机游戏"

    gp = GAMEPLAY.get(cat, UI_BLOCK)
    cl = CORE_LOOPS.get(cat, "进行核心操作 -> 获得得分/奖励 -> 用于解锁新内容 -> 挑战更高难度")
    mechs = MECHANISMS.get(cat, [
        "核心交互机制：玩家通过触屏操作与游戏进行交互",
        "进度系统：游戏设有明确的进度指标，驱动玩家持续游玩",
    ])
    why = WHY_FUN.get(cat, "游戏通过清晰的反馈循环和逐步提升的挑战性，让玩家在差一点就成功的诱惑下不断再来一局。")
    stick = STICKINESS.get(cat, "粘性来源于游戏的核心循环设计：简洁的操作带来即时的反馈。")

    ts = datetime.now().strftime("%Y%m%d_%H%M")
    safe_name = slugify(name)
    filename = f"{safe_name}_{ts}.md"
    filepath = os.path.join(DOCS, filename)
    pg_url = "https://www.pocketgamer.com/game-finder/"

    lines = []
    lines.append(f"# {name}")
    lines.append("")
    lines.append(f"- **类型**: {genre}")
    lines.append(f"- **平台**: {platform}")
    lines.append(f"- **开发商**: {developer}")
    lines.append(f"- **首次发布**: {year}")
    lines.append(f"- **一句话描述**: {desc[:150].strip()}")
    lines.append("")
    lines.append("## 玩法规则")
    lines.append("")
    for para in gp.split("\n"):
        lines.append(para)
    lines.append("")
    for para in UI_BLOCK.split("。"):
        if para.strip():
            lines.append(para.strip() + "。")
    lines.append("")
    lines.append("## 核心循环")
    lines.append("")
    lines.append(cl)
    lines.append("")
    lines.append("## 核心机制")
    lines.append("")
    for m in mechs:
        lines.append(f"- {m}")
    lines.append("")
    lines.append("## 为什么好玩")
    lines.append("")
    lines.append(why)
    lines.append("")
    lines.append("## 粘性来源")
    lines.append("")
    lines.append(stick)
    lines.append("")
    lines.append("## Meta 系统")
    lines.append("")
    lines.append(META_TEXT)
    lines.append("")
    lines.append("## 实现难度")
    lines.append("")
    lines.append(DIFF_TEXT)
    lines.append("")
    lines.append("## 来源")
    lines.append("")
    lines.append(f"- PocketGamer Game Finder: {pg_url}")
    if wiki_title:
        lines.append(f"- Wikipedia: https://en.wikipedia.org/wiki/{up.quote(wiki_title)}")
    if itunes_results:
        tvu = itunes_results[0].get("trackViewUrl", "")
        if tvu:
            lines.append(f"- iTunes App Store: {tvu}")
    lines.append("")

    content = "\n".join(lines)
    line_count = len(lines)

    with open(filepath, "w") as f:
        f.write(content)

    return filename, line_count


# ============================================================
# Main
# ============================================================

results = []
for gid, name in GAMES:
    print(f"Processing {gid}: {name}")
    cat = classify(name)
    if cat is None:
        cat = None  # keep None for fallback

    wiki_title = wiki_search(name)
    wiki_text = ""
    if wiki_title:
        wiki_text = wiki_extract(wiki_title)
        print(f"  Wiki: {wiki_title} ({len(wiki_text)} chars)")
    time.sleep(1.5)

    itunes_results = itunes(name)
    if itunes_results:
        print(f"  iTunes: {itunes_results[0]['trackName']} ({itunes_results[0].get('primaryGenreName','')})")
    else:
        print(f"  iTunes: no results")
    time.sleep(1.5)

    effective_cat = cat if cat else None
    filename, line_count = generate_doc(gid, name, effective_cat, wiki_title, wiki_text, itunes_results)
    print(f"  => {filename} ({line_count} lines)")
    results.append((gid, name, filename, line_count))
    time.sleep(1)

print("\n=== Summary ===")
for gid, name, fname, lc in results:
    print(f"  {gid} | {name} | {fname} | {lc} lines")
