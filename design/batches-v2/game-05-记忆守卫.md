# 记忆守卫 (Memory Guard) — 完整创意文档

> 核心组合：翻牌配对记忆 + 塔防召唤  
> 预估总分：**4.08**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <rect width="360" height="640" fill="#1a1a2e"/>
  <rect x="0" y="0" width="360" height="40" fill="#16213e"/>
  <text x="180" y="26" text-anchor="middle" fill="#eee" font-size="14">波次 2/5  |  记忆点 120  |  ❤❤❤</text>
  <rect x="0" y="40" width="360" height="80" fill="#0f3460"/>
  <text x="180" y="55" text-anchor="middle" fill="#aaa" font-size="10">敌人沿4列进攻  |  已召唤守卫: 3</text>
  <circle cx="70" cy="85" r="10" fill="#ff6b6b"/><circle cx="150" cy="80" r="10" fill="#ff6b6b"/>
  <circle cx="230" cy="90" r="10" fill="#ff6b6b"/><circle cx="310" cy="82" r="10" fill="#ff6b6b"/>
  <line x1="0" y1="120" x2="360" y2="120" stroke="#e94560" stroke-width="3"/>
  <rect x="10" y="135" width="340" height="300" fill="#16213e" rx="8"/>
  <text x="180" y="150" text-anchor="middle" fill="#888" font-size="10">翻牌区域 (4×5)</text>
  <g stroke="#0f3460" stroke-width="1">
    <line x1="10" y1="195" x2="350" y2="195"/><line x1="10" y1="255" x2="350" y2="255"/>
    <line x1="10" y1="315" x2="350" y2="315"/><line x1="10" y1="375" x2="350" y2="375"/>
    <line x1="78" y1="135" x2="78" y2="435"/><line x1="146" y1="135" x2="146" y2="435"/>
    <line x1="214" y1="135" x2="214" y2="435"/><line x1="282" y1="135" x2="282" y2="435"/>
  </g>
  <rect x="14" y="139" width="60" height="50" fill="#533483" rx="6"/>
  <text x="44" y="169" text-anchor="middle" fill="#fff" font-size="20">?</text>
  <rect x="82" y="139" width="60" height="50" fill="#533483" rx="6"/>
  <text x="112" y="169" text-anchor="middle" fill="#fff" font-size="20">?</text>
  <rect x="150" y="139" width="60" height="50" fill="#e74c3c" rx="6"/>
  <text x="180" y="169" text-anchor="middle" fill="#fff" font-size="16">⚔️</text>
  <rect x="218" y="139" width="60" height="50" fill="#533483" rx="6"/>
  <text x="248" y="169" text-anchor="middle" fill="#fff" font-size="20">?</text>
  <rect x="286" y="139" width="60" height="50" fill="#3498db" rx="6"/>
  <text x="316" y="169" text-anchor="middle" fill="#fff" font-size="16">🛡️</text>
  <rect x="14" y="199" width="60" height="50" fill="#533483" rx="6"/>
  <text x="44" y="229" text-anchor="middle" fill="#fff" font-size="20">?</text>
  <rect x="82" y="199" width="60" height="50" fill="#2ecc71" rx="6"/>
  <text x="112" y="229" text-anchor="middle" fill="#fff" font-size="16">🏹</text>
  <rect x="150" y="199" width="60" height="50" fill="#533483" rx="6"/>
  <text x="180" y="229" text-anchor="middle" fill="#fff" font-size="20">?</text>
  <rect x="218" y="199" width="60" height="50" fill="#533483" rx="6"/>
  <text x="248" y="229" text-anchor="middle" fill="#fff" font-size="20">?</text>
  <rect x="286" y="199" width="60" height="50" fill="#e74c3c" rx="6"/>
  <text x="316" y="229" text-anchor="middle" fill="#fff" font-size="16">⚔️</text>
  <rect x="0" y="445" width="360" height="100" fill="#16213e"/>
  <text x="180" y="465" text-anchor="middle" fill="#aaa" font-size="10">已召唤守卫 (自动攻击)</text>
  <rect x="30" y="475" width="70" height="60" fill="#e74c3c" rx="6"/>
  <text x="65" y="495" text-anchor="middle" fill="#fff" font-size="11">剑士</text>
  <text x="65" y="515" text-anchor="middle" fill="#aaa" font-size="9">攻击 25</text>
  <text x="65" y="530" text-anchor="middle" fill="#aaa" font-size="9">攻速 1.0</text>
  <rect x="110" y="475" width="70" height="60" fill="#3498db" rx="6"/>
  <text x="145" y="495" text-anchor="middle" fill="#fff" font-size="11">盾卫</text>
  <text x="145" y="515" text-anchor="middle" fill="#aaa" font-size="9">防御 30</text>
  <text x="145" y="530" text-anchor="middle" fill="#aaa" font-size="9">阻挡</text>
  <rect x="190" y="475" width="70" height="60" fill="#2ecc71" rx="6"/>
  <text x="225" y="495" text-anchor="middle" fill="#fff" font-size="11">弓手</text>
  <text x="225" y="515" text-anchor="middle" fill="#aaa" font-size="9">攻击 15</text>
  <text x="225" y="530" text-anchor="middle" fill="#aaa" font-size="9">射程 3</text>
  <rect x="0" y="550" width="360" height="90" fill="#0f3460"/>
  <text x="180" y="575" text-anchor="middle" fill="#fff" font-size="14">点击两张卡牌翻转  |  配对成功召唤守卫</text>
  <text x="180" y="605" text-anchor="middle" fill="#aaa" font-size="12">守卫类型: ⚔️剑士 🛡️盾卫 🏹弓手 🔥法师 💚牧师</text>
