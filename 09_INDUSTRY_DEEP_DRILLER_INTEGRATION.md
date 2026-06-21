# Industry Deep Driller 集成协议 — v5.0 双技能联动

> **核心哲学**：industry-deep-driller 找瓶颈（WHAT），new-investment-brain 投瓶颈（WHO & HOW MUCH）。
> 两条技能通过结构化协议交接，输出从产业链到投资标的的完整分析报告。

---

## 一、双技能分工

| 维度 | industry-deep-driller (🔴纯钻探) | new-investment-brain v5 (投资决策) |
|------|-------------------------------|----------------------------------|
| **核心问题** | "这条产业链的命门在哪？" | "命门被谁控制？值不值得投？" |
| **输出** | 瓶颈节点排名 + 图论指标 | 可投标的清单 + 投资推荐 + 仓位 |
| **方法论** | BOM拆解 → CR1标注 → 图论量化 | 六大脑 + 12人委员会 + Chokepoint |
| **关注点** | 供应链结构、技术壁垒、集中度 | 估值、财务、技术面、情绪、风险 |
| **不做的** | 财务分析、投资建议、估值 | 不重复做产业链拆解（接收结构化输入） |

---

## 二、输入协议（接收 industry-deep-driller 的输出）

### 2.1 结构化 JSON 格式

industry-deep-driller 纯钻探模式输出的瓶颈节点，由 `find_chokepoints.py` 生成：

```json
{
  "analysis_metadata": {
    "source": "industry-deep-driller v2.0",
    "mode": "pure_drilling",
    "industry": "AI GPU",
    "analysis_date": "2026-05-30",
    "total_nodes_analyzed": 25,
    "chokepoint_nodes_found": 8
  },
  "chokepoint_nodes": [
    {
      "node_id": "euv_photoresist",
      "node_name": "EUV光刻胶",
      "tier": "T0",
      "bottleneck_score": 0.87,
      "betweenness_centrality": 0.92,
      "cr1": 0.85,
      "structural_hole_constraint": 0.05,
      "tech_barrier_score": 0.90,
      "scarcity_score": 0.78,
      "bom_level": 4,
      "bom_path": ["H100 GPU", "EUV光刻", "光刻材料", "光刻胶"],
      "suppliers": [
        {"name": "JSR Corporation", "market_share": 0.35, "ticker": "4185.T", "market": "JP"},
        {"name": "TOK", "market_share": 0.20, "ticker": "unlisted", "market": "JP"},
        {"name": "Shin-Etsu Chemical", "market_share": 0.15, "ticker": "4063.T", "market": "JP"},
        {"name": "DuPont", "market_share": 0.10, "ticker": "DD", "market": "US"}
      ],
      "certification_barriers": [
        "ASML EUV 认证周期 3-5 年",
        "TSMC 供应商认证 ≥18 个月"
      ],
      "alternative_paths": [],
      "is_standardized": false,
      "customization_level": 9,
      "patent_count_estimated": 1200
    }
  ],
  "dependency_graph": {
    "format": "networkx JSON node-link",
    "path": "output/ai_gpu_chain.json"
  }
}
```

### 2.2 必选字段

每个 `chokepoint_node` 必须包含：

| 字段 | 类型 | 含义 | 用途 |
|------|------|------|------|
| `node_name` | string | 瓶颈节点名称 | 搜索上市公司 |
| `tier` | string | T0/T1/T2/T3 | 筛选优先级 |
| `bottleneck_score` | float | 综合瓶颈评分 | 排序用 |
| `betweenness_centrality` | float | 图论介数中心性 | 瓶颈客观量化 |
| `cr1` | float | 市场集中度 | 垄断程度 |
| `suppliers` | array | 供应商列表(含ticker) | **核心：映射上市公司** |
| `bom_path` | array | BOM层级路径 | 理解产业位置 |
| `is_standardized` | bool | 是否标准化 | 跳过无价值节点 |

### 2.3 降级输入（industry-deep-driller 不可用时）

当无法调用 industry-deep-driller 脚本时，使用文本协议：

