---
title: 夏普比率与卡玛比率：如何评估一个策略的好坏
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 1.4  三大风险比率的特色.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

很多人评估一个交易策略好不好，只看一个数字：年化收益率。

这是不够的。

两个策略，A全年收益30%，B全年收益30%。看起来一样好。但A的最大回撤是8%，B的最大回撤是50%。对于大多数人来说，A远比B好——因为B在某段时间会让你的账户缩水一半，大多数人在这个时候就放弃了，无法拿到那30%的全年收益。

评估策略，需要同时看**收益**和**风险**。这就是风险调整后收益指标的意义。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 1.4  三大风险比率的特色.jpg" alt="图 1.4 三大风险比率的特色" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 夏普比率：最常用的风险调整指标

**公式：夏普比率 = (年化收益率 - 无风险利率) / 收益率的年化标准差**

简单理解：每承受一单位波动，获得多少超额收益。

- 夏普比率 > 1：策略有价值，每单位风险能获得合理回报
- 夏普比率 > 2：优秀，很多机构投资者的策略目标
- 夏普比率 < 0：策略连无风险存款都跑不赢

**夏普比率的局限**

夏普比率用"标准差"来衡量风险，但标准差把上涨波动和下跌波动一视同仁。问题是，上涨的波动是好事，你不需要减少它；你真正想要减少的是下跌波动（回撤）。

这就是另一个指标出现的原因。

---

## 索提诺比率：只惩罚下行波动

**公式：索提诺比率 = (年化收益率 - 无风险利率) / 下行标准差**

下行标准差只计算负收益的波动，上涨波动不计入。因此，索提诺比率比夏普比率更能反映投资者真正关心的风险——亏损的波动性，而不是整体波动。

同样的策略，如果上涨时波动大、下跌时波动小，索提诺比率会高于夏普比率；反之则低。趋势跟踪策略通常有不错的索提诺比率，因为它止损快（减少下行波动），持盈慢（允许上行波动）。

---

## 卡玛比率：用最大回撤衡量风险

**公式：卡玛比率 = 年化收益率 / 最大回撤**

最大回撤是策略历史上从高点到低点的最大跌幅，反映的是最坏情况。

- 卡玛比率 = 1：赚了多少，最大时也亏了多少，对折扣线
- 卡玛比率 > 2：收益是最大回撤的两倍以上，风险回报较优

卡玛比率特别适合评估趋势跟踪策略：这类策略的回撤往往较大（横盘期连续止损），但年化收益也较高。关键是两者的比例是否合理。

**宽论的数据**：6个月8000笔、盈利250万的数据背后，对应的最大回撤和卡玛比率，是策略稳定性的重要指标。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.15 如何降低投资风险.jpg" alt="图 10.15 如何降低投资风险" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 三个比率的使用场景

| 指标 | 适用场景 | 局限 |
|------|----------|------|
| 夏普比率 | 评估整体波动是否合理，跨策略对比 | 把上涨波动也算风险 |
| 索提诺比率 | 评估下行风险控制是否好 | 样本量小时不稳定 |
| 卡玛比率 | 评估最坏情况下的风险回报 | 历史最大回撤不等于未来最大回撤 |

实践中，三个指标结合使用：
- 夏普比率看整体效率
- 索提诺比率看下行控制
- 卡玛比率看回撤承受力

三个都好的策略，才是真正稳健的策略。

<div style="margin: 30px 0; padding: 20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 三大风险比率的完整计算方法、宽论策略的历史数据解读、以及如何用这些指标评估和改进自己的交易系统，我在<strong style="color: #eb1313;">《概率的朋友》</strong>中做了系统讲解。这本书是<strong style="color: #ff6b35;">我桥博士30年交易经验的总结</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论完整知识体系都融入在这本书里</span>。
  </p>
  <div style="clear: both;"></div>
</div>

---

## 实际意义：为什么这些指标重要

很多交易者看到"年化收益100%"就兴奋，没想过这100%背后经历了多大的回撤。如果最大回撤是80%——卡玛比率只有1.25——意味着你在某段时间账户缩水了八成，心理上几乎没有人能承受，通常会在低点清仓认亏。

真正可持续的策略，不是追求最高收益，而是**在可接受的回撤范围内，获得稳定的正期望值**。

这也是宽论"先验证，后规模"原则的数字版本——在扩大仓位之前，先看清楚这套系统的夏普比率、索提诺比率和卡玛比率是否达到你的标准。

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
