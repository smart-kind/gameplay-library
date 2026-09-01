# 画线骑士 (Draw Knight) — 完整创意文档

> 核心组合：画线路径 + 自动战斗
> 预估总分：**4.15**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 背景 -->
  <rect width="360" height="640" fill="#1a1a2e"/>
  
  <!-- 顶部状态栏 -->
  <rect x="0" y="0" width="360" height="50" fill="#16213e"/>
  <text x="20" y="32" fill="#eee" font-size="14" font-family="sans-serif">第 12 关</text>
  <text x="180" y="32" text-anchor="middle" fill="#ffd700" font-size="16" font-family="sans-serif" font-weight="bold">⚔ 骑士 ×5</text>
  <text x="340" y="32" text-anchor="end" fill="#2ecc71" font-size="14" font-family="sans-serif">🏆 3⭐</text>
  
  <!-- 游戏区域 -->
  <rect x="10" y="60" width="340" height="400" fill="#0f3460" rx="8"/>
  
  <!-- 起点 -->
  <circle cx="50" cy="100" r="18" fill="#3498db" stroke="#2980b9" stroke-width="2"/>
  <text x="50" y="106" text-anchor="middle" fill="#fff" font-size="12" font-family="sans-serif">🏰</text>
  
  <!-- 终点/宝箱 -->
  <circle cx="310" cy="420" r="18" fill="#f39c12" stroke="#e67e22" stroke-width="2"/>
  <text x="310" y="426" text-anchor="middle" font-size="14">📦</text>
  
  <!-- 玩家画的路径 -->
  <path d="M 50,100 Q 100,80 130,140 T 180,180 T 220,240 T 260,300 T 310,350" 
        stroke="#2ecc71" stroke-width="4" fill="none" stroke-linecap="round"/>
  
  <!-- 路径上的骑士 -->
  <circle cx="90" cy="95" r="8" fill="#3498db" stroke="#fff" stroke-width="1"/>
  <text x="90" y="99" text-anchor="middle" fill="#fff" font-size="8">⚔</text>
  
  <circle cx="155" cy="160" r="8" fill="#3498db" stroke="#fff" stroke-width="1"/>
  <text x="155" y="164" text-anchor="middle" fill="#fff" font-size="8">⚔</text>
  
  <circle cx="200" cy="210" r="8" fill="#3498db" stroke="#fff" stroke-width="1"/>
  <text x="200" y="214" text-anchor="middle" fill="#fff" font-size="8">⚔</text>
  
  <circle cx="240" cy="270" r="8" fill="#3498db" stroke="#fff" stroke-width="1"/>
  <text x="240" y="274" text-anchor="middle" fill="#fff" font-size="8">⚔</text>
  
  <circle cx="285" cy="335" r="8" fill="#3498db" stroke="#fff" stroke-width="1"/>
  <text x="285" y="339" text-anchor="middle" fill="#fff" font-size="8">⚔</text>
  
  <!-- 敌人 -->
  <circle cx="140" cy="120" r="10" fill="#e74c3c" stroke="#c0392b" stroke-width="2"/>
  <text x="140" y="124" text-anchor="middle" fill="#fff" font-size="8">👹</text>
  
  <circle cx="200" cy="150" r="10" fill="#e74c3c" stroke="#c0392b" stroke-width="2"/>
  <text x="200" y="154" text-anchor="middle" fill="#fff" font-size="8">👹</text>
  
  <circle cx="170" cy="250" r="12" fill="#9b59b6" stroke="#8e44ad" stroke-width="2"/>
  <text x="170" y="255" text-anchor="middle" fill="#fff" font-size="10">👺</text>
  
  <circle cx="280" cy="280" r="10" fill="#e74c3c" stroke="#c0392b" stroke-width="2"/>
  <text x="280" y="284" text-anchor="middle" fill="#fff" font-size="8">👹</text>
  
  <!-- 资源点 -->
  <circle cx="120" cy="180" r="8" fill="#f39c12" stroke="#e67e22" stroke-width="1"/>
  <text x="120" y="184" text-anchor="middle" fill="#fff" font-size="8">🪙</text>
  
  <circle cx="230" cy="200" r="8" fill="#e74c3c" stroke="#c0392b" stroke-width="1"/>
  <text x="230" y="204" text-anchor="middle" fill="#fff" font-size="8">❤</text>
  
  <circle cx="190" cy="320" r="8" fill="#f39c12" stroke="#e67e22" stroke-width="1"/>
  <text x="190" y="324" text-anchor="middle" fill="#fff" font-size="8">🪙</text>
  
  <!-- 障碍物 -->
  <rect x="100" y="220" width="30" height="30" fill="#333" rx="4"/>
  <rect x="250" y="180" width="30" height="30" fill="#333" rx="4"/>
  <rect x="150" y="300" width="30" height="30" fill="#333" rx="4"/>
  
  <!-- 路径长度指示 -->
  <text x="180" y="445" text-anchor="middle" fill="#888" font-size="11" font-family="sans-serif">路径长度: 280m | 骑士速度: 2m/s</text>
  
  <!-- 底部控制区 -->
  <rect x="10" y="470" width="340" height="160" fill="#16213e" rx="8"/>
  <text x="180" y="495" text-anchor="middle" fill="#888" font-size="12" font-family="sans-serif">画线连接城堡到宝箱，骑士自动沿路径前进</text>
  
  <!-- 技能按钮 -->
  <rect x="30" y="515" width="70" height="45" fill="#3498db" rx="6"/>
  <text x="65" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">加速</text>
  <text x="65" y="550" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×3</text>
  
  <rect x="110" y="515" width="70" height="45" fill="#e74c3c" rx="6"/>
  <text x="145" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">狂暴</text>
  <text x="145" y="550" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×2</text>
  
  <rect x="190" y="515" width="70" height="45" fill="#9b59b6" rx="6"/>
  <text x="225" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">召唤</text>
  <text x="225" y="550" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×1</text>
  
  <rect x="270" y="515" width="70" height="45" fill="#f39c12" rx="6"/>
  <text x="305" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">护盾</text>
  <text x="305" y="550" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×2</text>
  
  <!-- 重画按钮 -->
  <rect x="120" y="575" width="120" height="35" fill="#e67e22" rx="6"/>
  <text x="180" y="597" text-anchor="middle" fill="#fff" font-size="12" font-family="sans-serif">🔄 重画路径</text>
  
  <!-- 剩余步数 -->
  <text x="180" y="630" text-anchor="middle" fill="#aaa" font-size="11" font-family="sans-serif">剩余重画次数: 2/3</text>
