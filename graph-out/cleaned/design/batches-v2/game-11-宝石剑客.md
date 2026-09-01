---
title: 宝石剑客 (Gem Swordsman) — 完整创意文档
original_filename: game-11-宝石剑客
source: gameplay-library
---

# 宝石剑客 (Gem Swordsman) — 完整创意文档

> 核心组合：Match-3颜色匹配 + RPG剑技战斗
> 预估总分：**4.11**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <rect width="360" height="640" fill="#1a1a2e"/>
  <rect x="0" y="0" width="360" height="40" fill="#16213e"/>
  <text x="180" y="26" text-anchor="middle" fill="#eee" font-size="14" font-family="sans-serif">关卡 12  |  连击 7  |  分数 24,500</text>
  <!-- 敌人区域 -->
  <rect x="0" y="40" width="360" height="130" fill="#0f3460"/>
  <text x="180" y="55" text-anchor="middle" fill="#aaa" font-size="10">敌人波次 — 击败全部敌人过关</text>
  <!-- 敌人1 -->
  <rect x="20" y="65" width="100" height="90" fill="#e74c3c" rx="8" opacity="0.8"/>
  <text x="70" y="95" text-anchor="middle" fill="#fff" font-size="20">🐺</text>
  <text x="70" y="120" text-anchor="middle" fill="#fff" font-size="11">HP: 45/120</text>
  <rect x="25" y="128" width="90" height="8" fill="#333" rx="4"/>
  <rect x="25" y="128" width="34" height="8" fill="#e74c3c" rx="4"/>
  <!-- 敌人2 -->
  <rect x="130" y="65" width="100" height="90" fill="#e74c3c" rx="8" opacity="0.9"/>
  <text x="180" y="95" text-anchor="middle" fill="#fff" font-size="20">🦇</text>
  <text x="180" y="120" text-anchor="middle" fill="#fff" font-size="11">HP: 80/80</text>
  <rect x="135" y="128" width="90" height="8" fill="#333" rx="4"/>
  <rect x="135" y="128" width="90" height="8" fill="#e74c3c" rx="4"/>
  <!-- 敌人3 -->
  <rect x="240" y="65" width="100" height="90" fill="#e74c3c" rx="8" opacity="0.7"/>
  <text x="290" y="95" text-anchor="middle" fill="#fff" font-size="20">👹</text>
  <text x="290" y="120" text-anchor="middle" fill="#fff" font-size="11">HP: 150/200</text>
  <rect x="245" y="128" width="90" height="8" fill="#333" rx="4"/>
  <rect x="245" y="128" width="68" height="8" fill="#e74c3c" rx="4"/>
  <!-- 宝石盘 -->
  <rect x="10" y="180" width="340" height="340" fill="#16213e" rx="8"/>
  <text x="180" y="198" text-anchor="middle" fill="#888" font-size="10">交换相邻宝石形成3连消除 (6×6)</text>
  <!-- 宝石网格 -->
  <g>
    <!-- 第1行 -->
    <rect x="15" y="205" width="50" height="50" fill="#e74c3c" rx="8" stroke="#c0392b" stroke-width="2"/>
    <text x="40" y="237" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="70" y="205" width="50" height="50" fill="#3498db" rx="8" stroke="#2980b9" stroke-width="2"/>
    <text x="95" y="237" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="125" y="205" width="50" height="50" fill="#2ecc71" rx="8" stroke="#27ae60" stroke-width="2"/>
    <text x="150" y="237" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="180" y="205" width="50" height="50" fill="#f1c40f" rx="8" stroke="#f39c12" stroke-width="2"/>
    <text x="205" y="237" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="235" y="205" width="50" height="50" fill="#e74c3c" rx="8" stroke="#c0392b" stroke-width="2"/>
    <text x="260" y="237" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="290" y="205" width="50" height="50" fill="#9b59b6" rx="8" stroke="#8e44ad" stroke-width="2"/>
    <text x="315" y="237" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <!-- 第2行 -->
    <rect x="15" y="260" width="50" height="50" fill="#2ecc71" rx="8" stroke="#27ae60" stroke-width="2"/>
    <text x="40" y="292" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="70" y="260" width="50" height="50" fill="#f1c40f" rx="8" stroke="#f39c12" stroke-width="2"/>
    <text x="95" y="292" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="125" y="260" width="50" height="50" fill="#e74c3c" rx="8" stroke="#c0392b" stroke-width="2"/>
    <text x="150" y="292" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="180" y="260" width="50" height="50" fill="#3498db" rx="8" stroke="#2980b9" stroke-width="2"/>
    <text x="205" y="292" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="235" y="260" width="50" height="50" fill="#2ecc71" rx="8" stroke="#27ae60" stroke-width="2"/>
    <text x="260" y="292" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="290" y="260" width="50" height="50" fill="#f1c40f" rx="8" stroke="#f39c12" stroke-width="2"/>
    <text x="315" y="292" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <!-- 第3行 -->
    <rect x="15" y="315" width="50" height="50" fill="#9b59b6" rx="8" stroke="#8e44ad" stroke-width="2"/>
    <text x="40" y="347" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="70" y="315" width="50" height="50" fill="#e74c3c" rx="8" stroke="#c0392b" stroke-width="2"/>
    <text x="95" y="347" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="125" y="315" width="50" height="50" fill="#f1c40f" rx="8" stroke="#f39c12" stroke-width="2"/>
    <text x="150" y="347" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="180" y="315" width="50" height="50" fill="#e74c3c" rx="8" stroke="#c0392b" stroke-width="2"/>
    <text x="205" y="347" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="235" y="315" width="50" height="50" fill="#3498db" rx="8" stroke="#2980b9" stroke-width="2"/>
    <text x="260" y="347" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="290" y="315" width="50" height="50" fill="#9b59b6" rx="8" stroke="#8e44ad" stroke-width="2"/>
    <text x="315" y="347" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <!-- 第4行 -->
    <rect x="15" y="370" width="50" height="50" fill="#3498db" rx="8" stroke="#2980b9" stroke-width="2"/>
    <text x="40" y="402" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="70" y="370" width="50" height="50" fill="#2ecc71" rx="8" stroke="#27ae60" stroke-width="2"/>
    <text x="95" y="402" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="125" y="370" width="50" height="50" fill="#9b59b6" rx="8" stroke="#8e44ad" stroke-width="2"/>
    <text x="150" y="402" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="180" y="370" width="50" height="50" fill="#f1c40f" rx="8" stroke="#f39c12" stroke-width="2"/>
    <text x="205" y="402" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="235" y="370" width="50" height="50" fill="#e74c3c" rx="8" stroke="#c0392b" stroke-width="2"/>
    <text x="260" y="402" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
    <rect x="290" y="370" width="50" height="50" fill="#3498db" rx="8" stroke="#2980b9" stroke-width="2"/>
    <text x="315" y="402" text-anchor="middle" fill="#fff" font-size="20">♦️</text>
  </g>
  <!-- 技能提示 -->
  <rect x="0" y="525" width="360" height="60" fill="#16213e"/>
  <text x="180" y="545" text-anchor="middle" fill="#aaa" font-size="10">消除颜色 → 发动剑技</text>
  <rect x="20" y="555" width="70" height="22" fill="#e74c3c" rx="4"/>
  <text x="55" y="570" text-anchor="middle" fill="#fff" font-size="9">🔥 火焰斩</text>
  <rect x="100" y="555" width="70" height="22" fill="#3498db" rx="4"/>
  <text x="135" y="570" text-anchor="middle" fill="#fff" font-size="9">❄️ 冰霜箭</text>
  <rect x="180" y="555" width="70" height="22" fill="#2ecc71" rx="4"/>
  <text x="215" y="570" text-anchor="middle" fill="#fff" font-size="9">💚 治疗术</text>
  <rect x="260" y="555" width="80" height="22" fill="#f1c40f" rx="4"/>
  <text x="300" y="570" text-anchor="middle" fill="#fff" font-size="9">⚡ 闪电链</text>
  <!-- 必杀条 -->
  <rect x="0" y="590" width="360" height="50" fill="#0f3460"/>
  <text x="20" y="608" fill="#f1c40f" font-size="11">必杀技</text>
  <rect x="70" y="595" width="270" height="12" fill="#333" rx="6"/>
  <rect x="70" y="595" width="189" height="12" fill="#f1c40f" rx="6"/>
  <text x="180" y="625" text-anchor="middle" fill="#f1c40f" font-size="12">连击7次 — 再3连击触发必杀！</text>
