# idle-defense (挂机防御者) — 完整创意文档

> 核心组合：塔防自动战斗 + 放置离线收益  
> 预估总分：**4.52**

---

## 一、界面布局

**整体结构**：
- 顶部：状态栏（常驻）
- 中间 75%：战场（路径 + 塔位）
- 底部：波次间隙才出现操作按钮，平时 clean

<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640">
  <!-- 背景 -->
  <rect width="360" height="640" fill="#1a1a2e"/>
  
  <!-- 顶部状态栏 -->
  <rect x="0" y="0" width="360" height="36" fill="#16213e"/>
  <text x="60" y="24" text-anchor="middle" fill="#ffd700" font-size="13" font-family="sans-serif">💰 12.5K</text>
  <text x="180" y="24" text-anchor="middle" fill="#eee" font-size="13" font-family="sans-serif">波次 5/10</text>
  <text x="300" y="24" text-anchor="middle" fill="#ff6b6b" font-size="13" font-family="sans-serif">❤️ 8/10</text>
  
  <!-- ====== 主战场区域 ====== -->
  <!-- 路径1：左上到左下 -->
  <rect x="40" y="45" width="80" height="540" fill="#0f3460" rx="4" opacity="0.6"/>
  <text x="80" y="65" text-anchor="middle" fill="#aaa" font-size="9">路径 ①</text>
  
  <!-- 路径2：中上到中下 -->
  <rect x="140" y="45" width="80" height="540" fill="#0f3460" rx="4" opacity="0.6"/>
  <text x="180" y="65" text-anchor="middle" fill="#aaa" font-size="9">路径 ②</text>
  
  <!-- 路径3：右上到右下 -->
  <rect x="240" y="45" width="80" height="540" fill="#0f3460" rx="4" opacity="0.6"/>
  <text x="280" y="65" text-anchor="middle" fill="#aaa" font-size="9">路径 ③</text>
  
  <!-- 塔位：路径两侧的空位（左侧） -->
  <rect x="10" y="120" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="10" y="200" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="10" y="320" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="10" y="440" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  
  <!-- 塔位：路径之间的空位 -->
  <rect x="128" y="160" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="128" y="280" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="128" y="400" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  
  <rect x="210" y="160" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="210" y="280" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="210" y="400" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  
  <!-- 塔位：路径右侧的空位 -->
  <rect x="328" y="120" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="328" y="200" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="328" y="320" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  <rect x="328" y="440" width="22" height="22" fill="none" stroke="#ab47bc" stroke-width="1.5" stroke-dasharray="3" rx="3"/>
  
  <!-- 已放置的塔 -->
  <!-- 左侧路径旁：箭塔 Lv.8 -->
  <circle cx="21" cy="211" r="14" fill="#4ecca3"/>
  <text x="21" y="216" text-anchor="middle" fill="#fff" font-size="9">🏹</text>
  <text x="21" y="200" text-anchor="middle" fill="#aaa" font-size="7">Lv.8</text>
  
  <!-- 路径1-2之间：法塔 Lv.5 -->
  <circle cx="139" cy="291" r="14" fill="#ab47bc"/>
  <text x="139" y="296" text-anchor="middle" fill="#fff" font-size="9">🔮</text>
  <text x="139" y="280" text-anchor="middle" fill="#aaa" font-size="7">Lv.5</text>
  
  <!-- 路径2-3之间：炮塔 Lv.12 -->
  <circle cx="221" cy="171" r="14" fill="#e94560"/>
  <text x="221" y="176" text-anchor="middle" fill="#fff" font-size="9">💣</text>
  <text x="221" y="160" text-anchor="middle" fill="#aaa" font-size="7">Lv.12</text>
  
  <!-- 右侧路径旁：箭塔 Lv.6 -->
  <circle cx="339" cy="331" r="14" fill="#4ecca3"/>
  <text x="339" y="336" text-anchor="middle" fill="#fff" font-size="9">🏹</text>
  <text x="339" y="320" text-anchor="middle" fill="#aaa" font-size="7">Lv.6</text>
  
  <!-- 敌人：在路径上移动 -->
  <!-- 路径1：小兵 -->
  <circle cx="80" cy="100" r="8" fill="#ff6b6b"/>
  <text x="80" y="104" text-anchor="middle" fill="#fff" font-size="8">👾</text>
  <circle cx="80" cy="160" r="8" fill="#ff6b6b"/>
  <text x="80" y="164" text-anchor="middle" fill="#fff" font-size="8">👾</text>
  <circle cx="80" cy="250" r="10" fill="#ff9800"/>
  <text x="80" y="254" text-anchor="middle" fill="#fff" font-size="8">🐢</text>
  
  <!-- 路径2：快速兵+Boss -->
  <circle cx="180" cy="85" r="7" fill="#ff6b6b"/>
  <text x="180" y="89" text-anchor="middle" fill="#fff" font-size="7">⚡</text>
  <circle cx="180" cy="130" r="7" fill="#ff6b6b"/>
  <text x="180" y="134" text-anchor="middle" fill="#fff" font-size="7">⚡</text>
  <circle cx="180" cy="210" r="16" fill="#d32f2f"/>
  <text x="180" y="216" text-anchor="middle" fill="#fff" font-size="10">👹</text>
  
  <!-- 路径3：小兵 -->
  <circle cx="280" cy="120" r="8" fill="#ff6b6b"/>
  <text x="280" y="124" text-anchor="middle" fill="#fff" font-size="8">👾</text>
  
  <!-- 防御线（底部红线） -->
  <line x1="0" y1="590" x2="360" y2="590" stroke="#e94560" stroke-width="4"/>
  <text x="180" y="585" text-anchor="middle" fill="#e94560" font-size="10">🛡️ 防御线</text>
  
  <!-- ====== 底部：波次间隙才出现的按钮 ====== -->
  <!-- "下一波"按钮（只在波次间隙显示） -->
  <rect x="110" y="600" width="140" height="32" fill="#4ecca3" rx="16" opacity="0.9"/>
  <text x="180" y="620" text-anchor="middle" fill="#16213e" font-size="12" font-weight="bold">▶ 开始第 6 波</text>
  
  <!-- ====== 点击塔后弹出的升级对话框（覆盖层示例） ====== -->
  <rect x="40" y="200" width="280" height="200" fill="#16213e" rx="12" stroke="#4ecca3" stroke-width="2" opacity="0.95"/>
  <text x="180" y="225" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">🏹 箭塔 Lv.8 → Lv.9</text>
  <text x="180" y="250" text-anchor="middle" fill="#aaa" font-size="11">攻击 120 → 144 (+20%)</text>
  <text x="180" y="270" text-anchor="middle" fill="#aaa" font-size="11">射程 2格 → 2格</text>
  <rect x="70" y="290" width="100" height="36" fill="#4ecca3" rx="6"/>
  <text x="120" y="312" text-anchor="middle" fill="#16213e" font-size="12" font-weight="bold">💰 500 升级</text>
  <rect x="190" y="290" width="100" height="36" fill="#666" rx="6"/>
  <text x="240" y="312" text-anchor="middle" fill="#fff" font-size="12">❌ 关闭</text>
  <text x="180" y="370" text-anchor="middle" fill="#ffd700" font-size="10">已攻击 1,240 次，消灭 586 敌人</text>
  
  <!-- ====== 技能按钮（右下角小圆，只在可释放时高亮） ====== -->
  <circle cx="330" cy="555" r="20" fill="#e94560" opacity="0.8"/>
  <text x="330" y="560" text-anchor="middle" fill="#fff" font-size="14">🔥</text>
  
  <circle cx="330" cy="510" r="20" fill="#26c6da" opacity="0.4"/>
  <text x="330" y="515" text-anchor="middle" fill="#fff" font-size="14">❄️</text>
