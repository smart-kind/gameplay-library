---
title: Roll In The Hole
original_filename: RollInTheHole_20260816_1242
date: 2026-08-16
time: 12:42
source: gameplay-library
---

# Roll in the Hole

- **类型**: Puzzle
- **平台**: Mobile (iOS)
- **开发商**: PocketGamer reviewed title
- **首次发布**: N/A (delisted)
- **一句话描述**: Physics puzzle game where players guide rolling balls into matching colored holes.

## 玩法规则

Players control one or more rolling objects on a game board. The objective is to guide each colored ball into its corresponding matching hole. The game board features obstacles, other balls, and holes that can block your path. Players drag and roll unique ball blocks across the board, matching each colored block with its matching hole. Other balls and holes act as blocking obstacles, requiring strategic thinking about movement order.

Players use touch drag controls to direct ball movement, navigating around obstacles while planning the optimal movement sequence. The board layout varies per level, with increasing numbers of colors, balls, and spatial complexity.

The game screen displays the current puzzle board as the main view area. Colored balls are scattered across the board, each with a corresponding colored hole somewhere on the same board. Players tap and drag individual balls to roll them toward their target holes. The drag direction and distance determine the initial velocity and direction of the ball roll.

When a ball reaches its matching hole, it falls in and is removed from the board. Players must clear all balls from the board to complete each level. The challenge increases as more colors, more balls, and more complex obstacle arrangements are introduced. Some levels feature moving obstacles, sloped surfaces that affect ball trajectory, and teleporters that move balls across the board.

游戏的整体节奏以关卡为单位推进，每完成一个关卡即可获得星级评价。星级评价基于完成效率、剩余资源和时间等因素。玩家可以通过多次尝试来优化每关的表现，追求完美的三星通关。游戏没有内购付费机制，所有内容通过关卡进度逐步解锁。

## 核心循环

Observe board layout - Drag ball to matching hole - Avoid obstacles - Clear board - Progress to next puzzle

## 核心机制

- Color Matching: Each ball must be matched to its corresponding colored hole, requiring players to identify correct pairings before committing to a move.
- Physics-Based Movement: Balls roll with simulated physics, meaning momentum and trajectory affect movement. Drag direction, distance, and speed all influence the ball path.
- Spatial Blocking: Other balls and holes act as obstacles that can block paths, requiring players to think about movement sequence and order of operations.
- Puzzle Progression: Each level presents a new board layout with increasing complexity in colors, obstacles, and spatial arrangement. Later levels introduce moving obstacles, slopes, and teleporters.

## 为什么好玩

The satisfaction of perfectly guiding each ball into its matching hole combined with the tension of navigating around blocking obstacles creates a compelling puzzle experience that is easy to learn but increasingly challenging. The physics-based rolling adds a layer of physical intuition that makes each successful match feel earned.

## 粘性来源

The immediate feedback loop of each successful match and the escalating challenge of more complex board layouts drives repeated play. The physics-based rolling adds unpredictability that keeps players engaged, as no two attempts produce exactly the same result.

## Meta 系统

Level progression with unlockable stages. New board configurations with more colors, obstacles, and complex spatial challenges introduced as players advance. Star ratings per level based on efficiency.

## 实现难度

Low - Physics engine stability and collision detection precision to ensure natural ball rolling behavior without clipping or tunneling through obstacles.

## 来源

- 抓取 URL: https://www.pocketgamer.com/roll-in-the-hole/
- PocketGamer Review by Damien McFerran