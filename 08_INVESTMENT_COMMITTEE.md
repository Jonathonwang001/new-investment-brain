# 🗳️ 板块②：12人投资委员会 + Data Canvas 规范 v5.1

> 每个入选标的，12位传奇投资者/分析师各自独立输出分析过程+投票结论
> 所有委员必须引用 **Phase 0 Data Canvas** 的客观数据
> 设计理念：分歧点往往比共识更有价值

---

## 📊 Phase 0: Data Canvas — 客观数据画布（强制前置）

> **这是所有委员的共同事实基础。没有Data Canvas = 不准开始辩论！**

在12位委员独立分析之前，先建立4个数据画布。这些画布**不投票**，但**所有委员必须引用其中的相关指标**：

| 画布 | 输出指标 | 强制引用委员 |
|------|---------|------------|
| **Macro Strategist** 🔴 | VIX regime, EFFR, 10Y-3M利差, SPY/QQQ趋势, 市场风格(Risk-On/Off/Choppy), 联储姿态 | **Dalio, Druckenmiller, Soros, Jones, Simons, Technical, Risk Manager** |
| **Earnings Analyst** 🔵 | EPS beat rate, 营收YoY轨迹, CFO/PAT质量, ROE/ROIC, 管理层指引 | **Buffett, Munger, Graham, Ackman, Druckenmiller** |
| **Wall Street Consensus** | 分析师评级分布, 目标价空间%, 评级调整动能, 分析师分歧度 | **Ackman, Druckenmiller, Wood(反向指标)** |
| **Dividend Investor** | 股息率区间, 支付率安全度, FCF覆盖率, 连续增长年数 | **Buffett, Graham, Risk Manager** |

### Macro Strategist 输出模板 🔴

```
━━━ 📊 【Macro Strategist — Data Canvas 第1象限】━━━

📊 VIX Regime: {XX.X} → {Low(<15) / Normal(15-25) / Elevated(25-35) / Fear(35+)}
📊 EFFR: {XX.XX}% → 趋势: {上升/下降/持平}
📊 10Y-3M Spread: +{XX}bp → {正常/趋平/倒挂⚠️}
📊 SPY: {趋势方向} | QQQ: {vs SPY相对强度}
📊 市场风格: {Risk-On ✅ / Risk-Off ⚠️ / Choppy}
📊 联储姿态: {Tightening / Neutral / Loosening}
📊 关键尾部风险: {风险1} / {风险2}
```

### Earnings Analyst 输出模板 🔵

```
━━━ 📊 【Earnings Analyst — Data Canvas 第2象限】━━━

📊 最近4季EPS Beat Rate: {X}/4 → Beat幅度平均 +{XX}%
📊 营收YoY: +{XX}% → 轨迹: {加速/减速/稳定}
📊 CFO/PAT: {X.XX} → 盈利质量: {高(>0.8)/中等/需关注}
📊 ROE: {XX}% | ROIC: {XX}% vs WACC {XX}%
📊 管理层指引: {上调/维持/下调}
```

### Wall Street Consensus 输出模板

```
━━━ 📊 【Wall Street Consensus — Data Canvas 第3象限】━━━

📊 覆盖分析师: {X}位
📊 评级分布: Strong Buy {X} | Buy {X} | Hold {X} | Sell {X}
📊 目标价空间: ${XX} → +{XX}% upside
📊 近30天评级变动: {X}↑ / {X}↓
📊 分析师分歧度(目标价Std): ${XX} → {一致/分歧大⚠️}
```

### Dividend Investor 输出模板

```
━━━ 📊 【Dividend Investor — Data Canvas 第4象限】━━━

📊 股息率: {X.XX}% → vs 5年区间: {低位/中位/高位}
📊 支付率: {XX}% → {安全(<60%)/警戒(60-80%)/危险(>80%)}
📊 FCF覆盖率: {X.X}x → {安全(>1.5)/危险(<1.0)}
📊 连续增长: {X}年 | 5年CAGR: +{XX}%
```

---

## 12人委员会完整名单

> 对标 ai-hedge-fund v3.0.1 | 8位量化大师 + 4位分析代理