</svg>

**界面说明**：
- **中间大片区域** = 战场，3 条垂直路径从上到下
- **路径两侧小方框** = 塔位（虚线 = 空位，实心圆 = 有塔）
- **路径上的 emoji** = 正在移动的敌人（👾 小兵 / ⚡ 快速兵 / 🐢 坦克 / 👹 Boss）
- **底部红线** = 防御线，敌人到达这里扣生命
- **"下一波"按钮** = 只在波次间隙出现，平时不显示
- **点击塔后弹出对话框** = 显示升级选项，不是常驻按钮
- **右下角小圆** = 技能按钮，冷却中时变暗

---

## 二、基础信息

| 字段 | 内容 |
|------|------|
| 游戏名称 | 挂机防御者 / Idle Defense |
| 核心组合 | 塔防自动战斗 + 放置离线收益 |
| 一句话描述 | 建造防御塔自动击退敌人波次，离线期间塔持续产金币，回来升级更强 |
| 目标平台 | Mobile (iOS+Android)，竖屏 |
| 预估单局时长 | 无需操作也可挂机，主动游玩 3-5 分钟/次 |
| 预估开发周期 | AI构建约 2-3 天 |

---

## 三、核心玩法

### 3.1 玩家输入

**常驻界面（战斗时）**：
| 操作 | 区域 | 反馈 |
|------|------|------|
| **点击空塔位** | 路径旁的虚线方框 | 弹出"建造菜单"：选择箭塔/法塔/炮塔 |
| **点击已有塔** | 塔图标 | 弹出"升级对话框"：显示当前属性+升级后属性+花费 |
| **点击技能图标** | 右下角小圆 | 释放技能（火焰风暴/冰冻领域） |
| **点击"下一波"** | 底部中央（仅波次间隙显示） | 立即开始下一波敌人 |
| **点击领取离线收益** | 顶部弹出的提示条（上线时） | 金币飞入，数字跳动 |

