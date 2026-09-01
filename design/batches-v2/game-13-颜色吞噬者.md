# 颜色吞噬者 (Color Devourer) — 完整创意文档

> 核心组合：颜色匹配 + 吞噬扩张
> 预估总分：**4.08**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 背景 -->
  <rect width="360" height="640" fill="#1a1a2e"/>
  
  <!-- 顶部状态栏 -->
  <rect x="0" y="0" width="360" height="50" fill="#16213e"/>
  <text x="20" y="32" fill="#eee" font-size="14" font-family="sans-serif">第 15 关</text>
  <text x="180" y="32" text-anchor="middle" fill="#3498db" font-size="16" font-family="sans-serif" font-weight="bold">🎨 蓝队 45%</text>
  <text x="340" y="32" text-anchor="end" fill="#e74c3c" font-size="14" font-family="sans-serif">红队 38%</text>
  
  <!-- 游戏区域 - 六边形网格 -->
  <rect x="10" y="60" width="340" height="400" fill="#0f3460" rx="8"/>
  
  <!-- 六边形网格 - 8x8 -->
  <!-- 蓝色领地 -->
  <polygon points="55,85 75,85 85,102 75,119 55,119 45,102" fill="#3498db" opacity="0.8" stroke="#2980b9" stroke-width="2"/>
  <polygon points="95,85 115,85 125,102 115,119 95,119 85,102" fill="#3498db" opacity="0.8" stroke="#2980b9" stroke-width="2"/>
  <polygon points="135,85 155,85 165,102 155,119 135,119 125,102" fill="#3498db" opacity="0.8" stroke="#2980b9" stroke-width="2"/>
  
  <!-- 红色领地 -->
  <polygon points="255,85 275,85 285,102 275,119 255,119 245,102" fill="#e74c3c" opacity="0.8" stroke="#c0392b" stroke-width="2"/>
  <polygon points="295,85 315,85 325,102 315,119 295,119 285,102" fill="#e74c3c" opacity="0.8" stroke="#c0392b" stroke-width="2"/>
  
  <!-- 中立区域 -->
  <polygon points="175,85 195,85 205,102 195,119 175,119 165,102" fill="#2c3e50" stroke="#34495e" stroke-width="1"/>
  <polygon points="215,85 235,85 245,102 235,119 215,119 205,102" fill="#2c3e50" stroke="#34495e" stroke-width="1"/>
  
  <!-- 更多蓝色 -->
  <polygon points="55,119 75,119 85,136 75,153 55,153 45,136" fill="#3498db" opacity="0.8" stroke="#2980b9" stroke-width="2"/>
  <polygon points="95,119 115,119 125,136 115,153 95,153 85,136" fill="#3498db" opacity="0.8" stroke="#2980b9" stroke-width="2"/>
  <polygon points="135,119 155,119 165,136 155,153 135,153 125,136" fill="#3498db" opacity="0.8" stroke="#2980b9" stroke-width="2"/>
  
  <!-- 更多红色 -->
  <polygon points="215,119 235,119 245,136 235,153 215,153 205,136" fill="#e74c3c" opacity="0.8" stroke="#c0392b" stroke-width="2"/>
  <polygon points="255,119 275,119 285,136 275,153 255,153 245,136" fill="#e74c3c" opacity="0.8" stroke="#c0392b" stroke-width="2"/>
  <polygon points="295,119 315,119 325,136 315,153 295,153 285,136" fill="#e74c3c" opacity="0.8" stroke="#c0392b" stroke-width="2"/>
  
  <!-- 中部争夺区 -->
  <polygon points="75,153 95,153 105,170 95,187 75,187 65,170" fill="#2c3e50" stroke="#f39c12" stroke-width="2"/>
  <polygon points="115,153 135,153 145,170 135,187 115,187 105,170" fill="#2c3e50" stroke="#f39c12" stroke-width="2"/>
  <polygon points="155,153 175,153 185,170 175,187 155,187 145,170" fill="#2c3e50" stroke="#f39c12" stroke-width="2"/>
  <polygon points="195,153 215,153 225,170 215,187 195,187 185,170" fill="#2c3e50" stroke="#f39c12" stroke-width="2"/>
  <polygon points="235,153 255,153 265,170 255,187 235,187 225,170" fill="#2c3e50" stroke="#f39c12" stroke-width="2"/>
  <polygon points="275,153 295,153 305,170 295,187 275,187 265,170" fill="#2c3e50" stroke="#f39c12" stroke-width="2"/>
  
  <!-- 玩家当前选中区域高亮 -->
  <polygon points="115,153 135,153 145,170 135,187 115,187 105,170" fill="none" stroke="#f39c12" stroke-width="3" stroke-dasharray="4,2"/>
  
  <!-- 颜色选择器 -->
  <text x="180" y="210" text-anchor="middle" fill="#f39c12" font-size="12" font-family="sans-serif">点击相邻同色区域吞噬扩张</text>
  
  <!-- 底部控制区 -->
  <rect x="10" y="470" width="340" height="160" fill="#16213e" rx="8"/>
  <text x="180" y="495" text-anchor="middle" fill="#888" font-size="12" font-family="sans-serif">点击自己的领地，再点击相邻区域扩张</text>
  
  <!-- 技能按钮 -->
  <rect x="30" y="515" width="70" height="40" fill="#e74c3c" rx="6"/>
  <text x="65" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">狂暴</text>
  <text x="65" y="550" text-anchor="middle" fill="#aaa" font-size="9">×2</text>
  
  <rect x="110" y="515" width="70" height="40" fill="#3498db" rx="6"/>
  <text x="145" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">染色</text>
  <text x="145" y="550" text-anchor="middle" fill="#aaa" font-size="9">×3</text>
  
  <rect x="190" y="515" width="70" height="40" fill="#9b59b6" rx="6"/>
  <text x="225" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">转换</text>
  <text x="225" y="550" text-anchor="middle" fill="#aaa" font-size="9">×1</text>
  
  <rect x="270" y="515" width="70" height="40" fill="#f39c12" rx="6"/>
  <text x="305" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">护盾</text>
  <text x="305" y="550" text-anchor="middle" fill="#aaa" font-size="9">×2</text>
  
  <!-- 领地对比条 -->
  <rect x="30" y="570" width="300" height="20" fill="#333" rx="10"/>
  <rect x="30" y="570" width="135" height="20" fill="#3498db" rx="10"/>
  <rect x="165" y="570" width="114" height="20" fill="#e74c3c" rx="10"/>
  <text x="97" y="584" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">45%</text>
  <text x="222" y="584" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">38%</text>
  
  <text x="180" y="620" text-anchor="middle" fill="#aaa" font-size="11" font-family="sans-serif">目标: 占领 70% 领地 | 回合: 12/20</text>
