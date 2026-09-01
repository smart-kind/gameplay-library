---
name: game-design-generator
version: 1.0.0
description: >
  基于 docgraph 知识库，每小时自动生成 1 个游戏创意文档。
  包含完整玩法设计、SVG 布局图、12维度评分、自动入榜。
  所有产出跟随仓库版本控制。
author: david-crazyamber
---

# SKILL: 游戏创意生成器

## 概述

从 gameplay-library 知识库中分析已有游戏组合模式，生成**1 个**全新的游戏创意文档，含完整评分并自动入榜。

**执行频率**：每小时 1 次（cron 驱动）
**工作目录**：`/data/workspace/gameplay-library/`
**输出目录**：`design/batches-v2/`

## 前置依赖

### 1. docgraph 知识库（子工具）

知识库已注册在 `~/.docgraph/config.json`：
```json
{
  "knowledgeBases": {
    "games": {
      "name": "games",
      "dir": "/data/workspace/gameplay-library",
      "graphPath": "/data/workspace/gameplay-library/graph-out/graph.json"
    }
  },
  "defaultKB": "games"
}
```

常用查询命令：
```bash
# 查类型频率（找大众玩法）
docgraph query "塔防" --kb games --format json

# 查两个概念是否有关联
docgraph path "物理弹射" "卡牌" --kb games

# 看某个游戏的完整信息
docgraph explain "愤怒的小鸟" --kb games
```

### 2. 知识库数据源

`docs/` 目录包含约 4000 个游戏文档，是只读数据源。不要修改。

## 执行步骤

### Step 0: 环境确认

```bash
cd /data/workspace/gameplay-library/
git pull origin main
```

### Step 1: 读取已有游戏（避免重复）

```bash
ls design/batches-v2/game-*.md 2>/dev/null | sort
```

记录已有游戏的编号和核心组合，确保新游戏不重复。

**已有游戏列表示例**：
| 编号 | 游戏名 | 核心组合 |
|------|--------|---------|
| 01 | 合并守卫者 | 2048合并+塔防 |
| 02 | 连线法师 | 连线消除+法术 |
| ... | ... | ... |

### Step 2: 分析知识库找灵感

用 docgraph 查询以下方向（选 1-2 个）：

1. **高频大众类型**：`docgraph query "塔防"`、`docgraph query "消除"`
2. **创新组合**：找两个看似无关但有连接点的类型
3. **参考成功游戏**：`docgraph explain "某个爆款"` 学习其机制

**目标**：找到一个**未被已有游戏覆盖**的核心组合。

### Step 3: 生成游戏创意文档

写入文件：`design/batches-v2/game-XX-游戏名.md`

编号规则：按已有编号递增（01→02→03...），不足两位补零。

**文档必须包含以下章节**：

#### 一、界面布局（SVG 嵌入）

用纯 SVG 代码画出游戏主界面，嵌入 Markdown：

```markdown
<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 这里放完整的 SVG 代码 -->
</svg>
```

**SVG 规范**：
- 尺寸 360×640（竖屏手机）
- 展示核心玩法的界面元素
- 用简单几何图形（rect/circle/text/line）
- 配色鲜明，区分功能区域

#### 二、基础信息

```markdown
| 项目 | 内容 |
|------|------|
| 游戏名 | XXX |
| 核心组合 | A玩法 + B玩法 |
| 一句话描述 | 15字以内说清怎么玩 |
| 目标平台 | iOS/Android |
| 单局时长 | X分钟 |
```

#### 三、核心玩法

- **操作方式**：玩家具体做什么（点击/拖动/滑动）
- **胜利条件**：怎么赢
- **失败条件**：怎么输
- **核心循环**：一步操作→发生什么→下一步

#### 四、局内成长

单局内的数值/能力提升，举例：
- 杀敌→金币→买升级
- 三消→连击→分数倍增
- 选择 buff（3选1）

#### 五、Meta Game

跨局的持久系统：
- 解锁新角色/皮肤/模式
- 排行榜
- 每日挑战
- 赛季/活动

#### 六、广告变现

| 插入时机 | 广告类型 | 说明 |
|---------|---------|------|
| 关卡完成 | 插屏 | 正向情绪点 |
| 关卡失败 | 激励视频 | 复活/继续 |
| Meta界面 | 激励视频 | 双倍奖励 |

#### 七、12维度评分卡

**评分规则**：每个维度 1-5 分，必须引用上文具体描述作为依据，禁止空泛打分。

| 维度 | 权重 | 评分 | 依据（必须引用上文） |
|------|------|------|---------------------|
| 受众广度 | 15% | X | 引用：单指操作/大众类型/... |
| 上手速度 | 15% | X | 引用：3秒理解/... |
| 常玩常新 | 12% | X | 引用：随机生成/... |
| 局内成长 | 10% | X | 引用：杀敌→升级/... |
| 无UI可验证 | 10% | X | 引用：离散状态/数值驱动/... |
| AI开发难度 | 10% | X | 引用：2D/状态机/JSON配置/... |
| 广告变现友好度 | 8% | X | 引用：关卡完成插屏/失败激励/... |
| 玩法新鲜度 | 5% | X | 引用：少见组合/... |
| 用户粘性 | 5% | X | 引用：差一点就过/... |
| 受众规模 | 5% | X | 引用：休闲类型/低配置/... |
| 难度递增 | 3% | X | 引用：波次递进/章节解锁/... |
| 局外Meta | 2% | X | 引用：角色解锁/排行榜/... |
| **加权总分** | 100% | **X.XX** | — |

**加权公式**：
```
总分 = Σ(评分 × 权重)
```

**目标**：总分 ≥ 3.8

### Step 4: 更新总榜

读取 `design/batches-v2/summary-总榜.md`，把新游戏加入总榜表格。

**规则**：每批只取最高分进入总榜（但现在是每小时1个，每个都进总榜）。

总榜表格格式：
```markdown
| 排名 | 批次 | 游戏名称 | 核心组合 | 总分 | 受众 | 上手 | 常新 | 成长 | 验证 | AI难度 | 广告 |
|------|------|---------|---------|------|------|------|------|------|------|--------|------|
```

### Step 5: Git 提交并推送

```bash
cd /data/workspace/gameplay-library/
git add design/batches-v2/
git commit -m "feat(game-XX): add 游戏名 design doc, score: X.XX"
git push origin main
```

**提交信息规范**：
- `feat(game-XX): add 游戏名 design doc, score: X.XX`

### Step 6: 删除触发标记

```bash
rm -f design/batches/.trigger-next
```

## 失败处理

如果某个步骤失败：
1. **记录错误**：写到 `design/batches/generate.log`
2. **不要删除触发标记**：下次 cron 会重试
3. **不要推送半成品**：只推送完整文档

## 关键约束

1. **1 个游戏/小时**，不要多生成
2. **SVG 必须内嵌**，不要用 base64 PNG
3. **评分必须引用具体描述**
4. **避免与已有游戏重复**
5. **工作目录必须是 `/data/workspace/gameplay-library/`**
6. **推送到 `origin main`**

## 已有游戏记录

执行前必须先读取此文件更新已有列表：

```bash
cat design/batches-v2/summary-总榜.md
ls design/batches-v2/game-*.md | sort
```