**对话框交互**：
- 升级对话框：显示 `Lv.X → Lv.X+1` 的属性对比 + 💰 花费按钮 + ❌ 关闭按钮
- 建造菜单：显示 3 种塔图标 + 攻击/射程/成本的简要对比

**无操作时**：塔自动攻击范围内敌人，无需玩家干预。

### 3.2 游戏实体

**防御塔类型**：
| 类型 | 攻击力 | 攻速 | 射程 | 特殊效果 | 升级成本 |
|------|--------|------|------|---------|---------|
| 箭塔 | 15 | 1.2/s | 2格 | 无 | 基础 |
| 法塔 | 40 | 0.8/s | 2.5格 | 减速 20% | 中 |
| 炮塔 | 100 | 0.4/s | 3格 | 范围溅射 | 高 |
| 电塔 | 5 | 3.0/s | 1.5格 | 连锁闪电（3目标） | 很高 |

**敌人波次**：
| 波次 | 敌人类型 | 血量 | 速度 | 金币掉落 |
|------|---------|------|------|---------|
| 1-3 | 小兵 | 50 | 1.0x | 10 |
| 4-6 | 快速兵 | 30 | 1.5x | 15 |
| 7-9 | 坦克 | 200 | 0.5x | 40 |
| 10 | Boss | 2000 | 0.3x | 500 |

### 3.3 胜负条件

- **胜利**：击败该关卡所有 10 波敌人
- **失败**：敌人到达防御线 10 次（生命归零）
- **星级**：⭐过关 / ⭐⭐剩余 5+ 生命 / ⭐⭐⭐满生命过关

### 3.4 核心循环（单局内）

```
Step 1: 观察敌人走到哪条路径、什么类型
Step 2: 点击路径旁的空塔位 → 选择建造箭塔/法塔/炮塔
Step 3: 塔自动攻击射程内的敌人（弹道从塔飞向敌人）
Step 4: 敌人被消灭 → 掉落金币（自动收集，顶部金币数字跳动）
Step 5: 本波敌人清空 → 底部出现"▶ 开始下一波"按钮
Step 6: 点击按钮 → 下一波更强的敌人出现
Step 7: 波次间隙可点击已有塔 → 弹出升级对话框，花费金币升级
```

**放置核心**：空位有限（每关固定 8-12 个），选择在哪里建什么塔是主要策略。

---

## 四、局内成长系统

### 4.1 单局内成长

**塔升级**：每座塔可无限升级，每次升级攻击+20%，成本×1.5。

**离线收益**：关闭游戏后，塔继续自动战斗（按当前战力推算），每小时产金币。
- 离线收益上限：24 小时
- 可观看激励视频双倍领取

**技能系统**：
| 技能 | 效果 | 冷却 | 消耗 |
|------|------|------|------|
| 火焰风暴 | 全屏敌人受到 3 秒持续伤害 | 60秒 | 免费 |
| 冰冻领域 | 全屏敌人减速 50%，持续 5 秒 | 90秒 | 免费 |
| 金币雨 | 立即获得 5 分钟离线收益 | 120秒 | 免费 |

### 4.2 难度递进

| 关卡 | 新机制 | 难度变化 |
|------|--------|---------|
| 1-5 | 基础 3 种塔 + 小兵/快速兵 | 熟悉操作 |
| 6-10 | 引入坦克（高血量） | 需要炮塔 |
| 11-15 | 引入飞行敌人（只能法塔/电塔打） | 塔类型搭配 |
| 16-20 | 敌人带护盾（需先破盾） | 输出节奏 |
| 21+ | Boss 波次 + 混合敌人 | 策略深度 |

---

## 五、Meta Game

### 5.1 局外持久成长

**科技树（3条线）**：
| 线名 | 升级内容 | 消耗 |
|------|---------|------|
| 攻击 | 塔基础攻击+10% / 暴击率+5% | 金币 |
| 经济 | 离线收益+20% / 金币掉落+15% | 金币 |
| 防御 | 防御线生命+1 / 敌人速度-5% | 金币 |

**塔皮肤**：升级科技树解锁皮肤（不影响数值）。

### 5.2 解锁系统

| 解锁内容 | 条件 |
|---------|------|
| 电塔 | 通关第 10 关 |
| 无尽模式 | 通关第 20 关 |
| 每日挑战 | 通关第 5 关 |
| 4 倍离线收益 | 观看 10 次激励视频 |

### 5.3 社交/竞技

