---
title: 用通达信麦语言把弹论写成代码一次你能跟上的全程实操
author: 桥博士
cover: C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 3.4 MACD 底背离形态.jpg
---

<blockquote style="background: linear-gradient(90deg, #ff6b35, #eb1313); padding: 10px 16px; border-radius: 6px; margin: 15px 0; color: white; font-weight: bold; border: none;">
📺 央视CCTV-2《经济半小时》专访 &nbsp;|&nbsp; 🏆 6个月盈利250万 &nbsp;|&nbsp; 🥇 国信证券CTA组月度第1名 &nbsp;|&nbsp; 📚《概率的朋友》作者桥博士 &nbsp;|&nbsp; 👥 22,768名会员社区
</blockquote>

很多读者私信问我：「桥博士，你书里讲的弹论五线、CDVA分型、带鱼验证，到底要怎么落到软件里？我不想再听理论了，能不能给我一次从零到信号亮起的全程实操？」今天这篇就是答案。我会用大家电脑里都有的通达信，配合麦语言，一步一步把弹论的核心判断写成代码，让你看完就能照着复刻。

不需要装Python，不需要搭服务器，不需要懂编译原理。你需要的只有一个能正常打开通达信的电脑，和愿意花二十分钟跟我一起敲键盘的耐心。

## 先讲清楚：麦语言到底是什么

麦语言是通达信、大智慧这一类股票软件内置的脚本语言，长得有点像Excel公式。它的设计初衷就是让交易员而不是程序员能用，所以函数名几乎都是英文单词的缩写：`C` 代表收盘价（Close），`O` 代表开盘价（Open），`H` 是最高，`L` 是最低，`MA(C,5)` 就是「过去5根K线收盘价的均值」。

写一条最简单的判断：「今天收盘价站上五日均线」——

```
C > MA(C,5)
```

就这么直白。没有import，没有class，没有def function。这就是为什么我说麦语言是散户做量化的最佳起点。

## 第一步：把弹论的「上部做多」翻译成代码

弹论里我经常讲一个概念叫「五线多头排列」，意思是5、10、20、60、120这五条均线从上到下依次排列，反映的是趋势已经在多头方向稳定下来。

用麦语言写就是这样——

```
DUOTOU := MA(C,5) > MA(C,10) 
       AND MA(C,10) > MA(C,20)
       AND MA(C,20) > MA(C,60)
       AND MA(C,60) > MA(C,120);
```

`:=` 在麦语言里是赋值，把这一长串判断条件打包成一个叫 `DUOTOU` 的变量。后面要用就直接写 `DUOTOU`，不用每次重复一大串。

接下来加上买入触发——价格回踩五日均线后再次站上：

```
BUY: DUOTOU AND CROSS(C, MA(C,5));
```

`CROSS(A,B)` 是麦语言内置函数，意思是A从下方上穿B。`BUY:` 这个前缀告诉软件「这一行是买入信号」。把这两段代码贴到通达信的「公式管理器」→「条件选股公式」里，保存为「弹论上部做多」，回车，软件立刻在所有满足条件的K线上画出箭头。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 3.4 MACD 底背离形态.jpg" alt="图 3.4 MACD 底背离形态" style="border-radius: 8px; max-width: 100%;" />

## 第二步：CDVA分型的金叉触发

弹论体系里另一个核心是CDVA分型——A型、B型、C型、D型四种MACD背离形态。其中最经典的入场信号是D型分型出现后的MACD金叉。

D型分型的关键特征是：价格创新低，但MACD的DIF没有创新低（底背离的一种）。麦语言写法——

```
DIF := EMA(C,12) - EMA(C,26);
DEA := EMA(DIF,9);
JINCHA := CROSS(DIF, DEA);
NEW_LOW_PRICE := L = LLV(L, 20);
NOT_NEW_LOW_DIF := DIF > LLV(DIF, 20);
D_FENXING := NEW_LOW_PRICE AND NOT_NEW_LOW_DIF;
BUY: D_FENXING AND JINCHA;
```

`LLV(X, N)` 是过去N根K线里X的最低值。这段代码做的事情是：今天最低价是过去20根K线的最低，但今天的DIF不是过去20根K线的最低，且今天MACD金叉——三个条件同时满足才触发买入。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 3.5 MACD 指标钝化形态.jpg" alt="MACD 指标钝化形态" style="border-radius: 8px; max-width: 100%;" />

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.12 “短鱼”是无效浪.jpg" alt="图 10.12 “短鱼”是无效浪" style="border-radius: 8px; max-width: 100%;" />

