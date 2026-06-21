# 方法论白皮书 — Investment Brain New v5.0

> **核心哲学**：不是在分析数字，而是在理解数字背后的商业逻辑。知道**为什么分析** → 才知道**分析什么** → 才能知道**怎么解读**。

---

## 一、四大方法论源头

### 1.1 原六大脑框架（v1.0-v2.0）

**核心思想**：程序化信号输出，每个Agent输出结构化AgentSignal，包含methodology/step_by_step/formulas/assumptions四个方法论字段。

**六个Agent权重**：
| Agent | 权重 | 核心能力 |
|-------|------|---------|
| ValuationAgent | 30% | DCF/DDM/PE Band/EV-EBITDA/PEG/PB |
| FundamentalsAgent | 25% | 14维综合评分（100分制） |
| TechnicalsAgent | 20% | MACD/RSI/KDJ/布林带/ATR |
| SentimentAgent | 15% | VIX/Fear&Greed/分析师评级 |
| RiskManager | 10% | VaR/CVaR/止损/仓位管理 |

**局限**：缺行业深度，缺买入/卖出时机框架，缺护城河分析，缺供应链瓶颈视角。

### 1.2 SOIC价值链与护城河体系（Girish-git/investment-brain）

**核心思想**：寻找价值链中最具利润的节点（Most Profitable Node），通过护城河分类判断竞争优势可持续性。

**关键贡献**：
- **14种估值指标**（PEG阈值、SOTP、EV/tonne、Order Book/Mcap等）+ 行业估值矩阵（25+行业）
- **14种护城河类型**（转换成本/规模/专有资产/网络效应等）
- **再投资护城河 vs 遗产护城河**区分（ROIIC>15%且机会空间大 = 再投资型）
- **Stage Analysis**（Stan Weinstein四阶段）买入/卖出时机
- **Speed Breaker**逆向买入策略
- **19项法医红旗**反舞弊检查
- **8步行业轮动工作流**
- **14个行业深度模块**（银行/化工/医疗/能源/工业/消费/SaaS等）
- **价值链利润池定位**（航空：零件>航空；医药：制剂>API；保险：分销>制造）

**局限**：不是程序化Agent框架，是知识库，不能直接跑；缺宏观情绪；缺技术面量化指标。

### 1.3 Serenity Chokepoint 策略

**核心思想**：通过技术链深度研究，锁定巨头依赖度高、替代性弱的细分领域龙头，利用市场认知差获取超额收益。

**关键战绩**：
- 公开推荐35只股票，31只上涨，胜率88.6%
- AXT：12→70美元（InP衬底出口管制催化，6倍）
- 树莓派：发行价看多→两日涨90%→55%增长验证（华尔街共识14%）
- 英伟达：6美元拒绝→4500%+涨幅
- SIVE：19.6倍涨幅
- 组合年化收益4502%

**底层方法论**：Chokepoint = 巨头依赖度高 + 替代性弱 + 市场认知差 + 合规/出口卡点

**局限**：缺程序化框架，缺财务硬指标验证，缺风险管理。

### 1.4 industry-deep-driller v2.0 — 产业链图论量化

**核心思想**：不分析公司，只分析产业链。通过BOM反向拆解+市场集中度标注+图论量化，精准定位产业链中不可替代的瓶颈节点。

**关键能力**：
- **产业链映射**：从终端产品向下逐层分解至底层材料/工艺
- **BOM拆解与节点注册**：标注每个组件的成本占比、标准化程度、技术壁垒
- **节点CR1集中度标注**：单源垄断(≥80%) / 寡头(≥50%) / 集中(≥30%) / 分散(<30%)
- **图论量化排名**：介数中心性×0.40 + CR1×0.35 + 技术壁垒×0.15 + 稀缺度×0.10
- **四Agent并发工作流**：BOM拆解员→市场集中度审计员→财务验证员→图论评级员

**局限**：不知道「谁控制这个瓶颈」——这正是 new-investment-brain v5.0 的职责。

**v5.0 集成**：industry-deep-driller 输出瓶颈节点 → new-investment-brain 映射上市公司 → 深度投资分析。

---

## 二、四位一体融合框架：「产业链→瓶颈→财务→验证」

### 2.1 战略筛选层：Chokepoint诊断

不再是泛泛地分析整条价值链，而是对每个行业强制执行四维穿透：

| 维度 | 评估内容 | 量化方式 | 权重 |
|------|---------|---------|------|
| **巨头依赖度** | 是否为NVIDIA/TSMC/苹果等不可或缺的供应商 | 客户集中度CR3 + 巨头收入占比 | 30% |
| **替代成本** | 巨头换掉它需要的时间/合规/资金成本 | 切换周期(月) + 合规壁垒级 + 重置成本/市值 | 25% |
| **市场认知差** | 华尔街是否低估其增速 | 实际增速vs共识增速差 + 卖方覆盖率 | 25% |
| **合规卡点** | 是否涉及出口管制/国家安全/核心专利 | 管制清单命中 + 专利数 + 资质许可数 | 20% |