- 全球无尽模式波数排行（周榜/总榜）
- 好友离线收益排行
- 过关战绩分享

---

## 六、广告变现设计

### 6.1 广告插入点

| 时机 | 广告类型 | 玩家情绪 | 预估频率 |
|------|---------|---------|---------|
| 波次间隙 | 插屏 | 短暂休息 | 每 3-4 波一次 |
| 关卡完成 | 插屏 | 成就感 | 每关一次 |
| 领取离线收益 | 激励视频 | 期待收益 | 每次上线 |
| 关卡失败 | 激励视频 | 遗憾，想继续 | 每局限 1 次 |
| 科技树升级 | 激励视频 | 加速成长 | 按需 |

### 6.2 激励视频场景

- **双倍离线收益**：上线领取时看广告 ×2
- **复活继续**：关卡失败看广告恢复 3 生命继续
- **免费加速**：看广告获得 10 分钟 2x 战斗速度
- **跳过等待**：科技树升级冷却看广告立即完成

### 6.3 付费点（IAP）

| 商品 | 价格 | 内容 |
|------|------|------|
| 去广告 | $2.99 | 移除所有插屏，保留激励视频 |
| 月卡 | $4.99/月 | 离线收益无上限+每日 5000 金币+2x 战斗速度 |
| Starter 包 | $0.99 | 10000 金币+电塔提前解锁 |

---

## 七、技术实现评估

| 项目 | 选择 | 理由 |
|------|------|------|
| 渲染 | Canvas 2D | 2D 塔+敌人+弹道，无需 3D |
| 物理 | 无（自定义） | 敌人直线移动，弹道直线飞行 |
| 网络 | 纯单机+排行榜 API | 核心玩法单机 |
| 存储 | localStorage | 进度本地存 |

**AI开发难度：5分** — 2D网格+状态机+JSON配置塔数据，开源塔防参考极多，AI可一次性生成可用代码。

---

## 八、参考游戏

| 参考游戏 | 借鉴点 |
|---------|--------|
| 王国保卫战 | 波次递进+塔类型搭配 |
| Tap Titans | 离线收益+自动战斗+回来升级 |
| 植物大战僵尸 | 防御线+敌人路径+塔自动攻击 |

---

## 九、评分卡

| 维度 | 权重 | 评分 | 评分依据（引用上文） |
|------|------|------|---------------------|
| 受众广度 | 15% | **5** | 塔防+放置均为亿级受众；目标平台 Mobile 竖屏；单指点击操作（见基础信息） |
| 上手速度 | 15% | **5** | 点击建造+自动战斗，无需操作塔；1 秒理解核心（见 3.1 玩家输入） |
| 常玩常新 | 12% | **4** | 离线收益驱动每日回来；关卡递进+新敌人类型；但核心循环较固定（见 4.1/4.2） |
| 局内成长 | 10% | **4** | 塔无限升级（攻击+20%/级）；技能系统；离线收益持续成长（见 4.1） |
| 无UI可验证 | 10% | **5** | 网格坐标+数值计算；敌人每帧 x/y 位移；弹道距离检测；纯离散状态（见技术实现） |
| AI开发难度 | 10% | **5** | Canvas 2D+无物理+JSON 配置塔数据；开源塔防参考极多（见技术实现评估） |
| 广告变现 | 8% | **5** | 波次间隙=天然断点；离线收益激励视频；失败复活；关卡完成插屏（见 6.1/6.2） |
| 玩法新鲜度 | 5% | **3** | 塔防+放置组合已存在（如 Idle Kingdom Defense），但数值体系可创新（见核心组合） |
| 用户粘性 | 5% | **4** | 离线收益驱动每日回来；科技树长期目标；排行榜竞争（见 5.1/5.3） |
| 受众规模 | 5% | **4** | 塔防+放置双热门叠加；竖屏休闲；低配置要求（见基础信息） |
| 难度递增 | 3% | **4** | 明确 5 阶段递进；每阶段新敌人类型+新机制（见 4.2） |
| 局外Meta | 2% | **3** | 3 条科技树+皮肤解锁；但深度一般（见 5.1） |
| **加权总分** | **100%** | **4.52** | — |

---

## 附录：MVP版本功能清单

**第一版（3天）**：
- [ ] 3 种基础塔（箭/法/炮）+ 自动攻击
- [ ] 10 波递进 + 3 种敌人类型
- [ ] 离线收益计算（关闭后按时间推算）
- [ ] 基础插屏广告

**完整版（+2天）**：
- [ ] 电塔 + 飞行敌人
- [ ] 科技树系统
- [ ] 激励视频（双倍离线/复活/加速）
- [ ] 无尽模式 + 排行榜
- [ ] IAP（去广告/月卡）
