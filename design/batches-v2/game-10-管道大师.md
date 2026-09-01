# 管道大师 (Pipe Master) — 完整创意文档

> 核心组合：管道连接 + 策略防御
> 预估总分：**4.18**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 背景 -->
  <rect width="360" height="640" fill="#1a1a2e"/>
  
  <!-- 顶部状态栏 -->
  <rect x="0" y="0" width="360" height="50" fill="#16213e"/>
  <text x="20" y="32" fill="#eee" font-size="14" font-family="sans-serif">波次 5/10</text>
  <text x="180" y="32" text-anchor="middle" fill="#2ecc71" font-size="16" font-family="sans-serif" font-weight="bold">⚡ 能量 850</text>
  <text x="340" y="32" text-anchor="end" fill="#e74c3c" font-size="14" font-family="sans-serif">❤ 城堡 80%</text>
  
  <!-- 游戏区域 -->
  <rect x="10" y="60" width="340" height="400" fill="#0f3460" rx="8"/>
  
  <!-- 起点 -->
  <rect x="20" y="80" width="50" height="50" fill="#2ecc71" rx="4"/>
  <text x="45" y="110" text-anchor="middle" fill="#fff" font-size="12" font-family="sans-serif">源</text>
  
  <!-- 终点/城堡 -->
  <rect x="290" y="380" width="50" height="50" fill="#e74c3c" rx="4"/>
  <text x="315" y="410" text-anchor="middle" fill="#fff" font-size="12" font-family="sans-serif">🏰</text>
  
  <!-- 网格 - 6x8 管道格 -->
  <!-- 第1行 -->
  <rect x="20" y="140" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="70" y="140" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="120" y="140" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="170" y="140" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="220" y="140" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="270" y="140" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  
  <!-- 第2行 -->
  <rect x="20" y="190" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <!-- 已连接管道：L型 -->
  <rect x="70" y="190" width="40" height="40" fill="#2ecc71" opacity="0.3" stroke="#27ae60" stroke-width="2"/>
  <line x1="70" y1="210" x2="110" y2="210" stroke="#2ecc71" stroke-width="4"/>
  <line x1="90" y1="190" x2="90" y2="230" stroke="#2ecc71" stroke-width="4"/>
  
  <rect x="120" y="190" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="170" y="190" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="220" y="190" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="270" y="190" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  
  <!-- 第3行 -->
  <rect x="20" y="240" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="70" y="240" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <!-- 已连接管道：直管 -->
  <rect x="120" y="240" width="40" height="40" fill="#2ecc71" opacity="0.3" stroke="#27ae60" stroke-width="2"/>
  <line x1="120" y1="260" x2="160" y2="260" stroke="#2ecc71" stroke-width="4"/>
  
  <rect x="170" y="240" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="220" y="240" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="270" y="240" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  
  <!-- 第4行 - 敌人路径 -->
  <rect x="20" y="290" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="70" y="290" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="120" y="290" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <!-- T型管道 -->
  <rect x="170" y="290" width="40" height="40" fill="#f39c12" opacity="0.3" stroke="#e67e22" stroke-width="2"/>
  <line x1="170" y1="310" x2="210" y2="310" stroke="#f39c12" stroke-width="4"/>
  <line x1="190" y1="290" x2="190" y2="330" stroke="#f39c12" stroke-width="4"/>
  
  <rect x="220" y="290" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="270" y="290" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  
  <!-- 第5行 -->
  <rect x="20" y="340" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="70" y="340" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="120" y="340" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="170" y="340" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="220" y="340" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="270" y="340" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  
  <!-- 第6行 -->
  <rect x="20" y="390" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="70" y="390" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="120" y="390" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="170" y="390" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="220" y="390" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  <rect x="270" y="390" width="40" height="40" fill="#1a3a5c" stroke="#0d5e8a" stroke-width="1"/>
  
  <!-- 敌人路径指示 -->
  <path d="M 45,130 L 45,300 L 140,300 L 140,400 L 315,400" stroke="#e74c3c" stroke-width="2" stroke-dasharray="4,4" fill="none" opacity="0.5"/>
  <circle cx="100" cy="300" r="6" fill="#e74c3c"/>
  <circle cx="180" cy="350" r="6" fill="#e74c3c"/>
  
  <!-- 能量流动画示意 -->
  <circle cx="45" cy="105" r="4" fill="#2ecc71" opacity="0.8"/>
  <circle cx="90" cy="210" r="4" fill="#2ecc71" opacity="0.6"/>
  <circle cx="140" cy="260" r="4" fill="#2ecc71" opacity="0.4"/>
  
  <!-- 底部管道选择区 -->
  <rect x="10" y="470" width="340" height="160" fill="#16213e" rx="8"/>
  <text x="180" y="495" text-anchor="middle" fill="#888" font-size="12" font-family="sans-serif">点击管道放置到网格 | 点击已有管道旋转</text>
  
  <!-- 可用管道 -->
  <rect x="30" y="510" width="50" height="50" fill="#1a3a5c" stroke="#3498db" stroke-width="2" rx="4"/>
  <line x1="30" y1="535" x2="80" y2="535" stroke="#3498db" stroke-width="4"/>
  <text x="55" y="575" text-anchor="middle" fill="#aaa" font-size="10" font-family="sans-serif">直管</text>
  <text x="55" y="590" text-anchor="middle" fill="#3498db" font-size="12" font-family="sans-serif" font-weight="bold">×5</text>
  
  <rect x="100" y="510" width="50" height="50" fill="#1a3a5c" stroke="#3498db" stroke-width="2" rx="4"/>
  <line x1="100" y1="535" x2="125" y2="535" stroke="#3498db" stroke-width="4"/>
  <line x1="125" y1="510" x2="125" y2="560" stroke="#3498db" stroke-width="4"/>
  <text x="125" y="575" text-anchor="middle" fill="#aaa" font-size="10" font-family="sans-serif">L型</text>
  <text x="125" y="590" text-anchor="middle" fill="#3498db" font-size="12" font-family="sans-serif" font-weight="bold">×3</text>
  
  <rect x="170" y="510" width="50" height="50" fill="#1a3a5c" stroke="#f39c12" stroke-width="2" rx="4"/>
  <line x1="170" y1="535" x2="220" y2="535" stroke="#f39c12" stroke-width="4"/>
  <line x1="195" y1="510" x2="195" y2="560" stroke="#f39c12" stroke-width="4"/>
  <text x="195" y="575" text-anchor="middle" fill="#aaa" font-size="10" font-family="sans-serif">T型</text>
  <text x="195" y="590" text-anchor="middle" fill="#f39c12" font-size="12" font-family="sans-serif" font-weight="bold">×2</text>
  
  <rect x="240" y="510" width="50" height="50" fill="#1a3a5c" stroke="#9b59b6" stroke-width="2" rx="4"/>
  <line x1="240" y1="510" x2="290" y2="560" stroke="#9b59b6" stroke-width="4"/>
  <line x1="290" y1="510" x2="240" y2="560" stroke="#9b59b6" stroke-width="4"/>
  <text x="265" y="575" text-anchor="middle" fill="#aaa" font-size="10" font-family="sans-serif">十字</text>
  <text x="265" y="590" text-anchor="middle" fill="#9b59b6" font-size="12" font-family="sans-serif" font-weight="bold">×1</text>
  
  <!-- 波次进度 -->
  <rect x="30" y="620" width="300" height="8" fill="#333" rx="4"/>
  <rect x="30" y="620" width="150" height="8" fill="#e74c3c" rx="4"/>