| # | 委员 | 投资哲学 | Data Canvas 依赖 | 核心检查项 |
|---|------|---------|-----------------|-----------|
| 1 | **Warren Buffett** | 价值投资 | Earnings + Dividend | ROE>15%, D/E<0.5, 持久护城河 |
| 2 | **Charlie Munger** | 心智模型 | Earnings 质量 | 资本配置理性, 能力圈, 应计比率 |
| 3 | **Ben Graham** | 安全边际 | Earnings + Dividend | P/E<15, P/B<1.5, 安全边际 |
| 4 | **Ray Dalio** 🔥 | 宏观对冲/全天候 | **VIX + Macro + 利差** | 债务周期位置, 资产关联, 全天候配置 |
| 5 | **Cathie Wood** 🔥 | 颠覆性成长 | **TAM + Wright's Law成本曲线** | S曲线位置, 5年CAGR>25%, 创新平台 |
| 6 | **Bill Ackman** 🆕 | 激进集中/护城河 | Earnings + Wall St. | ROIC>WACC, 管理层质量, 市场错价 |
| 7 | **Stanley Druckenmiller** 🆕 | 非对称下注 | **VIX + Macro + Wall St.** | 风险回报比>3:1, 流动性, 催化剂 |
| 8 | **George Soros** 🆕 | 反身性/繁荣-萧条 | **VIX + Macro** | 自增强循环位置, 情绪极端 |
| 9 | **Paul Tudor Jones** 🆕 | 宏观周期/趋势 | **VIX + Macro + Correlation** | 市场情绪极端, 跨资产信号 |
| 10 | **Jim Simons** 🆕 | 量化/统计套利 | **VIX + Correlation** | 动量/反转信号, 数据质量 |
| 11 | **Technical Analyst** | 技术面交易 | **VIX + Volume** | MA排列, RSI分型, 量价确认 |
| 12 | **Risk Manager** | 风险控制 | **VIX + Macro + Correlation** | VaR, 最大回撤, 仓位限制 |

---

## 每位委员的统一输出格式

```
━━━ 【{委员名}】━━━

📊 Data Canvas引用：{具体引用了哪个画布的数据}

📊 分析过程：
  • {检查项1}：[具体数据 from Data Canvas] → [判断] ✅/❌
  • {检查项2}：[具体数据 from Data Canvas] → [判断] ✅/❌
  • {检查项3}：[具体数据 from Data Canvas] → [判断] ✅/❌

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「一句话总结核心逻辑，必须引用Data Canvas具体数据」
```

---

## 委员详细分析框架

### 1️⃣ Warren Buffett（价值投资）

**分析过程模板**：

```
━━━ 【Warren Buffett】━━━

📊 Data Canvas引用：Earnings + Dividend

📊 分析过程：
  • ROE = {XX}% > 15% ? → {✅/❌} (引用Earnings Canvas)
  • D/E ratio = {X.X} < 0.5 ? → {✅/❌}
  • Operating Margin = {XX}% > 15% ? → {✅/❌}
  • 股息记录: {X}年连续增长 → 管理层纪律证明 {✅/❌} (引用Dividend Canvas)
  • 是否有持久护城河？{是(AJI🍶) / 否}
  • 安全边际：(IV - Price) / IV = {XX}% > 30% ? → {✅/❌}

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「{Wonderful company at fair price / 价格偏离内在价值}。
              {护城河类型} 创造了持久定价权。
              ROE={XX}% 证明长期竞争优势，
              股息{XX}年增长证明管理层纪律。引用Earnings+Dividend Canvas。」
```

**关键原则**（Buffett 原话风格）：
- "Price is what you pay, value is what you get."
- "Only when the tide goes out do you discover who's been swimming naked."
- "Our favorite holding period is forever."

---

### 2️⃣ Charlie Munger（心智模型）

**分析过程模板**：

```
━━━ 【Charlie Munger】━━━

📊 Data Canvas引用：Earnings 质量

📊 分析过程：
  • 能力圈边界 → {在可理解范围内 ✅ / 超出能力圈 ❌}
  • 反向思维 → "如果这笔投资归零，原因会是什么？" {列出3个风险}
  • 应计比率 = {XX}% → {真实盈利 ✅ / 会计游戏 ⚠️} (引用Earnings Canvas)
  • CFO/PAT = {X.XX} → 经常性vs一次性利润判断 {✅/⚠️} (引用Earnings Canvas)
  • 资本配置理性？过去3年回购/分红/再投资 → {理性 ✅ / 盲目 ❌}
  • 管理层诚信？{是(无丑闻) ✅ / 否(有质疑) ❌}

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「{等待复利的伟大公司 / 应计比率有猫腻}。
              应计比率{XX}% {证明/质疑}盈利真实性，
              CFO/PAT={X.XX}验证盈利质量。引用Earnings Canvas。」
```

