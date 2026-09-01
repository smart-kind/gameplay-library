---
title: Gameplay Discovery Pipeline
original_filename: SKILL
source: gameplay-library
---

---
name: gameplay-discovery-pipeline
category: gaming
description: |
  通用互联网数据收集 pipeline — 维护任务状态队列，批量发现/抓取/归档结构化资料。
  用于小游戏玩法资料收集，也可复用到其他"从互联网批量收集信息并结构化"的场景。
  用户提供输出格式约束（format-constraint.md），pipeline 按格式产出成果到 docs/。
---

# Gameplay Discovery Pipeline

## 触发方式

- Cron job 每 3 小时触发独立 session
- Session 加载此技能，按流程执行
- 技能不依赖对话上下文，唯一状态来源是 `task-queue.md`

## 目录结构

```
/data/games/gameplay-library/
├── pipeline/
│   ├── task-queue.md          # 任务状态表（唯一持久化状态）
│   ├── format-constraint.md   # 输出格式约束
│   └── run.log.md             # 执行步骤日志（每步骤一行，判断执行完整性）
└── docs/                      # 已归档的游戏资料 markdown
```

## 执行流程

### Phase 1: 读取状态

1. `read_file /data/games/gameplay-library/pipeline/task-queue.md`
2. `read_file /data/games/gameplay-library/pipeline/format-constraint.md` 获取输出格式
3. 检查各队列状态，决定本轮执行优先级
4. 生成 run_id（读取 run.log.md 最后一条，ID+1，如 R005）
5. 写入日志：`patch` 追加 `[时间] [Rxxx] [Phase 1: Read State] ✅ 完成 — 来源分布: Pending=N, Processing=N, Archived=N` 到 `run.log.md`

### Phase 2: 发现新来源（如果 Pending Sources 为空或少于 5 个）

1. 使用 `mcp_wigolo_search` 搜索小游戏资料（**注意：每次只传一个字符串 query，不要传数组** — 数组会被 JSON 序列化导致搜索偏离。多组关键词需要分多次调用）
2. 每轮最多 3 组关键词，轮换使用：
   - "best mini games mobile casual 2024 2025"
   - "viral hyper casual games list gameplay mechanics"
   - "indie puzzle game popular gameplay loop"
   - "PopCap classic games list mechanics"
   - "web browser mini games popular addictive"
   - "Google Play trending casual games"
   - "best small games app store hidden gems"
   - "Nintendo Switch indie puzzle casual"
   - "flash games best classic gameplay mechanics"
   - "io games popular mechanics"
   - "roguelike mini games mobile simple"
   - "idle clicker games best mechanics"
3. 每组关键词最多返回 10 个结果
4. 去重检查：如果 URL 已在 Sources（任何状态）中出现过，跳过
5. 新发现的 URL 写入 "Sources Pending"，格式：
   ```
   | S{ID} | search_result | 标题 | URL | {当前时间} |
   ```
   ID 从 S001 开始递增，检查已有最大 ID 继续编号
6. 写入日志：`patch` 追加 `[时间] [Rxxx] [Phase 2: Discover] ✅ 完成 — 搜索N组，发现M个新来源` 到 `run.log.md`（如跳过搜索，写 `⏭️ 跳过 — Pending Sources ≥ 5`）

### Phase 3: 处理 Sources Pending（最多 30 个/轮）

对每个 Pending Source（最多取 30 个）：

1. 移到 "Sources Processing"
2. 使用 `mcp_wigolo_fetch` 抓取页面内容
3. 分析页面内容：
   - **如果是游戏列表页**（包含多个游戏名称+简介）：
     - 提取每个游戏名和相关信息
     - 为每个游戏创建 "Games Pending" 条目
     - 该 Source 移到 "Sources Archived"，记录产出游戏数
   - **如果是单游戏介绍/评测页**：
     - 按 `format-constraint.md` 格式生成游戏文档
     - 文件名：`{游戏名或简称}_{YYYYMMDD_HHmm}.md`
     - 写入 `docs/` 目录
     - 该 Source 移到 "Sources Archived"，产出游戏数=1
   - **如果页面无法访问或内容不相关**：
     - 移到 "Sources Failed"，记录原因
