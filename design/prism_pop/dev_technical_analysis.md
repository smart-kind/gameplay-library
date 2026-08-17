# 开发文档：彩棱碰碰技术分析与实现方案

> 文档角色：开发（Developer）  
> 版本：v0.1（阶段性结论）  
> 日期：2026-08-15

---

## 一、技术难度总评

### 整体评估：中等偏低

| 模块 | 难度 | 说明 |
|------|------|------|
| 核心玩法（画圈+引爆） | ⭐⭐ 低 | 标准网格系统+闭环检测，成熟方案 |
| 组合系统 | ⭐⭐⭐ 中 | 查表匹配+新宝石生成，逻辑清晰 |
| 关卡生成 | ⭐⭐⭐⭐ 中高 | 需要保证"可解性"，是最大挑战 |
| 特殊宝石效果 | ⭐⭐⭐ 中 | 每种宝石一个状态机，工作量可控 |
| 行动力系统 | ⭐⭐ 低 | 简单的计数器+重置逻辑 |

**总结：** 技术上没有天堑，都是已知模式。最大挑战是关卡生成算法。

---

## 二、核心系统实现方案

### 2.1 网格系统

**数据结构：**
```javascript
// 棋盘网格
class Grid {
  constructor(rows, cols) {
    this.rows = rows;
    this.cols = cols;
    this.cells = []; // 二维数组
    
    // 初始化
    for (let r = 0; r < rows; r++) {
      this.cells[r] = [];
      for (let c = 0; c < cols; c++) {
        this.cells[r][c] = {
          type: 'empty',      // empty / gem / wall / trail
          color: null,         // red / blue / green / yellow / purple
          gemLevel: 0,         // 0=普通, 1=强化, 2=超级, 3=终极
          isSpecial: false,    // 是否是特殊宝石（彩虹等）
        };
      }
    }
  }
}
```

**技术要点：**
- 网格尺寸：6×6 到 12×12，动态可调
- 每个格子是一个对象，包含类型、颜色、等级等属性
- 用二维数组存储，访问复杂度 O(1)

**开发周期：** 1天

---

### 2.2 路径与光轨系统

**数据结构：**
```javascript
class TrailSystem {
  constructor() {
    this.trail = []; // 存储路径点 [{row, col}, ...]
    this.maxSteps = 30; // 基础步数上限
    this.currentSteps = 0; // 当前已用步数
  }
  
  addPoint(row, col) {
    if (this.currentSteps >= this.maxSteps) {
      return false; // 步数用完
    }
    
    this.trail.push({row, col});
    this.currentSteps++;
    return true;
  }
  
  clear() {
    this.trail = [];
    this.currentSteps = 0;
  }
  
  resetSteps() {
    this.currentSteps = 0; // 引爆后重置步数
  }
}
```

**技术要点：**
- 路径用数组存储，每步 push 一个点
- 步数限制：基础30步，引爆后重置
- 行动力宝石：修改 `maxSteps` 或临时增加 `currentSteps` 上限

**关键决策：**
- ✅ **引爆后清空所有光轨**（方案C）
  - 实现：`this.trail = []`，一行代码
  - 优点：最简单，无边界case
- ❌ ~~虹化状态~~（已废弃）
  - 需要状态机管理"正常/虹化"两种模式
  - 需要处理路径交叉、8字形等复杂拓扑

**开发周期：** 1-2天

---

### 2.3 闭环检测系统

**核心算法：**
```javascript
function detectLoop(trail, grid) {
  // 检查路径首尾是否相连
  const first = trail[0];
  const last = trail[trail.length - 1];
  
  // 判断首尾是否相邻（上下左右）
  const isAdjacent = 
    (Math.abs(first.row - last.row) === 1 && first.col === last.col) ||
    (Math.abs(first.col - last.col) === 1 && first.row === last.row);
  
  if (!isAdjacent) return null; // 未形成闭环
  
  // 提取闭环内的格子
  const enclosedCells = extractEnclosedCells(trail, grid);
  return enclosedCells;
}
```

**技术要点：**
- 闭环判定：路径首尾相邻
- 提取闭环内格子：用 Flood Fill 算法，从闭环边界向内填充
- 复杂度：O(n)，n 是网格大小（最大144格）

**边界case：**
- ✅ **无虹化状态**：路径不可能自相交（因为不能穿越光轨）
- ✅ **8字形问题不存在**：画到交叉点时会碰到已有光轨，路径自动终止

**开发周期：** 1-2天

---

### 2.4 组合检测系统

