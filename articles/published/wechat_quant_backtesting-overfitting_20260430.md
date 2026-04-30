---
title: 回测的正确方式：避免过拟合的三个原则
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 3.31 MACD 指标针对上证 50 指数所有个股品种做历史回测损益图.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

量化交易最常见的陷阱，不是策略写错，而是策略在历史数据上完美，但实盘里一塌糊涂。

这叫过拟合（Overfitting）。策略在历史数据上表现太好，好到它其实已经在记忆过去，而不是识别规律。一旦遇到新数据，就彻底失效。

**回测的目的不是找到一个历史表现最好的策略，而是找到一个在未来仍然有效的策略。** 这两件事根本不是同一件事。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 3.31 MACD 指标针对上证 50 指数所有个股品种做历史回测损益图.jpg" alt="图 3.31 MACD指标回测损益图" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

---

## 过拟合为什么这么常见

过拟合有一个隐蔽的诱惑：它让你感觉自己"发现了规律"。

你测试了100组参数，找到了一组历史回测年化收益率80%的参数。你感觉找到了圣杯，但实际上你只是找到了在历史数据上运气最好的那组数字。如果历史换一个时段，这组参数可能垫底。

过拟合的根本原因：数据有限，参数组合无穷。只要参数组合足够多，总能在历史数据里找到一组"完美拟合"的参数——但那是对过去的记忆，不是对市场的理解。

---

## 三个避免过拟合的原则

**原则一：样本外测试（Out-of-Sample Testing）**

把历史数据分成两段：训练集（用来优化参数）和测试集（用来验证）。策略开发只用训练集，参数确定后，在完全没碰过的测试集上跑一遍。

如果训练集表现好，但测试集表现差，这个策略已经过拟合了。

通常的比例：70%训练集，30%测试集。测试集一旦用过，就不能再回头修改策略——否则测试集就变成了第二个训练集，失去了验证意义。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 3.22 参数优化结果.jpg" alt="图 3.22 参数优化结果" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

**原则二：参数越少越好**

每多一个可调参数，过拟合的风险就上升一级。一个有10个参数的策略，需要的数据量是一个2参数策略的指数倍，才能得到同等可信的回测结果。

宽论体系的设计哲学就是极简参数：弹论的五根均线参数是固定的（5、10、20、30、60），CDVA分型不需要参数，波浪带鱼只需要一个量比阈值。整个系统的可调参数不超过3个。

参数少，不是因为简单，是因为简单的规则在新数据上的鲁棒性更强。

**原则三：多品种、多时段验证**

一个策略在A股日线数据上跑出来的结果，不能只在A股日线数据上验证。

如果这个策略发现的是市场的普遍规律，它应该在其他品种（期货、港股）、其他周期（小时线、周线）上也表现稳定——不需要完全一样好，但至少不应该在方向上完全相反。

宽论的核心策略，都经过了A股股票、期货商品、不同时间周期的多维度验证。跨品种表现一致，才是"发现了规律"的标志。

<div style="margin: 30px 0; padding:-20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px; padding: 20px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 回测方法论、过拟合的识别与规避、样本外验证的实操框架，我在<strong style="color: #eb1313;">《概率的朋友》</strong>中做了系统讲解。这本书是<strong style="color: #ff6b35;">我桥博士的著作</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论量化研究方法论都融入在这本书里</span>。
  </p>
  <div style="clear: both;"></div>
</div>

---

## 回测结果应该长什么样

一个可信的回测结果，不是历史年化收益率最大化，而是：

- **样本内和样本外表现接近**（差距在20%以内是可接受的）
- **在多个品种和时段上方向一致**（不是只有一个市场好）
- **最大回撤可以接受**（回撤超过30%，大多数人在实盘里扛不住）
- **交易频率合理**（年交易次数太少，统计意义不足；太多，可能是过度交易）

宽论用MACD策略对上证50成分股做过全样本回测（2000-2025年），多品种、全时段、无参数优化，结果显示稳定正收益。这是"策略发现了规律"而不是"策略记住了历史"的证明。

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