</svg>

---

## 二、基础信息

| 字段 | 内容 |
|------|------|
| 游戏名称 | 记忆守卫 / Memory Guard |
| 核心组合 | 翻牌配对记忆 + 塔防召唤 |
| 一句话描述 | 翻转卡牌配对记忆，配对成功召唤守卫自动攻击入侵敌人 |
| 目标平台 | Mobile (iOS+Android)，竖屏 |
| 预估单局时长 | 4-6分钟 |
| 预估开发周期 | AI构建约4-5天 |

---

## 三、核心玩法

### 3.1 玩家输入

| 操作 | 区域 | 反馈 |
|------|------|------|
| **点击卡牌** | 翻牌区域 | 卡牌翻转，显示守卫类型 |
| **点击守卫技能** | 已召唤守卫 | 释放守卫主动技能 |

### 3.2 游戏实体

**卡牌（5种守卫类型，每种2-4张）**：
| 守卫 | 图标 | 攻击 | 特殊能力 |
|------|------|------|---------|
| 剑士 | ⚔️ | 25/秒 | 无 |
| 盾卫 | 🛡️ | 10/秒 | 阻挡1个敌人（不可穿透） |
| 弓手 | 🏹 | 15/秒 | 射程3格，可穿透 |
| 法师 | 🔥 | 30/秒 | 范围攻击（溅射） |
| 牧师 | 💚 | 5/秒 | 每5秒治疗所有守卫+10HP |

**配对规则**：
- 翻开两张卡牌，相同类型→召唤对应守卫，卡牌消失
- 不同类型→卡牌翻回，扣除5点记忆点
- 连续配对成功→连击加成（伤害+10%/连击）

**敌人**：
| 类型 | HP | 速度 | 特殊 |
|------|-----|------|------|
| 普通怪 | 50 | 1.0× | 无 |
| 快速怪 | 30 | 1.5× | 闪避20% |
| 装甲怪 | 100 | 0.7× | 防御减半伤害 |
| 飞行怪 | 40 | 1.2× | 无视盾卫阻挡 |
| Boss | 600 | 0.5× | 召唤小兵 |

### 3.3 胜负条件

- **胜利**：击败5波敌人
- **失败**：生命归零（初始3心）
- **星级**：⭐过关 / ⭐⭐满血 / ⭐⭐⭐无错误配对通关