**核心逻辑：**
```javascript
function checkCombination(enclosedCells) {
  // 1. 统计圈内宝石的颜色分布
  const colorCount = {};
  enclosedCells.forEach(cell => {
    if (cell.type === 'gem') {
      colorCount[cell.color] = (colorCount[cell.color] || 0) + 1;
    }
  });
  
  // 2. 查组合表
  const combination = matchCombination(colorCount);
  
  // 3. 执行组合结果
  if (combination) {
    executeCombination(combination, enclosedCells);
  } else {
    // 不触发组合，普通收集
    collectGems(enclosedCells);
  }
}

// 组合表（JSON配置）
const COMBINATION_TABLE = {
  "3_red": { result: "enhanced_red", level: 1 },
  "4_red": { result: "super_red", level: 2 },
  "5_red": { result: "ultimate_red", level: 3 },
  "red_blue_green": { result: "rainbow", level: 0 },
  // ... 其他组合
};
```

**技术要点：**
- 颜色统计：遍历圈内格子，按颜色分桶，O(n)
- 查表匹配：JSON配置表，热更新友好
- 组合执行：移除旧宝石，生成新宝石

**关键决策：**
- ✅ **组合表必须是数据驱动**（JSON配置），不能硬编码
- ✅ **新宝石生成在棋盘随机空位**（方案B），避免位置冲突

**开发周期：** 2-3天

---

### 2.5 特殊宝石行为系统

**设计模式：** 策略模式（Strategy Pattern）

```javascript
// 宝石基类
class Gem {
  constructor(color, level) {
    this.color = color;
    this.level = level;
  }
  
  onCollect() {
    // 子类重写
    return { score: 10 };
  }
}

// 强化宝石（3同色）
class EnhancedGem extends Gem {
  onCollect() {
    // 范围消除：周围8格
    return { 
      type: 'area_clear', 
      radius: 1, 
      score: 50 
    };
  }
}

// 超级宝石（4同色）
class SuperGem extends Gem {
  onCollect() {
    // 十字线消除：整行+整列
    return { 
      type: 'cross_clear', 
      score: 100 
    };
  }
}

// 终极宝石（5同色）
class UltimateGem extends Gem {
  onCollect() {
    // 全屏消除：同色全部消失
    return { 
      type: 'full_clear', 
      color: this.color,
      score: 200 
    };
  }
}

// 彩虹宝石
class RainbowGem extends Gem {
  onCollect() {
    // 清屏：消除所有宝石
    return { 
      type: 'clear_all', 
      score: 500 
    };
  }
}
```

**技术要点：**
- 每种特殊宝石是一个独立类，实现 `onCollect()` 方法
- 效果解耦：新增宝石类型不需要修改核心逻辑
- 状态机：特殊宝石的动画、音效用状态机管理

**开发周期：** 3-5天（5种特殊宝石 × 0.5-1天/种）

---

### 2.6 关卡生成系统

**这是最大的技术挑战。**

#### 方案A：伪随机生成（不推荐）

```javascript
function generateLevel(levelConfig) {
  // 随机撒宝石
  for (let i = 0; i < levelConfig.gemCount; i++) {
    const pos = randomEmptyPosition();
    grid.cells[pos.row][pos.col] = createGem();
  }
  
  // 问题：可能生成"死局"（无法凑出目标组合）
}
```

**缺点：**
- 无法保证"可解性"
- 玩家可能连续10关都凑不出3个同色

#### 方案B：反向生成（推荐）

```javascript
function generateLevel(levelConfig) {
  // 1. 先确定"这关要让玩家凑出什么组合"
  const targetCombinations = levelConfig.targets;
  
  // 2. 反推"棋盘上需要放哪些宝石"
  const requiredGems = calculateRequiredGems(targetCombinations);
  
  // 3. 放置宝石（确保可达）
  placeGems(requiredGems);
  
  // 4. 加围墙和干扰
  addWalls(levelConfig.wallDensity);
  
  // 5. 验证可解性
  if (!validateSolvable()) {
    return generateLevel(levelConfig); // 重新生成
  }
}
```

**技术要点：**
- 约束求解器：确保宝石分布合理，同色宝石不被围墙完全隔开
- 可解性验证：遍历所有可能的画圈路径，检查是否存在至少一种组合可达
- 前20关手工打磨：用关卡编辑器手动设计

**开发周期：**
- 关卡编辑器：2-3天
- 反向生成算法：3-5天
- 可解性验证：2-3天
- **总计：7-11天**

---

### 2.7 行动力系统