**信号强度映射**：
| 总分 | 信号强度 | 含义 |
|------|---------|------|
| ≥80 | Extreme | 不可替代瓶颈，战略重仓 |
| 60-79 | Strong | 强瓶颈，优先配置 |
| 40-59 | Moderate | 中等瓶颈，观察等待催化 |
| 20-39 | Weak | 弱瓶颈，不作为核心逻辑 |
| <20 | None | 非瓶颈，回归传统分析 |

### 2.2 财务穿透层：硬指标验证

Chokepoint不能仅停留在"故事"层面，必须通过财务数据进行无情验证：

| 指标 | 阈值 | 验证目的 | 来源 |
|------|------|---------|------|
| 毛利率 | >50%或上升通道 | 定价权验证 | financial-analysis |
| ROIIC | >15% | 区分再投资vs遗产护城河 | SOIC |
| CFO/PAT | >1.0 | 现金流真实性 | financial-analysis |
| 14项标准化打分 | ≥80(强推)/≥60(准推) | 综合财务质量 | financial-analysis |
| 净营业周期 | 负值或改善中 | 产业链地位 | financial-analysis |
| ROE杜邦分解 | 净利率驱动(好) vs 杠杆驱动(差) | 盈利质量 | financial-analysis |

**关键洞察**：财务硬指标不是一刀切门槛，而是**分层推荐**的一维输入——Chokepoint强度可以弥补财务分数（瓶颈企业往往还在投入期），但必须配合技术面确认。

### 2.3 风险与安全边际层

| 工具 | 用途 | 来源 |
|------|------|------|
| Speed Breaker评估 | 短期负面事件是否为非实质性损害 | SOIC |
| 19项法医红旗 | 反舞弊审计 | SOIC |
| 12个卖出触发 | 系统性卖出纪律 | SOIC |
| Stage Analysis | 技术面阶段判断（绝不买Stage 4） | Stan Weinstein |
| 信息瀑布追踪 | 内幕→机构→媒体→散户 | SOIC |
| VaR/CVaR | 量化风险敞口 | 原RiskManager |

---

## 三、新增模块详解

### 3.1 MoatAnalyzer（护城河分析器）

**14种护城河类型**：
1. 转换成本（Switching Costs）
2. 规模经济（Scale）
3. 专有资产（Proprietary Assets）
4. 学习曲线（Learning Curve）
5. 牌照/许可（License）
6. 口味/品牌（Taste/Brand）
7. 先发优势（Early Mover）
8. 客户锁定（Customer Lock-in）
9. 网络效应（Network Effects）
10. "成为动词"（Becoming a Verb）
11. 地理位置（Location）
12. 纵向整合（Integration）
13. 最低成本（Lowest Cost）
14. 生态锁定（Ecosystem Lock-in）

**关键区分**：
- **再投资护城河**：高ROCE + 高ROIIC + 大增量机会 → PI Industries(ROIIC 15%+)
- **遗产护城河**：高ROCE + 低ROIIC + 无增量机会 → Ambika Cotton(ROIIC 7%)

**CDMO锁定6层模型**：
1. 监管验证（Regulatory Validation）
2. 工艺诀窍（Process Know-how）
3. 失败成本（Cost of Failure）
4. 多年合同（Multi-year Contracts）
5. NDA文档（NDA Documentation）
6. 关系资本（Relationship Capital）

**护城河信号追踪**：
- 强化信号：市场份额↑、定价权↑、客户粘性↑、新壁垒涌现
- 弱化信号：技术替代、客户自研、监管变化、毛利率↓

### 3.2 ChokepointScanner（瓶颈扫描器）

**输入**：标的股票代码 + 行业/供应链上下文

**输出**：
```json
{
  "ticker": "AXTI",
  "chokepoint_score": 82,
  "signal_strength": "Extreme",
  "dimensions": {
    "giant_dependency": {"score": 90, "detail": "InP衬底全球3大供应商之一，NVIDIA光模块依赖"},
    "replacement_cost": {"score": 85, "detail": "切换周期18-24月，合规重置成本$200M+"},
    "cognitive_gap": {"score": 75, "detail": "华尔街增速共识25% vs 实际产能释放55%"},
    "regulatory_chokepoint": {"score": 78, "detail": "InP已列入出口管制EAR99，国产替代遥遥无期"}
  },
  "supply_chain_position": "上游",
  "key_customers": ["NVIDIA", "Broadcom", "Intel"],
  "recent_catalysts": ["出口管制升级", "800G光模块放量"],
  "risk_flags": []
}
```

**与SOIC价值链对接**：
- 自动匹配SOIC行业模块中的价值链利润池定位
- 输出"Most Profitable Node"判断（此标的是否处于价值链最赚钱环节）

---

## 四、方法论融合映射表