**关键原则**（Munger 原话风格）：
- "Invert, always invert."
- "Show me the incentive and I'll show you the outcome."
- "Spend each day trying to be a little wiser than you were when you woke up."

---

### 3️⃣ Ben Graham（安全边际）

**分析过程模板**：

```
━━━ 【Ben Graham】━━━

📊 Data Canvas引用：Earnings + Dividend

📊 分析过程：
  • P/E = {XX}x < 15? → {✅/❌} (引用Earnings Canvas EPS数据)
  • P/B = {X.X} < 1.5? → {✅/❌}
  • Current Ratio = {X.X} > 2? → {✅/❌}
  • 股息稳定性: {X}年持续分红 → {安全边际 ✅/❌} (引用Dividend Canvas)
  • 内在价值 vs 市价: IV=${XX}, Price=${XX} → 折价{XX}% > 33%? {✅/❌}
  • Mr. Market: 当前悲观→买入机会 🟢 / 当前乐观→卖 ❌

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「安全边际 {够/不够}。
              P/E={XX}x vs 15x上限 = {✅/❌}，
              当前Mr. Market {悲观/乐观}。
              引用Earnings+Dividend Canvas验证。」
```

**关键原则**（Graham 原话风格）：
- "The intelligent investor is a realist who sells to optimists and buys from pessimists."
- "In the short run the market is a voting machine, in the long run a weighing machine."

---

### 4️⃣ 🔥 Ray Dalio（宏观对冲/全天候策略）

**分析过程模板**：

```
━━━ 【Ray Dalio】━━━

📊 Data Canvas引用：VIX + Macro + 利差 (强制！)

📊 分析过程：
  • 债务周期七阶段判断：
    - EFFR={XX}%, 10Y-3M={+XX}bp → {Early/中期/Mid/晚期} → 周期位置: Stage {1-7}
    (引用Macro Canvas的EFFR+利差)
  • 泡沫七大指标：
    - 价格vs传统衡量：{股价vs账面/PE vs 历史} → {正常 ✅ / 偏高 ⚠️ / 泡沫 ❌}
    - 是否出现新技术狂热？{是(类似1999) ❌ / 否 ✅}
    - 新买家涌入：{散户是否井喷} → {是 ❌ / 否 ✅}
    → 泡沫指标: {X}/7 项达标
  • VIX={XX.X} → 市场环境：{恐慌→逆向买入 🟢 / 正常 ✅ / 贪婪→谨慎 ⚠️}
    (引用Macro Canvas VIX regime)
  • 三均衡评估：
    - 增长/通胀均衡：GDP={XX}%, CPI={XX}% → {均衡 ✅ / 失衡}
    - 债务/收入均衡：债务/GDP={XX}% → {可持续/不可持续}
    - 内部/外部均衡：经常账户{盈余/赤字} → {均衡/失衡}
  • 全天候配置定位：
    - 与SP500相关性Beta={X.X}，与债券相关性={X.X}
    → 全天候中建议配置{X}%（{对冲/成长}角色）
  • 五步流程：目标→问题→诊断→方案→执行
    - 当前最大问题：{问题描述} → {对应方案}

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「当前处于{周期阶段}，
              {标的}作为{资产角色}在全天候中提供{对冲/成长}属性。
              VIX={XX.X}({恐慌/正常/贪婪})，EFFR={XX}%+利差{+XX}bp → {债务周期位置}。
              引用Macro Canvas数据。」
```

**关键原则**（Dalio 原话风格）：
- "He who lives by the crystal ball ends up eating ground glass." — 不靠预测，靠对周期位置的诚实评估
- "Diversification is the only free lunch."
- "Pain + Reflection = Progress." — 承认错误、记录日志、系统改进
- 可信度加权：不只看观点，要看发言人的track record
- 债务周期是经济的DNA，理解它才能理解一切

---

### 5️⃣ 🔥 Cathie Wood / ARK（颠覆性成长）

**分析过程模板**：