</svg>

---

## 二、基础信息

| 字段 | 内容 |
|------|------|
| 游戏名称 | 宝石剑客 / Gem Swordsman |
| 核心组合 | Match-3颜色匹配 + RPG剑技战斗 |
| 一句话描述 | 交换宝石形成同色连线消除，释放对应属性的剑技攻击上方敌人 |
| 目标平台 | Mobile (iOS+Android)，竖屏 |
| 预估单局时长 | 3-5分钟/关 |
| 预估开发周期 | AI构建约5-7天 |

---

## 三、核心玩法

### 3.1 玩家输入

| 操作 | 区域 | 反馈 |
|------|------|------|
| **拖拽交换** | 宝石盘内相邻宝石 | 两个宝石交换位置，如形成3连则消除+下落填充，播放消除动画和音效 |
| **点击必杀** | 必杀条满时点击 | 释放全屏大招，清除所有敌人并播放华丽特效 |

### 3.2 游戏实体

**宝石（6种颜色）**：
| 颜色 | 剑技 | 伤害 | 特效 |
|------|------|------|------|
| 红色 🔥 | 火焰斩 | 高（1.5×基础） | 单体高伤，暴击率+20% |
| 蓝色 ❄️ | 冰霜箭 | 中 | 减速敌人下回合50% |
| 绿色 💚 | 治疗术 | 0 | 恢复角色HP 5% |
| 黄色 ⚡ | 闪电链 | 中 | 弹射最多3个敌人 |
| 紫色 💜 | 暗影击 | 高（2×基础） | 无视防御 |
| 橙色 🧡 | 大地震 | 中 | 眩晕敌人1回合 |

