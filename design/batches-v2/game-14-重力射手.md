# 重力射手 (Gravity Shooter) — 完整创意文档

> 核心组合：重力翻转 + 消除射击
> 预估总分：**4.05**

---

## 一、界面布局

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 背景 -->
  <rect width="360" height="640" fill="#1a1a2e"/>
  
  <!-- 顶部状态栏 -->
  <rect x="0" y="0" width="360" height="50" fill="#16213e"/>
  <text x="20" y="32" fill="#eee" font-size="14" font-family="sans-serif">第 20 关</text>
  <text x="180" y="32" text-anchor="middle" fill="#2ecc71" font-size="16" font-family="sans-serif" font-weight="bold">🎯 得分 12,580</text>
  <text x="340" y="32" text-anchor="end" fill="#e74c3c" font-size="14" font-family="sans-serif">❤ 3</text>
  
  <!-- 游戏区域 -->
  <rect x="10" y="60" width="340" height="400" fill="#0f3460" rx="8"/>
  
  <!-- 方块网格 6x10 -->
  <!-- 第1行 -->
  <rect x="20" y="70" width="50" height="30" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  <rect x="75" y="70" width="50" height="30" fill="#3498db" stroke="#2980b9" stroke-width="1" rx="2"/>
  <rect x="130" y="70" width="50" height="30" fill="#f39c12" stroke="#e67e22" stroke-width="1" rx="2"/>
  <rect x="185" y="70" width="50" height="30" fill="#2ecc71" stroke="#27ae60" stroke-width="1" rx="2"/>
  <rect x="240" y="70" width="50" height="30" fill="#9b59b6" stroke="#8e44ad" stroke-width="1" rx="2"/>
  <rect x="295" y="70" width="50" height="30" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  
  <!-- 第2行 -->
  <rect x="20" y="105" width="50" height="30" fill="#3498db" stroke="#2980b9" stroke-width="1" rx="2"/>
  <rect x="75" y="105" width="50" height="30" fill="#f39c12" stroke="#e67e22" stroke-width="1" rx="2"/>
  <rect x="130" y="105" width="50" height="30" fill="#2ecc71" stroke="#27ae60" stroke-width="1" rx="2"/>
  <rect x="185" y="105" width="50" height="30" fill="#9b59b6" stroke="#8e44ad" stroke-width="1" rx="2"/>
  <rect x="240" y="105" width="50" height="30" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  <rect x="295" y="105" width="50" height="30" fill="#3498db" stroke="#2980b9" stroke-width="1" rx="2"/>
  
  <!-- 第3行 -->
  <rect x="20" y="140" width="50" height="30" fill="#f39c12" stroke="#e67e22" stroke-width="1" rx="2"/>
  <rect x="75" y="140" width="50" height="30" fill="#2ecc71" stroke="#27ae60" stroke-width="1" rx="2"/>
  <rect x="130" y="140" width="50" height="30" fill="#9b59b6" stroke="#8e44ad" stroke-width="1" rx="2"/>
  <rect x="185" y="140" width="50" height="30" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  <rect x="240" y="140" width="50" height="30" fill="#3498db" stroke="#2980b9" stroke-width="1" rx="2"/>
  <rect x="295" y="140" width="50" height="30" fill="#f39c12" stroke="#e67e22" stroke-width="1" rx="2"/>
  
  <!-- 第4行 - 部分为空，方块在掉落 -->
  <rect x="20" y="175" width="50" height="30" fill="#2ecc71" stroke="#27ae60" stroke-width="1" rx="2"/>
  <rect x="75" y="175" width="50" height="30" fill="#9b59b6" stroke="#8e44ad" stroke-width="1" rx="2"/>
  <rect x="130" y="175" width="50" height="30" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  <!-- 空 -->
  <rect x="185" y="185" width="50" height="30" fill="#3498db" stroke="#2980b9" stroke-width="1" rx="2" opacity="0.7"/>
  <!-- 空 -->
  <rect x="295" y="175" width="50" height="30" fill="#2ecc71" stroke="#27ae60" stroke-width="1" rx="2"/>
  
  <!-- 第5行 -->
  <rect x="20" y="210" width="50" height="30" fill="#9b59b6" stroke="#8e44ad" stroke-width="1" rx="2"/>
  <rect x="75" y="210" width="50" height="30" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  <!-- 空 -->
  <!-- 空 -->
  <rect x="240" y="210" width="50" height="30" fill="#f39c12" stroke="#e67e22" stroke-width="1" rx="2"/>
  <rect x="295" y="210" width="50" height="30" fill="#9b59b6" stroke="#8e44ad" stroke-width="1" rx="2"/>
  
  <!-- 第6行及以下为空 -->
  
  <!-- 玩家飞船/发射器 -->
  <polygon points="170,420 190,420 185,405 175,405" fill="#2ecc71" stroke="#27ae60" stroke-width="2"/>
  <text x="180" y="418" text-anchor="middle" fill="#fff" font-size="10">▲</text>
  
  <!-- 发射的子弹 -->
  <circle cx="180" cy="390" r="5" fill="#f39c12"/>
  <line x1="180" y1="380" x2="180" y2="350" stroke="#f39c12" stroke-width="2" stroke-dasharray="3,3"/>
  
  <!-- 重力方向指示 -->
  <text x="320" y="300" fill="#888" font-size="20" font-family="sans-serif">↓</text>
  <text x="318" y="320" fill="#888" font-size="8" font-family="sans-serif">重力</text>
  
  <!-- 底部控制区 -->
  <rect x="10" y="470" width="340" height="160" fill="#16213e" rx="8"/>
  <text x="180" y="495" text-anchor="middle" fill="#888" font-size="12" font-family="sans-serif">滑动瞄准 | 点击发射 | 点击重力按钮翻转重力</text>
  
  <!-- 重力翻转按钮 -->
  <circle cx="60" cy="530" r="25" fill="#f39c12" stroke="#e67e22" stroke-width="2"/>
  <text x="60" y="525" text-anchor="middle" fill="#fff" font-size="12" font-family="sans-serif">↕</text>
  <text x="60" y="540" text-anchor="middle" fill="#f39c12" font-size="8" font-family="sans-serif">重力</text>
  
  <!-- 下一个子弹预览 -->
  <text x="120" y="520" fill="#aaa" font-size="10" font-family="sans-serif">下一个:</text>
  <rect x="115" y="530" width="40" height="25" fill="#e74c3c" stroke="#c0392b" stroke-width="1" rx="2"/>
  
  <!-- 技能按钮 -->
  <rect x="170" y="515" width="70" height="45" fill="#e74c3c" rx="6"/>
  <text x="205" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">炸弹</text>
  <text x="205" y="550" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×2</text>
  
  <rect x="250" y="515" width="70" height="45" fill="#3498db" rx="6"/>
  <text x="285" y="535" text-anchor="middle" fill="#fff" font-size="10" font-family="sans-serif">激光</text>
  <text x="285" y="550" text-anchor="middle" fill="#aaa" font-size="9" font-family="sans-serif">×1</text>
  
  <!-- 得分 -->
  <text x="180" y="590" text-anchor="middle" fill="#ffd700" font-size="14" font-family="sans-serif">连击 ×5 | 倍率 ×2.5</text>
  
  <!-- 关卡进度 -->
  <rect x="30" y="615" width="300" height="8" fill="#333" rx="4"/>
  <rect x="30" y="615" width="200" height="8" fill="#2ecc71" rx="4"/>