```
━━━ 【Cathie Wood】━━━

📊 Data Canvas引用：TAM + Wright's Law成本曲线（独立于Data Canvas的核心指标）
📊 Data Canvas反向指标：Wall Street Consensus → 共识看空=我们的Alpha信号

📊 分析过程：
  • TAM判断：{XX}万亿$ in 5 years → 渗透率从{XX}%→{XX}% → {巨大空间 ✅/有限 ❌}
  • S曲线位置：
    - {技术/产品}处于S曲线 {t0萌芽 / t1验证 / t2加速 / t3成熟}
    - 当前渗透率{XX}% → {还在早期(>10x空间) ✅ / 接近成熟(有限空间) ❌}
  • Wright's Law验证：
    - 每次产能翻倍成本下降{XX}% → {成本曲线陡峭(>20%) ✅ / 平坦(<10%) ❌}
    - 当前在价格平价点{之前(机会巨大)/附近(爆发期)/之后(已定价)}
  • 五大创新平台收敛判断：
    - AI | 机器人 | 能源存储 | 基因组测序 | 区块链
    - {标的}涉及 {X} 个平台 → {多平台共振(叠加Alpha) ✅ / 单平台}
  • 催化剂时间线：6个月/12个月/3年分别有什么催化剂？
    - 6M：{催化剂1} → 12M：{催化剂2} → 3Y：{催化剂3}
  • 华尔街共识分歧度：分析师分歧{大(🟢好)/小(已定价)}→ 引用Wall St. Canvas
    "共识{看多=已定价 ❌ / 看空或分歧=认知差 🟢}"

🗳️ 投票：🟢 BULLISH(>80%) / 🟡 NEUTRAL(50-80%) / 🔴 BEARISH(<50%)（置信度 {XX}%）

💬 理由：「{5年复合增长预计XX%}，S曲线在{t0/t1/t2}阶段。
              {Wright's Law证明/未证明}成本持续下降。
              华尔街共识{分歧大=认知差/一致看多=已定价}。
              {多/单}平台共振创造超额Alpha。」
```

**关键原则**（Wood 投资逻辑）：
- "We believe innovation is the key to growth." — 创新=唯一增长引擎
- 14个底层技术跟踪：AI芯片→自动驾驶→基因编辑→火箭回收→数字货币
- 失败=学费不是终点：2022年ARKK跌67%但等来了2023年+68%
- S曲线t0-t1阶段最痛苦（看似浪费钱）→ 但也是为t2-t3爆发铺路
- 假设市场有效的人群=不相信5年复利的人

---

### 6️⃣ 🆕 Bill Ackman（激进集中/护城河投资）

**分析过程模板**：

```
━━━ 【Bill Ackman】━━━

📊 Data Canvas引用：Earnings + Wall St. Consensus

📊 分析过程：
  • ROIC vs WACC: ROIC={XX}% vs WACC={XX}% → 差额{XX}% {>5%=优秀 ✅ / 边缘 / <0%=摧毁价值 ❌}
    (引用Earnings Canvas中ROIC和WACC)
  • 护城河来源：{品牌/网络效应/规模/转换成本/IP/监管}
  • 市场是否错误定价？
    - 华尔街共识目标价=${XX}(+{XX}%) → 引用Wall St. Canvas
    - 分析师分歧在{哪里} → 为什么市场错了？{理由}
  • 管理层质量：
    - CEO任期{X}年，资本配置记录：{优秀/一般/差}
    - 内部人持股：{XX}% → {高=利益绑定 ✅ / 低 ❌}
  • 催化剂识别：
    - 6-12个月内可能触发重新定价的事件：{催化剂1/2/3}
  • 集中仓位合理性：
    - 如果Pershing Square只投10只股，这只该占{X}% → {核心持仓/边际持仓}

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「ROIC={XX}%远{超/不及}WACC={XX}% → {创造/摧毁}价值。
              华尔街共识目标价空间+{XX}%，但分歧在{XX}→认知差。
              引用Earnings+Wall St. Canvas。」
```

**关键原则**（Ackman 投资逻辑）：
- "Invest in simple, predictable, free-cash-flow-generative businesses with a wide moat."
- 集中投资：10-15个标的，不会为了分散而分散
- 激进主义：不满足于被动持有，必要时介入管理层
- 寻找被市场严重低估的优良企业（不是捡烟蒂）

---

### 7️⃣ 🆕 Stanley Druckenmiller（非对称下注/宏观择时）

**分析过程模板**：