**消除伤害公式**：
- 3连 = 基础伤害 × 1.0
- 4连 = 基础伤害 × 2.0
- 5连 = 基础伤害 × 4.0 + 额外效果
- T/L型 = 基础伤害 × 3.0 + 生成特殊宝石

**连击系统**：
- 连续消除不中断（每次消除后3秒内再次消除算连击）
- 连击3次：伤害×1.5
- 连击5次：伤害×2.0
- 连击7次：伤害×3.0，必杀条+30%
- 连击10次：触发"狂怒模式"（5秒内所有伤害×2）

**敌人**：
| 敌人类型 | HP | 攻击 | 特殊 |
|----------|-----|------|------|
| 野狼 🐺 | 120 | 15/回合 | 无 |
| 蝙蝠 🦇 | 80 | 10/回合 | 闪避20% |
| 巨魔 👹 | 200 | 25/回合 | 每3回合恢复20HP |
| 史莱姆 🟢 | 60 | 5/回合 | 分裂：死亡时分裂为2个 |
| Boss 🐉 | 500 | 40/回合 | 每5回合全屏攻击 |

### 3.3 胜负条件

- **胜利**：击败该关所有敌人
- **失败**：角色HP归零
- **星级**：⭐过关 / ⭐⭐剩余HP≥50% / ⭐⭐⭐无伤过关

### 3.4 核心循环

```
Step 1: 观察宝石盘，寻找可形成3连的交换
Step 2: 交换宝石，触发消除
Step 3: 根据消除颜色释放对应剑技攻击敌人
Step 4: 敌人回合：敌人攻击，角色扣HP
Step 5: 重复直到敌人全灭或角色死亡
Step 6: 过关结算，获得金币/经验/装备
```

---

## 四、局内成长系统

### 4.1 单局内成长

**武器升级**：
| 等级 | 基础伤害 | 解锁技能 |
|------|---------|---------|
| 1 | 20 | 无 |
| 2 | 35 | 连击伤害+20% |
| 3 | 55 | 4连生成火焰宝石（十字消除） |
| 4 | 80 | 5连生成雷电宝石（全屏同色消除） |
| 5 | 120 | 必杀技伤害×2 |

**剑技精通**：每使用一种颜色的剑技100次，该颜色伤害+10%（永久累积）。

### 4.2 难度递进

| 阶段 | 关卡 | 新变量 | 难度变化 |
|------|------|--------|---------|
| 教学期 | 1-5 | 3种颜色宝石 | 学习基础交换消除 |
| 入门期 | 6-15 | 4种颜色+简单敌人 | 需要颜色策略选择 |
| 成长期 | 16-30 | 5种颜色+多敌人 | 需要连击管理 |
| 挑战期 | 31-50 | 6种颜色+特殊敌人 | 需要精通所有剑技 |
| 大师期 | 51+ | 步数限制+限时 | 高压下的快速决策 |

---

## 五、Meta Game

### 5.1 局外持久成长