</svg>

---

## 二、核心玩法

### 一句话描述
用手指画出骑士前进的路径，骑士自动沿路径收集资源、击败敌人，到达终点宝箱完成关卡。

### 详细规则

**画线机制**：
- 玩家从城堡起点按住屏幕，自由画线到终点宝箱
- 路径可以是任意曲线，但不能穿过障碍物
- 路径长度有限制（每关不同，如 300m）
- 画完后骑士自动沿路径前进

**骑士行为**：
- 骑士沿路径匀速前进（默认 2m/s）
- 遇到敌人自动进入战斗（攻击力 vs 敌人血量）
- 遇到资源自动收集（金币、生命药水、装备）
- 到达终点宝箱，关卡完成

**战斗系统**：
- 骑士攻击力 = 基础攻击 + 装备加成 + 沿途收集的增益
- 敌人有攻击范围和血量
- 骑士进入敌人攻击范围，双方同时造成伤害
- 骑士血量归零 = 路径失败，可重画或复活

**三星评价**：
- ⭐ 到达终点
- ⭐⭐ 收集所有资源点
- ⭐⭐⭐ 不损失任何骑士到达终点

---

## 三、局内成长

**沿途收集系统**：
| 收集物 | 效果 |
|--------|------|
| 🪙 金币 | 关卡结算奖励 |
| ❤ 生命药水 | 恢复 30% 血量 |
| ⚔ 剑 | 攻击力+20%（持续 10 秒） |
| 🛡 盾 | 受到伤害-50%（持续 10 秒） |
| ⚡ 闪电 | 秒杀路径上的下一个敌人 |
| 🍖 食物 | 移动速度+30%（持续 10 秒） |

**连击系统**：
- 连续收集 3 个同类型物品 → 效果翻倍
- 连续击败 3 个敌人 → 攻击力+50%（持续 15 秒）
- 无伤通过 5 个敌人 → 解锁"完美冲刺"（移动速度×2）

**路径策略选择**：
- 长路径：收集更多资源，但遭遇更多敌人
- 短路径：快速到达终点，但奖励较少
- 绕路路径：避开强敌，但消耗路径长度配额
- 穿敌路径：穿过敌人密集区，高风险高回报

**技能释放**：
- 加速：骑士移动速度×2，持续 5 秒
- 狂暴：攻击力×3，但受到伤害也×2，持续 5 秒
- 召唤：路径中额外召唤 2 个骑士
- 护盾：免疫所有伤害，持续 5 秒

---

## 四、Meta Game（局外系统）

**关卡系统**：
- 共 120 关，分 6 个大陆（草原→森林→雪山→沙漠→火山→天空城）
- 每大陆 20 关，最后 1 关为 Boss 战
- Boss 战：画线引导骑士攻击 Boss 弱点

