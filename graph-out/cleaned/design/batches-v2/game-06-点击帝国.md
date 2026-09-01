---
title: 点击帝国 (Click Empire) — 完整创意文档
original_filename: game-06-点击帝国
source: gameplay-library
---

# 点击帝国 (Click Empire) — 完整创意文档

> 核心组合：疯狂点击收集 + 放置经营  
> 预估总分：**4.19**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <rect width="360" height="640" fill="#1a1a2e"/>
  <rect x="0" y="0" width="360" height="40" fill="#16213e"/>
  <text x="180" y="26" text-anchor="middle" fill="#eee" font-size="14">金币 1.2M  |  宝石 50  |  离线收益 +450K</text>
  <rect x="10" y="50" width="340" height="200" fill="#16213e" rx="8"/>
  <text x="180" y="70" text-anchor="middle" fill="#aaa" font-size="12">帝国全景</text>
  <rect x="30" y="85" width="60" height="60" fill="#4ecca3" rx="4"/>
  <text x="60" y="110" text-anchor="middle" fill="#fff" font-size="10">🏰 城堡</text>
  <text x="60" y="130" text-anchor="middle" fill="#aaa" font-size="9">Lv.12</text>
  <rect x="100" y="85" width="60" height="60" fill="#f9a825" rx="4"/>
  <text x="130" y="110" text-anchor="middle" fill="#fff" font-size="10">🏭 工厂</text>
  <text x="130" y="130" text-anchor="middle" fill="#aaa" font-size="9">Lv.8</text>
  <rect x="170" y="85" width="60" height="60" fill="#e74c3c" rx="4"/>
  <text x="200" y="110" text-anchor="middle" fill="#fff" font-size="10">⚔️ 兵营</text>
  <text x="200" y="130" text-anchor="middle" fill="#aaa" font-size="9">Lv.5</text>
  <rect x="240" y="85" width="60" height="60" fill="#3498db" rx="4"/>
  <text x="270" y="110" text-anchor="middle" fill="#fff" font-size="10">🏪 市场</text>
  <text x="270" y="130" text-anchor="middle" fill="#aaa" font-size="9">Lv.6</text>
  <rect x="30" y="155" width="60" height="60" fill="#2ecc71" rx="4"/>
  <text x="60" y="180" text-anchor="middle" fill="#fff" font-size="10">🌾 农场</text>
  <text x="60" y="200" text-anchor="middle" fill="#aaa" font-size="9">Lv.15</text>
  <rect x="100" y="155" width="60" height="60" fill="#9b59b6" rx="4"/>
  <text x="130" y="180" text-anchor="middle" fill="#fff" font-size="10">🔮 魔法塔</text>
  <text x="130" y="200" text-anchor="middle" fill="#aaa" font-size="9">Lv.3</text>
  <rect x="0" y="260" width="360" height="200" fill="#0f3460"/>
  <text x="180" y="280" text-anchor="middle" fill="#aaa" font-size="12">点击生产区</text>
  <circle cx="180" cy="360" r="60" fill="#e94560" stroke="#fff" stroke-width="3"/>
  <text x="180" y="355" text-anchor="middle" fill="#fff" font-size="20">点击!</text>
  <text x="180" y="380" text-anchor="middle" fill="#fff" font-size="14">+1K 金币</text>
  <text x="180" y="410" text-anchor="middle" fill="#f9a825" font-size="12">自动产出: +500/秒</text>
  <rect x="0" y="470" width="360" height="170" fill="#16213e"/>
  <text x="180" y="490" text-anchor="middle" fill="#aaa" font-size="12">升级面板</text>
  <rect x="20" y="500" width="70" height="50" fill="#4ecca3" rx="6"/>
  <text x="55" y="520" text-anchor="middle" fill="#fff" font-size="10">农场升级</text>
  <text x="55" y="538" text-anchor="middle" fill="#aaa" font-size="9">50K</text>
  <rect x="100" y="500" width="70" height="50" fill="#f9a825" rx="6"/>
  <text x="135" y="520" text-anchor="middle" fill="#fff" font-size="10">工厂升级</text>
  <text x="135" y="538" text-anchor="middle" fill="#aaa" font-size="9">200K</text>
  <rect x="180" y="500" width="70" height="50" fill="#e74c3c" rx="6"/>
  <text x="215" y="520" text-anchor="middle" fill="#fff" font-size="10">兵营升级</text>
  <text x="215" y="538" text-anchor="middle" fill="#aaa" font-size="9">150K</text>
  <rect x="260" y="500" width="80" height="50" fill="#e94560" rx="6"/>
  <text x="300" y="525" text-anchor="middle" fill="#fff" font-size="12">全部×2</text>
  <rect x="20" y="560" width="320" height="70" fill="#1a1a2e" rx="8"/>
  <text x="180" y="585" text-anchor="middle" fill="#fff" font-size="14">任务: 累计点击1000次  (进度: 650/1000)</text>
  <text x="180" y="610" text-anchor="middle" fill="#f9a825" font-size="12">奖励: 宝石×10</text>
</svg>

---

## 二、基础信息

| 字段 | 内容 |
|------|------|
| 游戏名称 | 点击帝国 / Click Empire |
| 核心组合 | 疯狂点击收集 + 放置经营 |
| 一句话描述 | 疯狂点击赚取金币，建设自动产出建筑，离线也能持续积累，打造最强帝国 |
| 目标平台 | Mobile (iOS+Android)，竖屏 |
| 预估单局时长 | 碎片化（每次1-2分钟，长期积累） |
| 预估开发周期 | AI构建约3-4天 |

---