</svg>

---

## 二、核心玩法

### 一句话描述
控制飞船发射彩色子弹击中方块，点击重力按钮翻转重力让方块下落，凑齐3个同色方块消除并转化为得分。

### 详细规则

**方块系统**：
- 6 列×10 行的网格，顶部不断生成新方块
- 5 种颜色：红、蓝、黄、绿、紫
- 方块受重力影响向下掉落
- 初始重力方向：向下

**射击机制**：
- 玩家控制底部的飞船，左右滑动瞄准
- 点击屏幕发射子弹
- 子弹颜色与飞船当前装载的颜色一致
- 子弹击中方块：该方块变为子弹颜色

**重力翻转**：
- 点击"重力按钮"翻转重力方向（上↔下）
- 重力翻转后，所有方块向新方向掉落
- 翻转冷却：5 秒

**消除规则**：
- 3 个或以上同色方块相连（横/竖）→ 消除
- 消除得分 = 方块数 × 100 × 连击倍率
- 消除后上方方块掉落填补空缺

**失败条件**：
- 任意一列方块堆到第 10 行（触顶）→ 游戏结束

---

## 三、局内成长

**连击系统**：
- 连续消除不中断（间隔<3秒）→ 连击
- 连击×2：得分×1.5
- 连击×3：得分×2
- 连击×5：得分×3，解锁"彩虹子弹"（可匹配任何颜色）