**骑士养成**：
| 养成项 | 效果 |
|--------|------|
| 等级 | 提升基础攻击和血量 |
| 武器 | 剑/斧/枪，不同攻击范围和速度 |
| 护甲 | 轻甲（速度快）/重甲（防御高）/法袍（技能强化） |
| 坐骑 | 马（速度快）/熊（攻击高）/鹰（可飞越障碍） |

**装备系统**：
- 白色（普通）→ 绿色（优秀）→ 蓝色（稀有）→ 紫色（史诗）→ 橙色（传说）
- 装备可强化（消耗金币）和附魔（消耗材料）

**公会系统**：
- 加入公会，共享路径攻略
- 公会战：集体画线攻略巨型地图
- 公会排行榜

**每日挑战**：
- "最短路径"：用最短路径到达终点
- "全收集"：收集地图上所有物品
- "限时冲刺"：60 秒内到达终点
- "无伤挑战"：不损失任何骑士通关

---

## 五、广告变现

**自然断点设计**：

| 断点类型 | 时机 | 广告形式 | 预估 eCPM |
|---------|------|---------|----------|
| 关卡完成 | 每关结束（约2-3分钟） | 插屏广告 | $8-12 |
| 路径失败 | 骑士全部阵亡 | 激励视频（复活继续） | $15-25 |
| 重画次数用尽 | 3次重画用完仍失败 | 激励视频（+3次重画） | $12-18 |
| 装备强化 | 强化失败时 | 激励视频（强化成功率+30%） | $10-15 |
| 双倍金币 | 关卡结算 | 激励视频（2倍金币） | $10-15 |
| 每日奖励 | 领取每日奖励 | 激励视频（双倍奖励） | $8-12 |

**广告频率控制**：
- 每 3 关强制插屏 1 次
- 激励视频每局限 3 次
- 去广告内购：$2.99

**广告友好度分析**：
- ✅ 关卡完成/失败天然断点
- ✅ 路径失败复活需求强烈
- ✅ 装备强化失败时"再试一次"心理
- ✅ 单局时长 2-3 分钟，频率适中

---

## 六、评分卡

| 维度 | 权重 | 评分 (1-5) | 依据来源 | 备注 |
|------|------|-----------|---------|------|
| 受众广度 | 15% | **5** | 画线操作极简单，全年龄段 | 类似游戏：Flight Control |
| 上手速度 | 15% | **5** | 画线即可，2秒理解 | 比滑动更直觉 |
| 常玩常新 | 12% | **4** | 每关地图不同+路径自由 | 但核心玩法固定 |
| 局内成长 | 10% | **4** | 收集物品+连击+技能 | 成长路径清晰 |
| 无UI可验证 | 10% | **4** | 路径坐标+碰撞检测+战斗计算 | 画线路径可矢量化 |
| AI开发难度 | 10% | **4** | 2D路径跟踪+碰撞检测+状态机 | 路径简化后可验证 |
| 广告变现友好度 | 8% | **4** | 关卡结束/失败/重画 | 断点较多 |
| 玩法新鲜度 | 5% | **4** | 画线+自动战斗组合少见 | 有 Flight Control 影子但+战斗 |
| 用户粘性 | 5% | **4** | 三星追求+骑士养成+装备收集 | RPG要素增加留存 |
| 受众规模 | 5% | **4** | 画线类+轻RPG叠加 | 估算千万级 |
| 难度递增 | 3% | **4** | 新障碍物+新敌人类型+新技能 | 120关梯度丰富 |
| 局外Meta | 2% | **4** | 装备+坐骑+公会+每日挑战 | 内容丰富 |
| **加权总分** | 100% | **4.15** | — | 目标≥3.8 ✅ |

**评分计算过程**：
```
5×0.15 + 5×0.15 + 4×0.12 + 4×0.10 + 4×0.10 + 4×0.10 + 4×0.08 + 4×0.05 + 4×0.05 + 4×0.05 + 4×0.03 + 4×0.02
= 0.75 + 0.75 + 0.48 + 0.40 + 0.40 + 0.40 + 0.32 + 0.20 + 0.20 + 0.20 + 0.12 + 0.08
= 4.30
```
（保守估计 **4.15**）

---

## 七、为什么符合目标

1. **3秒上手**：画线是最直觉的操作，无需教学
2. **常玩常新**：每关地图布局不同，路径选择千变万化
3. **局内成长**：沿途收集→连击→技能释放，成长感清晰
4. **无UI可验证**：路径坐标+碰撞检测+战斗数值，纯代码可推演
5. **AI开发友好**：2D路径跟踪+状态机，AI擅长生成
6. **广告变现优秀**：关卡结束/失败/重画都是天然断点

---

> 生成时间：2026-09-02 03:00 | 批次：02 | 编号：game-11
