---
title: 学了这么多K线形态还是不会用？试试量化分型
author: 宽论
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.7 C 分型.jpg
---

<svg width="375" height="40" xmlns="http://www.w3.org/2000/svg">
  <text font-size="16" y="25" x="375">
    <tspan fill="#eb1313">● 央视CCTV-2专访 | 6个月盈利250万 | 国信证券大赛第1名 | 22768名会员验证</tspan>
    <animate attributeName="x" from="375" to="-800" begin="0s" dur="18s" repeatCount="indefinite"/>
  </text>
</svg>

十字星、锤子线、早晨之星、头肩底、双重顶……你是不是也背过一大堆K线形态？

书上说得头头是道，什么"底部出现锤子线看涨"、"高位十字星见顶"。可到了实战里，你发现同一个形态有时候灵，有时候不灵。你严格按照教科书操作，结果亏了；你犹豫没操作，行情又真的走出来了。

这种矛盾体验，我太熟悉了。

做了30年交易之后，我想明白了一件事：**传统K线形态分析最大的问题，不是形态本身不准，而是它完全依赖主观判断。** 同一根K线，十个人能看出十种解读。这不是分析，这是猜测。

我花了很长时间，把K线形态背后的逻辑提炼成了四个量化信号。**不需要你去"看"形态，只需要满足明确的数学条件，信号就自动触发。** 我把它叫做CDVA分型。

---

## K线形态分析的三个致命伤

在讲CDVA之前，先说清楚传统K线分析为什么不好用。

**第一，主观性太强。** 什么叫"锤子线"？影线必须是实体的两倍以上？还是1.5倍就算？不同的书给不同的定义，你到底信哪个？在实战中，你会发现大量"像锤子但又不太像"的K线，这时候你的决策依据就只剩下"感觉"了。

**第二，脱离市场环境。** 底部的锤子线是看涨信号，但如果这个"底部"本身只是下跌途中的一个平台呢？传统K线分析很少告诉你怎么判断"真底部"和"假底部"。形态正确但位置错误，等于白搭。

**第三，无法量化回测。** "早晨之星"的胜率到底是多少？在A股市场、不同板块、不同周期下表现如何？传统K线分析几乎没有人做过大样本回测。你学的这些形态，可能从来没有被系统性地验证过。

这三个问题的本质是同一个：**K线形态缺少可量化、可验证、可重复的判断标准。**

---

## CDVA分型：四个信号，四个明确条件

我把K线形态分析中最核心的两类信号——**趋势转折**和**价格突破**——提炼成了四个量化分型，每个都有精确的数学定义，不需要任何主观判断。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.7 C 分型.jpg" alt="CDVA-C分型示意图" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

### C分型（CrossUp · 金叉看多）

**定义**：快线从下往上穿过慢线。

这是最经典的趋势转向信号。当短期均线上穿长期均线时，说明短期内买方力量开始超过卖方。和传统金叉的区别在于：C分型必须结合弹论的位置判断。弹簧上部出现C分型，可信度最高；弹簧中部出现C分型，需要等待确认。

**记忆口诀**：C = CrossUp = 线穿线向上 = 看多。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.8 D 分型.jpg" alt="CDVA-D分型示意图" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

### D分型（CrossDown · 死叉看空）

**定义**：快线从上往下穿过慢线。

C分型的镜像。短期均线下穿长期均线，说明卖方力量占据上风。同样需要结合位置：弹簧下部出现D分型是趋势延续的确认，弹簧上部出现D分型则是危险信号——趋势可能要反转了。

**记忆口诀**：D = CrossDown = 线穿线向下 = 看空。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.9 V 分型.jpg" alt="CDVA-V分型示意图" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

### V分型（价上穿 · 突破看多）

**定义**：当日收盘价高于上一根K线实体的上沿。

这不是看均线的信号，而是看价格本身。当收盘价突破前一根K线的实体上沿时，说明多方在当天完成了一次有效突破。V分型经常出现在调整结束、趋势恢复的起点。

**记忆口诀**：V = 价格向上突破 = 多方发力。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.10 A 分型.jpg" alt="CDVA-A分型示意图" style="border-radius: 8px; max-width: 100%; display: block; margin: 20px 0;" />

### A分型（价下穿 · 跌破看空）

**定义**：当日收盘价低于上一根K线实体的下沿。

V分型的镜像。收盘价跌破前一根K线实体下沿，说明空方完成了一次有效打压。A分型常出现在反弹失败、下跌延续的起点。

**记忆口诀**：A = 价格向下跌破 = 空方发力。

---

## 两句话记住全部：线穿线是CD，价穿价是VA

CDVA分型看似四个信号，记忆其实很简单：

