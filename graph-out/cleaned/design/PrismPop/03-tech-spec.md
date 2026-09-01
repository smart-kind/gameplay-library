---
title: 技术规格文档
original_filename: 03-tech-spec
source: gameplay-library
---

# 技术规格文档

> 作者：开发  
> 状态：✅ 已完成  
> 最后更新：2026-08-15

---

## 技术栈

| 层级 | 技术选型 | 说明 |
|------|---------|------|
| 前端渲染 | Canvas/WebGL | 纯客户端，无后端 |
| 游戏逻辑 | JavaScript/TypeScript | 纯客户端 |
| 数据存储 | localStorage | 本地保存进度 |
| 关卡数据 | JSON 配置 | 支持热更新 |

**理由**：纯单机，无联网，无后端，无运维。1个前端开发 + 1个美术即可启动。

---

## 核心系统

### 1. 网格系统

```typescript
interface Grid {
  width: number;      // 6-12
  height: number;     // 6-12
  cells: Cell[][];    // 二维数组
}

interface Cell {
  x: number;
  y: number;
  gem: Gem | null;    // 宝石或空
  trail: boolean;     // 是否有光轨
}
```

**实现**：标准二维数组，O(1) 访问。

### 2. 路径追踪系统

```typescript
class PathManager {
  private path: Point[] = [];       // 当前路径点
  private maxTrailLength: number;   // 最大光轨格数（行动力）
  
  addPoint(x: number, y: number): boolean {
    // 检查是否碰撞已有光轨
    if (this.isTrailAt(x, y)) return false;
    this.path.push({ x, y });
    return true;
  }
  
  isClosed(): boolean {
    // 首尾相连 = 闭合
    const first = this.path;
    const last = this.path[this.path.length - 1];
    return Math.abs(first.x - last.x) <= 1 && Math.abs(first.y - last.y) <= 1;
  }
}
```

**关键点**：
- 路径不能交叉（碰到已有光轨自动停止）
- 8字形路径不需要处理（因为路径不能交叉）
- 引爆后清空所有路径

### 3. 闭环检测与宝石收集

```typescript
function collectGemsInsideLoop(trail: Point[], grid: Grid): Gem[] {
  // 方法：从圈内任意点出发，Flood Fill 判断哪些格子在圈内
  // 或使用射线法：对每个宝石判断是否在闭合路径内
  
  const collected: Gem[] = [];
  for (const gem of grid.allGems) {
    if (isInsideLoop(gem.x, gem.y, trail)) {
      collected.push(gem);
    }
  }
  return collected;
}
```

**复杂度**：O(n×m)，n=宝石数，m=路径长度。网格最大12×12=144格，性能无忧。

### 4. 组合检测系统

```typescript
interface GemGroup {
  colors: Record<string, number>;  // { red: 3, blue: 1 }
  result: CombinationResult;
}

const COMBINATION_TABLE: Record<string, CombinationResult> = {
  'red:3': { type: 'enhanced', color: 'red', power: 1 },
  'blue:3': { type: 'enhanced', color: 'blue', power: 1 },
  // ... 其他组合
  'red:1,green:1,blue:1': { type: 'rainbow', power: 3 },
};

function detectCombination(gems: Gem[]): CombinationResult | null {
  const colorCount = countColors(gems);
  const key = Object.entries(colorCount)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([c, n]) => `${c}:${n}`)
    .join(',');
  
  return COMBINATION_TABLE[key] || null;
}
```

**关键点**：
- 组合表必须是JSON配置，不能硬编码
- 支持热更新，方便调平衡

### 5. 行动力系统

```typescript
class ActionManager {
  private remaining: number;       // 剩余行动力（格子数）
  private maxAction: number;       // 最大行动力（基础值）
  
  constructor(baseAction: number = 30) {
    this.maxAction = baseAction;
    this.remaining = baseAction;
  }
  
  use(amount: number = 1): boolean {
    if (this.remaining <= 0) return false;
    this.remaining--;
    return true;
  }
  
  add(amount: number) {
    this.remaining += amount;
  }
  
  reset() {
    this.remaining = this.maxAction;
  }
}
```