## 第三步：带鱼验证——判断这条浪是不是有效浪

弹论的带鱼验证是我自创的一个浪型有效性识别工具。简单讲，从一次MACD金叉到下一次死叉，价格如果走出了足够大的波动幅度，就叫「带鱼」（有效浪）；走得太短就叫「短鱼」（无效浪）。

用麦语言判断——

```
SICHA := CROSS(DEA, DIF);
JC_PRICE := VALUEWHEN(JINCHA, C);
SC_PRICE := VALUEWHEN(SICHA, C);
LANG_RATIO := (SC_PRICE - JC_PRICE) / JC_PRICE;
DAIYU := LANG_RATIO > 0.05;
```

`VALUEWHEN(条件, 值)` 这个函数会记住「最近一次满足条件时的值」。所以 `JC_PRICE` 就是最近一次金叉那天的收盘价，`SC_PRICE` 是最近一次死叉那天的收盘价。两者相除得到这一段波动的幅度，超过5%就标记为带鱼。

把这段加在策略后面，就能在K线图上把每一段「有效浪」自动框出来。这正是我在书里反复强调的：**眼睛看到的不算，软件标出来的才算。**

## 第四步：把信号导出，回测胜率

写完信号还没结束。量化的灵魂是回测。在通达信里点开「公式管理器」→「条件选股」→选中你刚保存的策略→点「测试」，软件会自动用过去一段时间的全部历史数据跑一遍，告诉你这个信号触发了多少次、其中多少次三日内上涨、多少次下跌、平均涨幅多少、最大回撤多少。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 1.5 胜率盈亏.jpg" alt="图 1.5 胜率盈亏" style="border-radius: 8px; max-width: 100%;" />

这一步是真正把你从「感觉这次能赚」升级到「我知道这套规则的胜率是62%、盈亏比是1.8、每次入场可期望收益是11%」的关键。**没有数字的策略不是策略，是迷信。**

## 第五步：把麦语言代码模板化，复用到其他品种

写好的策略可以一键应用到所有股票、ETF、可转债。这就是量化最大的杠杆——**一套规则同时盯着几千个标的**，比人工看盘效率高几个数量级。

我自己的实盘账户就是按这个逻辑组织的：弹论上部做多策略扫沪深300、CDVA D型分型策略扫中证500、带鱼验证作为持仓筛选条件叠加在前两者之上。每天收盘后软件自动跑一遍，第二天开盘前看一眼信号清单决定是否执行。整个过程从不需要我盯盘，更不需要我临时拍脑袋。

<img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友配图/图 10.3 如何提高整体收益.jpg" alt="如何提高整体收益" style="border-radius: 8px; max-width: 100%;" />

<div style="background: #fff3cd; border-left: 4px solid #ff6b35; padding: 16px; margin: 20px 0; border-radius: 8px;">
  <img src="C:/Users/anzib/gzhpublisher/assets/概率的朋友封面.jpg" alt="概率的朋友封面" style="border-radius: 8px; max-width: 100%; display: block; margin: 0 auto 12px;" />
  <p style="color: #eb1313; font-weight: bold; font-size: 1.1em;">📚 <strong>《概率的朋友：9天入门AI股票量化交易与技术分析》</strong></p>
  <p>本文展示的弹论五线多头、CDVA分型、带鱼验证三套麦语言代码模板，在书里都有更完整的版本——包含参数优化逻辑、不同周期的适配方法、与其他指标的组合方式。9天的学习路径是按照「先理解概率优势 → 再掌握麦语言写法 → 最后做参数回测」设计的，每天的内容都对应一个可以直接贴进通达信的代码片段。如果你想从「会看图」升级到「会写信号」，这本书是最短的路径。</p>
</div>

---

📚 **想深入学习宽论实战技巧？**

<img src="C:/Users/anzib/gzhpublisher/assets/微信二维码-桥楚.jpg" alt="交流探讨·桥博士" style="border-radius: 8px; max-width: 100%;" />

交流探讨·桥博士

如果本文对您有帮助，还请麻烦给文章点个在看或者免费的赞，感谢您的阅读。

*免责声明：本文介绍的是量化分析技术培训，不构成投资建议。投资有风险，入市需谨慎。*