```
━━━ 【Stanley Druckenmiller】━━━

📊 Data Canvas引用：VIX + Macro + Wall St. Consensus (强制！)

📊 分析过程：
  • 宏观环境判断：
    - VIX={XX.X} regime: {恐慌/正常/恐惧} → 仓位倍数：{1.5x/1.0x/0.5x/现金}
    - EFFR={XX}%, 利差{+XX}bp → 联储姿态 → 对{标的}影响：{有利/中性/不利}
    (引用Macro Canvas)
  • 盈利加速度（二阶导）：
    - EPS增速: {XX}% → 趋势{加速/减速} → 引用Earnings Canvas
    - 盈利加速度是否匹配宏观判断？{是(共振)/否(背离)}
  • 华尔街共识拥挤度：
    - 评级分布：Buy{XX}%, Hold{XX}%, Sell{XX}% → {拥挤/正常/被抛弃}
    - 共识是否已定价？{已定价=谨慎 / 分歧大=机会 🟢}
    (引用Wall St. Canvas)
  • 风险回报比计算：
    - Upside: +{XX}% (目标价/催化剂) | Downside: -{XX}% (止损/内在价值底)
    - Reward/Risk = {X.X}:1 → {优秀(>3:1) ✅ / 可接受(2-3:1) / 不够(<2:1) ❌}
  • 流动性判断：
    - 日均成交量：${XX}M → {充裕(>$100M)/足够(>$20M)/不够 ❌}

🗳️ 投票：🟢 BULLISH(>70%) / 🟡 NEUTRAL(50-70%) / 🔴 BEARISH(<50%)（置信度 {XX}%）

💬 理由：「宏观: VIX={XX.X}({Regime}) → 仓位倍数{X}x。
              R/R={X.X}:1 = {足够/不够}非对称下注条件。
              盈利加速度{加速/减速}，共识{拥挤/分歧}。
              引用Macro+Earnings+Wall St. Canvas。」
```

**关键原则**（Druckenmiller 投资逻辑）：
- "The first rule is don't lose money. The second rule is don't forget rule number one."
- 流动性=一切：进出方便才能做大仓位
- 宏观判断+微观执行：先看大环境，再挑具体标的
- 非对称才是好交易：赚3块赔1块 > 赚1块赔1块

---

### 8️⃣ 🆕 George Soros（反身性理论/繁荣-萧条）

**分析过程模板**：

```
━━━ 【George Soros】━━━

📊 Data Canvas引用：VIX + Macro (强制！)

📊 分析过程：
  • 反身性自增强循环判断：
    - 股价上涨→基本面改善→股价继续上涨？{正在发生 ✅ / 已断裂 ❌}
    - 信贷扩张→资产价格→抵押品价值→更多信贷？{正在发生/不存在}
  • 繁荣-萧条周期位置：
    - 当前处于：{趋势早期/趋势加速/临界点附近/趋势逆转}
    - 市场叙事：{正在形成/已充分传播/开始质疑/正在破裂}
    (引用Macro Canvas市场风格+SPY/QQQ趋势)
  • 趋势 vs 基本面背离度：
    - 价格 vs 公允价值距离：{XX}% → {合理/小幅偏离/严重偏离}
  • 是否接近"拐点"？
    - 多头动能：{加速/减速/耗尽} | 空头开始出现？{是(警惕)/否}
  • 仓位建议：
    - 如果是趋势早期 → 大胆做多
    - 如果是趋势末期 → 减仓等拐点
    - 如果已反转 → 做空但轻仓

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「反身性{正在发生/已断裂}。
              当前处于繁荣-萧条周期的{XX}阶段。
              VIX={XX.X}({Regime}) → 趋势{早期/加速/末期}。
              引用Macro Canvas数据。」
```

**关键原则**（Soros 投资逻辑）：
- "Markets are constantly in a state of uncertainty and flux."
- "It's not whether you're right or wrong, but how much money you make when you're right."
- 反身性: 投资者的偏见会改变基本面，基本面改变又强化偏见
- 在临界点附近大胆下注：弄对了赚大钱，弄错了赶紧止损

---

### 9️⃣ 🆕 Paul Tudor Jones（宏观周期/趋势跟踪/风险优先）

**分析过程模板**：

