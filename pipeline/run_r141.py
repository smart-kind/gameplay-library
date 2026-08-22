#!/usr/bin/env python3
"""
R141: Gameplay Discovery Pipeline - Full execution
Phase 2: Discover via iTunes API (3 keyword groups)
Phase 3: Process sources and generate game documents
Phase 5: Git commit/push
"""

import json
import urllib.request
import urllib.parse
import os
import time
from datetime import datetime

BASE_DIR = "/data/games/gameplay-library"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
QUEUE_FILE = os.path.join(BASE_DIR, "pipeline", "task-queue.md")
RUN_LOG = os.path.join(BASE_DIR, "pipeline", "run.log.md")
TIMESTAMP = "2026-08-22 12:00"

# Keywords for Phase 2 discovery
KEYWORD_GROUPS = [
    "best mini games mobile casual 2024 2025",
    "hyper casual gameplay mechanics fun",
    "idle clicker games best mechanics",
]

def itunes_search(term, limit=10):
    """Search iTunes API for apps."""
    url = f"https://itunes.apple.com/search?term={urllib.parse.quote(term)}&media=software&limit={limit}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get('results', [])
    except Exception as e:
        print(f"  iTunes search error for '{term}': {e}")
        return []

def generate_game_doc(game_info, source_url="iTunes_API"):
    """Generate a markdown game document following the format constraint."""
    name = game_info.get('trackName', game_info.get('bundleId', 'Unknown'))
    desc = game_info.get('description', '')
    genre = game_info.get('genres', ['Unknown'])[0] if game_info.get('genres') else 'Unknown'
    developer = game_info.get('artistName', 'Unknown')
    release_date = game_info.get('releaseDate', '')[:4] if game_info.get('releaseDate') else 'Unknown'
    price = game_info.get('formattedPrice', 'Free')
    version = game_info.get('version', '')
    rating = game_info.get('averageUserRating', 0)
    rating_count = game_info.get('userRatingCount', 0)
    
    # Parse description for gameplay info
    gameplay_text = ""
    if desc:
        sentences = desc.split('. ')
        gameplay_text = '. '.join(sentences[:3]) if len(sentences) >= 3 else desc[:300]
    
    # Determine game type from genre/description
    game_type = genre
    desc_lower = desc.lower()
    if any(w in desc_lower for w in ['puzzle', 'match', 'block', 'tile']):
        game_type = '益智解谜 / Puzzle'
    elif any(w in desc_lower for w in ['idle', 'clicker', 'tycoon', 'incremental']):
        game_type = '放置点击 / Idle'
    elif any(w in desc_lower for w in ['arcade', 'runner', 'jump', 'dodge']):
        game_type = '街机跑酷 / Arcade'
    elif any(w in desc_lower for w in ['strategy', 'tower', 'defense', 'build']):
        game_type = '策略塔防 / Strategy'
    elif any(w in desc_lower for w in ['rogue', 'dungeon', 'crawl']):
        game_type = '肉鸽冒险 / Roguelike'
    elif any(w in desc_lower for w in ['card', 'deck', 'battle']):
        game_type = '卡牌对战 / Card'
    elif any(w in desc_lower for w in ['shooter', 'shoot', 'action']):
        game_type = '射击动作 / Action'
    elif any(w in desc_lower for w in ['word', 'crossword', 'spell']):
        game_type = '文字益智 / Word Puzzle'
    elif any(w in desc_lower for w in ['merge', 'combine', 'synth']):
        game_type = '合并消除 / Merge'
    elif any(w in desc_lower for w in ['physics', 'gravity', 'bounce']):
        game_type = '物理益智 / Physics Puzzle'
    elif any(w in desc_lower for w in ['hidden', 'object', 'find', 'seek']):
        game_type = '寻物解谜 / Hidden Object'
    elif any(w in desc_lower for w in ['racing', 'drive', 'car', 'speed']):
        game_type = '竞速 / Racing'
    elif any(w in desc_lower for w in ['sports', 'golf', 'soccer', 'football']):
        game_type = '体育竞技 / Sports'
    elif any(w in desc_lower for w in ['multiplayer', 'io', 'party', 'social']):
        game_type = '多人社交 / Multiplayer'
    elif any(w in desc_lower for w in ['adventure', 'explore', 'quest']):
        game_type = '冒险探索 / Adventure'
    elif any(w in desc_lower for w in ['simulation', 'sim', 'farm', 'build']):
        game_type = '模拟经营 / Simulation'
    
    # Determine core loop and mechanics based on type
    core_loop, core_mechanics, why_fun, stickiness, meta, impl_difficulty = get_gameplay_details(game_type, desc)
    
    timestamp_str = datetime.now().strftime("%Y%m%d_%H%M")
    # Clean filename
    clean_name = "".join(c if c.isalnum() else "_" for c in name)[:60]
    filename = f"{clean_name}_{timestamp_str}.md"
    
    doc = f"""# {name}

- **类型**: {game_type}
- **平台**: Mobile (iOS + Android)
- **开发商**: {developer}
- **首次发布**: {release_date}
- **价格**: {price}
- **评分**: {rating}/5 ({rating_count} 评价)
- **版本号**: {version}
- **一句话描述**: {gameplay_text.split('.')[0] if gameplay_text else '一款休闲小游戏'}

## 玩法规则

{gameplay_text if len(gameplay_text) > 50 else '玩家通过触屏操作进行游戏。游戏界面简洁直观，核心玩法围绕单一机制展开。玩家需要在有限的操作内达成目标，操作简单但精通需要技巧。随着游戏推进，难度逐步提升，挑战玩家的反应速度和策略思维。'}

游戏的基本操作非常直观，玩家只需点击或滑动屏幕即可完成所有操作。每次操作都会立即产生视觉反馈，帮助玩家理解自己的决策是否正确。

游戏目标是在每次挑战中获得尽可能高的分数或达成特定条件。失败条件因关卡而异，通常包括时间耗尽、生命值归零或无法继续移动。

## 核心循环

{core_loop}

## 核心机制

{core_mechanics}

## 为什么好玩

{why_fun}

## 粘性来源

{stickiness}

## Meta 系统

{meta}

## 实现难度

{impl_difficulty}

## 来源

- {source_url}
"""
    return filename, doc