**技能系统**：
| 技能 | 效果 | 冷却 |
|------|------|------|
| 炸弹 | 消除 3×3 范围内所有方块 | 10 秒 |
| 激光 | 消除一整列方块 | 15 秒 |
| 彩虹子弹 | 下 3 发子弹可匹配任何颜色 | 20 秒 |
| 时间暂停 | 方块停止生成 5 秒 | 30 秒 |

**重力策略**：
- 翻转重力可让分散的方块聚集
- 利用重力制造大规模连锁消除
- 危急时翻转重力让即将触顶的方块远离

**难度递增**：
- 前 10 关：只有向下重力，方块生成慢
- 11-30 关：增加向左/向右重力方向
- 31-60 关：增加"无重力"模式（方块漂浮）
- 61-100 关：多种重力方向混合，方块生成加速

---

## 四、Meta Game（局外系统）

**关卡系统**：
- 共 100 关，分 5 个主题（太空→海底→火山→冰原→次元）
- 每主题 20 关，重力机制不同
  - 太空：标准重力
  - 海底：重力翻转时水流效果
  - 火山：岩浆方块（无法消除，需特殊处理）
  - 冰原：冰冻方块（需击中2次才能变色）
  - 次元：重力方向每 10 秒自动随机切换

**飞船升级**：
| 升级项 | 效果 |
|--------|------|
| 射速 | 子弹发射间隔缩短 |
| 装载 | 可同时装载 2 种颜色子弹 |
| 重力 | 重力翻转冷却减少 |
| 护盾 | 自动抵挡一次触顶 |

**无尽模式**：
- 方块无限生成，速度逐渐加快
- 全球排行榜：比谁得分最高

**每日挑战**：
- "单色模式"：只有一种颜色方块
- "极速模式"：方块生成速度×2
- "重力混乱"：每 5 秒自动翻转重力

---

## 五、广告变现

**自然断点设计**：

| 断点类型 | 时机 | 广告形式 | 预估 eCPM |
|---------|------|---------|----------|
| 关卡完成 | 每关结束（约2-3分钟） | 插屏广告 | $8-12 |
| 游戏结束 | 方块触顶 | 激励视频（复活清除底部3行） | $15-25 |
| 技能冷却 | 急需技能 | 激励视频（重置冷却） | $10-15 |
| 双倍得分 | 游戏结束 | 激励视频（2倍本局得分） | $10-15 |

---

## 六、评分卡

| 维度 | 权重 | 评分 (1-5) | 依据来源 | 备注 |
|------|------|-----------|---------|------|
| 受众广度 | 15% | **4** | 消除类受众广 | 类似游戏：Candy Crush |
| 上手速度 | 15% | **5** | 滑动瞄准+点击发射，2秒理解 | 操作极简 |
| 常玩常新 | 12% | **4** | 重力翻转+随机方块 | 每局不同 |
| 局内成长 | 10% | **4** | 连击+技能升级 | 成长感清晰 |
| 无UI可验证 | 10% | **5** | 网格+重力物理+消除判定 | 纯数学可验证 |
| AI开发难度 | 10% | **5** | 2D网格+重力模拟+碰撞检测 | AI最擅长的技术栈 |
| 广告变现友好度 | 8% | **4** | 关卡结束/失败 | 断点较多 |
| 玩法新鲜度 | 5% | **4** | 重力翻转+射击消除组合新颖 | 市面极少见 |
| 用户粘性 | 5% | **4** | 连击追求+排行榜 | 消除类天然粘性 |
| 受众规模 | 5% | **4** | 消除类亿级受众 | 估算千万级 |
| 难度递增 | 3% | **4** | 新重力机制+新方块类型 | 100关梯度丰富 |
| 局外Meta | 2% | **3** | 飞船升级+无尽模式 | 较为常规 |
| **加权总分** | 100% | **4.05** | — | 目标≥3.8 ✅ |

---

## 七、为什么符合目标

1. **3秒上手**：滑动瞄准+点击发射，极简操作
2. **常玩常新**：随机方块+重力翻转策略
3. **局内成长**：连击加成→技能解锁
4. **无UI可验证**：网格+重力+消除，纯数学
5. **AI开发友好**：2D网格+物理模拟
6. **广告变现优秀**：关卡结束/失败断点

---

> 生成时间：2026-09-02 03:00 | 批次：02 | 编号：game-14