**角色系统**：
| 角色 | 解锁条件 | 特色 |
|------|---------|------|
| 火焰剑士 | 初始 | 红色伤害+30% |
| 冰霜法师 | 通关10关 | 蓝色附带冻结效果 |
| 自然德鲁伊 | 通关25关 | 绿色治疗量×2 |
| 暗影刺客 | 通关50关 | 紫色无视防御概率+30% |

**装备锻造**：
- 武器：攻击力+ / 暴击率+ / 连击加成+
- 护甲：HP+ / 防御+ / 闪避+
- 饰品：金币收益+ / 经验收益+ / 特殊效果

### 5.2 解锁系统

**新宝石类型**：通关特定关卡解锁（彩虹宝石=任意颜色，炸弹宝石=3×3爆炸）。

**剑技特效皮肤**：火焰→冰霜/雷电/暗影等不同视觉风格。

**主题场景**：森林/沙漠/冰雪/火山/深渊。

### 5.3 社交/竞技

- 全球关卡竞速排行（最少步数/最短时间）
- 好友最高连击挑战
- 分享"10连击截图"

---

## 六、广告变现设计

### 6.1 广告插入点

| 时机 | 广告类型 | 说明 |
|------|------|------|
| 关卡完成 | 插屏 | 每3关一次 |
| 关卡失败 | 激励视频 | 复活（恢复50%HP，保留当前局面） |
| 步数耗尽 | 激励视频 | +5步 |
| 每日奖励 | 激励视频 | 双倍 |

### 6.2 激励视频场景

- **复活继续**：死亡时复活
- **+5步**：步数不足时补充
- **免费重排**：宝石盘无可消除时免费重排
- **双倍收益**：过关金币×2

### 6.3 付费点

| 商品 | 价格 | 内容 |
|------|------|------|
| 去广告 | $2.99 | 移除插屏 |
| 生命包 | $1.99 | 5颗复活心 |
|  starter包 | $0.99 | 武器+护甲+1000金币 |

---

## 七、技术实现评估

| 项目 | 选择 | 理由 |
|------|------|------|
| 渲染 | Canvas 2D / PixiJS | 2D宝石网格+消除动画 |
| 物理 | 无 | 宝石下落用缓动动画，无需物理引擎 |
| 网络 | 单机 + 排行榜 | 核心单机 |
| 存储 | localStorage | 进度+装备 |

**AI开发难度：5分** — 2D网格+匹配检测算法+下落填充，开源Match-3参考多。

---

## 八、参考游戏

| 参考游戏 | 借鉴点 |
|---------|--------|
| Puzzle Quest | Match-3+RPG战斗的先驱 |
| Candy Crush | 交换消除的核心交互 |
| Bejeweled | 连击系统+特殊宝石 |

---

## 九、评分卡

| 维度 | 权重 | 评分 | 评分依据 |
|------|------|------|---------|
| 受众广度 | 15% | **5** | Match-3（Candy Crush亿级下载）+RPG均为大众类型；竖屏Mobile；拖拽操作直觉 |
| 上手速度 | 15% | **5** | 交换相邻宝石跟Candy Crush完全一致，2秒上手；消除→攻击逻辑直觉 |
| 常玩常新 | 12% | **4** | 随机宝石盘面；不同敌人需要不同颜色策略；但核心消除机制固定 |
| 局内成长 | 10% | **4** | 武器升级1→5攻击力20→120；连击伤害递增；剑技精通累积；但局内成长主要在数值 |
| 无UI可验证 | 10% | **5** | 6×6网格坐标+宝石颜色数组+3连检测算法+伤害数值计算；全部可单元测试 |
| AI开发难度 | 10% | **5** | 2D网格+Match-3检测算法（BFS/DFS）+下落填充+伤害计算；开源参考极多 |
| 广告变现 | 8% | **4** | 关卡完成/失败复活/步数补充均为自然断点；但单局3-5分钟插屏频率需控制 |
| 玩法新鲜度 | 5% | **3** | Puzzle Quest（2007年）已开创Match-3+RPG品类，市面类似品较多 |
| 用户粘性 | 5% | **4** | 连击爽快感强；角色/装备解锁驱动；三星挑战；但Match-3后期可能倦怠 |
| 受众规模 | 5% | **4** | 估算千万级（Match-3受众广但竞争激烈） |
| 难度递增 | 3% | **4** | 颜色数量递增（3→6）；敌人类型递增；步数/限时限制出现 |
| 局外Meta | 2% | **3** | 4角色+装备锻造+皮肤解锁；Meta深度中等 |
| **加权总分** | **100%** | **4.11** | — |