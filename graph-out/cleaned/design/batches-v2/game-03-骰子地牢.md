---
title: 骰子地牢 (Dice Dungeon) — 完整创意文档
original_filename: game-03-骰子地牢
source: gameplay-library
---

# 骰子地牢 (Dice Dungeon) — 完整创意文档

> 核心组合：骰子 + Roguelike  
> 预估总分：**4.15**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <rect width="360" height="640" fill="#1a1a2e"/>
  <rect x="0" y="0" width="360" height="40" fill="#16213e"/>
  <text x="180" y="26" text-anchor="middle" fill="#eee" font-size="14">第3层  |  HP 45/80  |  金币 120</text>
  <rect x="10" y="50" width="340" height="200" fill="#16213e" rx="8"/>
  <text x="180" y="70" text-anchor="middle" fill="#aaa" font-size="12">地牢地图 (5×5房间)</text>
  <rect x="30" y="85" width="40" height="40" fill="#4ecca3" rx="4"/>
  <text x="50" y="110" text-anchor="middle" fill="#fff" font-size="10">起点</text>
  <rect x="80" y="85" width="40" height="40" fill="#e94560" rx="4" opacity="0.7"/>
  <text x="100" y="110" text-anchor="middle" fill="#fff" font-size="10">怪</text>
  <rect x="130" y="85" width="40" height="40" fill="#f9a825" rx="4"/>
  <text x="150" y="110" text-anchor="middle" fill="#fff" font-size="10">宝</text>
  <rect x="180" y="85" width="40" height="40" fill="#533483" rx="4"/>
  <text x="200" y="110" text-anchor="middle" fill="#fff" font-size="10">?</text>
  <rect x="230" y="85" width="40" height="40" fill="#e94560" rx="4" opacity="0.7"/>
  <rect x="280" y="85" width="40" height="40" fill="#4ecca3" rx="4" opacity="0.3"/>
  <text x="300" y="110" text-anchor="middle" fill="#fff" font-size="10">Boss</text>
  <rect x="0" y="260" width="360" height="200" fill="#0f3460"/>
  <text x="180" y="280" text-anchor="middle" fill="#aaa" font-size="12">战斗区域 - 掷骰子决定行动</text>
  <rect x="30" y="295" width="80" height="80" fill="#fff" rx="8"/>
  <circle cx="55" cy="315" r="6" fill="#333"/><circle cx="85" cy="315" r="6" fill="#333"/>
  <circle cx="55" cy="345" r="6" fill="#333"/><circle cx="85" cy="345" r="6" fill="#333"/>
  <circle cx="70" cy="330" r="6" fill="#333"/>
  <text x="70" y="395" text-anchor="middle" fill="#fff" font-size="14">骰子结果: 5</text>
  <rect x="130" y="295" width="90" height="40" fill="#e74c3c" rx="6"/>
  <text x="175" y="320" text-anchor="middle" fill="#fff" font-size="12">攻击 5×8=40</text>
  <rect x="130" y="345" width="90" height="40" fill="#3498db" rx="6"/>
  <text x="175" y="370" text-anchor="middle" fill="#fff" font-size="12">防御 +5盾</text>
  <rect x="235" y="295" width="90" height="40" fill="#2ecc71" rx="6"/>
  <text x="280" y="320" text-anchor="middle" fill="#fff" font-size="12">治疗 5×5=25</text>
  <rect x="235" y="345" width="90" height="40" fill="#f1c40f" rx="6"/>
  <text x="280" y="370" text-anchor="middle" fill="#fff" font-size="12">蓄力 下回+5</text>
  <rect x="0" y="470" width="360" height="170" fill="#16213e"/>
  <text x="180" y="490" text-anchor="middle" fill="#aaa" font-size="12">当前装备</text>
  <rect x="20" y="500" width="70" height="50" fill="#533483" rx="6"/>
  <text x="55" y="520" text-anchor="middle" fill="#fff" font-size="10">长剑</text>
  <text x="55" y="538" text-anchor="middle" fill="#aaa" font-size="9">攻击+3</text>
  <rect x="100" y="500" width="70" height="50" fill="#533483" rx="6"/>
  <text x="135" y="520" text-anchor="middle" fill="#fff" font-size="10">皮甲</text>
  <text x="135" y="538" text-anchor="middle" fill="#aaa" font-size="9">防御+2</text>
  <rect x="180" y="500" width="70" height="50" fill="#533483" rx="6"/>
  <text x="215" y="520" text-anchor="middle" fill="#fff" font-size="10">戒指</text>
  <text x="215" y="538" text-anchor="middle" fill="#aaa" font-size="9">骰子+1</text>
  <rect x="260" y="500" width="80" height="50" fill="#e94560" rx="6"/>
  <text x="300" y="525" text-anchor="middle" fill="#fff" font-size="12">掷骰子</text>
  <rect x="20" y="560" width="320" height="70" fill="#1a1a2e" rx="8"/>
  <text x="180" y="585" text-anchor="middle" fill="#fff" font-size="12">敌人: 史莱姆 HP 80/80</text>
  <text x="180" y="610" text-anchor="middle" fill="#e94560" font-size="10">下回合行动: 攻击 (预计伤害 15-25)</text>