4. 每个任务间间隔 2-3 秒（`terminal` 调用 `sleep 3`）
5. 写入日志：`patch` 追加 `[时间] [Rxxx] [Phase 3: Process Sources] ✅ 完成 — 处理N个来源(S0xx-S0yy)，产出M款游戏，K个失败` 到 `run.log.md`（如跳过，写 `⏭️ 跳过 — Pending Sources 为空`）

### Phase 4: 处理 Games Pending（最多 30 个/轮）

对每个 Pending Game（最多取 30 个）：

1. 使用 `mcp_wigolo_search` 搜索该游戏的详细资料（游戏名 + gameplay mechanics review）
2. 抓取 2-3 个相关页面获取详细信息
3. 按 `format-constraint.md` 格式生成文档
4. 文件名：`{游戏名或简称}_{YYYYMMDD_HHmm}.md`
5. 写入 `docs/` 目录
6. 移到 "Games Archived"
7. 如果搜索无结果或抓取失败，移到 "Games Failed"
8. 写入日志：`patch` 追加 `[时间] [Rxxx] [Phase 4: Process Games] ✅ 完成 — 处理N款游戏，K个失败` 到 `run.log.md`（如跳过，写 `⏭️ 跳过 — Games Pending 为空`）

### Phase 5: Git 提交和推送

1. `terminal: cd /data/games/gameplay-library && git add -A`
2. `terminal: cd /data/games/gameplay-library && git diff --cached --stat`（确认变更）
3. `terminal: cd /data/games/gameplay-library && git commit -m "auto: gameplay discovery run $(date '+%Y-%m-%d %H:%M')"`
4. `terminal: cd /data/games/gameplay-library && git push origin main`
5. 如果 push 失败（网络问题），不阻塞本轮执行
6. 写入日志：`patch` 追加 `[时间] [Rxxx] [Phase 5: Git Push] ✅ 完成` 到 `run.log.md`（如失败，标记 `❌ 失败 — 原因`）

> ~~Phase 5 (Graphify)~~ 已移除：不再同步知识图谱，只做文档收集。如需启用请手动执行 `graphify update .`。

### Phase 6: 更新执行日志

1. 在 task-queue.md 的 Execution Log 中添加一行记录本轮执行情况
2. 写入日志：`patch` 追加 `[时间] [Rxxx] [Phase 6: Update Log] ✅ 完成` 到 `run.log.md`（如失败，标记 `❌ 失败 — 未更新task-queue.md`）

## 工具使用技巧（详见 references/search-pitfalls.md）

- **wigolo_search**: 每次只传单个字符串 query，不要传数组
- **wigolo_fetch**: 缓存可能只返回标题，用 `force_refresh=true` 或切换到 browser 工具
- **Browser 提取**: 用 `browser_console` + `document.querySelectorAll('h2')` 快速提取列表页游戏名
- **批量写入**: 用 `execute_code` 一次性写入多篇文档，效率远高于逐个 write_file

## 用户查询

在 task-queue.md 的 Execution Log 中添加一行记录本轮执行情况

## 关键规则

1. **每次执行上限**：新搜索最多 3 组关键词（每组关键词搜索后 sleep 2-3 分钟），处理 Sources 最多 30 个，处理 Games 最多 30 个
2. **速率控制**：每个网络请求间 sleep 2-3 秒；每次搜索之间 sleep 2-3 分钟（`terminal` 调用 `sleep 120`）
3. **不去重**：同一游戏多次发现也分别生成文档，用时间戳区分文件名
4. **唯一状态**：所有状态在 task-queue.md 中，技能本身不记忆任何游戏名
5. **幂等性**：如果某次执行中断，下次从 task-queue.md 的当前状态继续
6. **不编造**：所有文档内容必须基于实际抓取的内容

## 用户查询

当用户问"收集了多少个游戏了"，读取 task-queue.md 的 Games Archived 行数即可统计。