</svg>

---

## 二、核心玩法

### 一句话描述
点击自己的领地，再点击相邻区域进行颜色吞噬扩张，与 AI 对手争夺版图，率先占领 70% 区域获胜。

### 详细规则

**棋盘**：六边形蜂窝网格，10×10，共 100 个格子。

**初始状态**：
- 玩家（蓝色）：左下角 3×3 区域
- 敌方 AI（红色）：右上角 3×3 区域
- 其余为中立区域（灰色）

**回合制**：
1. 玩家点击自己的任意一个领地格子
2. 再点击与该格子相邻的 6 个格子之一
3. 如果目标格子是中性或敌方领地，进行"吞噬判定"
4. 吞噬判定：玩家领地数 vs 目标格子周围敌方领地数
   - 玩家占优（≥50%相邻格子为己方）→ 成功吞噬
   - 敌方占优 → 吞噬失败，玩家失去出击格子
   - 平局 → 双方各失去该格子（变为中立）
5. 敌方 AI 回合，同样的规则

**连锁吞噬**：
- 成功吞噬后，如果新领地周围有其他可吞噬格子，可继续吞噬（连锁）
- 连锁上限：初始 2 次，可通过升级增加

**边界优势**：
- 位于棋盘边缘的领地：吞噬判定+1 优势
- 位于角落的领地：吞噬判定+2 优势

---

## 三、局内成长

**领地等级**：
- 每块被占领的领地有等级（Lv.1-Lv.3）
- Lv.1：基础吞噬力
- Lv.2：吞噬判定+1（需要该领地连续 3 回合未被攻击）
- Lv.3：吞噬判定+2，且被吞噬时敌方需多判定一次（需要 5 回合）

**技能系统**：
| 技能 | 效果 | 冷却 |
|------|------|------|
| 狂暴 | 下回合吞噬判定×2 | 3 回合 |
| 染色 | 将一个中立格子直接变为己方 | 2 回合 |
| 转换 | 将一个敌方 Lv.1 领地转换为中立 | 5 回合 |
| 护盾 | 一个领地免疫下次吞噬 | 2 回合 |

