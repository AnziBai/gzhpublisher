---
title: 期望值思维：单笔结果不重要，100笔的数学期望才重要
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 1.5 胜率盈亏.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

大多数交易者是这样思考的：

这笔交易能赚钱吗？→ 感觉能赚 → 进场。

这是单笔思维。它的问题是：无论你对这笔交易判断多准，单笔结果里仍然有大量随机成分。就算一个胜率70%的系统，也会出现连续5笔止损——这是正常的统计波动，不是系统失效。

用单笔结果评价系统，就像用一次骰子的结果来判断骰子是否公平——样本太小，结论不可靠。

**正确的思维方式：这个系统的数学期望是多少？跑100笔之后，我应该盈利还是亏损？**

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 1.5 胜率盈亏.jpg" alt="图 1.5 胜率盈亏" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 数学期望：一个交易系统的核心指标

数学期望的计算公式很简单：

**期望值 = 胜率 × 平均盈利 - 败率 × 平均亏损**

举例：
- 胜率40%，平均盈利2000元，平均亏损1000元
- 期望值 = 40% × 2000 - 60% × 1000 = 800 - 600 = **+200元/笔**

这是一个正期望值系统。虽然胜率只有40%——6笔里有4笔是亏损的——但每笔交易平均能赚200元。跑100笔，期望总盈利是2万元。

再看一个反例：
- 胜率70%，平均盈利500元，平均亏损2000元
- 期望值 = 70% × 500 - 30% × 2000 = 350 - 600 = **-250元/笔**

这是一个负期望值系统。胜率很高，但亏的时候亏太多，长期必然亏损。这就是"死扛不止损"的人的典型结果——胜率看起来不错，但总资金在慢慢流失。

---

## 期望值思维改变了什么

理解期望值之后，你对交易的看法会发生三个变化：

**1. 单笔止损不再痛苦**

止损是正期望值系统在正常运行——它是你在一个100次实验里经历的正常失败结果，不是系统失效的信号。

就像知道某个骰子有60%的概率出现6点，即使连续出现了3次非6，你也不会觉得骰子坏了——你知道样本量还太小，需要继续执行。

**2. 高胜率不再是目标**

很多交易者痴迷于找"高胜率"系统。理解期望值之后你会发现，胜率只是公式里的一个变量，盈亏比是另一个变量。40%胜率+3:1盈亏比，比70%胜率+0.5:1盈亏比要好得多。

宽论体系的目标不是追求高胜率，而是追求正期望值——通过弹论过滤低胜率环境、通过止损控制亏损上限、通过趋势跟踪放大盈利来实现正期望值。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 4.22 持续稳定的回报.jpg" alt="图 4.22 持续稳定的回报" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

**3. 执行纪律有了数学基础**

为什么宽论强调"你不是在操控这笔交易的结果，你只是在重复一个正期望值的过程"？

因为单笔结果是随机的，但100笔的总结果在正期望值下是必然正的（在足够大的样本量下）。破坏执行纪律——跳过止损、随意改变仓位——会打乱这个过程，让100笔的总结果偏离数学期望，甚至把正期望变成负期望。

---

## 如何验证你的系统是正期望值

**第一步**：完整记录至少50笔交易（包括进出场价格、盈亏）

**第二步**：计算胜率 = 盈利笔数 / 总笔数

**第三步**：计算平均盈利（只算盈利的笔）和平均亏损（只算亏损的笔）

**第四步**：代入期望值公式计算

**第五步**：如果期望值为正，继续执行；如果为负，分析是胜率问题还是盈亏比问题

<div style="margin: 30px 0; padding: 20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 期望值思维的完整框架、如何用宽论体系构建正期望值交易系统、以及胜率与盈亏比的实战平衡，我在<strong style="color: #eb1313;">《概率的朋友》</strong>中做了系统讲解。这本书是<strong style="color: #ff6b35;">我桥博士的著作</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论完整交易框架都融入在这本书里</span>。
  </p>
  <div style="clear: both;"></div>
</div>

---

宽论的交易哲学有一句话：**"交易者不控制结果，只控制过程。"**

每笔交易的结果有随机性，但过程——按正期望值系统执行——是可以掌控的。把注意力从结果转移到过程，是从业余向职业跨越的关键一步。

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