**实现：**
```javascript
class ActionPointSystem {
  constructor() {
    this.baseMaxSteps = 30;
    this.currentMaxSteps = 30;
    this.currentSteps = 0;
    this.temporaryBonus = 0; // 临时加成（时钟宝石）
  }
  
  useStep() {
    if (this.currentSteps >= this.currentMaxSteps + this.temporaryBonus) {
      return false; // 步数用完
    }
    this.currentSteps++;
    return true;
  }
  
  onLoopComplete() {
    // 引爆后重置步数
    this.currentSteps = 0;
    this.temporaryBonus = 0; // 临时加成清零
  }
  
  addPermanentBonus(amount) {
    // 闪电宝石：永久增加基础步数
    this.baseMaxSteps += amount;
    this.currentMaxSteps += amount;
  }
  
  addTemporaryBonus(amount) {
    // 时钟宝石：临时增加本次步数
    this.temporaryBonus += amount;
  }
}
```

**技术要点：**
- 基础步数：30，引爆后重置
- 永久加成：闪电宝石，修改 `baseMaxSteps`
- 临时加成：时钟宝石，修改 `temporaryBonus`，引爆后清零

**开发周期：** 1天

---

## 三、技术栈选择

### 3.1 前端渲染

| 选项 | 优点 | 缺点 | 推荐 |
|------|------|------|------|
| Canvas 2D | 简单，性能好 | 特效受限 | ✅ **推荐** |
| WebGL | 特效强大 | 复杂，学习成本高 | ❌ 过度设计 |
| DOM | 简单 | 性能差 | ❌ 不适合游戏 |

**推荐：Canvas 2D**
- 网格渲染：简单，性能好
- 粒子效果：Canvas 2D 足够
- 发光效果：用 `shadowBlur` 实现

### 3.2 游戏框架

| 选项 | 优点 | 缺点 | 推荐 |
|------|------|------|------|
| Phaser | 成熟，文档全 | 体积大 | ✅ **推荐** |
| PixiJS | 轻量，性能好 | 需要自己写游戏逻辑 | ❌ 工作量大 |
| 原生 Canvas | 完全控制 | 需要自己实现一切 | ❌ 重复造轮子 |

**推荐：Phaser 3**
- 内置网格系统、动画、音效
- 社区活跃，问题好解决
- 学习成本低

### 3.3 后端（可选）

**MVP版本：无后端**
- 单机游戏，所有逻辑在客户端
- 数据本地存储（localStorage）

**后续版本：可选后端**
- 排行榜、玩家数据同步
- 技术栈：Node.js + MongoDB

---

## 四、开发周期估算

### 4.1 MVP版本（核心玩法验证）

| 模块 | 工作量 | 说明 |
|------|--------|------|
| 网格系统 | 1天 | 基础数据结构 |
| 路径与光轨 | 1-2天 | 移动+留轨+清空 |
| 闭环检测 | 1-2天 | 首尾相连判定 |
| 组合系统（基础版） | 2-3天 | 只做3同色组合 |
| 特殊宝石（1种） | 1天 | 先做强化宝石 |
| 关卡生成（手工） | 2-3天 | 前5关手工设计 |
| 基础UI | 1-2天 | 开始/暂停/结算 |
| **总计** | **9-14天** | **约2周** |

### 4.2 完整版本

| 模块 | 工作量 | 说明 |
|------|--------|------|
| MVP版本 | 2周 | 核心玩法验证 |
| 完整组合系统 | 1-2周 | 混色组合+4-5同色 |
| 完整特殊宝石 | 1-2周 | 5种特殊宝石 |
| 关卡生成系统 | 2-3周 | 反向生成+可解性验证 |
| 前20关手工打磨 | 1-2周 | 关卡编辑器+手工设计 |
| 美术资源 | 2-3周 | 与开发并行 |
| 音效音乐 | 1周 | 与开发并行 |
| 测试调优 | 1-2周 | 平衡性+性能优化 |
| **总计** | **11-17周** | **约2.5-4个月** |

---

## 五、技术风险

### 5.1 高风险

| 风险 | 影响 | 应对 |
|------|------|------|
| **关卡生成算法** | 可能无法保证"可解性" | 先手工设计前20关，后续再研究算法 |
| **组合平衡性** | 可能导致某些组合过强/过弱 | 组合表用JSON配置，方便调参 |

### 5.2 中风险

| 风险 | 影响 | 应对 |
|------|------|------|
| **特殊宝石效果复杂** | 可能导致Bug | 每种宝石独立测试 |
| **性能问题** | 低端机可能卡顿 | 控制粒子数量，优化渲染 |

### 5.3 低风险

| 风险 | 影响 | 应对 |
|------|------|------|
| **闭环检测边界case** | 可能漏判/误判 | 无虹化状态，边界case大幅减少 |
| **行动力系统** | 可能破坏平衡 | 数值可调，测试验证 |

---

## 六、开发优先级建议

### 阶段1：核心验证（2周）

**目标：** 验证"画圈+组合"是否好玩