```markdown
## industry-deep-driller 输出（文本降级）

### 瓶颈节点排名
1. **EUV光刻胶** T0 | 评分 0.87 | CR1: 85%
   - 供应商: JSR (4185.T, 35%), TOK (未上市, 20%), Shin-Etsu (4063.T, 15%)
2. **InP衬底** T0 | 评分 0.82 | CR1: 80%
   - 供应商: AXT (AXTI, 33%), Sumitomo Electric (5802.T, 30%)
...
```

---

## 三、节点→公司映射引擎

### 3.1 映射规则

```
输入: ChokepointNode (含 suppliers[])
输出: CandidateStock[]

规则:
├─ 规则1: CR1 ≥ 80% → 锁定 suppliers[0]（唯一或近乎唯一供应商）
├─ 规则2: 50% ≤ CR1 < 80% → 锁定 Top 2 suppliers
├─ 规则3: CR1 < 50% → 锁定 Top 3 suppliers
└─ 过滤:
    ├─ 跳过 ticker == "unlisted" 或 "private"
    ├─ 跳过市值 < $100M 的微盘股（流动性风险）
    ├─ 跳过已在破产/退市流程中的公司
    └─ 标记 "is_adr" = True（外国公司在美上市）
```

### 3.2 全球市场路由

```python
# 根据 ticker 后缀判断交易所和最佳数据源
MARKET_ROUTING = {
    # 美股（无后缀或特殊处理）
    "US":  {"suffixes": [""],     "primary": "Finnhub",     "fallback": "Yahoo Finance", "proxy": True},
    # A股
    "CN":  {"suffixes": [".SZ", ".SH"], "primary": "a-stock-data", "fallback": "AKShare", "proxy": False},
    # 港股
    "HK":  {"suffixes": [".HK"],  "primary": "AKShare",     "fallback": "Finnhub",      "proxy": False},
    # 日股
    "JP":  {"suffixes": [".T"],   "primary": "Yahoo Finance","fallback": "Finnhub",      "proxy": True},
    # 韩股
    "KR":  {"suffixes": [".KS", ".KQ"], "primary": "Yahoo Finance","fallback": "Finnhub","proxy": True},
    # 台股
    "TW":  {"suffixes": [".TW", ".TWO"],"primary": "Yahoo Finance","fallback": "Finnhub","proxy": True},
    # 欧股
    "EU":  {"suffixes": [".DE", ".PA", ".L", ".MI", ".AS", ".MC", ".SW"],
            "primary": "Yahoo Finance","fallback": "Finnhub",      "proxy": True},
}

# 代理规则（遵守 MEMORY.md 网络配置）
# 🇨🇳 国内数据源 → 清除代理直连
# 🌍 海外数据源 → 检测全局代理状态，自动决定
```

### 3.3 外国公司在美上市检测

部分瓶颈环节的实际公司注册在海外但在美股有 ADR：

| 信号 | 含义 | 数据来源 |
|------|------|---------|
| ISIN 非 US 开头 | 外国注册公司 | Yahoo Finance profile |
| 有 .T / .DE 等同名股票 | 多地上市 | 搜索验证 |
| SEC 文件为 20-F（非10-K） | 外国发行人 | SEC EDGAR |

**标记**: `is_foreign_listed_on_us: true` → 在报告中明确提示流动性/汇率/ADR溢价风险。

---

## 四、Pipeline 调用流程

### 4.1 完整流程（v5.0 全局模式）

