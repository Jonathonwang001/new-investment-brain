# 六大脑自进化系统 — Self-Evolving Brains v5.0

> **核心原则**：这个 skill 不是静态的。六条方法论像器官一样长在决策流的每个节点，让它会自我反思、记忆偏好、扩展模板、同步知识。
>
> **设计理念**：来自 industry-deep-driller v2.0 的六大脑体系，适配 new-investment-brain 的投资决策场景。

---

## 🧠 1. self-improving — 分析质量自检引擎

### 嵌入位置
每个标的六大脑分析完成后 + 每次输出投资推荐后

### 触发规则

```python
每次投资分析完成时:
  # 1. 记录分析快照
  record = {
    "ticker": ticker,
    "date": today,
    "recommendation": final_tier,
    "six_brain_signals": {agent: signal for agent, signal in ...},
    "committee_consensus": bullish_votes/11,
    "chokepoint_strength": chokepoint.strength,
    "key_financial_figures": {pe, pb, gross_margin, roe, ...}
  }
  write_to memory/YYYY-MM-DD.md

  # 2. 3个月后回测触发
  if date.today() - record.date >= 90 days:
      actual_return = get_stock_return(record.ticker, record.date+90d)
      predicted_signal = record.six_brain_signals["ValuationAgent"]
      if predicted_signal == BULLISH and actual_return < -0.20:
          misjudgment_count["ValuationAgent"] += 1
          log_to LEARNINGS.md

每周一自检:
  for agent in six_agents:
      rate = misjudgment_count[agent] / total_analyses_last_90d
      if rate > 0.10:
          upgrade_agent_thresholds(agent, rate)
          通知主人: f"{agent} 误判率 {rate:.1%}，已自动升级评分阈值"

  # 写入 MEMORY.md
  update_learnings(f"Agent准确率自检 [MM/DD] ...")
```

### mem0 记忆锚点（轻量版）

```
投资分析记录:
  - 日期: [MM/DD HH:MM]
  - 标的: TICKER
  - 六大脑信号: {各Agent信号分布}
  - 委员会共识: X/11
  - 最终推荐: 🔴/🟠/🟡/🔵/⚪
  - 核心逻辑: 1句话
  - 待回测: 3个月后
```

---

## 🧠 2. mem0 — 跨会话投资记忆

### 三个记忆锚点（每次任务必读必写）

#### 锚点1: 用户投资偏好（分析开始时必读）

```
触发: 每次收到主人新请求时
读取: memory/ 目录中最新偏好记录
内容:
  ├─ 行业偏好: 主人关注哪些行业（AI芯片/新能源/生物医药/...）
  ├─ 风险容忍度: 最大单标的仓位、最大组合回撤
  ├─ 持仓限制: 已持有的标的（来源: portfolio/CURRENT.md）
  ├─ 市场偏好: 美/A/港 权重分配
  └─ 特殊偏好: 是否偏好"非本土潜力股"（美股中的外国公司）
```

#### 锚点2: 数据源状态（数据获取前检查）

```
触发: 每次开始数据获取前
读取: memory/ 中数据源可用性记录
内容:
  ├─ Finnhub API: 可用/限流/失效 → 自动切换备用
  ├─ AKShare: 可用/被封 → 切换 a-stock-data
  ├─ Yahoo Finance: 可用 → 海外市场主力
  ├─ FRED API: 可用/失败 → 自动切换备选
  ├─ 英为财情: 可用/403 → 跳过
  └─ serper: 可用/Key失效 → 切换 multi-search
```

#### 锚点3: 分析结论回测（分析结束时记录）

```
触发: 每次分析结论输出后
记录:
  ├─ 产业链 + 核心判断 + 时间戳
  ├─ 推荐标的全列表（含推荐评级）
  ├─ 标记: "待3个月后回测验证"
  └─ 3个月后: 自动对比实际走势，更新准确度
```

### 写入规范

