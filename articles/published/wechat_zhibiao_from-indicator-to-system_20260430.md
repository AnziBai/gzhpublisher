---
title: 从单一指标到系统：搭建自己的交易框架
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 7.1 程序化交易四大优势.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

很多交易者走过的路是这样的：

刚开始学MACD，觉得金叉死叉很神奇，用了一段时间，发现假信号太多，亏钱。然后换RSI，再换KDJ，再换布林带，再换均线……一路换下去，每个指标都单独用一段时间，每个都有效一会儿，然后都开始失效。

**问题不在指标，在于你用的是单一指标，而不是系统。**

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 7.1 程序化交易四大优势.jpg" alt="图 7.1 程序化交易四大优势" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 单一指标为什么不够

任何单一指标，本质上都只是在回答市场的一个问题。

MACD回答的是："动量是否改变了方向？"
均线回答的是："中长期趋势方向是什么？"
成交量回答的是："价格变动背后有没有资金支撑？"
RSI回答的是："市场是否进入超买/超卖状态？"

这些问题都很重要，但没有一个能独立回答"现在应不应该买"这个完整的交易决策问题。

**一个完整的交易决策需要回答四个问题**：

1. 背景：现在的市场趋势方向是什么？（大背景）
2. 信号：在这个趋势下，有没有具体的买卖信号？（触发条件）
3. 仓位：如果要操作，该用多少仓位？（风险控制）
4. 出口：如果方向判断错了，在哪里止损？（退出机制）

单一指标最多能回答其中一个问题。系统才能回答全部四个。

---

## 宽论系统的四层结构

宽论体系是一个完整的回答这四个问题的系统，每一层对应一个问题：

**第一层：弹论（趋势背景）**

五根均线构成的"弹簧"系统，判断市场当前处于弹上（多头趋势）、弹下（空头趋势）还是弹中（震荡）。这一层回答第一个问题：背景。

只有弹上才考虑做多信号，弹下不考虑做多。这一层过滤掉了80%的低胜率操作。

**第二层：CDVA分型（买卖信号）**

在弹论确认背景之后，CDVA分型给出具体的入场信号。C分型（价格从弹中/弹下回到弹上）是做多信号，D分型（价格从弹上跌到弹中/弹下）是止损/做空信号。这一层回答第二个问题：信号。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.7 C 分型.jpg" alt="图 10.7 C 分型" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

**第三层：六字诀（仓位和纪律）**

轻仓、止损、顺势，这是回答第三个问题（仓位）和第四个问题（出口）的行为规则。轻仓确保每笔交易的资金风险可控，止损确保每笔交易的最大亏损有限。

**第四层：QR值（品种筛选）**

QR值（量化相对强弱）帮助你在全市场里筛选出当前阶段相对强势的品种，作为操作的优先对象。同样的系统，用在强势品种上效果更好。

<div style="margin: 30px 0; padding: 20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 从弹论到CDVA到六字诀到QR值的完整系统逻辑，我在<strong style="color: #eb1313;">《概率的朋友》</strong>中做了系统讲解。这本书是<strong style="color: #ff6b35;">我桥博士30年交易经验的总结</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论完整交易框架都融入在这本书里</span>。
  </p>
  <p style="font-size: 15px; color: #555; line-height: 1.8;">
    不是东拼西凑的指标组合，而是四层相互支撑的完整系统。每一层都有其存在的逻辑，缺一不可。
  </p>
  <div style="clear: both;"></div>
</div>

---

## 搭建系统的原则

如果你想从零开始搭建自己的交易系统，宽论的建议是：

**原则一：从趋势背景开始。**

任何系统的第一层，都应该是判断市场趋势方向的工具。没有趋势过滤，信号系统就是在噪音里找信号，胜率天然偏低。

**原则二：信号不能太多。**

一个系统里的信号层，指标不超过3个。太多指标会产生矛盾信号，让你无从下手；也会产生"分析瘫痪"——总有某一个指标说不该进，你就一直等，错过所有机会。

**原则三：止损在进场时就确定。**

每一个系统都必须内置明确的止损规则。止损不是"亏损太多了就跑"，而是"当哪个信号失效了就跑"。用信号失效来定义止损，比用亏损幅度定义止损更有交易逻辑。

**原则四：先用小仓位验证，再扩大规模。**

任何新系统，先在小仓位上跑100-200笔交易，看看实际胜率、盈亏比是不是和你预期的一致。验证通过后，再扩大仓位。这是职业交易者的标准流程。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.16 选择最优模型.jpg" alt="图 10.16 选择最优模型" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 系统的核心价值：可重复性

为什么要有系统，而不是靠经验和直觉？

因为经验和直觉无法在压力下稳定执行。你在平静状态下做出的判断，和你在账户亏损15%时做出的判断，可能完全不同。

系统的核心价值，是**在你情绪最差的时候，告诉你应该怎么做**。不是靠你去想，而是靠规则去执行。这就是"可量化、可验证、可重复"——宽论最核心的三个字。

我用宽论系统在6个月里完成8000多笔交易，盈利250万，盈亏比2.76。这不是靠某几笔神操作，而是8000笔里每一笔都遵守系统规则的累积结果。这就是系统的力量。

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
