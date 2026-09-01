---
title: 宝石剑客 (Gem Swordsman) — 完整创意文档
original_filename: game-07-宝石剑客
source: gameplay-library
---

# 宝石剑客 (Gem Swordsman) — 完整创意文档

> 核心组合：宝石三消 + RPG回合战斗  
> 预估总分：**4.11**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <rect width="360" height="640" fill="#1a1a2e"/>
  <rect x="0" y="0" width="360" height="40" fill="#16213e"/>
  <text x="180" y="26" text-anchor="middle" fill="#eee" font-size="14">回合 5  |  HP 80/100  |  敌人HP 60/120</text>
  <rect x="0" y="40" width="360" height="100" fill="#0f3460"/>
  <text x="180" y="55" text-anchor="middle" fill="#aaa" font-size="10">战斗区域</text>
  <rect x="30" y="65" width="80" height="60" fill="#4ecca3" rx="6"/>
  <text x="70" y="85" text-anchor="middle" fill="#fff" font-size="12">🗡️ 剑客</text>
  <text x="70" y="105" text-anchor="middle" fill="#fff" font-size="10">HP 80/100</text>
  <rect x="250" y="65" width="80" height="60" fill="#e94560" rx="6"/>
  <text x="290" y="85" text-anchor="middle" fill="#fff" font-size="12">👹 哥布林</text>
  <text x="290" y="105" text-anchor="middle" fill="#fff" font-size="10">HP 60/120</text>
  <text x="180" y="125" text-anchor="middle" fill="#e94560" font-size="12">敌人下回合行动: 攻击 (预计伤害 15-20)</text>
  <rect x="10" y="150" width="340" height="300" fill="#16213e" rx="8"/>
  <text x="180" y="165" text-anchor="middle" fill="#888" font-size="10">宝石盘 (6×6)</text>
  <g stroke="#0f3460" stroke-width="1">
    <line x1="10" y1="200" x2="350" y2="200"/><line x1="10" y1="250" x2="350" y2="250"/>
    <line x1="10" y1="300" x2="350" y2="300"/><line x1="10" y1="350" x2="350" y2="350"/>
    <line x1="10" y1="400" x2="350" y2="400"/>
    <line x1="67" y1="150" x2="67" y2="450"/><line x1="124" y1="150" x2="124" y2="450"/>
    <line x1="181" y1="150" x2="181" y2="450"/><line x1="238" y1="150" x2="238" y2="450"/>
    <line x1="295" y1="150" x2="295" y2="450"/>
  </g>
  <rect x="14" y="154" width="49" height="42" fill="#e74c3c" rx="4"/>
  <text x="38" y="182" text-anchor="middle" fill="#fff" font-size="20">♦</text>
  <rect x="71" y="154" width="49" height="42" fill="#3498db" rx="4"/>
  <text x="95" y="182" text-anchor="middle" fill="#fff" font-size="20">♠</text>
  <rect x="128" y="154" width="49" height="42" fill="#2ecc71" rx="4"/>
  <text x="152" y="182" text-anchor="middle" fill="#fff" font-size="20">♣</text>
  <rect x="185" y="154" width="49" height="42" fill="#f1c40f" rx="4"/>
  <text x="209" y="182" text-anchor="middle" fill="#fff" font-size="20">★</text>
  <rect x="242" y="154" width="49" height="42" fill="#e74c3c" rx="4"/>
  <text x="266" y="182" text-anchor="middle" fill="#fff" font-size="20">♦</text>
  <rect x="299" y="154" width="49" height="42" fill="#9b59b6" rx="4"/>
  <text x="323" y="182" text-anchor="middle" fill="#fff" font-size="20">💎</text>
  <rect x="14" y="204" width="49" height="42" fill="#f1c40f" rx="4"/>
  <text x="38" y="232" text-anchor="middle" fill="#fff" font-size="20">★</text>
  <rect x="71" y="204" width="49" height="42" fill="#e74c3c" rx="4"/>
  <text x="95" y="232" text-anchor="middle" fill="#fff" font-size="20">♦</text>
  <rect x="128" y="204" width="49" height="42" fill="#3498db" rx="4"/>
  <text x="152" y="232" text-anchor="middle" fill="#fff" font-size="20">♠</text>
  <rect x="185" y="204" width="49" height="42" fill="#2ecc71" rx="4"/>
  <text x="209" y="232" text-anchor="middle" fill="#fff" font-size="20">♣</text>
  <rect x="0" y="460" width="360" height="180" fill="#0f3460"/>
  <text x="180" y="480" text-anchor="middle" fill="#aaa" font-size="12">技能栏</text>
  <rect x="20" y="495" width="70" height="50" fill="#e74c3c" rx="6"/>
  <text x="55" y="515" text-anchor="middle" fill="#fff" font-size="11">🔥 火剑</text>
  <text x="55" y="535" text-anchor="middle" fill="#aaa" font-size="9">3♦=发动</text>
  <rect x="100" y="495" width="70" height="50" fill="#3498db" rx="6"/>
  <text x="135" y="515" text-anchor="middle" fill="#fff" font-size="11">🛡️ 冰盾</text>
  <text x="135" y="535" text-anchor="middle" fill="#aaa" font-size="9">3♠=发动</text>
  <rect x="180" y="495" width="70" height="50" fill="#2ecc71" rx="6"/>
  <text x="215" y="515" text-anchor="middle" fill="#fff" font-size="11">⚡ 雷暴</text>
  <text x="215" y="535" text-anchor="middle" fill="#aaa" font-size="9">3♣=发动</text>
  <rect x="260" y="495" width="80" height="50" fill="#f1c40f" rx="6"/>
  <text x="300" y="520" text-anchor="middle" fill="#fff" font-size="11">⭐ 大招</text>
  <text x="180" y="570" text-anchor="middle" fill="#fff" font-size="14">交换相邻宝石 → 3个同色连成一线消除 → 释放对应技能</text>
  <text x="180" y="600" text-anchor="middle" fill="#aaa" font-size="12">♦火攻击  ♠冰防御  ♣雷范围  ★治疗  💎万能</text>