```python
每次分析结束时:
  memory/YYYY-MM-DD.md.append(f"""
## [HH:MM] {模式} - {行业/标的}
### 分析摘要
- 标的数: {n}
- Top Pick: {ticker} ({tier})
- 核心逻辑: {1-3句话}
- 数据源: {使用的数据源列表}
- 待回测: YYYY-MM-DD + 90天
### 方法论触发
- self-improving: 已记录快照
- ragflow-skill: {"已同步" if ragflow_ok else "未配置-跳过"}
- openclaw-project-iteration: {"待评估" if chain_complete else "N/A"}
""")
```

---

## 🧠 3. openclaw-project-iteration — 模板扩展引擎

### 嵌入位置
每完成一个产业链分析（全局模式）后

### 模板扩展标准（同时满足3条才触发）

```
1. 产业链节点 ≥ 5 个（上游/中游/下游三层完整）
2. CR1 数据 ≥ 3 个瓶颈节点已知
3. BOM 拆解数据完整（核心组件成本占比已知）
4. 🆕 可投资的上市公司 ≥ 3 家（有实际标的，非纯学术分析）

同时满足 → 触发模板扩展:
  1. 提取产业链图谱（节点+边+权重）→ 导出 JSON
  2. 提取卡脖子排名（前5名）+ 对应上市公司
  3. 记录到 memory/template-expansion-pending.md
  4. 通知主人: "是否将「{行业}」产业链加入预设模板库？"
  5. 主人确认后 → 更新 templates/presets/{industry}.json
```

### 预设模板库位置

```
templates/presets/
├── ai_gpu.json          # AI GPU 产业链
├── humanoid_robot.json  # 人形机器人产业链
├── evtol.json           # 低空经济产业链
└── {new_industry}.json  # 扩展的新模板
```

每个模板包含：
```json
{
  "name": "AI GPU",
  "description": "AI GPU 从晶圆到服务器的完整产业链",
  "nodes": [...],
  "edges": [...],
  "known_chokepoints": ["EUV光刻胶", "InP衬底", "HBM"],
  "last_updated": "2026-05-30",
  "analysis_count": 3
}
```

---

## 🧠 4. ragflow-skill — 知识库同步

### 嵌入位置
产业链图谱构建完成后 + 分析报告生成后

### 同步内容

```
图谱构建完成时:
  ├─ 产业链节点列表（name, tier, cr1, is_standardized）
  ├─ 依赖边列表（from_node, to_node, dependency_type）
  ├─ 卡脖子评分结果（node, score, tier, rating）
  └─ 目标数据集: "investment-chokepoint-knowledge"

分析报告生成后:
  ├─ 核心结论（≤200字摘要）
  ├─ 推荐标的列表（ticker, recommendation, position）
  ├─ 委员会投票结果（共识/分歧点）
  └─ 数据源引用列表
```

### 配置要求

```bash
# 必须设置 RAGFLOW_API_URL 和 RAGFLOW_API_KEY
export RAGFLOW_API_URL="http://your-ragflow-server/api/v1"
export RAGFLOW_API_KEY="your-api-key"

# 数据集准备（首次运行）
python3 scripts/init_ragflow_datasets.py
```

> ⚠️ 当前 RAGFLOW_API_KEY 未配置。ragflow 同步功能在文档中保留完整规范，待主人配置环境变量后自动激活。

### 降级策略

当 RAGFLOW 不可用时：
1. 本地文件仍正常写入（`knowledge/investment-brain/`）
2. 分析质量和投资推荐完全不受影响
3. 下次 RAGFLOW 可用时，可批量同步历史数据

---

## 🧠 5. universal-agent-skill — 多Agent编排

### 嵌入位置
Pipeline 启动时（Step 0）

### 三模式编排决策

