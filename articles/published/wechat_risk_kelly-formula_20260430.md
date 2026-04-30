---
title: 资金管理进阶：凯利公式的实战改造
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.3 如何提高整体收益.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

如果你研究过资金管理，大概率听说过凯利公式。

凯利公式告诉你，在一个正期望值的赌局或交易中，每次应该投入多大比例的资金，才能在长期内最大化资产增长率。

公式是：**f = (bp - q) / b**

其中 f 是投入比例，b 是盈亏比，p 是胜率，q = 1 - p 是败率。

理论上，按凯利公式下注，长期资产增长速度是最快的。但直接用凯利公式做交易，实盘里通常会出大问题。原因在于：**凯利公式假设你能精确知道胜率和盈亏比，但实盘里这两个数字都是估算值，有误差。**

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.3 如何提高整体收益.jpg" alt="图 10.3 如何提高整体收益" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 凯利公式为什么在实盘里危险

凯利公式有一个隐含假设：你的胜率和盈亏比是稳定的已知值。

但实盘里，你对胜率和盈亏比的估计都来自有限的历史数据，有统计误差。如果你低估了败率或高估了盈亏比，凯利公式会给出一个过大的仓位建议。

更危险的是，凯利公式在边界条件下非常敏感：估计误差哪怕只有10%，推荐的仓位可能相差一倍以上。仓位过大，遇到连续止损，账户回撤可能让你在心理上无法继续执行系统。

这就是为什么量化交易界有一个共识：**全凯利仓位是理论最优，但实战中通常用半凯利（Half-Kelly）甚至更低。**

---

## 宽论的实战资金管理框架

宽论不直接套用凯利公式，而是用一套更保守、更适合实盘心理的框架：

**核心原则：单笔风险不超过总资金的1-2%**

无论信号多好，单笔交易的最大亏损（从进场到止损位的距离×仓位）不超过总资金的1-2%。

以50万账户为例：
- 单笔最大风险：1% × 50万 = 5000元
- 如果止损位距进场价2%，则仓位 = 5000 ÷ (50万 × 2%) = 50%
- 如果止损位距进场价5%，则仓位 = 5000 ÷ (50万 × 5%) = 20%

止损越宽，仓位越轻。这是宽论"轻仓"原则的量化实现——不是固定轻仓，而是根据风险动态调整仓位。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 1.4  三大风险比率的特色.jpg" alt="图 1.4 三大风险比率的特色" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 为什么1-2%是合理的上限

从数学上看：单笔最大风险1%，即使连续亏损20笔（这在正期望值系统里极为罕见），账户总资金还剩82%。回撤18%，心理上是可以承受的，执行系统的意志不会崩溃。

从心理上看：当单笔亏损在可接受范围内，你不会在止损时做出"再等等看"的情绪化决策，执行率会更高。

从系统韧性来看：小仓位意味着你有足够的子弹继续执行系统，验证期望值的样本量能够积累到足够大。

宽论6个月8000笔交易、盈利250万的数据背后，资金管理纪律是核心支撑——不是靠每笔都重仓，而是靠每笔都严格控制风险、让正期望值在足够多的笔数上充分实现。

<div style="margin: 30px 0; padding: 20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 凯利公式的完整推导、半凯利与固定比例的对比、以及宽论动态仓位控制的实战应用，我在<strong style="color: #eb1313;">《概率的朋友》</strong>中做了系统讲解。这本书是<strong style="color: #ff6b35;">我桥博士的著作</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论完整交易框架都融入在这本书里</span>。
  </p>
  <div style="clear: both;"></div>
</div>

---

## 三条资金管理红线

不管系统多好，有三条红线不能踩：

**红线一：单笔风险超过5%。** 超过这个比例，连续止损会造成无法恢复的心理创伤，执行系统的意志会崩溃。

**红线二：没有止损就进场。** 没有止损的仓位是没有定义风险的仓位，所有的资金管理计算都建立在已知止损位的基础上。

**红线三：在连续亏损后加仓。** 这是"翻本心理"的表现——连续亏损后市场状态可能发生了变化，此时加仓只是在放大暴露于不确定市场的风险。

资金管理的核心逻辑不是"怎么赚更多"，而是"怎么确保系统有机会跑够足够多的笔数，让正期望值充分实现"。

（数据来源：宽论官方公开资料）

---

<div style="text-align: center; margin: 30px 0 20px 0;">
  <img src="C:/Users/anzib/gzhpublisher/assets/微信二维码-桥楚.jpg" 
       style="border-radius: 8px; width: 200px; display: block; margin: 0 auto 12px auto;" 
       alt="桥博士微信" />
  <p style="font-size: 13px; color: #888; line-height: 1.8;">交流探讨 · 桥博士</p>
</div>

<div style="text-align: center; margin: 20px 0; padding: 15px; color: #666;">
  <p style="font-size: 14px; line-height: 1.8;">如果本文对您有帮助，欢迎点个在看，让更多人看到这些内容。</p>
</div>

*免责声明：本文为量化分析技术方法论分享，不构成投资建议。投资有风险，入市需谨慎。*