</svg>

---

## 二、基础信息

| 字段 | 内容 |
|------|------|
| 游戏名称 | 宝石剑客 / Gem Swordsman |
| 核心组合 | 宝石三消 + RPG回合战斗 |
| 一句话描述 | 交换宝石消除释放对应技能，回合制战斗中击败怪物升级装备 |
| 目标平台 | Mobile (iOS+Android)，竖屏 |
| 预估单局时长 | 5-8分钟/关卡 |
| 预估开发周期 | AI构建约4-5天 |

---

## 三、核心玩法

### 3.1 玩家输入

| 操作 | 区域 | 反馈 |
|------|------|------|
| **交换宝石** | 宝石盘 | 宝石交换，匹配检测，消除动画 |
| **点击技能** | 底部技能栏 | 消耗匹配宝石释放技能 |

### 3.2 游戏实体

**宝石类型（5种）**：
| 宝石 | 颜色 | 对应技能 | 效果 |
|------|------|---------|------|
| 红宝石 | 红色 | 火剑 | 单体高伤害 |
| 蓝宝石 | 蓝色 | 冰盾 | 获得护盾 |
| 绿宝石 | 绿色 | 雷暴 | 范围伤害 |
| 黄宝石 | 黄色 | 治疗 | 恢复生命 |
| 紫水晶 | 紫色 | 万能 | 替代任意宝石 |

**消除规则**：
- 3个同色连成一线（横/竖）→消除→释放基础技能
- 4个连成一线→消除+该技能强化版
- 5个连成一线→消除+全屏技能
- L型/T型→消除+炸弹（消除周围3×3）

**敌人**：
| 敌人 | HP | 攻击 | 特殊 |
|------|-----|------|------|
| 哥布林 | 120 | 15-20 | 无 |
| 兽人 | 200 | 25-35 | 狂暴（HP<50%攻击×2） |
| 巫师 | 150 | 20-30 | 每3回合治疗自己 |
| 巨龙 | 500 | 40-60 | 火焰吐息（每4回合全体伤害） |