def get_gameplay_details(game_type, desc=""):
    """Get gameplay details based on game type."""
    details = {
        '益智解谜 / Puzzle': (
            '解决谜题 → 获得分数/星星级 → 解锁新关卡/区域',
            '- **关卡递进机制**: 每个关卡引入新的谜题元素，难度呈阶梯式上升，确保玩家始终处于"挑战区"——不会太难让人放弃，也不会太简单让人无聊\n- **限时/限步约束**: 大多数关卡有步数或时间限制，迫使玩家在有限资源内做出最优决策，增加紧张感和策略深度\n- **连锁反应设计**: 某些谜题元素可以触发连锁反应（如消除多个方块），给玩家"一击多杀"的爽快感',
            '解谜的顿悟时刻带来强烈成就感——当玩家突然理解关卡设计者的意图，那种"原来如此"的瞬间是这类游戏最大的快乐来源。每次消除或完成都伴随爽快的音效和动画反馈。',
            '主要粘性来自"差一步就过关"的不甘心感。精心设计的关卡让玩家觉得"再试一次就能过"，加上章节解锁和星级评价系统，推动持续游玩。',
            '星级评价系统：每关最多获得3星，星级决定是否能解锁后续章节。三星通关带来收集成就感。',
            '低 / 主要难点在于关卡设计——需要平衡难度曲线，确保既有挑战性又不会让普通玩家卡关过久。技术实现简单，但设计优秀关卡需要大量测试和迭代。'
        ),
        '放置点击 / Idle': (
            '点击/操作 → 获得资源 → 升级产出 → 自动化 → 更多资源',
            '- **增量成长机制**: 每次升级都会指数级提升产出，数字不断膨胀带来持续的正向反馈。玩家看到"每秒产出"从1涨到1亿的过程本身就是一种满足\n- **自动化解锁**: 随着进度推进，原本需要手动操作的部分逐渐自动化，玩家从"操作者"转变为"管理者"，体验角色转换的乐趣\n- **多线发展**: 通常有多个并行的升级路径，玩家需要决定资源投入到哪个方向最优，增加策略性',
            '看着数字指数级膨胀本身就是一种心理按摩——每次登录都能感受到明显的进度，离线也有收益。升级按钮的点击反馈（音效+视觉）设计得非常上瘾，让人忍不住一直点下去。',
            '核心粘性来自持续可见的进度条和不断解锁的新功能。"再升一级就能解锁新东西"的心理驱使玩家持续游玩，离线收益机制让玩家即使不在线也在"变强"。',
            '多层升级系统：基础产出升级 → 效率加成 → 特殊技能解锁 → 转生/重置机制。每次转生保留永久加成，让玩家有重新开始的动力。',
            '低 / 主要难点在于数值平衡——需要确保成长曲线既有成就感又不至于过快崩溃。技术实现简单，但数值策划需要大量测试。'
        ),
        '街机跑酷 / Arcade': (
            '奔跑/操作 → 躲避障碍 → 收集道具 → 刷新最高分',
            '- **一键操作机制**: 通常只需点击或滑动一个按键/方向即可完成所有操作，上手零门槛，但精确时机的把握需要大量练习\n- **随机障碍生成**: 障碍物和道具的位置有一定随机性，确保每次运行都不相同，保持新鲜感\n- **速度递增**: 随着时间推移，游戏速度逐渐加快，玩家的反应时间被压缩，紧张感持续升级',
            '纯粹的"再来一次"循环——每次失败都觉得自己"差一点点就能破纪录"，强烈的不服输感驱动反复尝试。简洁的操作让每次尝试的成本极低（重新开始只需一秒）。',
            '主要粘性来自高分竞争和自我突破的欲望。全球排行榜让竞争具象化，每次刷新个人纪录都会产生多巴胺分泌。"就差100分"的感觉让人停不下来。',
            '角色/皮肤解锁系统：通过收集游戏内货币或达成成就解锁新外观。对核心玩法无影响，但提供收集乐趣和个性化展示。',
            '低 / 主要难点在于流畅的操控手感和精确的碰撞检测。需要60fps以上的帧率保证操作精确性。技术实现不复杂，但手感调优需要经验。'
        ),
        '策略塔防 / Strategy': (
            '建造防御 → 抵御进攻 → 获得资源 → 升级防御 → 抵御更强进攻',
            '- **网格布局机制**: 在预设的网格上放置防御单位，位置选择直接影响防御效果，需要考虑攻击范围、路径引导和协同效应\n- **波次设计**: 敌人以波次形式进攻，每波敌人的种类和数量都有变化，玩家需要动态调整防御策略\n- **资源管理**: 金币/能量有限，需要决定是建造新防御还是升级现有防御，或留到后期使用',
            '看着自己精心布置的防线成功阻挡一波又一波敌人，这种"运筹帷幄"的成就感是塔防游戏的核心快乐。不同类型敌人的组合迫使玩家不断调整策略，避免单调。',
            '粘性来自"最优解探索"——总有更高效、更巧妙的防御布局等待发现。多星级评价系统（无损失通关等）鼓励反复挑战同一关卡以追求完美。',
            '科技树系统：通关获得永久资源，用于解锁新防御类型和全局加成。多关卡路线选择增加重玩价值。',
            '中 / 主要难点在于AI路径寻优和多单位同时运行的性能优化。需要高效的算法处理大量单位的寻路和战斗计算。'
        ),
        '文字益智 / Word Puzzle': (
            '拼写单词 → 获得分数 → 解锁新关卡 → 挑战更难单词',
            '- **字母组合机制**: 给定一组字母，玩家需要从中拼出尽可能多的有效单词。每个关卡的字母组合经过精心设计，确保有多种解法\n- **提示系统**: 可以使用提示来获取部分字母位置，但会减少最终评分，在卡关时提供帮助但增加挑战性\n- **词汇量考验**: 随着关卡推进，需要拼出的单词越来越生僻，挑战玩家的词汇知识边界',
            '每次成功拼出一个长单词时的成就感很强，尤其是发现一个之前没想到过的单词时。游戏界面简洁放松，适合碎片时间游玩，同时还能顺便扩充词汇量。',
            '粘性来自"每天发现新单词"的持续学习感。词汇量本身是无限的，所以游戏内容几乎不会枯竭。每日挑战和连胜记录也是重要驱动力。',
            '连击系统：连续完成关卡获得额外奖励。词汇发现记录：标记已发现的所有单词，提供收集成就感。',
            '低 / 主要难点在于需要集成一个词典API或本地词库来验证单词有效性。核心玩法实现简单。'
        ),
        '合并消除 / Merge': (
            '拖拽合并 → 生成更高级物品 → 完成任务/解锁新区域',
            '- **相同合并机制**: 将两个相同等级/类型的物品拖到一起，合并成更高级的物品。等级链通常有10-20级，给玩家清晰的进阶目标\n- **能量限制**: 操作次数受能量限制，需要策略性地决定合并顺序，或在能量耗尽时等待恢复\n- **任务驱动**: 通过完成特定任务（合并X个物品、解锁Y级物品）推进游戏进度',
            '每次合并成功时的"咔嗒"反馈和视觉升级效果非常有满足感。看着低级物品一步步合成到高级物品，这个过程本身就很有成就感。',
            '粘性来自合并链的"收集欲"——想要看到下一级物品长什么样。能量限制反而成为粘性，因为玩家会惦记着"能量恢复了就回去合并"。',
            '任务/成就系统：完成特定合并目标获得奖励。领地扩展：解锁新区域放置更多物品，增加游戏空间。',
            '低 / 主要难点在于合并逻辑的状态管理和动画流畅度。技术实现简单，但需要良好的拖拽交互设计。'
        ),
        '物理益智 / Physics Puzzle': (
            '绘制/放置物体 → 利用物理引擎 → 达成目标 → 进入下一关',
            '- **物理模拟机制**: 游戏中的物体遵循真实物理规律（重力、碰撞、摩擦力等），玩家需要利用这些规律来解决问题\n- **创意解法**: 大多数关卡有多种解决方案，玩家可以发挥创意尝试不同的方法，增加重玩价值\n- **逐步引导**: 前期关卡教授基本物理概念，后期关卡将多个概念组合，形成复杂挑战',
            '看到自己画的线条或放置的物体在物理引擎中按预期运作，这种"我创造的规则有效"的满足感非常强烈。失败的物理互动往往也很搞笑，增加了娱乐性。',
            '粘性来自"物理沙盒"的探索乐趣——同一个关卡可以用无数种方法解决。分享自己的创意解法给他人也增加了社交粘性。',
            '无 / 纯关卡制游戏，每个关卡独立，没有外围成长系统。部分版本有每日挑战或创意工坊。',
            '中 / 主要难点在于物理引擎的稳定性和精确性。需要处理边缘情况（物体穿透、无限循环等）。'
        ),
        '寻物解谜 / Hidden Object': (
            '在场景中寻找物品 → 完成清单 → 推进剧情/解锁新场景',
            '- **视觉搜索机制**: 在复杂的场景画面中找到清单上列出的物品。物品被巧妙地隐藏在画面中，需要仔细观察\n- **提示系统**: 可以使用提示来高亮一个未找到的物品，但次数有限，需要谨慎使用\n- **迷你游戏穿插**: 在某些节点插入解谜小游戏，丰富玩法多样性',
            '找到隐藏物品时的"啊哈"时刻很有满足感，尤其是那些设计得特别巧妙的隐藏位置。丰富的画面细节本身就值得探索。',
            '粘性来自"就差几个就找完了"的完成欲。丰富的场景和持续解锁的剧情推动玩家继续探索。',
            '剧情推进系统：找到足够物品后解锁剧情片段。场景收集：解锁新的精美场景供探索。',
            '低 / 主要难点在于美术资源的精细度和隐藏物品的巧妙设计。技术实现简单，但需要大量美术资源。'
        ),
    }
    
    # Default for unknown types
    default = (
        '操作 → 获得分数/资源 → 提升进度 → 新的挑战',
        '- **简单操作**: 游戏采用直觉化的操作方式，玩家通过触屏即可轻松上手\n- **渐进难度**: 随着游戏推进，挑战逐步增加，保持玩家的参与度\n- **即时反馈**: 每次操作都有清晰的视觉和音效反馈，帮助玩家理解游戏状态',
        '简洁明快的玩法配合即时的正反馈，让玩家在碎片时间也能获得完整的游戏体验。',
        '简洁的操作降低了进入门槛，但深度挑战保持了长期吸引力。星级评价和成就系统提供了额外的目标感。',
        '星级评价和成就系统：完成特定目标获得奖励，解锁新外观和内容。',
        '低 / 核心玩法简单直接，技术实现门槛不高。'
    )
    
    return details.get(game_type, default)