## 三、核心玩法

### 3.1 玩家输入

| 操作 | 区域 | 反馈 |
|------|------|------|
| **点击** | 中央大按钮 | 金币增加，按钮缩放动画 |
| **点击升级** | 底部升级面板 | 建筑升级，产出增加 |
| **滑动** | 建筑区域 | 查看不同建筑 |

### 3.2 游戏实体

**建筑系统（6种）**：
| 建筑 | 初始产出 | 升级成本 | 特殊效果 |
|------|---------|---------|---------|
| 农场 | +10/秒 | 100金币 | 基础产出 |
| 工厂 | +50/秒 | 1K金币 | 产出×2 |
| 市场 | +200/秒 | 10K金币 | 点击收益+20% |
| 兵营 | +500/秒 | 50K金币 | 解锁战斗功能 |
| 魔法塔 | +2K/秒 | 200K金币 | 离线收益+50% |
| 城堡 | +10K/秒 | 1M金币 | 全建筑产出+10% |

**点击收益**：
- 基础点击+1金币
- 升级后每次点击+100/1K/10K
- 连点加速：连续点击不中断→点击收益×2（最高×10）

**离线收益**：
- 退出游戏后，建筑继续产出（最多8小时）
- 魔法塔等级提升离线收益上限

### 3.3 胜负条件

- 无失败条件，纯积累型
- 目标：解锁全部建筑并升到最高级
- 成就：点击1M次/累计1B金币/全建筑Lv.50

### 3.4 核心循环

```
Step 1: 点击中央按钮获取金币
Step 2: 金币足够时升级建筑
Step 3: 建筑自动产出更多金币
Step 4: 离线后上线领取离线收益
Step 5: 完成任务获取宝石奖励
Step 6: 用宝石购买永久加成
```

---

## 四、局内成长系统

### 4.1 单局内成长

**建筑升级**：核心成长载体。每次升级产出翻倍，成本指数增长。

**任务系统**：
| 任务 | 要求 | 奖励 |
|------|------|------|
| 点击新手 | 点击100次 | 宝石×5 |
| 升级达人 | 升级建筑20次 | 宝石×10 |
| 百万富翁 | 累计1M金币 | 宝石×20 |
| 帝国霸主 | 全建筑Lv.10 | 宝石×50 |

**宝石使用**：
- 永久点击收益+10%（50宝石）
- 离线时间延长（30宝石）
- 立即获得1小时收益（20宝石）

### 4.2 难度递进

| 阶段 | 金币目标 | 解锁建筑 |
|------|---------|---------|
| 起步 | 0-10K | 农场、工厂 |
| 发展 | 10K-1M | 市场、兵营 |
| 扩张 | 1M-100M | 魔法塔、城堡 |
| 帝国 | 100M+ | 全建筑Lv.50 |

---

## 五、Meta Game

### 5.1 局外持久成长

**科技树**：
| 科技 | 效果 |
|------|------|
| 自动点击 | 每秒自动点击1次 |
| 暴击点击 | 5%概率点击收益×10 |
| 连锁反应 | 升级建筑时有概率免费升级另一个 |

**赛季系统**：每月重置，根据最高金币排名发放奖励。

### 5.2 解锁系统

- 建筑皮肤（古代/科幻/魔法）
- 点击特效（粒子/音效）
- 新建筑（需赛季解锁）

### 5.3 社交/竞技

- 金币积累排行榜
- 点击次数排行
- 分享里程碑

---

## 六、广告变现设计

| 时机 | 类型 | 说明 |
|------|------|------|
| 上线领取离线收益 | 激励视频 | 离线收益×2 |
| 任务完成 | 插屏 | 每3个任务 |
| 升级加速 | 激励视频 | 免费升级1次 |

### 6.2 付费点

- 去广告 $2.99
- 自动点击器 $4.99（永久每秒自动点击）
- 宝石包 $0.99-$9.99

---

## 七、技术实现评估

- 渲染：Canvas 2D / DOM
- 物理：无
- 网络：单机+排行榜
- 存储：localStorage

**AI开发难度：5分** — 数值公式+点击计数+离线计算，逻辑简单。

---

## 八、参考游戏

| 参考游戏 | 借鉴点 |
|---------|--------|
| Cookie Clicker | 点击放置鼻祖 |
| AdVenture Capitalist | 多建筑系统 |
| Tap Titans | 点击+离线收益 |

---

## 九、评分卡

| 维度 | 权重 | 评分 | 依据 |
|------|------|------|------|
| 受众广度 | 15% | **5** | 点击放置受众极广；碎片化友好 |
| 上手速度 | 15% | **5** | 点击1秒上手；无学习成本 |
| 常玩常新 | 12% | **4** | 数字膨胀驱动；但核心单调 |
| 局内成长 | 10% | **4** | 建筑升级+离线收益；成长感强 |
| 无UI可验证 | 10% | **5** | 纯数值公式；点击计数+建筑产出 |
| AI开发难度 | 10% | **5** | 数值公式+本地存储；无复杂逻辑 |
| 广告变现 | 8% | **5** | 离线收益×2天然激励；点击间隙插屏 |
| 玩法新鲜度 | 5% | **3** | 点击放置常见；帝国主题稍新 |
| 用户粘性 | 5% | **4** | 数字膨胀+离线收益驱动每日回归 |
| 受众规模 | 5% | **4** | 估算千万级（放置类受众） |
| 难度递增 | 3% | **3** | 数值膨胀，无实质难度变化 |
| 局外Meta | 2% | **4** | 赛季+科技树+排行榜 |
| **加权总分** | **100%** | **4.19** | — |