### 3.3 胜负条件

- **胜利**：敌人HP归零
- **失败**：玩家HP归零
- **星级**：⭐过关 / ⭐⭐回合数≤限制 / ⭐⭐⭐无伤

### 3.4 核心循环

```
Step 1: 观察宝石盘，寻找最佳交换
Step 2: 交换宝石，触发消除
Step 3: 根据消除宝石类型释放技能
Step 4: 技能伤害/效果作用于敌人
Step 5: 敌人回合→攻击玩家
Step 6: 重复直到一方HP归零
```

---

## 四、局内成长系统

### 4.1 单局内成长

**装备系统**：
| 装备 | 效果 |
|------|------|
| 铁剑 | 火剑伤害+20% |
| 魔法盾 | 冰盾护盾值+30% |
| 雷戒 | 雷暴范围+1格 |

**连击系统**：
- 连续消除（不敌人回合）→连击数增加→伤害加成
- 5连击触发"剑圣模式"（下回合伤害×2）

### 4.2 难度递进

| 关卡 | 敌人 | 新要素 |
|------|------|--------|
| 1-5 | 哥布林 | 基础消除 |
| 6-10 | 兽人 | 狂暴机制 |
| 11-15 | 巫师 | 敌人治疗 |
| 16-20 | 巨龙 | 全体攻击 |
| 21+ | 混合 | 限时回合 |

---

## 五、Meta Game

### 5.1 局外持久成长

**角色等级**：
- 过关获经验，升级提升基础HP/攻击力

**装备锻造**：
- 收集材料强化装备
- 套装效果（2件/4件/6件）

**技能树**：
| 分支 | 效果 |
|------|------|
| 攻击 | 火剑伤害+10%/暴击率+5% |
| 防御 | 冰盾持续时间+1回合/反伤 |
| 辅助 | 治疗量+15%/雷暴麻痹概率 |

### 5.2 解锁系统

- 新角色（法师/弓箭手/刺客）
- 宝石皮肤（古代/魔法/科技）
- 挑战模式（限时/无限/BOSS Rush）

### 5.3 社交/竞技

- 无尽模式排行
- 伤害输出排行
- 分享Build

---

## 六、广告变现设计

| 时机 | 类型 | 说明 |
|------|------|------|
| 关卡完成 | 插屏 | 每2关 |
| 关卡失败 | 激励视频 | 复活+恢复50%HP |
| 体力不足 | 激励视频 | +5体力 |

### 6.2 付费点

- 去广告 $2.99
- 体力包 $0.99
- 月卡 $4.99

---

## 七、技术实现评估

- 渲染：Canvas 2D
- 物理：无（交换动画）
- 网络：单机+排行榜
- 存储：localStorage

**AI开发难度：5分** — 三消算法+回合制+数值公式。

---

## 八、参考游戏

| 参考游戏 | 借鉴点 |
|---------|--------|
| Puzzle Quest | 三消+RPG |
| 智龙迷城 | 消除战斗 |
| 宝石迷阵 | 消除机制 |

---

## 九、评分卡

| 维度 | 权重 | 评分 | 依据 |
|------|------|------|------|
| 受众广度 | 15% | **5** | 三消+RPG均为大众类型 |
| 上手速度 | 15% | **5** | 交换消除1秒上手 |
| 常玩常新 | 12% | **4** | 随机盘面+装备Build |
| 局内成长 | 10% | **4** | 装备+连击+技能 |
| 无UI可验证 | 10% | **5** | 消除算法+伤害公式 |
| AI开发难度 | 10% | **5** | 三消检测+回合制 |
| 广告变现 | 8% | **4** | 关卡断点；失败复活 |
| 玩法新鲜度 | 5% | **3** | 三消+RPG已有Puzzle Quest |
| 用户粘性 | 5% | **4** | 装备收集+Build搭配 |
| 受众规模 | 5% | **4** | 估算千万级 |
| 难度递增 | 3% | **4** | 敌人技能递进 |
| 局外Meta | 2% | **4** | 多角色+装备锻造 |
| **加权总分** | **100%** | **4.11** | — |