### 3.4 核心循环

```
Step 1: 观察已翻开的卡牌，记忆位置
Step 2: 点击两张卡牌尝试配对
Step 3: 配对成功→召唤守卫，守卫自动攻击
Step 4: 配对失败→扣除记忆点，卡牌翻回
Step 5: 敌人从上方入侵，守卫自动防御
Step 6: 波次结束→新卡牌补充，守卫保留
```

---

## 四、局内成长系统

### 4.1 单局内成长

**守卫升级**：
- 同类型守卫再次配对→守卫升级（攻击+50%）
- 最高3级

**记忆点系统**：
- 初始100点
- 错误配对-5点
- 连续正确配对+10点
- 记忆点可用于：刷新卡牌（20点）、透视（查看一张卡牌10秒，30点）

### 4.2 难度递进

| 阶段 | 波次 | 卡牌数 | 新要素 |
|------|------|--------|--------|
| 教学 | 1-2 | 4×3 (12张) | 3种守卫 |
| 成长 | 3-4 | 4×4 (16张) | 5种守卫 |
| 挑战 | 5 | 4×5 (20张) | 飞行怪+Boss |

---

## 五、Meta Game

### 5.1 局外持久成长

**记忆大师等级**：通关获经验，升级提升初始记忆点。

**守卫精通**：
| 线名 | 效果 |
|------|------|
| 剑士专精 | 剑士攻击+20% / 暴击率+10% |
| 防御专精 | 盾卫阻挡数+1 / 护甲+20% |
| 远程专精 | 弓手射程+1 / 穿透+1 |

### 5.2 解锁系统

- 守卫皮肤（金/银/水晶）
- 卡牌背面图案
- 挑战模式（限时记忆/ blind模式）

### 5.3 社交/竞技

- 最少错误配对排行
- 最速通关排行

---

## 六、广告变现设计

| 时机 | 类型 | 说明 |
|------|------|------|
| 波次结束 | 插屏 | 每2波一次 |
| 关卡失败 | 激励视频 | 复活+补充记忆点 |
| 记忆点不足 | 激励视频 | +50记忆点 |

### 6.2 付费点

- 去广告 $2.99
- 记忆包 $0.99（透视次数+10）

---

## 七、技术实现评估

- 渲染：Canvas 2D
- 物理：无
- 网络：单机+排行榜
- 存储：localStorage

**AI开发难度：5分** — 翻牌逻辑+守卫AI+敌人路径，状态机简单。

---

## 八、参考游戏

| 参考游戏 | 借鉴点 |
|---------|--------|
| 记忆翻牌 | 配对记忆机制 |
| 植物大战僵尸 | 自动防御塔 |
| 皇室战争 | 兵种搭配策略 |

---

## 九、评分卡

| 维度 | 权重 | 评分 | 依据 |
|------|------|------|------|
| 受众广度 | 15% | **5** | 记忆游戏+塔防均为大众类型 |
| 上手速度 | 15% | **5** | 翻牌1秒上手；守卫自动战斗 |
| 常玩常新 | 12% | **4** | 随机卡牌布局；但记忆可背诵 |
| 局内成长 | 10% | **3** | 守卫升级简单；成长感一般 |
| 无UI可验证 | 10% | **5** | 翻牌状态+守卫属性+敌人数值 |
| AI开发难度 | 10% | **5** | 翻牌逻辑+自动攻击AI |
| 广告变现 | 8% | **4** | 波次断点；失败复活 |
| 玩法新鲜度 | 5% | **3** | 记忆+塔防组合少见但逻辑不复杂 |
| 用户粘性 | 5% | **4** | 记忆挑战+三星追求 |
| 受众规模 | 5% | **4** | 估算千万级 |
| 难度递增 | 3% | **4** | 卡牌增加+新敌人类型 |
| 局外Meta | 2% | **3** | 守卫精通+皮肤 |
| **加权总分** | **100%** | **4.08** | — |