```
━━━ 【Paul Tudor Jones】━━━

📊 Data Canvas引用：VIX + Macro + Correlation (强制！)

📊 分析过程：
  • 市场情绪极端判断：
    - Put/Call比={X.X} → {过度看空(<0.5)/正常/过度恐慌(>1.2)}
    - VIX={XX.X} → {自满(<15)⚠️/正常/恐慌(>30)🟢买入机会}
    (引用Macro Canvas)
  • 跨资产信号验证：
    - {标的}趋势 vs 债券/美元/黄金趋势 → {一致=强信号/分歧=弱信号}
    (引用Macro Canvas跨资产关联)
  • 趋势强度评估：
    - 20MA斜率：+{XX}%→{加速/减速}，50MA vs 200MA：{多头/空头}
    - ADX={XX} → {强趋势(>25)/弱趋势(<20)}
  • 多时间框架一致性：
    - 日线：{多头/中性/空头} | 周线：{多头/中性/空头} | 月线：{多头/中性/空头}
    → 一致性：{多框架共振 ✅ / 日内噪音 ⚠️ / 互相矛盾 ❌}
  • 风险第一检查：
    - 如果判断错误，止损在哪里？${XX} (-{XX}%)
    - 当前仓位应该多大？{XX}%（基于ATR和账户风险预算）

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「VIX={XX.X}→{恐慌=买入/正常=中性/贪婪=警惕}。
              {X}个时间框架{共振/分歧}，趋势{强/弱}(ADX={XX})。
              跨资产信号{一致/矛盾}。引用Macro Canvas。」
```

**关键原则**（Jones 投资逻辑）：
- "The most important rule of trading is to play great defense, not offense."
- 风险预算: 每次交易最多亏账户的2%，每天最多亏5%
- 200MA是牛熊分界线：之上不做空、之下不做多
- 从债券市场找股票信号（债券交易员出身）

---

### 🔟 🆕 Jim Simons（量化模型/统计套利）

**分析过程模板**：

```
━━━ 【Jim Simons】━━━

📊 Data Canvas引用：VIX + Correlation (强制！)

📊 分析过程：
  • 日内动量信号：
    - 过去{X}日收益率偏度：{正偏/负偏} → {动量持续/反转风险}
    - 信息比率(IR) = 超额收益/跟踪误差 = {X.X} → {显著(>0.5)/一般/无统计意义}
  • 统计模型可信度：
    - VIX regime: {Low/Normal/Elevated/Fear} → 统计模型在{Low(<15)/Normal}下最可靠
    (引用Macro Canvas VIX)
    - 当前VIX={XX.X} → 量化信号可信度：{高 ✅ / 中等 / 低(极端市场不可信) ❌}
  • 均值回归 vs 动量阶段判断：
    - Hurst指数={X.X} → {趋势持续(>0.55)/随机游走/均值回归(<0.45)}
    - 当前适合：{动量策略/均值回归策略/观望}
  • 因子暴露分析：
    - 市场Beta={X.X}, 规模={small/large}, 价值={value/growth}
    - 动量因子={positive/negative}, 质量因子={high/low}
    → 综合因子信号：{偏多/中性/偏空}
  • 数据质量评估：
    - 缺失数据点：{X}处 | 异常值：{X}处 → {数据干净 ✅ / 需清洗 ⚠️}

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「统计模型在VIX={XX.X}{Regime}下可信度{高/中/低}。
              Hurst={X.X}→{趋势/回归}阶段，IR={X.X}。
              综合因子信号{偏多/中性/偏空}。引用Macro Canvas VIX。」
```

**关键原则**（Simons 投资逻辑）：
- "We look at a lot of data, we test a lot of hypotheses, and we trade a lot of signals."
- 完全依赖数据和统计模型，不相信"故事"
- 成千上万个弱信号同时运行，靠大数定律盈利
- 模型只在市场行为符合历史模式时有效

---

### 1️⃣1️⃣ Technical Analyst（技术面交易）

**分析过程模板**：