**连击奖励**：
- 连续吞噬 3 个格子 → 下回合可多行动 1 次
- 连续吞噬 5 个格子 → 所有领地临时升级 1 级（持续 2 回合）
- 一回合内吞噬敌方核心领地（初始 3×3 中心）→ 敌方全领地降级 1 级

**难度递增**：
- 前 5 关：AI 随机选择目标
- 6-15 关：AI 优先攻击玩家高等级领地
- 16 关后：AI 会使用技能，优先占领边界
- Boss 关：AI 初始领地×2，需要占领 80% 才能赢

---

## 四、Meta Game（局外系统）

**关卡系统**：
- 共 100 关，分 5 个主题（草地→沙漠→雪地→岩浆→星空）
- 每主题 20 关，棋盘形状不同（标准/环形/岛屿/分裂/迷宫）

**颜色皮肤**：
| 皮肤 | 解锁条件 |
|------|---------|
| 火焰 | 通过第20关 |
| 冰霜 | 通过第40关 |
| 自然 | 通过第60关 |
| 虚空 | 通过第80关 |
| 彩虹 | 通过第100关 |

**策略家等级**：
- 升级解锁：更大初始领地、更高连锁上限、更快技能冷却
- 天赋树：
  - 侵略路线：吞噬判定加成、攻击连锁增加
  - 防守路线：领地升级加速、护盾持续时间增加
  - 平衡路线：初始资源增加、技能冷却减少

**无尽模式**：
- 与无限波次 AI 对战，每波 AI 智能提升
- 全球排行榜：比谁坚持的波次最多

**每日挑战**：
- "极速模式"：每回合限时 5 秒
- "大地图"：20×20 超大棋盘
- "单色模式"：只能使用一种技能
- "反向模式"：初始只有 1 个格子，需要反向扩张

---

## 五、广告变现

**自然断点设计**：

| 断点类型 | 时机 | 广告形式 | 预估 eCPM |
|---------|------|---------|----------|
| 关卡完成 | 每关结束（约3-5分钟） | 插屏广告 | $8-12 |
| 关卡失败 | 敌方占领 70% | 激励视频（重来） | $15-25 |
| 技能冷却 | 急需技能 | 激励视频（重置冷却） | $10-15 |
| 撤销操作 | 误操作 | 激励视频（撤销上步） | $8-12 |
| 双倍金币 | 关卡结算 | 激励视频（2倍金币） | $10-15 |

**广告频率控制**：
- 每 2 关强制插屏 1 次
- 激励视频每局限 3 次
- 去广告内购：$2.99

---

## 六、评分卡

| 维度 | 权重 | 评分 (1-5) | 依据来源 | 备注 |
|------|------|-----------|---------|------|
| 受众广度 | 15% | **4** | 策略类受众稳定 | 类似游戏：Risk, Hex |
| 上手速度 | 15% | **4** | 点击领地+点击目标，5秒理解 | 规则稍复杂 |
| 常玩常新 | 12% | **4** | 棋盘不同+AI策略变化 | 但核心机制固定 |
| 局内成长 | 10% | **4** | 领地升级+连击+技能 | 成长感清晰 |
| 无UI可验证 | 10% | **5** | 六边形网格+数值判定 | 纯状态机可验证 |
| AI开发难度 | 10% | **5** | 六边形网格+Minimax算法 | AI最擅长的技术栈 |
| 广告变现友好度 | 8% | **4** | 回合结束/失败/技能冷却 | 断点较多 |
| 玩法新鲜度 | 5% | **4** | 颜色吞噬+六边形棋盘有新意 | 类似游戏较少 |
| 用户粘性 | 5% | **4** | 三星追求+天赋树+排行榜 | 策略深度驱动 |
| 受众规模 | 5% | **3** | 策略类偏小众 | 估算百万级 |
| 难度递增 | 3% | **4** | 新棋盘形状+AI智能提升 | 100关梯度丰富 |
| 局外Meta | 2% | **4** | 皮肤+天赋树+无尽模式 | 内容丰富 |
| **加权总分** | 100% | **4.08** | — | 目标≥3.8 ✅ |

---

## 七、为什么符合目标

1. **3秒上手**：点击+点击，直觉操作
2. **常玩常新**：棋盘形状变化+AI策略调整
3. **局内成长**：领地升级→连击→技能释放
4. **无UI可验证**：六边形坐标+数值判定
5. **AI开发友好**：六边形网格+Minimax
6. **广告变现优秀**：回合制天然断点

---

> 生成时间：2026-09-02 03:00 | 批次：02 | 编号：game-13
