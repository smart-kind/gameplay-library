# 轨道射手 (Orbit Shooter) — 完整创意文档

> 核心组合：环形轨道 + 射击
> 预估总分：**4.10**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 背景 -->
  <rect width="360" height="640" fill="#0a0a1a"/>
  
  <!-- 星空背景 -->
  <circle cx="50" cy="80" r="1" fill="#fff" opacity="0.6"/>
  <circle cx="120" cy="50" r="1.5" fill="#fff" opacity="0.4"/>
  <circle cx="280" cy="90" r="1" fill="#fff" opacity="0.7"/>
  <circle cx="320" cy="150" r="1" fill="#fff" opacity="0.5"/>
  <circle cx="40" cy="200" r="1.5" fill="#fff" opacity="0.3"/>
  <circle cx="300" cy="250" r="1" fill="#fff" opacity="0.6"/>
  
  <!-- 顶部状态栏 -->
  <rect x="0" y="0" width="360" height="50" fill="#16213e" opacity="0.9"/>
  <text x="20" y="32" fill="#eee" font-size="14" font-family="sans-serif">波次 6/10</text>
  <text x="180" y="32" text-anchor="middle" fill="#2ecc71" font-size="16" font-family="sans-serif" font-weight="bold">🔫 火力 Lv.4</text>
  <text x="340" y="32" text-anchor="end" fill="#e74c3c" font-size="14" font-family="sans-serif">❤ 核心 70%</text>
  
  <!-- 游戏区域 -->
  <rect x="10" y="60" width="340" height="340" fill="#0f0f2e" rx="50%" opacity="0.5"/>
  
  <!-- 中心核心 -->
  <circle cx="180" cy="230" r="25" fill="#e74c3c" stroke="#c0392b" stroke-width="3"/>
  <text x="180" y="236" text-anchor="middle" fill="#fff" font-size="16">🔥</text>
  
  <!-- 环形轨道 -->
  <circle cx="180" cy="230" r="60" fill="none" stroke="#3498db" stroke-width="2" stroke-dasharray="4,4" opacity="0.6"/>
  <circle cx="180" cy="230" r="100" fill="none" stroke="#9b59b6" stroke-width="2" stroke-dasharray="4,4" opacity="0.6"/>
  <circle cx="180" cy="230" r="140" fill="none" stroke="#f39c12" stroke-width="2" stroke-dasharray="4,4" opacity="0.6"/>
  
  <!-- 玩家飞船 -->
  <g transform="rotate(-30, 240, 230)">
    <polygon points="240,215 250,230 240,245 225,230" fill="#2ecc71" stroke="#27ae60" stroke-width="2"/>
    <text x="238" y="234" fill="#fff" font-size="8">🚀</text>
  </g>
  
  <!-- 轨道上的敌人 -->
  <circle cx="120" cy="230" r="10" fill="#e74c3c"/>
  <text x="120" y="234" text-anchor="middle" fill="#fff" font-size="8">👹</text>
  
  <circle cx="180" cy="130" r="12" fill="#9b59b6"/>
  <text x="180" y="135" text-anchor="middle" fill="#fff" font-size="9">👺</text>
  
  <circle cx="280" cy="170" r="10" fill="#e74c3c"/>
  <text x="280" y="174" text-anchor="middle" fill="#fff" font-size="8">👹</text>
  
  <circle cx="100" cy="300" r="10" fill="#e74c3c"/>
  <text x="100" y="304" text-anchor="middle" fill="#fff" font-size="8">👹</text>
  
  <!-- 子弹 -->
  <line x1="235" y1="230" x2="180" y2="230" stroke="#2ecc71" stroke-width="3" stroke-linecap="round"/>
  <circle cx="180" cy="230" r="3" fill="#2ecc71"/>
  
  <!-- 轨道切换箭头 -->
  <path d="M 180,160 L 175,165 M 180,160 L 185,165" stroke="#3498db" stroke-width="2" fill="none"/>
  <path d="M 180,300 L 175,295 M 180,300 L 185,295" stroke="#3498db" stroke-width="2" fill="none"/>
  
  <!-- 底部控制区 -->
  <rect x="10" y="410" width="340" height="220" fill="#16213e" rx="8"/>
  <text x="180" y="435" text-anchor="middle" fill="#888" font-size="12" font-family="sans-serif">滑动切换轨道 | 自动射击最近敌人</text>
  
  <!-- 火力等级 -->
  <text x="50" y="460" fill="#aaa" font-size="11" font-family="sans-serif">火力:</text>
  <rect x="90" y="450" width="150" height="15" fill="#333" rx="4"/>
  <rect x="90" y="450" width="120" height="15" fill="#e74c3c" rx="4"/>
  <text x="250" y="462" fill="#e74c3c" font-size="10" font-family="sans-serif">Lv.4</text>
  
  <!-- 技能按钮 -->
  <rect x="30" y="480" width="70" height="45" fill="#3498db" rx="6"/>
  <text x="65" y="500" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">轨道炮</text>
  <text x="65" y="515" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×2</text>
  
  <rect x="110" y="480" width="70" height="45" fill="#e74c3c" rx="6"/>
  <text x="145" y="500" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">全屏炸</text>
  <text x="145" y="515" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×1</text>
  
  <rect x="190" y="480" width="70" height="45" fill="#9b59b6" rx="6"/>
  <text x="225" y="500" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">时间缓</text>
  <text x="225" y="515" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×2</text>
  
  <rect x="270" y="480" width="70" height="45" fill="#f39c12" rx="6"/>
  <text x="305" y="500" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">护盾</text>
  <text x="305" y="515" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×3</text>
  
  <!-- 升级选项 -->
  <text x="180" y="550" text-anchor="middle" fill="#888" font-size="11" font-family="sans-serif">击败敌人收集能量，波次结束后升级:</text>
  
  <rect x="30" y="565" width="95" height="40" fill="#2c3e50" stroke="#3498db" stroke-width="1" rx="4"/>
  <text x="77" y="582" text-anchor="middle" fill="#3498db" font-size="9" font-family="sans-serif">射速+20%</text>
  <text x="77" y="596" text-anchor="middle" fill="#aaa" font-size="8" font-family="sans-serif">100⚡</text>
  
  <rect x="132" y="565" width="95" height="40" fill="#2c3e50" stroke="#e74c3c" stroke-width="1" rx="4"/>
  <text x="179" y="582" text-anchor="middle" fill="#e74c3c" font-size="9" font-family="sans-serif">伤害+25%</text>
  <text x="179" y="596" text-anchor="middle" fill="#aaa" font-size="8" font-family="sans-serif">100⚡</text>
  
  <rect x="234" y="565" width="95" height="40" fill="#2c3e50" stroke="#2ecc71" stroke-width="1" rx="4"/>
  <text x="281" y="582" text-anchor="middle" fill="#2ecc71" font-size="9" font-family="sans-serif">新轨道</text>
  <text x="281" y="596" text-anchor="middle" fill="#aaa" font-size="8" font-family="sans-serif">200⚡</text>
  
  <!-- 波次进度 -->
  <rect x="30" y="620" width="300" height="8" fill="#333" rx="4"/>
  <rect x="30" y="620" width="180" height="8" fill="#2ecc71" rx="4"/>