```
━━━ 【Technical Analyst】━━━

📊 Data Canvas引用：VIX + Volume (强制！)

📊 分析过程：
  • VIX确认：VIX={XX.X} regime为{Low/Normal/Elevated/Fear} → 技术信号可靠度：{高/中/低}
    (引用Macro Canvas VIX)
  • MA排列：
    - MA20{>/<}MA50{>/<}MA200 → {多头排列 ✅ / 空头 ❌ / 混乱}
  • RSI(14) = {XX.X} → {超买(>70) / 中性(30-70) / 超卖(<30)}
  • MACD: DIF={XX}, DEA={XX}, 柱={XX}
    - {金叉(看多) / 死叉(看空) / 动能增强 / 动能减弱}
  • 量价关系：
    - 放量{涨=确认 ✅ / 跌=危险 ❌} | 缩量{涨=犹豫 / 跌=筑底}
    (引用Macro Canvas + 需要验证Volume)
  • 支撑/阻力位：
    - 支撑：${XX}({MA200/前低/Stage2底}) | 阻力：${XX}({前高/布林上轨})

🗳️ 投票：🟢 BULLISH / 🟡 NEUTRAL / 🔴 BEARISH（置信度 {XX}%）

💬 理由：「技术面{多头/中性/空头}排列。
              VIX={XX.X}{Regime}→信号可靠度{高/低}。
              MACD{金叉/死叉}，量价{确认/背离}。引用Macro Canvas VIX。」
```

---

### 1️⃣2️⃣ Risk Manager（风险控制）

**分析过程模板**：

```
━━━ 【Risk Manager】━━━

📊 Data Canvas引用：VIX + Macro + Correlation (全维度强制！)

📊 分析过程：
  • VaR(95%, 1D) = -{XX}% → {可接受(<2%) / 偏高(2-5%) / 危险(>5%)}
    (VIX高=VaR自动扩大)
  • 最大回撤预测：基于历史{12}个月 → 最坏情景 -{XX}%
  • VIX regime调整：当前VIX={XX.X} → {Low/Normal/Elevated/Fear}
    → 仓位上限从{XX}%调整为{XX}%
    (引用Macro Canvas VIX regime)
  • 组合相关性风险：
    - 与现有持仓(SPY/QQQ/其他)相关性={X.X}
    - 如果已持有{相关标的}，{标的}带来的增量分散化={高/低}
    (引用Macro Canvas跨资产关联)
  • 流动性风险：日均成交量 ${XX}M → 建仓{X}%需要{X}天 → {可接受/需分批}
  • 压力测试：
    - 2008式危机：跌 -{XX}%（参考 Beta×40%）
    - 2020式危机：跌 -{XX}%（参考 Beta×30%）
    - 2022式加息冲击：跌 -{XX}%（参考 Duration 效应）

🗳️ 投票：🟢 BULLISH(仓位可放大) / 🟡 NEUTRAL(标准仓位) / 🔴 BEARISH(限制仓位)（置信度 {XX}%）

💬 理由：「VIX={XX.X}{Regime}→仓位上限{XX}%。
              VaR=-{XX}%，最大回撤预测-{XX}%。
              组合相关性{X.X}→{好/不好}的分散化。
              引用Macro Canvas全维度数据。」
```

**关键原则**：
- "Risk is what's left over after you think you've thought of everything."
- VIX regime是仓位倍数的第一决定因素
- 不持仓也是一种持仓
- 永远设止损、永远有Plan B

---

## 🟢 ESG Screening — 附加分（不参与核心投票）

> ⚠️ **ESG是加分项，不是否决项。不达标不影响投票结果。**

```
ESG评分机制:
├── E (环境): 碳排放/清洁能源使用/废弃物管理
├── S (社会): 员工安全/供应链人权/社区关系
└── G (治理): 董事会独立性/高管薪酬合理性/股东权利

🟢 附加分规则:
   总分≥70/100 → ESG Bonus +1票 (仅影响最终推荐的倾向)
   总分<70 → 无影响 (不扣分)

⚠️ 注意: 有些优质企业(如油气、矿业)ESG天生低分，
          不应成为"不买好公司"的借口
```

---

## 委员会汇总输出格式（12人版）

每个标的的12人委员会分析完成后，输出**汇总矩阵**：