```
用户请求分析
│
├─ 关键词: 产业链/卡脖子/瓶颈 + 投资/标的
│   → 🌐 全局模式（链式调用）
│   ├─ Agent编排: sequential_chain
│   ├─ Step 1: industry-deep-driller 🔴纯钻探
│   │   ├─ Agent A (BOM拆解) → Agent B (集中度审计) → Agent D (图论评级)
│   │   └─ Agent C (财务验证) → 休眠
│   └─ Step 2: new-investment-brain v5
│       ├─ 映射引擎 → CandidateStock[]
│       ├─ 六大脑并行 (6 Agents concurrent)
│       └─ 12人委员会并行 (12 Members concurrent)
│
├─ 关键词: 分析/评估 具体标的 + 无产业链词
│   → 📊 标准模式（并发全量）
│   ├─ Agent编排: concurrent_full
│   ├─ 六大脑并行 → 12人委员会并行
│   └─ PortfolioManager汇总
│
├─ 关键词: 快速/简要 + 无产业链词
│   → ⚡ 轻量模式（并发精简）
│   ├─ Agent编排: concurrent_lightweight
│   ├─ ValuationAgent + FundamentalsAgent + TechnicalsAgent
│   └─ 委员会休眠
│
└─ 默认 → 📊 标准模式
```

### Agent 状态追踪（universal-agent-skill 规范）

```json
{
  "pipeline_id": "v5-global-20260530-001",
  "steps": [
    {
      "step_id": 1,
      "action": "industry-deep-driller.pure_drill",
      "status": "completed",
      "output": "chokepoint_nodes.json",
      "verified": true,
      "timestamp": "[05/30 13:00]"
    },
    {
      "step_id": 2,
      "action": "mapping_engine.map_to_stocks",
      "status": "completed",
      "output": "CandidateStock[]",
      "verified": true,
      "timestamp": "[05/30 13:02]"
    }
  ]
}
```

---

## 🧠 6. LLM wiki — 结构化知识规范

### 嵌入位置
每个报告/输出的生成结束时

### 必须遵守的规范

#### 输出格式

```
来源标注:
  [来源: 机构名, YYYY-MM] — 已知来源
  [⚠️ 待验证] — 无法确认的数据
  [⚠️ 推测] — 基于逻辑推断但无直接证据
  [⚠️ 猜测] — 纯假设

传播力分级:
  事实 (Fact): 直接可验证 → 必须标注来源
  推断 (Inference): 逻辑推导 → 标注 [⚠️ 推测]
  猜测 (Guess): 假设 → 标注 [⚠️ 猜测]

结构化占比:
  表格/列表 ≥ 60%
  纯文字 ≤ 40%
```

#### 时间格式

```
所有时间戳: [MM/DD HH:MM] 格式
禁止: "May 30, 2026" / "2026年5月30日" / "5/30/2026"
正确: [05/30 13:00]
```

#### 报告结构模式

参考 `docs/wiki/SCHEMA.md`：
- 投资分析报告模式
- 产业链分析报告模式
- 快速简报模式

---

## 📐 自迭代触发器汇总

| 触发事件 | 调用的方法论 | 具体动作 |
|----------|-------------|---------|
| 收到新请求 | mem0 锚点1+2 | 读取偏好 + 检查数据源状态 |
| 模式判断完成 | universal-agent-skill | 编排决策（全局/标准/轻量） |
| 每个标的分析完成 | self-improving | 记录分析快照 + 3月回测标记 |
| 产业链图谱构建 | ragflow-skill | 同步节点+边到知识库 |
| 产业链完整分析 | openclaw-project-iteration | 评估模板扩展 |
| 分析报告输出 | LLM wiki | 格式校验（表格≥60%、来源标注） |
| 全流程结束 | mem0 锚点3 | 写入结论+偏好更新 |
| 主人纠正结论 | self-improving | 误判+1 → 更新LEARNINGS.md |
| 每周一 09:00 | self-improving 自检 | 计算误判率，必要时升级阈值 |
| 每90天 | self-improving 回测 | 验证历史结论准确度 |

---

_版本: v1.0 | 创建: 2026-05-30 | 关联: new-investment-brain v5.0_