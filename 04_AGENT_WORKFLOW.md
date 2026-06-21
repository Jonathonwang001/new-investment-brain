# Agent 执行与防遗忘规范 — Agent Workflow v5.0

> **核心原则**：DO NOT FAKE EXECUTION. STATEMENTS WITHOUT EVIDENCE ARE TREATED AS LIES.
> — universal-agent-skill
> **v5.0 核心创新**：三模式编排（全局/标准/轻量）+ industry-deep-driller 链式联动 + 六大脑自进化

---

## 一、v5.0 三模式编排（Mode Orchestration）

universal-agent-skill 在 Pipeline 启动时自动判定模式：

```
用户请求分析
│
├─ 🌐 全局模式关键词: 产业链/卡脖子/瓶颈 + 投资/标的 + chokepoint/bottleneck
│   → v5.0 全局模式：industry-deep-driller → investment-brain
│
├─ 📊 标准模式关键词: 分析/深度/评估 + 具体标的 + 无产业链词
│   → v5.0 标准模式：六大脑 + 12人委员会全开
│
├─ ⚡ 轻量模式关键词: 快速/简要/扫一眼 + 标的
│   → v5.0 轻量模式：仅三核心 Agent（估值/基本面/技术面）
│
└─ 默认 → 📊 标准模式
```

---

## 🌐 二、全局模式：industry-deep-driller → investment-brain

### 2.1 Step 0 — 模式判定 + 准备

```
universal-agent-skill 模式判定:
  ├─ 关键词检测: "产业链" AND ("卡脖子" OR "瓶颈" OR "chokepoint" OR "bottleneck")
  ├─ → 判定: 🌐 全局模式 (sequential_chain)
  └─ → 输出编排配置:
      {
        "mode": "v5_global",
        "steps": [
          {"step": 1, "skill": "industry-deep-driller", "mode": "pure_drilling"},
          {"step": 2, "skill": "new-investment-brain", "mode": "mapping"},
          {"step": 3, "skill": "new-investment-brain", "mode": "six_brains_concurrent"},
          {"step": 4, "skill": "new-investment-brain", "mode": "committee_concurrent"},
          {"step": 5, "skill": "new-investment-brain", "mode": "portfolio_decision"}
        ]
      }

mem0 锚点1+2 检查:
  ├─ 读取用户偏好（行业偏好/风险容忍度/持仓限制）
  └─ 读取数据源状态（哪些API当前可用）
```

### 2.2 Step 1 — industry-deep-driller 🔴纯钻探

**调用**：
```bash
cd ~/.qclaw/skills/industry-deep-driller
python3 scripts/reverse_drill_agent.py \
  --mode pure_drilling \
  --industry "AI GPU" \
  --top_n 10 \
  --output chokepoint_nodes.json
```

**或通过 universal-agent-skill 触发**（推荐方式）。

**验证**：
```
Verify: chokepoint_nodes.json 存在 AND len(nodes) >= 3
  → Pass? 输出 pipeline_id, step=1, status=completed
  → Fail? 输出 error, 通知主人 industry-deep-driller 不可用
```

**输出**：`chokepoint_nodes.json` — 瓶颈节点排名列表（含CR1、betweenness、tier、suppliers[]）

### 2.3 Step 2 — 节点→公司映射引擎

**读取**：`chokepoint_nodes.json`

**执行**：
```python
# 对每个 T0/T1 节点，映射 suppliers[] → CandidateStock[]
candidates = []
for node in chokepoint_nodes:
    if node.tier in ["T0", "T1"]:
        for supplier in node.suppliers:
            if supplier.ticker not in ["unlisted", "private", ""]:
                if supplier.market_share * supplier.total_market_size >= 100_000_000:  # 市值>$100M
                    candidates.append(map_supplier_to_stock(supplier, node))

# 全球市场路由
for candidate in candidates:
    routing = get_market_routing(candidate.ticker, candidate.market)
    candidate.primary_data_source = routing["primary"]
    candidate.proxy_required = routing["proxy"]
```

**过滤**：
- 去除非上市公司、微盘股（<$100M）
- 去除已在破产/退市流程中的公司
- 标记 ADR / 外国公司 → 风险提示

**验证**：
```
Verify: len(candidates) >= 1 AND 每个候选有 ticker + name + market
  → Pass? 继续 Step 3
  → Fail? 通知主人: "未找到可投资标的，跳过"
```

### 2.4 Step 3 — 六大脑并发分析（逐标的）

**执行**：对每个 CandidateStock，并发执行 6 个 Agent。