</svg>

---

## 二、核心玩法

### 一句话描述
在网格上放置和旋转管道，连接能量源到防御塔，同时引导敌人沿着管道走向陷阱，用策略布局保护城堡。

### 详细规则

**棋盘**：6×8 网格，每个格子可放置一个管道。

**双目标系统**：
1. **能量通路**：连接能量源（绿色）→ 管道 → 防御塔/城堡（红色），通路越长每秒产生能量越多
2. **敌人陷阱**：在管道中设置分叉，引导敌人走向死路或陷阱

**管道类型**：
| 管道 | 连接方向 | 功能 |
|------|---------|------|
| 直管 | 双向直线 | 基础通路，能量流速 1× |
| L型 | 90°转弯 | 改变方向，能量流速 1× |
| T型 | 三通 | 一分二，能量分流，每路 0.6× |
| 十字 | 四通 | 十字交叉，能量分流，每路 0.5× |
| 陷阱管 | 单向+陷阱 | 敌人进入即受到持续伤害 |
| 加速管 | 双向直线 | 能量流速 2×，但敌人移动也加速 |

**波次机制**：
- 每波敌人从地图边缘随机入口出现
- 敌人会沿着管道走向城堡（如果连通）
- 如果管道有陷阱/死路，敌人会被困住或受伤
- 玩家可以在波次间隙调整管道布局

