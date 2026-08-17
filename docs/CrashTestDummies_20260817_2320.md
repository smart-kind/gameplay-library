# 碰撞测试假人（Crash Test Dummies）

- **类型**: 物理/休闲
- **平台**: Mobile (Java)
- **开发商**: 未知
- **首次发布**: 2010
- **一句话描述**: With all the car recalls we're currently suffering, you'd think your average crash test dummy would be knee deep in work right now. Apparently not, and if Crash Test Dummies is to 

## 玩法规则

Apparently not, and if Crash Test Dummies is to be believed their time off is spent experimenting with their own mortality. This is essentially a theme park for all things crash, bang, and wallop.

The trick is to put the poor old dummy through as much pain and carnage as you can, your spineless friend - quite endearingly - coming with his own submissive personality. In terms of plot, each level is an testbed to see what the dummy can put up with.

In reality, Crash Test Dummies is like Burnout's crash junctions meets Crazy Penguin Catapult, mixed with a whole lot of Ragdoll Blaster for good measure.

The end result is a whole heap of fun. The game gives you a variety of ways to launch your dummy (a personal favourite being a diving board style run-and-jump, which sees you triggering springs on the floor with the '5' key), with you initially taking charge of a swinging ball positioned behind him, where you place it determining the force, speed, and direction of the impact.

Once in the air, it's a question of hoping your dummy hits as many objects as possible. Extra points are awarded for mid-flight tricks and picking up stars. As the levels progress, the game also gives you some influence beyond the initial launch: hitting the '5' key triggers further springs or punching fists that prod your dummy back into the action.

## 核心循环

发射假人撞击物体 → 获得分数和空中技巧加分 → 解锁新关卡和发射方式

## 核心机制

- 物理弹射：通过摆锤弹簧等方式将假人发射出去
- 空中碰撞计分：撞击越多物体得分越高，空中技巧有额外加分
- 关卡内编辑：可以在发射前调整场景物体位置
- 多目标模式：既有破坏模式也有距离目标模式

## 为什么好玩

将Burnout的碰撞 Junction和物理弹射结合，每次发射都充满不确定性。幸运弹射和精心设计的碰撞都能带来满足感，轻松有趣且容易上瘾。

## 粘性来源

爽感反馈是核心粘性。每次发射后看到假人疯狂碰撞的物理效果带来即时满足，加上随机碰撞带来的惊喜感和评分系统的挑战欲，让人想不断刷新自己的最高分。

## Meta 系统

分数排行榜和关卡解锁系统，通过积累分数解锁新的发射方式和场景。

## 实现难度

中 — 物理引擎和碰撞检测是核心难点。需要模拟真实的物理碰撞效果，同时保证假人的ragdoll动画自然流畅，不同发射方式的力度和角度计算也需要精确的物理模型。

## 来源

- 抓取 URL: https://www.pocketgamer.com/crash-test-dummies/review/
- 评测来源: Pocket Gamer