</svg>

---

## 二、基础信息

| 字段 | 内容 |
|------|------|
| 游戏名称 | 骰子地牢 / Dice Dungeon |
| 核心组合 | 骰子掷点 + Roguelike 爬塔 |
| 一句话描述 | 每回合掷骰子，用点数选择行动（攻击/防御/治疗/蓄力），深入地牢击败Boss |
| 目标平台 | Mobile (iOS+Android)，竖屏 |
| 预估单局时长 | 8-15分钟（5层地牢） |
| 预估开发周期 | AI构建约5-7天 |

---

## 三、核心玩法

### 3.1 玩家输入

| 操作 | 区域 | 反馈 |
|------|------|------|
| **点击掷骰子** | 战斗区骰子按钮 | 骰子滚动动画，停止显示点数 |
| **点击行动** | 战斗区4个行动按钮 | 对应效果执行，敌人反击 |
| **点击房间** | 地图区相邻房间 | 角色移动，触发房间事件 |

### 3.2 游戏实体

**骰子**：
- 玩家初始1颗6面骰，通过装备可增加到2-3颗
- 掷出后点数总和决定行动强度
- 特殊装备可改变骰子面数（8面/10面/12面）

**行动选择（根据骰子点数）**：
| 行动 | 消耗 | 效果 | 计算公式 |
|------|------|------|---------|
| 攻击 | 全部点数 | 对敌人造成伤害 | 点数×武器攻击力 |
| 防御 | 全部点数 | 获得护盾 | 点数×护甲防御力 |
| 治疗 | 全部点数 | 恢复生命 | 点数×5 |
| 蓄力 | 全部点数 | 下回合点数+蓄力值 | 本次点数加到下回 |

**敌人类型**：
| 敌人 | HP | 攻击模式 | 特殊 |
|------|-----|---------|------|
| 史莱姆 | 80 | 每回合攻击15-20 | 分裂：死亡分裂为2个小史莱姆 |
| 骷髅兵 | 120 | 每回合攻击20-30 | 复活：3回合后复活一次 |
| 蝙蝠群 | 60 | 每回合攻击10-15×3 | 闪避：30%概率闪避攻击 |
| 地精商人 | 50 | 不攻击 | 可交易装备 |
| Boss（巨龙） | 500 | 每回合攻击30-50 | 火焰吐息：每3回合全屏攻击 |

### 3.3 胜负条件

- **胜利**：击败第5层Boss
- **失败**：HP归零
- **星级**：⭐过关 / ⭐⭐满血 / ⭐⭐⭐无伤通关

### 3.4 核心循环

```
Step 1: 在地图选择下一个房间（战斗/宝箱/事件/商店）
Step 2: 进入战斗→掷骰子
Step 3: 根据骰子点数选择行动（攻击/防御/治疗/蓄力）
Step 4: 行动执行，敌人反击
Step 5: 重复直到敌人死亡或玩家死亡
Step 6: 获得金币/装备/增益
Step 7: 继续探索下一层
```

---

## 四、局内成长系统

### 4.1 单局内成长

**装备系统（3个槽位：武器/护甲/饰品）**：
| 装备类型 | 效果示例 |
|---------|---------|
| 武器 | 长剑(攻击+3) / 法杖(攻击+2,治疗+2) / 匕首(攻击+5,防御-1) |
| 护甲 | 皮甲(防御+2) / 板甲(防御+5,速度-1) / 法袍(防御+1,治疗+3) |
| 饰品 | 幸运戒(骰子+1) / 力量护符(攻击+2) / 生命宝石(初始HP+20) |