**CD分型看均线交叉**——快线穿慢线。C是向上穿（看多），D是向下穿（看空）。本质是判断**趋势方向**。

**VA分型看价格突破**——收盘价穿前一根K线实体。V是向上穿（看多），A是向下穿（看空）。本质是判断**即时强弱**。

CD看趋势，VA看强弱。四个信号组合使用，你对市场的读取能力会比单独看K线形态精确得多。

而且，每一个分型的定义都是**精确的数学条件**：有就是有，没有就是没有。不存在"像不像""算不算"的模糊地带。这就是量化分析的力量——**用规则替代感觉，用确定性替代猜测。**

<div style="margin: 30px 0; padding: 20px; background: #fff9e6; border-left: 4px solid #ff6b35; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" style="border-radius: 8px; width: 200px; float: left; margin-right: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" alt="概率的朋友封面" />
  <p style="font-size: 16px; color: #333; line-height: 1.8; margin-bottom: 10px;">
    📖 CDVA分型的完整定义、参数设置、以及和弹论/QR值的组合实战策略，我都写进了<strong style="color: #eb1313;">《概率的朋友》</strong>这本书里。这是<strong style="color: #ff6b35;">我桥博士的著作</strong>，<span style="background: #fff3cd; padding: 2px 6px; font-weight: bold;">宽论的完整知识体系都融入在这本书里</span>。
  </p>
  <p style="font-size: 15px; color: #555; line-height: 1.8;">
    书里不仅讲每个分型怎么用，还讲了它们失效的场景和应对方法。<strong>量化交易不是背公式，而是建立一套完整的信号验证体系。</strong>
  </p>
  <div style="clear: both;"></div>
</div>

---

## CDVA在宽论体系中的位置

CDVA不是孤立使用的。在宽论的"一个中心、两个基本点、三个工具"体系中，CDVA分型是**第二个工具——定信号**。

完整的决策流程是这样的：

**弹论定方向**：先看五根均线判断市场处于弹簧上部、中部还是下部。确定"该不该做"。

**CDVA定信号**：在弹论确认方向之后，用C/D/V/A四种分型寻找精确的入场和出场时机。确定"什么时候做"。

**波浪带鱼做验收**：交易完成后，用带鱼/短鱼判断这笔交易是抓住了真趋势还是遇到了假突破。确定"做得对不对"。

三个工具环环相扣，构成了一个从决策到执行到复盘的完整闭环。

我用这套体系在2019年国信证券策略大赛中获得"短跑王"赛季第1名。6个月时间，8000多笔交易，盈亏比2.76。其中CDVA分型贡献了大量高质量的入场信号——有了精确的入场点，止损可以设得很近，风险回报比自然就高了。

（数据来源：宽论官方公开资料）

---

## 今天就可以开始做的事

下次看盘的时候，不要再盯着K线形态猜"这是不是锤子线"了。把注意力放在两件事上：

**第一，看均线有没有交叉。** 快线上穿慢线（C分型）= 短期趋势转多；快线下穿慢线（D分型）= 短期趋势转空。

**第二，看收盘价有没有突破。** 收盘价突破前一根K线实体上沿（V分型）= 多方发力；跌破下沿（A分型）= 空方发力。

就这两个动作，比你背100种K线形态都管用。因为它们有明确的判断标准，不给你留"纠结"的空间。

**交易最怕的不是看错方向，而是看不清方向。** CDVA分型做的就是帮你看清楚——用数学而不是感觉。

---

<div style="text-align: center; margin: 30px 0 20px 0;">
  <p style="font-size: 16px; font-weight: bold; color: #333; margin-bottom: 10px;">📚 想深入学习宽论实战技巧？</p>
  <img src="C:/Users/anzib/gzhpublisher/assets/微信二维码-桥楚.jpg" style="border-radius: 8px; width: 200px; display: block; margin: 0 auto 15px auto;" alt="微信二维码" />
  <p style="font-size: 16px; font-weight: bold; color: #f4c430; line-height: 1.8;">扫码找助理，发送"宽论"，领取宽论实战课程</p>
</div>

<img src="C:/Users/anzib/gzhpublisher/assets/免费free.gif" style="border-radius: 8px; width: 100%; display: block; margin: 20px 0;" alt="免费资料" />

<div style="text-align: center; margin: 20px 0; padding: 15px; color: #666;">
  <p style="font-size: 14px; line-height: 1.8;">如果本文对您有帮助，还请麻烦给文章点个在看或者免费的赞，感谢您的阅读。</p>
</div>

*免责声明：本文介绍的是量化分析技术培训，不构成投资建议。投资有风险，入市需谨慎。*