**任务：**
1. 实现基础网格+移动+留轨
2. 实现闭环检测+引爆+清空
3. 实现3同色组合（只做1种组合）
4. 手工设计5个测试关卡
5. 找5个用户试玩，收集反馈

**决策点：**
- 如果用户反馈"好玩" → 进入阶段2
- 如果用户反馈"不好玩" → 调整核心玩法或放弃

### 阶段2：扩展组合（2周）

**目标：** 加入完整组合系统

**任务：**
1. 实现混色组合（红蓝绿→彩虹）
2. 实现4-5同色组合
3. 实现5种特殊宝石
4. 手工设计10个关卡（6-15关）

### 阶段3：关卡系统（3周）

**目标：** 实现关卡生成系统

**任务：**
1. 开发关卡编辑器
2. 实现反向生成算法
3. 实现可解性验证
4. 手工打磨前20关

### 阶段4： polish（2-3周）

**目标：** 打磨体验

**任务：**
1. 美术资源替换（临时素材→正式素材）
2. 音效音乐
3. 动画优化
4. 平衡性调优
5. 性能优化

---

## 七、给策划的建议

### 7.1 组合表设计

**建议先做最小版本：**

| 组合 | 产物 | 效果 |
|------|------|------|
| 3同色 | 强化宝石 | 范围消除（周围8格） |
| 红蓝绿 | 彩虹宝石 | 清屏 |

**理由：**
- 先验证"同色组合"是否好玩
- 混色组合可以后续加
- 避免一开始就复杂

### 7.2 关卡设计原则

**前10关：**
- 只引入1-2种组合
- 宝石分布要明显，玩家容易凑出组合
- 每关都有"可完成的组合"，不能出现死局

**第11-20关：**
- 引入混色组合
- 增加围墙密度
- 引入行动力宝石

### 7.3 行动力宝石的数值

**建议：**
- 基础步数：30
- 闪电宝石：+10步（永久）
- 时钟宝石：+20步（临时）

**理由：**
- 30步足够完成一次中等规模的画圈
- +10步是明显但不夸张的加成
- +20步是临时爆发，不会永久破坏平衡

---

## 八、给美术的建议

### 8.1 美术资源清单

**宝石类（优先级高）：**
- 5种普通宝石（红/蓝/绿/黄/紫）
- 5种强化宝石（带光效）
- 5种超级宝石（更大更亮）
- 5种终极宝石（双光环+光翼）
- 1种彩虹宝石（全光谱旋转）
- **总计：21种静态宝石**

**动画类（优先级高）：**
- 合并动画（螺旋汇聚→光芒爆发→新宝石落地）
- 引爆动画（光束填满+粒子四散）
- 特殊宝石触发动画（范围消除/十字线/全屏）

**场景类（优先级中）：**
- 深色棱镜底板
- 围墙（灰色石块）
- 光轨（半透明果冻状）

### 8.2 美术风格建议

**深色底板是关键：**
- 确保所有宝石在深色背景上清晰可读
- 控制发光强度：普通宝石低调，组合宝石中等，彩虹宝石最炫

**合并动画是核心爽点：**
- 需要比引爆更炫
- 建议时长：0.7-1秒
- 节奏：快但不乱，让玩家看清过程

---

## 九、给市场的建议

### 9.1 买量素材方向

**核心卖点：**
- "画圈三消"——区别于传统三消的"拖动交换"
- 合并动画——3颗宝石飞到一起合并的瞬间

**素材建议：**
- 15秒短视频：展示"画圈→组合→特效"
- 重点展示彩虹宝石的合并瞬间
- 强调"一看就会，越玩越难"

### 9.2 用户预期

**目标用户：**
- 休闲解谜游戏玩家
- Candy Crush、Toon Blast 等三消游戏的用户

**预期指标：**
- D1留存：35-45%（休闲解谜品类优秀水平）
- D7留存：15-20%
- ARPU：$1-3（中等水平）

---

## 十、总结

### 技术可行性：✅ 可行

- 核心玩法技术上没有天堑
- 最大挑战是关卡生成算法，但可以分阶段解决
- 开发周期可控，2周可出MVP验证

### 关键决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 光轨管理 | 引爆后清空 | 最简单，无边界case |
| 组合表 | JSON配置 | 热更新友好，方便调参 |
| 新宝石位置 | 棋盘随机空位 | 视觉表现好 |
| 连锁反应 | MVP不做 | 先验证核心玩法 |
| 关卡生成 | 前20关手工 | 确保可解性 |

### 下一步

1. **策划确认组合表**（今天）
2. **美术出概念图**（1周）
3. **开发做MVP原型**（2周）
4. **用户测试验证**（第3周）

---

**文档结束**

> 本文档为阶段性技术分析，后续会根据原型验证结果迭代更新。