</svg>

---

## 二、核心玩法

### 一句话描述
控制飞船在环形轨道上移动，自动射击轨道上的敌人，收集能量升级火力，保护中心核心不被摧毁。

### 详细规则

**轨道系统**：
- 3 条同心圆轨道，半径分别为 60/100/140（像素）
- 玩家飞船在轨道上自动匀速移动（可切换方向）
- 上下滑动切换内/中/外轨道
- 点击屏幕切换移动方向（顺时针/逆时针）

**自动射击**：
- 飞船自动瞄准并射击轨道上最近的敌人
- 射击方向始终指向中心核心（径向射击）
- 不同轨道射程不同：内轨短但射速快，外轨长但射速慢

**敌人行为**：
- 敌人在各轨道上生成，向中心核心移动
- 敌人接触核心 → 核心受到伤害
- 敌人被子弹击中 → 受到伤害，血量归零被消灭
- 部分敌人会反击（向飞船发射子弹）

**能量系统**：
- 击败敌人掉落能量（⚡）
- 能量用于波次间隙升级
- 能量也可用于释放技能

**波次机制**：
- 共 10 波，每波敌人数量和类型递增
- 波次间隙可消耗能量升级
- 全部 10 波完成后关卡通过

---

## 三、局内成长

**波次间隙升级**：
| 升级项 | 效果 | 消耗 |
|--------|------|------|
| 射速+20% | 射击间隔缩短 | 100⚡ |
| 伤害+25% | 单发伤害增加 | 100⚡ |
| 新轨道 | 解锁第 4 条轨道 | 200⚡ |
| 子弹穿透 | 子弹可穿透 1 个敌人 | 150⚡ |
| 爆炸弹 | 子弹命中后小范围爆炸 | 200⚡ |
| 自动修复 | 核心每秒恢复 1% | 150⚡ |

**连击系统**：
- 连续击败敌人不中断（间隔<2秒）→ 连击
- 连击×5：射速+10%
- 连击×10：伤害+20%
- 连击×15：进入"狂热模式"（射速×2，持续 5 秒）

**技能系统**：
- 轨道炮：当前轨道发射穿透激光，消灭轨道上所有敌人
- 全屏炸：消灭屏幕上所有敌人
- 时间缓：敌人移动速度减半，持续 5 秒
- 护盾：核心无敌 3 秒

**敌人种类**：
| 敌人类型 | 特性 | 应对策略 |
|---------|------|---------|
| 普通型 | 血量低，直线移动 | 任意轨道消灭 |
| 快速型 | 移动快，血量低 | 内轨高射速 |
| 坦克型 | 移动慢，血量高 | 外轨高伤害 |
| 分裂型 | 被消灭后分裂为 2 个小敌人 | 爆炸弹/穿透弹 |
| 反击型 | 会向飞船射击 | 切换轨道躲避 |
| Boss 型 | 血量极高，占领整条轨道 | 多轨道合力攻击 |

