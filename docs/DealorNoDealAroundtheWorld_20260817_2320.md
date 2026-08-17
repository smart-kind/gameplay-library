# 交易或不交易：环游世界（Deal or No Deal Around the World）

- **类型**: 卡牌/竞猜
- **平台**: Mobile (Android)
- **开发商**: 未知
- **首次发布**: 2010
- **一句话描述**: Deal or No Deal really shouldn’t work as a gameshow. For one thing there’s absolutely no skill involved, other than the ability to say numbers out loud while standing up and breath

## 玩法规则

For one thing there’s absolutely no skill involved, other than the ability to say numbers out loud while standing up and breathing, I guess.

There’s also no way that the contestant cannot win, with every person who competes guaranteed to walk away with at least a pound to their name.

It does work, though, because of the way it’s presented. The tense psychological battles with The Banker and the contestant’s constant fear of ‘only’ winning five pounds because they picked their mother’s birthday instead of their dog’s, help give the show a tangible sense of tension.

But to make it work on your Android handset it’s going to need a lot to disguise the fact that you’re just picking random numbers. With no real money involved there’s nothing at stake. And with no superstitious competitors around, who’s there to laugh at/cheer on?

Yet if that's the case, why am I mumbling to myself and insulting The Banker out loud in public?

## 核心循环

选择箱子排除金额 → 与Banker进行心理博弈 → 决定接受offer或继续冒险

## 核心机制

- 开箱排除：逐轮打开箱子排除金额，缩小可能范围
- Banker报价心理战：每轮后Banker给出收购报价，需要判断是否接受
- 全球化主题：融入不同国家元素增加新鲜感
- 无失败机制：保证至少获得最低金额，降低挫败感

## 为什么好玩

虽然本质上是随机选择，但紧张的心理博弈和Banker的报价机制让人欲罢不能。即使在公共场合玩也会不自觉地跟Banker较劲，沉浸感极强。

## 粘性来源

心理博弈和随机性让人欲罢不能。每次开箱都是一次小小的赌博，Banker的报价让人既想接受又怕错过大奖，这种不确定性是最强的粘性来源。

## Meta 系统

全球化主题带来的内容轮换，不同国家版本的箱子金额和场景有所不同。

## 实现难度

低 — 核心是UI交互和数值逻辑，技术难度不高。难点在于Banker报价算法的设计，需要让报价既合理又充满戏剧性。

## 来源

- 抓取 URL: https://www.pocketgamer.com/deal-or-no-deal-around-the-world/review/
- 评测来源: Pocket Gamer