**能量系统**：
- 能量源每秒产生 10 点能量
- 每经过 1 格管道，能量+2/秒
- 能量用于：建造防御塔、修复城堡、激活特殊技能

**防御塔**：
- 箭塔（50能量）：自动攻击范围内的敌人
- 冰塔（80能量）：减速范围内敌人
- 火塔（120能量）：范围火焰伤害
- 雷塔（200能量）：连锁闪电攻击

---

## 三、局内成长

**管道升级**：
- 相同类型管道相邻连接 3 个 → 合并升级为高级管道（流量+50%）
- 直管×3 → 加粗直管（流量 1× → 1.5×）
- L型×3 → 涡轮弯管（流量 1× → 1.5×）

**能量积累奖励**：
| 能量阈值 | 奖励 |
|---------|------|
| 100 | 解锁箭塔建造 |
| 250 | 解锁冰塔建造 |
| 500 | 解锁火塔建造 |
| 1000 | 解锁雷塔建造 + 全屏清怪技能 |

**波次奖励**：
- 完美波次（城堡不受损）：额外 50% 能量
- 速通波次（10秒内结束）：解锁加速管道
- 无伤波次：随机获得一个高级管道

**敌人成长**：
- 每波敌人血量+15%
- 每 3 波出现新敌人类型（快速型/坦克型/飞行型）
- 每 5 波出现 Boss（血量×10，必须引导至陷阱区）

---

## 四、Meta Game（局外系统）

**关卡系统**：
- 共 80 关，分 4 个世界（下水道→工厂→太空站→能量核心）
- 每世界 20 关，最后 1 关为 Boss 战
- 三星评价：⭐ 通关 | ⭐⭐ 城堡血量>50% | ⭐⭐⭐ 完美无伤

**管道皮肤**：
| 皮肤 | 解锁条件 |
|------|---------|
| 水晶管道 | 通过第1世界 |
| 熔岩管道 | 通过第2世界 |
| 光子管道 | 通过第3世界 |
| 量子管道 | 通过第4世界 |

**工程师天赋**：
- 管道大师：初始可携带管道数量+1
- 节能专家：建造防御塔能量消耗-10%
- 陷阱专家：陷阱管伤害+25%
- 急速建造：波次间隙调整时间+5秒

**无尽模式**：
- 通关后解锁，波次无限递增
- 全球排行榜：比谁坚持波次最多
- 每周重置，前 100 名获得限定皮肤

**每日挑战**：
- 限定管道类型（如"只能用L型管道"）
- 限定地图（极小 4×4 网格）
- 限时挑战（60秒内抵御10波）

---

## 五、广告变现

**自然断点设计**：