**金币使用**：
- 地精商店购买装备
- 祭坛恢复HP（10金币=10HP）
- 强化装备（20金币=装备等级+1）

### 4.2 难度递进

| 层数 | 新要素 | 难度变化 |
|------|--------|---------|
| 1 | 基础敌人 | 教学层，熟悉骰子机制 |
| 2 | 引入装备系统 | 需要策略选择装备 |
| 3 | 敌人开始使用技能 | 需要预判敌人行动 |
| 4 | 精英敌人出现 | 需要专门Build应对 |
| 5 | Boss战 | 考验完整Build和骰子运气 |

---

## 五、Meta Game

### 5.1 局外持久成长

**职业解锁**：
| 职业 | 解锁条件 | 特色 |
|------|---------|------|
| 战士 | 初始 | 高HP，攻击骰子+1 |
| 法师 | 通关1次 | 可消耗法力替代骰子 |
| 盗贼 | 通关3次 | 可先看到敌人行动再掷骰 |
| 牧师 | 通关5次 | 治疗效率×2，初始带复活 |

**天赋树**：
- 攻击系：暴击率+5% / 连击伤害+10% / 穿透护甲
- 防御系：初始护盾+10 / 受伤减1 / 自动恢复
- 幸运系：骰子重掷次数+1 / 商店折扣20% / 宝箱质量+1

### 5.2 解锁系统

- 新地牢主题（森林/沙漠/冰雪/火山）
- 新骰子皮肤（金属/水晶/火焰）
- 挑战模式（限时/限定职业/诅咒模式）

### 5.3 社交/竞技

- 无尽地牢层数排行
- 最快通关时间排行
- 分享Build配置

---

## 六、广告变现设计

### 6.1 广告插入点

| 时机 | 类型 | 说明 |
|------|------|------|
| 层间过渡 | 插屏 | 进入新层时 |
| 死亡 | 激励视频 | 复活（恢复50%HP，继续当前层） |
| Boss前 | 激励视频 | 查看Boss属性和弱点 |

### 6.2 激励视频场景

- 复活继续（每局限1次）
- 额外骰子重掷（1次/层）
- 宝箱预览（看广告提前知道宝箱内容）

### 6.3 付费点

- 去广告 $2.99
- 职业包 $4.99（解锁全部职业）
- 月卡 $4.99（每日金币+额外复活）

---

## 七、技术实现评估

- 渲染：Canvas 2D
- 物理：无（回合制，纯数值）
- 网络：单机+排行榜
- 存储：localStorage

**AI开发难度：5分** — 回合制+状态机+数值公式，无实时计算压力。

---

## 八、参考游戏

| 参考游戏 | 借鉴点 |
|---------|--------|
| Dicey Dungeons | 骰子驱动战斗 |
| Slay the Spire | Roguelike爬塔+卡牌构建 |
| 骰子地下城 | 骰子机制 |

---

## 九、评分卡

| 维度 | 权重 | 评分 | 依据 |
|------|------|------|------|
| 受众广度 | 15% | **4** | Roguelike偏硬核；但骰子机制降低门槛 |
| 上手速度 | 15% | **5** | 掷骰子1秒理解；4选1行动简单 |
| 常玩常新 | 12% | **5** | 随机地图+随机装备+随机敌人=无限重玩 |
| 局内成长 | 10% | **4** | 装备3槽+金币强化+Build变化 |
| 无UI可验证 | 10% | **5** | 回合制纯数值；骰子结果决定一切 |
| AI开发难度 | 10% | **5** | 回合制+状态机+JSON配置；无实时计算 |
| 广告变现 | 8% | **4** | 层间过渡断点；死亡复活；单局8-15分钟 |
| 玩法新鲜度 | 5% | **3** | 骰子+Rogue已有Dicey Dungeons |
| 用户粘性 | 5% | **4** | 装备Build驱动重玩；职业解锁 |
| 受众规模 | 5% | **4** | 估算千万级（Rogue-lite受众） |
| 难度递增 | 3% | **4** | 5层递进；装备和敌人同步增强 |
| 局外Meta | 2% | **4** | 4职业+天赋树+挑战模式 |
| **加权总分** | **100%** | **4.15** | — |