---

## 四、Meta Game（局外系统）

**关卡系统**：
- 共 80 关，分 4 个星系（太阳系→仙女座→黑洞边缘→宇宙中心）
- 每星系 20 关，最后 1 关为 Boss 战
- Boss 战：巨型敌人，需要切换轨道攻击不同弱点

**飞船升级**：
| 升级项 | 效果 |
|--------|------|
| 船体 | 增加血量，被反击时更耐打 |
| 引擎 | 轨道移动速度+20% |
| 武器 | 解锁新武器类型（激光/导弹/散弹） |
| 护盾 | 自动抵挡一次伤害（冷却 30 秒） |

**武器类型**：
- 机枪（默认）：射速快，伤害低
- 激光：穿透攻击，可穿透 3 个敌人
- 导弹：追踪最近敌人，有爆炸范围
- 散弹：同时发射 3 发，扇形分布

**无尽模式**：
- 波次无限递增
- 全球排行榜：比谁坚持波次最多
- 每周特殊规则（如"只能用一个轨道"、"敌人体型×2"）

**每日挑战**：
- "单轨挑战"：只能用 1 条轨道通关
- "反向挑战"：飞船只能逆时针移动
- "极速挑战"：敌人移动速度×2
- "生存挑战"：核心只有 10% 血量开始

---

## 五、广告变现

**自然断点设计**：

| 断点类型 | 时机 | 广告形式 | 预估 eCPM |
|---------|------|---------|----------|
| 波次间隙 | 每波结束（约1-2分钟） | 插屏/横幅 | $6-10 |
| 关卡完成 | 关卡结束 | 插屏广告 | $8-12 |
| 核心被毁 | 关卡失败 | 激励视频（复活50%核心血量） | $15-25 |
| 能量不足 | 想升级但能量不够 | 激励视频（+100能量） | $10-15 |
| 技能冷却 | 急需技能 | 激励视频（重置技能冷却） | $12-18 |
| 双倍能量 | 关卡结算 | 激励视频（2倍能量） | $10-15 |

**广告频率控制**：
- 每 3 波可观看 1 次激励视频
- 每 2 关强制插屏 1 次
- 去广告内购：$2.99

**广告友好度分析**：
- ✅ 波次间隙天然断点，升级选择不急
- ✅ 核心被毁时"挽救"需求强烈
- ✅ 能量不足时激励视频转化高
- ✅ 单波 1-2 分钟，节奏紧凑

---

## 六、评分卡

| 维度 | 权重 | 评分 (1-5) | 依据来源 | 备注 |
|------|------|-----------|---------|------|
| 受众广度 | 15% | **4** | 射击类受众广，环形轨道有新意 | 类似游戏较少 |
| 上手速度 | 15% | **5** | 上下滑动+点击，2秒理解 | 操作极简 |
| 常玩常新 | 12% | **4** | 随机敌人组合+升级选择 | 每局升级路线不同 |
| 局内成长 | 10% | **4** | 升级射速/伤害/新轨道 | 成长感清晰 |
| 无UI可验证 | 10% | **5** | 极坐标+轨道运动+碰撞检测 | 纯数学可验证 |
| AI开发难度 | 10% | **5** | 极坐标系统+状态机 | AI最擅长的技术栈 |
| 广告变现友好度 | 8% | **5** | 波次间隙极多 | 每波都是断点 |
| 玩法新鲜度 | 5% | **4** | 环形轨道射击有独特性 | 市面极少见 |
| 用户粘性 | 5% | **4** | 升级组合+无尽排行+每日挑战 | "再试一种升级"驱动力 |
| 受众规模 | 5% | **3** | 环形轨道可能需适应 | 估算百万级 |
| 难度递增 | 3% | **4** | 新敌人类型+反击机制+Boss | 4星系80关 |
| 局外Meta | 2% | **4** | 飞船升级+武器解锁+排行榜 | 内容丰富 |
| **加权总分** | 100% | **4.10** | — | 目标≥3.8 ✅ |

**评分计算过程**：
```
4×0.15 + 5×0.15 + 4×0.12 + 4×0.10 + 5×0.10 + 5×0.10 + 5×0.08 + 4×0.05 + 4×0.05 + 3×0.05 + 4×0.03 + 4×0.02
= 0.60 + 0.75 + 0.48 + 0.40 + 0.50 + 0.50 + 0.40 + 0.20 + 0.20 + 0.15 + 0.12 + 0.08
= 4.38
```
（保守估计 **4.10**）

---

## 七、为什么符合目标

1. **3秒上手**：上下滑动切轨道，点击换方向，极简操作
2. **常玩常新**：随机敌人组合+升级路线选择，每局不同
3. **局内成长**：射速/伤害/新轨道升级，成长感清晰
4. **无UI可验证**：极坐标+轨道运动+碰撞检测，纯数学可推演
5. **AI开发友好**：极坐标系统+状态机，AI最擅长
6. **广告变现优秀**：波次间隙天然断点极多

---

> 生成时间：2026-09-02 03:00 | 批次：02 | 编号：game-16