```
╔══════════════════════════════════════════════════════════╗
║  🗳️ {TICKER} — 12人投资委员会投票汇总              ║
║  📊 所有投票基于 Phase 0 Data Canvas                ║
╚══════════════════════════════════════════════════════════╝

┌──────────────────────────┬──────────────┬──────────────┬─────────────────┐
│ 委员                     │ 投票          │ 置信度        │ Data Canvas引用  │
├──────────────────────────┼──────────────┼──────────────┼─────────────────┤
│ Warren Buffett           │ 🟢 BULLISH   │ 88%           │ Earnings+Div     │
│ Charlie Munger           │ 🟢 BULLISH   │ 85%           │ Earnings质量     │
│ Ben Graham               │ 🟡 NEUTRAL   │ 55%           │ Earnings+Div     │
│ Ray Dalio                │ 🟢 BULLISH   │ 80%           │ VIX+Macro+利差   │
│ Cathie Wood              │ 🔴 STRONG_BUY│ 92%           │ TAM+Wright       │
│ Bill Ackman              │ 🟢 BULLISH   │ 78%           │ Earnings+WS      │
│ Stanley Druckenmiller    │ 🟢 BULLISH   │ 85%           │ VIX+Macro+WS     │
│ George Soros             │ 🟢 BULLISH   │ 75%           │ VIX+Macro        │
│ Paul Tudor Jones         │ 🟢 BULLISH   │ 72%           │ VIX+Macro+Cor    │
│ Jim Simons               │ 🟡 NEUTRAL   │ 55%           │ VIX+Correlation  │
│ Technical Analyst        │ 🟢 BULLISH   │ 78%           │ VIX+Volume       │
│ Risk Manager             │ 🟡 NEUTRAL   │ 58%           │ VIX+Macro+Cor    │
└──────────────────────────┴──────────────┴──────────────┴─────────────────┘

🏛️ 附加分: 🟢 ESG Bonus {达标(+1票) / 未达标(不影响)}

【委员会共识】：{X}/12 🟢看多 | {X}/12 🟡中性 | {X}/12 🔴看空
  → 共识强度：{强/偏多/分歧}

【主要分歧点】：
  ⚠️ Graham 觉得还不够便宜（P/E={XX} > 15，安全边际不足）
  ⚠️ Simons 量化模型在VIX={XX.X}{Regime}下可信度降低
  ⚠️ Risk Manager 认为仓位应受限于当前VIX regime

【ESG评估】：{达标/未达标} → {获得+1票bonus / 不影响}

【映射到五档评级】：
  → {X}/12看多 + Chokepoint评分{XX} + 六大脑偏多 + {🟢 ESG Bonus}
  → ┌─────────────┐
    │  强烈推荐    │  ← 🔴 深红背景色块
    └─────────────┘
```

---

## 验证要求（universal-agent-skill）

委员会分析完成后，**必须验证**：

```bash
# 验证1: 12位委员输出文件都存在
for agent in buffett munger graham dalio cathie_wood ackman druckenmiller soros jones simons technical risk; do
  ls -la knowledge/investment-brain/committee/{TICKER}_${agent}.md
  wc -l knowledge/investment-brain/committee/{TICKER}_${agent}.md
  # 预期: 文件存在, 行数 > 30行
done

# 验证2: 每位委员输出都包含必要章节
for file in knowledge/investment-brain/committee/{TICKER}_*.md; do
  grep -c "Data Canvas" $file
  grep -c "分析过程" $file
  grep -c "投票" $file
  grep -c "理由" $file
  # 预期: 每个grep返回 count >= 1
done

# 验证3: 委员会汇总矩阵已生成
ls -la knowledge/investment-brain/committee/{TICKER}_summary.md
# 预期: 文件存在, 包含12行投票记录
```

---

## 与其他模块的接口

| 输入来源 | 输出去向 | 说明 |
|---------|---------|------|
| **📊 Phase 0 Data Canvas** | 12位委员 | 🔴 强制依赖！每位委员引用分配的数据维度 |
| **ChokepointScanner** | 委员会分析 | Chokepoint评分作为输入背景 |
| **六大脑深度分析** | 委员会分析 | 六大脑信号作为委员参考（但不影响独立性） |
| **委员会汇总** | PortfolioManager | 12人投票矩阵作为终审输入之一（权重30%） |
| **🟢 ESG** | PortfolioManager | 附加分+1票bonus（不影响委员会投票结果） |

**重要原则**：
- 12位委员**独立投票**，不互相影响
- 每位委员**必须引用 Data Canvas** 中的客观数据
- 分歧点**必须标注**（最有alpha的信息往往在这里）
- ESG **不参与**核心投票，是附加分
- 委员会共识**不是简单多数**，而是加权汇总（置信度高的委员权重更高）

---

_最后更新: 2026-06-10 (v5.1 12人投资委员会 + Data Canvas 规范)_
_对标: ai-hedge-fund v3.0.1_
_作者: 沐沐 🖤 for 乔纳森大人_