**特殊宝石效果**：
- 闪电宝石：+20行动力
- 时钟宝石：+10行动力

---

## 关卡生成系统

### 生成流程

```
1. 确定关卡参数（尺寸、宝石种类、目标）
2. 生成宝石分布（约束求解器）
3. 生成围墙布局
4. 验证可解性（是否存在可达的组合路径）
5. 输出关卡数据
```

### 约束求解

**问题**：确保每关都有"可完成的组合"，不出现死局。

**方案A：伪随机分布**
- 每关生成时，保证至少有2-3组"可凑成的组合"
- 比如：这关有6个红宝石、6个蓝宝石，分散在不同位置

**方案B：反向生成（推荐）**
- 先设计"这关要让玩家凑出什么组合"
- 再反推"棋盘上需要放哪些宝石、放在哪"
- 最后加围墙和干扰

**技术实现**：
```typescript
function generateLevel(targetCombination: Combination): Level {
  // 1. 放置目标组合所需的宝石
  placeGemsForCombination(targetCombination);
  
  // 2. 填充剩余宝石（随机）
  fillRemainingGems();
  
  // 3. 放置围墙（确保组合可达）
  placeWalls();
  
  // 4. 验证可解性
  if (!isSolvable()) return generateLevel(targetCombination);
  
  return level;
}
```

---

## 数据结构

### 关卡数据（JSON）

```json
{
  "levelId": 1,
  "gridSize": [6, 6],
  "targetScore": 500,
  "baseAction": 30,
  "gems": [
    { "x": 2, "y": 3, "color": "red", "type": "normal" },
    { "x": 3, "y": 3, "color": "red", "type": "normal" },
    { "x": 4, "y": 3, "color": "red", "type": "normal" }
  ],
  "walls": [
    { "x": 1, "y": 2 },
    { "x": 5, "y": 2 }
  ]
}
```

### 宝石数据

```typescript
interface Gem {
  id: string;
  x: number;
  y: number;
  color: 'gold' | 'red' | 'blue' | 'green' | 'purple';
  type: 'normal' | 'frozen' | 'lightning' | 'clock';
  power?: number;       // 组合等级（1-3）
  effect?: GemEffect;   // 特殊效果
}

type GemEffect = 
  | 'expand_blast'    // 下次引爆范围更大
  | 'freeze_area'     // 冻结周围区域
  | 'restore_action'  // 恢复行动力
  | 'clear_screen';   // 清屏（彩虹宝石）
```

---

## 性能要求

| 指标 | 目标 | 说明 |
|------|------|------|
| 帧率 | 60fps | 主流设备 |
| 低端机 | 30fps | 最低要求 |
| 内存 | < 200MB | 包含所有资源 |
| 启动时间 | < 3s | 冷启动 |

**性能优化点**：
- 网格渲染：只渲染可见区域
- 粒子效果：控制数量，低端机降级
- 关卡数据：JSON 预加载，不实时计算

---

## 开发周期

| 阶段 | 内容 | 周期 |
|------|------|------|
| 原型验证 | 核心闭环+组合检测 | 1周 |
| 基础系统 | 网格+路径+引爆+清空 | 1周 |
| 组合系统 | 组合表+特殊宝石+合并动画 | 1周 |
| 关卡生成 | 约束求解器+关卡编辑器 | 1周 |
| 前20关打磨 | 手工设计+测试 | 2周 |
| 美术资源 | 宝石+光效+动画 | 2周 |
| **总计** | | **8周** |

---

## 技术风险

| 风险 | 影响 | 应对 |
|------|------|------|
| 关卡生成可解性验证 | 高 | 反向生成 + 验证算法 |
| 组合平衡性调优 | 中 | JSON配置，热更新 |
| 低端机性能 | 中 | 粒子效果降级 |

---

## 下一步

- [ ] 完成核心闭环原型（1周）
- [ ] 实现组合表配置系统
- [ ] 开发关卡编辑器（网页工具）
- [ ] 手工打磨前10关