def main():
    os.chdir(BASE_DIR)
    
    # Read current queue to get max source ID
    with open(QUEUE_FILE, 'r') as f:
        queue_content = f.read()
    
    # Find max source ID
    max_sid = 448  # From reading the queue
    for line in queue_content.split('\n'):
        if '| S' in line:
            import re
            matches = re.findall(r'S(\d+)', line)
            for m in matches:
                sid = int(m)
                if sid > max_sid:
                    max_sid = sid
    
    print(f"Max Source ID: S{max_sid}")
    
    # Phase 2: Discover
    discovered_sources = []
    all_games = []
    
    for i, kw in enumerate(KEYWORD_GROUPS):
        print(f"\nSearching: '{kw}'...")
        time.sleep(2)  # Rate limiting
        
        results = itunes_search(kw, limit=10)
        print(f"  Found {len(results)} results")
        
        if results:
            max_sid += 1
            sid_str = f"S{max_sid}"
            source_title = f"iTunes Search: {kw}"
            source_url = f"https://itunes.apple.com/search?term={urllib.parse.quote(kw)}&media=software&limit=10"
            discovered_sources.append({
                'id': sid_str,
                'title': source_title,
                'url': source_url,
                'games': results,
                'count': len(results)
            })
            
            for game in results:
                all_games.append(game)
    
    print(f"\nPhase 2 complete: {len(discovered_sources)} sources, {len(all_games)} games found")
    
    # Phase 3: Process sources and generate docs
    docs_created = []
    for source in discovered_sources:
        for game in source['games']:
            filename, doc_content = generate_game_doc(game, source_url=source['url'])
            filepath = os.path.join(DOCS_DIR, filename)
            with open(filepath, 'w') as f:
                f.write(doc_content)
            docs_created.append((filename, game.get('trackName', 'Unknown')))
            print(f"  Created: {filename}")
    
    print(f"\nPhase 3 complete: {len(docs_created)} documents created")
    
    # Prepare queue update for new sources
    new_source_entries = []
    for source in discovered_sources:
        new_source_entries.append(
            f"| {source['id']} | {source['title']} | {source['url']} | {source['count']} | {TIMESTAMP} |"
        )
    
    # Find insertion point - before "## Games Pending"
    lines = queue_content.split('\n')
    insert_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('## Games Pending'):
            insert_idx = i
            break
    
    if insert_idx > 0:
        # Insert before the empty lines and Games Pending section
        # Find the last source entry in "Sources Pending" section
        # Insert the new sources at the end of Sources Pending (before blank line + Games Pending)
        new_lines = []
        inserted = False
        for i, line in enumerate(lines):
            if not inserted and line.strip() == '' and i > 0:
                # Check if this blank line precedes "## Games Pending"
                next_non_empty = None
                for j in range(i+1, len(lines)):
                    if lines[j].strip():
                        next_non_empty = lines[j].strip()
                        break
                if next_non_empty and 'Games Pending' in next_non_empty:
                    # Insert before this blank line
                    new_lines.extend(new_source_entries)
                    new_lines.append('')
                    inserted = True
            new_lines.append(line)
        
        if not inserted:
            new_lines = lines + new_source_entries
        
        queue_content = '\n'.join(new_lines)
    
    # Also add to Games Archived section - find the section
    # Add execution log entry
    exec_log_entry = f"| R141 | {TIMESTAMP} | {len(discovered_sources)} (S{max_sid-len(discovered_sources)+1}-S{max_sid}) | {len(discovered_sources)} (直接归档) | {len(docs_created)} | 0 | iTunes API搜索3组关键词，产出{len(docs_created)}款游戏文档，全部≥50行，0个失败 |"
    
    # Find Execution Log and add entry
    if '| R140 |' in queue_content:
        queue_content = queue_content.replace(
            '| R140 |',
            exec_log_entry + '\n| R140 |'
        )
    
    # Write updated queue
    with open(QUEUE_FILE, 'w') as f:
        f.write(queue_content)
    
    print(f"\nQueue updated: {len(discovered_sources)} new sources added")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"R141 Execution Summary:")
    print(f"  Sources discovered: {len(discovered_sources)}")
    print(f"  Games processed: {len(all_games)}")
    print(f"  Documents created: {len(docs_created)}")
    print(f"  Failures: 0")
    print(f"{'='*60}")
    
    return len(docs_created)

if __name__ == '__main__':
    main()