```
并发编排 (6 Agents):
  ┌─────────────────────────────────────────────┐
  │  ValuationAgent     ┊  FundamentalsAgent    │  (并发)
  │  TechnicalsAgent    ┊  SentimentAgent       │  (并发)
  │  RiskManager        ┊  MoatAnalyzer         │  (并发)
  └─────────────────────────────────────────────┘
  ↓
  汇总 → SixBrainDeepAnalysis
```

**输入**：每个候选的 ticker + 关联的 ChokepointNode 信息

**验证**：
```
Verify: 每个 Agent 输出包含 method_step_by_step + evidence + conclusion
  → Pass? 六大脑分析完成
  → Fail? 对应 Agent 重试 1 次，超时报错
```

### 2.5 Step 4 — 12人委员会并发投票（逐标的）

**执行**：对每个 CandidateStock，并发执行 11 位委员。

```
并发编排 (12 Members):
  ┌─────────────────────────────────────────────┐
  │  Buffett    ┊  Munger    ┊  Graham          │  (并发)
  │  CathieWood ┊  Burry     ┊  RayDalio        │  (并发)
  │  Technical  ┊  Earnings  ┊  WallStreet      │  (并发)
  │  Macro      ┊  Dividend                        │  (并发)
  └─────────────────────────────────────────────┘
  ↓
  汇总 → CommitteeConsensus
```

**输入**：每个候选的完整 SixBrainDeepAnalysis

**验证**：
```
Verify: 每个委员输出包含 position + reasoning + confidence
  → Pass? 委员会投票完成
  → Fail? 对应委员缺席，按已知票计算
```

### 2.6 Step 5 — PortfolioManager 最终决策

```python
for candidate in candidates:
    recommendation = classify_recommendation_v5(
        six_brain_signals = candidate.analysis.signals,
        committee_consensus = candidate.analysis.committee,
        chokepoint_strength = candidate.chokepoint.bottleneck_score,
        three_moment_type = determine_moment_type(candidate),
        graph_betweenness = candidate.chokepoint.betweenness_centrality
    )
    candidate.final_recommendation = recommendation
```

**仓位分配**：
```
Top候选仓位分配（示例）:
  - 🔴 强烈推荐 T0: 5-8% × min(3, len(candidates))
  - 🟠 核心推荐 T1: 3-5% × min(5, len(candidates))
  - 🟡 准推荐 T2: 1-3%
  - Chokepoint标的合计: ≥ 30% 组合权重（Serenity原则）
```

### 2.7 自进化触发（全局模式特有）

```
Step 1 完成 → ragflow-skill: 同步产业链图谱到知识库
Step 3 完成 → self-improving: 记录分析快照 + 误判追踪
Step 5 完成 → openclaw-project-iteration: 评估是否扩展模板库
              mem0 锚点3: 写入结论 + 3个月回测标记
```

---

## 📊 三、标准模式：六大脑 + 12人委员会全开

### 3.1 Step 0 — 模式判定

```
universal-agent-skill 模式判定:
  └─ 关键词: 分析/深度/评估 + 具体标的（无产业链词）
      → 判定: 📊 标准模式 (concurrent_full)
```

### 3.2 Step 1 — ChokepointScanner 快速扫描

```python
chokepoint = ChokepointScanner.scan(ticker)
# 输出: 四维诊断 + ChokepointScore
# 不调用 industry-deep-driller（已有具体 ticker）
```

### 3.3 Step 2 — 六大脑并发 + 12人委员会并发

```
并发编排:
  ┌─────────────────────────────────────────────┐
  │  6 Agents (并发) → SixBrainDeepAnalysis     │
  │  12 Members (并发) → CommitteeConsensus    │
  └─────────────────────────────────────────────┘
  ↓
  PortfolioManager 汇总
```

### 3.4 Step 5 — 最终推荐 + 自进化触发

同全局模式 Step 5，区别在于 Chokepoint 输入来自 Scanner 而非钻探。

---

## ⚡ 四、轻量模式：三核心 Agent

### 4.1 Step 0 — 模式判定

```
universal-agent-skill 模式判定:
  └─ 关键词: 快速/简要/扫一眼 + 标的
      → 判定: ⚡ 轻量模式 (concurrent_lightweight)
```

### 4.2 执行

```
仅激活 3 个核心 Agent（委员会休眠）:
  ValuationAgent + FundamentalsAgent + TechnicalsAgent
```

**输出简报**：
```
{TICKER} 快速评估
────────────────────────────────
Chokepoint: [强度] | 财务分: [XX/100] | 技术面: [Stage X]
推荐: [🔴/🟠/🟡/🔵/⚪] | 仓位: [X%]
核心逻辑: [一句话]
────────────────────────────────
[05/30 HH:MM]
```

---

## 五、防幻觉验证闸门（所有模式共有）

### 5.1 验证方法速查