```
用户请求: "分析 {行业/产品} 产业链的 Chokepoint 投资机会"

Step 0: 技能识别（universal-agent-skill）
  ├─ 检测关键词: 产业链/卡脖子/瓶颈/chokepoint + 投资/标的
  ├─ → 触发 v5.0 全局模式
  └─ → 链式调用: industry-deep-driller → new-investment-brain

Step 1: 产业链钻探（industry-deep-driller 🔴纯钻探模式）
  ├─ 产业链映射 → BOM拆解 → 节点CR1 → 图论量化
  ├─ 输出: chokepoint_nodes.json + dependency_graph.json
  └─ ⏱ 预计耗时: 3-5分钟

Step 2: 节点→公司映射（new-investment-brain v5 映射引擎）
  ├─ 读取 chokepoint_nodes.json
  ├─ 对每个 T0/T1 节点，映射 suppliers[] → CandidateStock[]
  ├─ 过滤: 去除非上市公司、微盘股
  └─ ⏱ 预计耗时: 1-2分钟

Step 3: 逐标的深度分析（六大脑 + 12人委员会，并发执行）
  ├─ 对每个 CandidateStock，并发执行:
  │   ├─ 六大脑深度分析（6 Agents 并行）
  │   └─ 12人投资委员会投票（12 Members 并行）
  ├─ 排序: 按综合推荐分数
  └─ ⏱ 预计耗时: 5-10分钟

Step 4: 组合建议（PortfolioManager）
  ├─ 四维加权: 六大脑30% + 委员会30% + Chokepoint25% + 时刻15%
  ├─ 仓位分配: Chokepoint标的 ≥ 30% 组合
  └─ ⏱ 预计耗时: 1分钟

Step 5: 输出最终报告
  ├─ 板块一: 产业链瓶颈全景（来源: industry-deep-driller）
  ├─ 板块二: 可投标的清单（来源: 映射引擎）
  ├─ 板块三: 逐标的深度分析（来源: 六大脑+委员会）
  ├─ 板块四: 组合建议 + 仓位分配
  └─ 板块五: 风险提示 + 数据来源 Proof-of-Work
```

### 4.2 标准模式（已知标的，非产业链）

```
用户请求: "用 new-investment-brain 分析 AAPL"

→ 跳过 Step 1（不调用 industry-deep-driller）
→ 直接 Step 2-5（已有ticker，无需映射）
→ Agent编排: 六大脑并行 + 委员会并行
```

### 4.3 轻量模式（时间敏感/快速评估）

```
用户请求: "快速评估 NVDA"

→ 仅: 估值Agent + 基本面Agent + 技术面Agent
→ 委员会休眠
→ 输出简版: Chokepoint强度 | 财务分 | 技术面 | 推荐 | 仓位
```

---

## 五、报告融合规范

### 5.1 来源标注

最终报告必须明确标注哪些内容来自 industry-deep-driller：

```markdown
> 📊 产业链数据来源: industry-deep-driller v2.0 🔴纯钻探模式 [05/30 13:00]
> 📈 投资分析来源: new-investment-brain v5.0 六大脑+12人委员会
```

### 5.2 报告结构模板

```markdown
# {行业}产业链 Chokepoint 投资分析报告
**日期**: YYYY-MM-DD | **模式**: v5.0 全局模式

## 📊 一、产业链瓶颈全景 [来源: industry-deep-driller]
（BOM拆解树 + CR1标注 + 图论排名）

## 🔗 二、可投标的清单 [来源: 映射引擎]
| 瓶颈节点 | Tier | 公司 | Ticker | 市场 | 市值 | 垄断地位 |
|---------|------|------|--------|------|------|---------|

## 🧠 三、逐标的深度分析 [来源: 六大脑+委员会]
（每个标的完整的六大脑分析 + 12人委员会投票）

## 📋 四、投资建议
（五档分级推荐 + 仓位 + 止损 + 催化时间表）

## ⚠️ 五、风险提示
（全球市场特有风险: ADR溢价/汇率/流动性/时区）

## 🔍 六、数据来源 Proof-of-Work
（所有数据来源，区分 industry-deep-driller vs investment-brain）
```

---

## 六、自进化触发点

| 触发位置 | 方法论 | 动作 |
|---------|--------|------|
| Step 1 完成 | ragflow-skill | 同步产业链图谱到知识库 |
| Step 3 完成 | self-improving | 记录分析结论+3个月回测标记 |
| Step 4 完成 | openclaw-project-iteration | 评估是否扩展模板库 |
| Step 5 完成 | mem0 | 写入偏好+数据源状态+分析结论 |
| 全流程 | universal-agent-skill | Agent编排决策+状态追踪 |
| 输出 | LLM wiki | 遵循 SCHEMA.md 格式规范 |

---

_版本: v1.0 | 创建: 2026-05-30 | 关联: new-investment-brain v5.0 + industry-deep-driller v2.0_