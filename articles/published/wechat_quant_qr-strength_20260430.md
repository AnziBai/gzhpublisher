---
title: QR值（量化相对强弱）：如何筛选强势品种
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.17 两个核心环节.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

趋势跟踪的前提是找到有趋势的品种。

问题是，A股有5000多只股票，期货有几十个品种，你不可能每天逐一分析。你需要一套快速筛选工具，帮你从大量品种中找到正在运行趋势的那一批。

QR值（量化相对强弱），就是宽论用于品种筛选的核心工具之一。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.17 两个核心环节.jpg" alt="图 10.17 两个核心环节" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 什么是相对强弱

相对强弱的核心逻辑：**在同等市场环境下，强势品种比大盘跌得少、涨得多；弱势品种比大盘涨得少、跌得多。**

当整个市场在震荡或下跌时，依然保持强势的品种，通常有资金在主动介入——这是趋势形成的早期信号。

传统的相对强弱指标（RSI）是单品种的技术指标，衡量品种自身价格的动量。QR值不同，它衡量的是**品种与基准指数之间的相对表现**——超额收益的强弱。

---

## QR值的计算逻辑

QR值的基本计算框架：

**QR = 品种在N日内的涨幅 ÷ 基准指数在N日内的涨幅**

- QR > 1：品种跑赢指数，相对强势
- QR < 1：品种跑输指数，相对弱势
- QR > 1 且绝对涨幅为正：主动上涨，强势信号最清晰

在实际应用中，通常用多个时间周期的QR值加权（如5日、20日、60日），来过滤短期噪音，识别具有持续性的强势。

---

## QR值如何融入宽论的筛选流程

宽论的品种筛选是一个漏斗：

**第一层：弹论过滤**

只看弹上（均线多头排列）的品种，排除弹中和弹下。这一步大幅减少候选品种数量。

**第二层：QR值排序**

在弹上品种中，按QR值排序，优先选择相对强弱最高的前N个品种进入候选池。

**第三层：CDVA信号确认**

在候选品种上等待CDVA信号（C分型或V分型），信号出现时入场。

这个漏斗的逻辑：弹论保证大背景正确，QR值保证选的是强中之强，CDVA保证入场时机精准。三层过滤之后，信号的质量会显著高于随机选股。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.19 交易六字诀的演化.jpg" alt="图 10.19 交易六字诀的演化" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 强势品种的直觉判断

如果你没有量化工具，也可以用直觉判断法接近QR值的效果：

**看相对表现**：大盘跌3%时，候选品种跌了多少？跌不到1%甚至横盘，是强势；跌了5%，是弱势。

**看成交量结构**：上涨时量能放大，下跌时量能萎缩，是强势结构；反过来是弱势结构。

**看均线结构**：均线多头排列、回调不破支撑均线，是强势结构。

**看高低点结构**：每次回调的低点比前一次高，是强势结构（趋势的定义）。

这四个维度，是量化相对强弱指标背后的底层逻辑——把直觉变成数字，让筛选可以规模化、可以回测验证。

<div style="margin: 30px 0; padding: 20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 QR值的完整计算公式、多周期相对强弱的权重设计、以及宽论品种筛选漏斗的实战应用，我在<strong style="color: #eb1313;">《概率的朋友》</strong>中做了系统讲解。这本书是<strong style="color: #ff6b35;">我桥博士30年交易经验的总结</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论完整知识体系都融入在这本书里</span>。
  </p>
  <div style="clear: both;"></div>
</div>

---

## 为什么要选强势品种

很多人的直觉是：强势品种已经涨了那么多，该轮到弱势品种补涨了。

这个逻辑在均值回归的框架里是有道理的。但在趋势跟踪的框架里，结论完全相反：

**强者恒强，弱者恒弱。** 有资金持续介入的品种，趋势会延续；被资金持续抛售的品种，弱势也会延续。补涨行情偶尔存在，但在统计上它的可靠性远不如趋势延续。

宽论的实战数据也印证了这一点：优先选择弹上+QR值高的品种，和随机选股相比，胜率和盈亏比都有显著提升。

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