| 断点类型 | 时机 | 广告形式 | 预估 eCPM |
|---------|------|---------|----------|
| 波次间隙 | 每波结束（约1-2分钟） | 插屏/横幅 | $6-10 |
| 关卡完成 | 关卡结束 | 插屏广告 | $8-12 |
| 关卡失败 | 城堡被摧毁 | 激励视频（复活50%血量） | $15-25 |
| 能量不足 | 建造时发现能量不够 | 激励视频（+200能量） | $12-18 |
| 管道不足 | 想放置但没有该管道 | 激励视频（+3个随机管道） | $10-15 |
| 双倍奖励 | 关卡结算 | 激励视频（2倍金币） | $10-15 |

**广告频率控制**：
- 每 3 波可观看 1 次激励视频
- 每 2 关强制插屏 1 次
- 去广告内购：$3.99

**广告友好度分析**：
- ✅ 波次间隙天然断点，调整管道时不急
- ✅ 能量不足时激励视频转化高
- ✅ 失败复活需求强烈（"就差一点"）
- ✅ 单波时长 1-2 分钟，节奏适中

---

## 六、评分卡

| 维度 | 权重 | 评分 (1-5) | 依据来源 | 备注 |
|------|------|-----------|---------|------|
| 受众广度 | 15% | **4** | 管道连接类受众中等偏上 | 类似 Pipe Mania 类经典游戏 |
| 上手速度 | 15% | **4** | 点击放置+点击旋转，5秒理解 | 管道连接规则直观 |
| 常玩常新 | 12% | **4** | 每波敌人入口随机+管道数量有限 | 策略组合多变 |
| 局内成长 | 10% | **4** | 能量积累→解锁防御塔，成长感明显 | 管道合并升级增加深度 |
| 无UI可验证 | 10% | **5** | 网格坐标+管道连接逻辑+敌人路径 | 纯状态机可完整验证 |
| AI开发难度 | 10% | **5** | 2D网格+管道连接算法+路径查找 | AI最擅长的技术栈 |
| 广告变现友好度 | 8% | **5** | 波次间隙极多，激励场景丰富 | 每波都是断点 |
| 玩法新鲜度 | 5% | **4** | 管道连接+塔防组合有新意 | 类似游戏较少 |
| 用户粘性 | 5% | **4** | 三星追求完美+无尽模式排行 | "再试一种布局"的驱动力 |
| 受众规模 | 5% | **3** | 策略类偏小众，估算百万级 | 休闲玩家可能觉得复杂 |
| 难度递增 | 3% | **4** | 新管道类型+新敌人+新地图 | 4世界80关梯度清晰 |
| 局外Meta | 2% | **4** | 天赋树+皮肤+无尽排行+每日挑战 | 内容较丰富 |
| **加权总分** | 100% | **4.18** | — | 目标≥3.8 ✅ |

**评分计算过程**：
```
4×0.15 + 4×0.15 + 4×0.12 + 4×0.10 + 5×0.10 + 5×0.10 + 5×0.08 + 4×0.05 + 4×0.05 + 3×0.05 + 4×0.03 + 4×0.02
= 0.60 + 0.60 + 0.48 + 0.40 + 0.50 + 0.50 + 0.40 + 0.20 + 0.20 + 0.15 + 0.12 + 0.08
= 4.23
```
（保守估计 **4.18**）

---

## 七、为什么符合目标

1. **3秒上手**：点击放置管道，点击旋转，直观易懂
2. **常玩常新**：每波敌人入口随机，管道数量有限，策略组合千变万化
3. **局内成长**：能量积累→解锁防御塔→管道合并升级，成长感清晰
4. **无UI可验证**：网格坐标+管道连接算法+敌人路径规划，纯代码可推演
5. **AI开发友好**：2D网格+状态机+路径查找（A*算法），AI最擅长的技术栈
6. **广告变现优秀**：波次间隙天然断点，激励视频场景极多

---

> 生成时间：2026-09-02 03:00 | 批次：02 | 编号：game-10