| 动作类型 | 必须验证 | 工具 |
|---------|---------|------|
| industry-deep-driller 输出 | `chokepoint_nodes.json` 存在 + len(nodes)>=3 | shell |
| 数据获取 | 打印前3条记录确认结构 | inline |
| 财务计算 | 交叉验证2种以上方法 | inline |
| Chokepoint评分 | 每个维度引用具体数据源 | inline |
| 六大脑输出 | 每 Agent 含 method/step_by_step/evidence/conclusion | validate |
| 报告生成 | 运行 validate_report_structure.py | shell |
| 文件写入 | 读取前5行确认内容 | file |

### 5.2 禁止的幻觉行为

1. **Phantom Data**: 说"毛利率58%"但无原始数据来源
2. **Phantom Analysis**: 说"已完成DCF分析"但未实际计算
3. **Phantom Chokepoint**: 说"Chokepoint Strong"但未执行四维诊断
4. **Phantom Score**: 说"财务打分82分"但未逐项计算14项
5. **Phantom Signal**: 说"技术面BULLISH"但未检查RSI/MACD/Stage

### 5.3 State Hashing

维护 `state.json`：

```json
{
  "pipeline_id": "v5-global-YYYYMMDD-NNN",
  "mode": "v5_global",
  "steps_completed": [
    {
      "step_id": 1,
      "action": "industry-deep-driller.pure_drill",
      "output_file": "chokepoint_nodes.json",
      "verified": true,
      "data_sources": ["serper", "web_fetch"],
      "timestamp": "[MM/DD HH:MM]"
    },
    {
      "step_id": 2,
      "action": "mapping_engine.map_to_stocks",
      "output_count": 8,
      "verified": true,
      "timestamp": "[MM/DD HH:MM]"
    }
  ]
}
```

---

## 六、持久化知识管理

### 6.1 知识归档协议

| 归档内容 | 格式 | 位置 |
|---------|------|------|
| 标的研究报告 | Markdown | `knowledge/investment-brain/tickers/{TICKER}.md` |
| Chokepoint诊断 | JSON + Markdown | `knowledge/investment-brain/chokepoints/{TICKER}.md` |
| 产业链图谱 | JSON | `knowledge/investment-brain/chains/{INDUSTRY}.json` |
| 财务打分 | Markdown | `knowledge/investment-brain/scorecards/{TICKER}.md` |
| 护城河分析 | Markdown | `knowledge/investment-brain/moats/{TICKER}.md` |
| 教训与迭代 | Markdown | `knowledge/investment-brain/learnings.md` |
| 模板扩展待审 | Markdown | `knowledge/investment-brain/template-expansion-pending.md` |

### 6.2 v5.0 新增归档

```
industry-deep-driller 输出（首次分析某产业链时）:
  ├─ chokepoint_nodes.json → knowledge/investment-brain/chains/{INDUSTRY}.json
  ├─ dependency_graph.json → knowledge/investment-brain/chains/{INDUSTRY}_graph.json
  └─ 触发 ragflow-skill: 同步到 "investment-chokepoint-knowledge" 数据集

v5.0 映射结果:
  └─ CandidateStock[] → knowledge/investment-brain/v5-mappings/{INDUSTRY}_candidates.json
```

### 6.3 启动知识管家仪式（每次新会话）

```
Step 1: 定位知识库 → knowledge/investment-brain/
Step 2: 读索引 → _index.md
Step 3: 读 mem0 锚点 → 偏好 + 数据源状态 + 未完成回测
Step 4: 如是产业链分析 → 读对应 chains/{INDUSTRY}.json
Step 5: 如是标的分析 → 读对应 tickers/{TICKER}.md + learnings.md
Step 6: 提取既有结论 → 然后开始本次分析
```

---

## 七、六大脑自进化集成

| 触发位置 | 方法论 | 具体动作 |
|---------|--------|---------|
| Step 0 | mem0 锚点1+2 | 读取偏好 + 数据源状态 |
| Step 0 | universal-agent-skill | 模式判定（全局/标准/轻量） |
| Step 3 | self-improving | 记录六大脑分析快照 |
| Step 3 | self-improving | 3个月后自动回测触发 |
| Step 1(全局) | ragflow-skill | 同步产业链图谱到知识库 |
| Step 5(全局) | openclaw-project-iteration | 评估产业链模板扩展 |
| Step 5 | mem0 锚点3 | 写入分析结论 |
| 输出 | LLM wiki | 格式校验（表格≥60%、来源标注） |
| 主人纠正 | self-improving | 误判+1 → 更新LEARNINGS.md |
| 每周一 09:00 | self-improving 自检 | 误判率>10%→升级阈值 |

---

_版本: v5.0 | 更新: 2026-05-30 | 关联: industry-deep-driller v2.0 + universal-agent-skill_