| 能力 | 原六大脑 | SOIC | Serenity | financial-analysis | 融合后位置 |
|------|---------|------|----------|-------------------|-----------|
| DCF/DDM/PE估值 | ✅ | | | | ValuationAgent |
| 14种估值指标+行业矩阵 | | ✅ | | | ValuationAgent |
| 稀缺性溢价估值 | | | ✅ | | ValuationAgent |
| 14维基本面评分 | ✅ | | | | FundamentalsAgent |
| 杜邦分解+CFO/PAT | | | | ✅ | FundamentalsAgent |
| ROIIC(增量资本回报) | | ✅ | | | FundamentalsAgent |
| 14项标准化打分 | | | | ✅ | FundamentalsAgent |
| 19项法医红旗 | | ✅ | | | RiskManager |
| RSI/MACD/布林带 | ✅ | | | | TechnicalsAgent |
| Stage Analysis | | ✅ | | | TechnicalsAgent |
| CANSLIM | | ✅ | | | TechnicalsAgent |
| 瓶颈突破形态 | | | ✅ | | TechnicalsAgent |
| VIX/Fear&Greed | ✅ | | | | SentimentAgent |
| 行业RS/RRG轮动 | | ✅ | | | SentimentAgent |
| 信息瀑布追踪 | | ✅ | | | SentimentAgent |
| VaR/CVaR/止损 | ✅ | | | | RiskManager |
| 12卖出触发 | | ✅ | | | RiskManager |
| Speed Breaker评估 | | ✅ | | | RiskManager |
| 14种护城河分类 | | ✅ | | | MoatAnalyzer |
| 再投资vs遗留护城河 | | ✅ | | | MoatAnalyzer |
| CDMO锁定6层 | | ✅ | | | MoatAnalyzer |
| 四维Chokepoint诊断 | | | ✅ | | ChokepointScanner |
| 市场认知差量化 | | | ✅ | | ChokepointScanner |
| 价值链利润池定位 | | ✅ | | | PortfolioManager |
| 大象故事多视角校验 | | ✅ | | | PortfolioManager |
| 组合凸性(Chokepoint≥30%) | | | ✅ | | PortfolioManager |
| 防幻觉验证闸门 | | | | | universal-agent-skill |
| 产业链映射+BOM拆解 | | | | | 🆕 industry-deep-driller |
| 节点CR1集中度标注 | | | | | 🆕 industry-deep-driller |
| 图论瓶颈量化(介数中心性/结构洞) | | | | | 🆕 ChokepointScanner(增强) |
| 节点→公司映射引擎 | | | | | 🆕 v5.0 MappingEngine |
| 全球七地市场路由 | | | | | 🆕 v5.0 GlobalRouter |
| 持久化知识归档 | | | | | fulltime-knowledge-butler |
| ragflow知识库同步 | | | | | 🆕 ragflow-skill |
| 六大脑自进化(误判自检) | | | | | 🆕 self-improving |
| 跨会话记忆(三锚点) | | | | | 🆕 mem0 |
| 产业链模板扩展 | | | | | 🆕 openclaw-project-iteration |
| Agent编排(三模式切换) | | | | | 🆕 universal-agent-skill |

---

## 五、v5.0 双技能联动哲学

```
industry-deep-driller  v2.0          new-investment-brain  v5.0
┌─────────────────────────┐      ┌─────────────────────────────┐
│  找 WHAT                 │      │  投 WHO & HOW MUCH           │
│                          │ JSON │                              │
│  产业链映射              │─────→│  节点→公司映射引擎            │
│  BOM拆解 + 节点注册      │      │  六大脑深度分析(并发)         │
│  节点CR1集中度标注       │      │  12人委员会投票(并发)         │
│  图论量化 + 瓶颈排名     │      │  五档分级推荐 + 全球仓位      │
│                          │      │                              │
│  输出: ChokepointNode[]  │      │  输出: CandidateStock[]      │
│        + dependency_graph│      │        + V5FinalRecommendation│
└─────────────────────────┘      └─────────────────────────────┘
```

---

## 六、哲学原则

1. **商业逻辑驱动，而非数字堆砌**（financial-analysis核心）
2. **寻找价值链中最赚钱的节点，而非最显眼的公司**（SOIC核心）
3. **锁定巨头依赖度高、替代性弱的细分领域龙头**（Serenity核心）
4. **不是在分析数字，而是在理解数字背后的商业逻辑**（所有方法论的共识）
5. **不要成为被迫的长期投资者**（SOIC核心信条）
6. **每个信号必须有Proof-of-Work验证**（universal-agent-skill核心）
7. **知识必须持久化，不依赖短期记忆**（fulltime-knowledge-butler核心）
8. **🆕 先找命门再找公司：产业链瓶颈发现是投资发现的前置条件**（v5.0核心哲学）
9. **🆕 技能不是静态的：六大脑在每次分析中自我进化、记忆偏好、积累模板**（v5.0自进化哲学）
