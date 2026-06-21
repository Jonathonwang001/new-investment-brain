"""
Investment Brain New v5.0 — 双技能联动(industry-deep-driller→标的) + 六大脑深度分析 + 11人委员会 + Chokepoint + Moat + 六大脑自进化
融合：原六大脑 + SOIC + Serenity Chokepoint + financial-analysis + ai-hedge-fund committee + industry-deep-driller v2.0
v5.0新增：产业链→标的映射引擎 + 图论瓶颈指数接入 + 全球七地市场路由 + 六大脑自进化系统
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional


class Signal(Enum):
    BULLISH = "BULLISH"
    SLIGHTLY_BULLISH = "SLIGHTLY_BULLISH"
    NEUTRAL = "NEUTRAL"
    SLIGHTLY_BEARISH = "SLIGHTLY_BEARISH"
    BEARISH = "BEARISH"


class ChokepointStrength(Enum):
    EXTREME = "Extreme"
    STRONG = "Strong"
    MODERATE = "Moderate"
    WEAK = "Weak"
    NONE = "None"


class ThreeMomentType(Enum):
    """三种时刻类型 (v3.1+"""
    AJI = "🍶 AJI"       # 味之素时刻 — 配方/工艺独门绝技
    RPI = "🍓 RPI"       # 树莓派时刻 — 基础但不可或缺
    GATE = "🛡️ GATE"     # 关隘时刻 — 制造必经环节寡头
    NONE = "❓ 未判定"


class RecommendationTier(Enum):
    """v4.0五档分级推荐（含圆角背景色块CSS映射）"""
    STRONG_BUY = "🔴 强烈推荐"    # 深红 #ffebee
    CORE_BUY = "🟠 核心推荐"      # 橙色 #fff3e0
    QUALIFYING = "🟡 准推荐"     # 金黄 #fffde7
    SECONDARY = "🔵 次级推荐"    # 蓝色 #e3f2fd
    WATCHLIST = "⚪ 观察池"       # 灰色 #fafafa

    @property
    def css_class(self) -> str:
        """Returns CSS class for v4_report.css color blocks"""
        mapping = {
            RecommendationTier.STRONG_BUY: "rec-extreme",
            RecommendationTier.CORE_BUY: "rec-strong",
            RecommendationTier.QUALIFYING: "rec-moderate",
            RecommendationTier.SECONDARY: "rec-weak",
            RecommendationTier.WATCHLIST: "rec-avoid",
        }
        return mapping.get(self, "rec-avoid")


@dataclass
class ChokepointDiagnosis:
    """四维Chokepoint诊断结果"""
    ticker: str
    giant_dependency: float = 0.0
    replacement_cost: float = 0.0
    cognitive_gap: float = 0.0
    regulatory_chokepoint: float = 0.0
    detail: Dict = field(default_factory=dict)

    @property
    def total_score(self) -> float:
        return (0.30 * self.giant_dependency
                + 0.25 * self.replacement_cost
                + 0.25 * self.cognitive_gap
                + 0.20 * self.regulatory_chokepoint)

    @property
    def strength(self) -> ChokepointStrength:
        s = self.total_score
        if s >= 80: return ChokepointStrength.EXTREME
        if s >= 60: return ChokepointStrength.STRONG
        if s >= 40: return ChokepointStrength.MODERATE
        if s >= 20: return ChokepointStrength.WEAK
        return ChokepointStrength.NONE


@dataclass
class AgentSignal:
    """单个Agent的分析信号（含完整方法论）"""
    agent_name: str
    signal: Signal
    score: float  # 0-100
    methodology: str = ""
    step_by_step: List[Dict] = field(default_factory=list)
    formulas: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    data_sources: List[str] = field(default_factory=list)

    def full_report(self) -> str:
        lines = [
            f"## {self.agent_name} — {self.signal.value} (Score: {self.score:.1f})",
            f"\n### 方法论\n{self.methodology}",
            "\n### 分步推导",
        ]
        for step in self.step_by_step:
            lines.append(f"  Step {step.get('step', '?')}: {step.get('description', '')}")
            if 'formula' in step:
                lines.append(f"    公式: {step['formula']}")
            if 'output' in step:
                lines.append(f"    输出: {step['output']}")
        if self.formulas:
            lines.append("\n### 公式汇总")
            for f in self.formulas:
                lines.append(f"  - {f}")
        if self.assumptions:
            lines.append("\n### 关键假设")
            for a in self.assumptions:
                lines.append(f"  - {a}")
        if self.data_sources:
            lines.append("\n### 数据来源")
            for s in self.data_sources:
                lines.append(f"  - {s}")
        return "\n".join(lines)


@dataclass
class FinancialScorecard:
    """14项标准化财务打分"""
    roe: float = 0.0
    roic: float = 0.0
    roiic: float = 0.0
    gross_margin: float = 0.0
    net_margin: float = 0.0
    rev_cagr: float = 0.0
    earnings_cagr: float = 0.0
    cfo_pat: float = 0.0
    fcf_yield: float = 0.0
    debt_equity: float = 0.0
    net_operating_cycle: float = 0.0
    cash_rev_ratio: float = 0.0
    interest_coverage: float = 0.0
    dividend_buyback: float = 0.0

    @property
    def total(self) -> float:
        return (self.roe + self.roic + self.roiic + self.gross_margin +
                self.net_margin + self.rev_cagr + self.earnings_cagr +
                self.cfo_pat + self.fcf_yield + self.debt_equity +
                self.net_operating_cycle + self.cash_rev_ratio +
                self.interest_coverage + self.dividend_buyback)

    @property
    def grade(self) -> str:
        t = self.total
        if t >= 80: return "优秀(≥80)"
        if t >= 70: return "良好(70-79)"
        if t >= 60: return "及格(60-69)"
        if t >= 50: return "偏弱(50-59)"
        if t >= 40: return "差(40-49)"
        return "极差(<40)"


@dataclass
class MoatAssessment:
    """护城河评估"""
    moat_types: List[str] = field(default_factory=list)
    is_reinvestment_moat: bool = False
    roiic: float = 0.0
    cdmo_lock_layers: int = 0
    strengthening_signals: List[str] = field(default_factory=list)
    weakening_signals: List[str] = field(default_factory=list)

    @property
    def moat_strength(self) -> str:
        if self.is_reinvestment_moat and self.roiic > 15:
            return "Strong (再投资型)"
        if self.is_reinvestment_moat:
            return "Moderate (再投资型，ROIIC偏低)"
        if len(self.moat_types) >= 2:
            return "Moderate (多护城河，但非再投资型)"
        if len(self.moat_types) == 1:
            return "Weak (单一护城河)"
        return "None (无明显护城河)"


@dataclass
class SpeedBreakerAssessment:
    """Speed Breaker评估结果"""
    event_description: str = ""
    is_short_lived: bool = False
    core_business_intact: bool = False
    cashflow_intact: bool = False
    management_response_ok: bool = False
    historical_precedent_ok: bool = False
    valuation_safety: bool = False

    @property
    def passed(self) -> bool:
        return sum([self.is_short_lived, self.core_business_intact,
                    self.cashflow_intact, self.management_response_ok,
                    self.historical_precedent_ok, self.valuation_safety]) >= 4

    @property
    def check_summary(self) -> str:
        checks = [
            ("事件短期性", self.is_short_lived),
            ("核心业务完好", self.core_business_intact),
            ("现金流完好", self.cashflow_intact),
            ("管理层应对", self.management_response_ok),
            ("历史先例", self.historical_precedent_ok),
            ("估值安全边际", self.valuation_safety),
        ]
        lines = []
        for name, result in checks:
            lines.append(f"  {'✅' if result else '❌'} {name}")
        return "\n".join(lines)

@dataclass
class SixBrainDeepAnalysis:
    """v4.0 六大脑深度分析汇总（板块①）"""
    ticker: str
    valuation: Optional[AgentSignal] = None
    fundamentals: Optional[AgentSignal] = None
    technicals: Optional[AgentSignal] = None
    sentiment: Optional[AgentSignal] = None
    risk: Optional[AgentSignal] = None
    moat: Optional[AgentSignal] = None

    @property
    def bullish_count(self) -> int:
        signals = [self.valuation, self.fundamentals, self.technicals,
                   self.sentiment, self.risk, self.moat]
        return sum(1 for s in signals if s and s.signal in (Signal.BULLISH, Signal.SLIGHTLY_BULLISH))

    @property
    def bearish_count(self) -> int:
        signals = [self.valuation, self.fundamentals, self.technicals,
                   self.sentiment, self.risk, self.moat]
        return sum(1 for s in signals if s and s.signal in (Signal.BEARISH, Signal.SLIGHTLY_BEARISH))

    @property
    def overall_signal(self) -> str:
        b = self.bullish_count
        n = sum(1 for s in [self.valuation, self.fundamentals, self.technicals,
                           self.sentiment, self.risk, self.moat] if s and s.signal == Signal.NEUTRAL)
        if b >= 5: return "🟢 强烈看多"
        if b >= 3: return "🟡 偏多"
        if n >= 4: return "⚪ 中性"
        return "🔴 偏空"


@dataclass
class CommitteeConsensus:
    """v4.0 11人委员会共识（板块②）"""
    ticker: str
    bullish_votes: int = 0
    neutral_votes: int = 0
    bearish_votes: int = 0
    avg_confidence: float = 0.0
    key_divergences: List[str] = field(default_factory=list)

    @property
    def consensus_ratio(self) -> float:
        return self.bullish_votes / 11

    @property
    def is_strong_consensus(self) -> bool:
        return self.consensus_ratio >= 0.72  # 8/11


@dataclass
class V4FinalRecommendation:
    """v4.0 综合终审结果"""
    ticker: str
    moment_type: ThreeMomentType = ThreeMomentType.NONE
    chokepoint: Optional[ChokepointDiagnosis] = None
    six_brain: Optional[SixBrainDeepAnalysis] = None
    committee: Optional[CommitteeConsensus] = None
    recommendation: RecommendationTier = RecommendationTier.WATCHLIST
    suggested_position: float = 0.0
    key_risks: List[str] = field(default_factory=list)
    catalysts: List[str] = field(default_factory=list)

    def to_summary(self) -> str:
        return (
            f"{self.ticker} | {self.moment_type.value} | "
            f"Chokepoint: {self.chokepoint.strength.value if self.chokepoint else 'N/A'} | "
            f"六大脑: {self.six_brain.overall_signal if self.six_brain else 'N/A'} | "
            f"委员会: {self.committee.bullish_votes}/11看多" if self.committee else "N/A"
        )


def classify_recommendation_v4(
    financial_score: float,
    chokepoint_strength: ChokepointStrength,
    technical_signal: Signal,
    committee_consensus_ratio: float,
    forensic_red_flags: int = 0,
) -> RecommendationTier:
    """
    v4.0 五档分层推荐
    四维加权：财务(25%) + Chokepoint(25%) + 技术面(20%) + 委员会共识(30%)
    """
    if forensic_red_flags >= 3:
        return RecommendationTier.WATCHLIST

    chokepoint_strong = chokepoint_strength in (ChokepointStrength.EXTREME, ChokepointStrength.STRONG)
    chokepoint_moderate = chokepoint_strength == ChokepointStrength.MODERATE
    tech_bullish = technical_signal in (Signal.BULLISH, Signal.SLIGHTLY_BULLISH)
    tech_bearish = technical_signal in (Signal.BEARISH, Signal.SLIGHTLY_BEARISH)
    committee_strong = committee_consensus_ratio >= 0.72  # 8/11
    committee_bullish = committee_consensus_ratio >= 0.55  # 6/11

    # 技术面硬止损
    if tech_bearish and financial_score < 40 and not committee_strong:
        return RecommendationTier.WATCHLIST

    # 🔴 强烈推荐：四维全优
    if financial_score >= 70 and chokepoint_strong and tech_bullish and committee_strong:
        return RecommendationTier.STRONG_BUY

    # 🟠 核心推荐：三维优秀
    if financial_score >= 70 and chokepoint_strong and committee_bullish:
        return RecommendationTier.CORE_BUY
    if financial_score >= 60 and chokepoint_strong and committee_strong:
        return RecommendationTier.CORE_BUY

    # 🟡 准推荐：Chokepoint + 委员会弥补财务
    if chokepoint_strong and committee_strong:
        return RecommendationTier.QUALIFYING
    if financial_score >= 60 and chokepoint_moderate and committee_bullish:
        return RecommendationTier.QUALIFYING

    # 🔵 次级推荐：综合略有欠缺
    if committee_bullish and (chokepoint_moderate or financial_score >= 50):
        return RecommendationTier.SECONDARY
    if chokepoint_strong and financial_score >= 50:
        return RecommendationTier.SECONDARY

    # ⚪ 观察池：不满足任何条件
    return RecommendationTier.WATCHLIST


def position_sizing_v4(recommendation: RecommendationTier) -> float:
    """v4.0 五档仓位建议"""
    sizes = {
        RecommendationTier.STRONG_BUY: 0.17,    # 15-20%
        RecommendationTier.CORE_BUY: 0.12,      # 10-15%
        RecommendationTier.QUALIFYING: 0.07,    # 5-10%
        RecommendationTier.SECONDARY: 0.04,     # 3-5%
        RecommendationTier.WATCHLIST: 0.0,
    }
    return sizes.get(recommendation, 0.0)


# === Deprecated: v3.0 兼容层（保留向后兼容） ===

def classify_recommendation(*args, **kwargs) -> RecommendationTier:
    """[v3.0 compat] Use classify_recommendation_v4 for new code."""
    return classify_recommendation_v4(*args, **kwargs)


def position_sizing(recommendation: RecommendationTier) -> float:
    """[v3.0 compat] Use position_sizing_v4 for new code."""
    return position_sizing_v4(recommendation)


# ===== Serenity Alpha Detection Model =====

@dataclass
class AlphaSignal:
    """Serenity第一性发现模型 - Alpha信号"""
    ticker: str
    irreplaceability_score: float = 0.0    # 0-100, 六维不可替代性
    cognitive_gap_score: float = 0.0       # 0-100, 认知差
    financial_inflection_score: float = 0.0 # 0-100, 财务拐点预判
    catalyst_density: float = 0.0          # 0-100, 催化剂密度
    supply_demand_imbalance: float = 0.0   # 0-100, 供需失衡度
    historical_analog_score: float = 0.0   # 0-100, 历史类比匹配度

    @property
    def alpha_score(self) -> float:
        return (0.25 * self.irreplaceability_score
                + 0.20 * self.cognitive_gap_score
                + 0.20 * self.financial_inflection_score
                + 0.15 * self.catalyst_density
                + 0.10 * self.supply_demand_imbalance
                + 0.10 * self.historical_analog_score)

    @property
    def phase(self) -> str:
        s = self.alpha_score
        if s >= 80: return "🔴 Phase-1 Alpha"
        if s >= 60: return "🟠 Phase-2 Alpha"
        if s >= 40: return "🟡 Phase-3 Alpha"
        if s >= 20: return "🔵 潜在Alpha"
        return "⚪ 无Alpha"

    @property
    def can_break_financial_gate(self) -> bool:
        """Alpha≥60时可突破v3.0财务闸门"""
        return self.alpha_score >= 60


def classify_with_alpha(
    alpha_score: float,
    financial_score: float,
    chokepoint_strength: ChokepointStrength,
    technical_signal: Signal,
    forensic_red_flags: int = 0,
) -> RecommendationTier:
    """
    Serenity Alpha + v3.0 联合推荐
    Alpha Score≥60时可突破财务闸门
    """
    # 法医红旗仍是无条件底线
    if forensic_red_flags >= 3:
        return RecommendationTier.AVOID

    # Alpha极强(≥60)时，财务闸门可降级
    if alpha_score >= 60:
        # 技术面BEARISH仍是底线
        if technical_signal in (Signal.BEARISH, Signal.SLIGHTLY_BEARISH) and financial_score < 40:
            return RecommendationTier.AVOID

        if alpha_score >= 80:
            if financial_score >= 60:
                return RecommendationTier.STRONG_BUY
            if financial_score >= 40:
                return RecommendationTier.SPECULATIVE  # 标注"Alpha极强，等待财务拐点"
            return RecommendationTier.SPECULATIVE  # 标注"Alpha极强+财务极差，仅极小仓位"

        # Alpha 60-79
        if financial_score >= 60:
            return RecommendationTier.CORE_BUY
        if financial_score >= 40:
            return RecommendationTier.QUALIFYING
        return RecommendationTier.SPECULATIVE

    # Alpha<60时，回归v3.0常规分层推荐
    return classify_recommendation(financial_score, chokepoint_strength, technical_signal, forensic_red_flags)


def position_sizing_with_alpha(alpha_score: float, recommendation: RecommendationTier) -> float:
    """Alpha强化的仓位建议"""
    base = position_sizing_v4(recommendation)
    # Alpha≥80时，投机级仓位从2%提到3-5%
    if alpha_score >= 80:
        return 0.03
    if alpha_score >= 60:
        return 0.08
    return base


# ===== v5.0: 双技能联动数据模型 =====

@dataclass
class SupplierInfo:
    """瓶颈节点供应商信息（来自 industry-deep-driller）"""
    name: str
    market_share: float = 0.0
    ticker: str = ""
    market: str = "US"  # US/CN/HK/JP/KR/TW/EU


@dataclass
class ChokepointNode:
    """v5.0 瓶颈节点 — industry-deep-driller 结构化输入"""
    node_id: str
    node_name: str
    tier: str = "T2"  # T0/T1/T2/T3
    bottleneck_score: float = 0.0
    betweenness_centrality: float = 0.0
    cr1: float = 0.0
    structural_hole_constraint: float = 0.0
    tech_barrier_score: float = 0.0
    scarcity_score: float = 0.0
    bom_level: int = 0
    bom_path: List[str] = field(default_factory=list)
    suppliers: List[SupplierInfo] = field(default_factory=list)
    certification_barriers: List[str] = field(default_factory=list)
    alternative_paths: List[str] = field(default_factory=list)
    is_standardized: bool = False
    customization_level: int = 0
    patent_count_estimated: int = 0

    @property
    def is_investable(self) -> bool:
        return not self.is_standardized and self.tier in ("T0", "T1")

    @property
    def tier_color(self) -> str:
        return {"T0": "node-tier-0", "T1": "node-tier-1", "T2": "node-tier-2"}.get(self.tier, "node-standard")


@dataclass
class GlobalMarket:
    """v5.0 全球市场路由"""
    code: str          # US/CN/HK/JP/KR/TW/EU
    name: str          # 市场名称
    ticker_suffixes: List[str] = field(default_factory=list)
    primary_source: str = "Yahoo Finance"
    fallback_source: str = "Finnhub"
    proxy_required: bool = True
    currency: str = "USD"
    trading_hours: str = ""


# 全球市场路由配置表
GLOBAL_MARKETS: Dict[str, GlobalMarket] = {
    "US": GlobalMarket("US", "美国", [], "Finnhub", "Yahoo Finance", True, "USD", "09:30-16:00 EST"),
    "CN": GlobalMarket("CN", "A股", [".SZ", ".SH"], "a-stock-data", "AKShare", False, "CNY", "09:30-15:00 CST"),
    "HK": GlobalMarket("HK", "港股", [".HK"], "AKShare", "Finnhub", False, "HKD", "09:30-16:00 HKT"),
    "JP": GlobalMarket("JP", "日本", [".T"], "Yahoo Finance", "Finnhub", True, "JPY", "09:00-15:00 JST"),
    "KR": GlobalMarket("KR", "韩国", [".KS", ".KQ"], "Yahoo Finance", "Finnhub", True, "KRW", "09:00-15:30 KST"),
    "TW": GlobalMarket("TW", "台湾", [".TW", ".TWO"], "Yahoo Finance", "Finnhub", True, "TWD", "09:00-13:30 CST"),
    "EU": GlobalMarket("EU", "欧洲", [".DE", ".PA", ".L", ".MI", ".AS", ".MC", ".SW"], "Yahoo Finance", "Finnhub", True, "EUR", "09:00-17:30 CET"),
}


def detect_market(ticker: str) -> Optional[GlobalMarket]:
    """根据 ticker 后缀自动检测市场"""
    ticker_upper = ticker.upper()
    for code, market in GLOBAL_MARKETS.items():
        for suffix in market.ticker_suffixes:
            if ticker_upper.endswith(suffix.upper()):
                return market
    # 无后缀 → 默认美股
    return GLOBAL_MARKETS.get("US")


@dataclass
class CandidateStock:
    """v5.0 映射引擎输出 — 瓶颈节点→可投标的"""
    ticker: str
    company_name: str
    market: str = "US"
    chokepoint_node: Optional[ChokepointNode] = None
    market_share_in_node: float = 0.0
    is_adr: bool = False
    is_foreign_listed_on_us: bool = False
    foreign_market: str = ""
    data_source_routing: Dict = field(default_factory=dict)

    @property
    def display_ticker(self) -> str:
        suffix = " (ADR)" if self.is_adr else ""
        return f"{self.ticker}{suffix}"

    @property
    def risk_flags(self) -> List[str]:
        flags = []
        if self.is_adr:
            flags.append("ADR溢价风险")
        if self.is_foreign_listed_on_us:
            flags.append(f"非美国本土注册({self.foreign_market})")
        return flags


@dataclass
class V5PipelineConfig:
    """v5.0 全局 Pipeline 配置"""
    mode: str = "v5_standard"  # v5_global / v5_standard / v5_lightweight
    industry: str = ""
    enable_industry_deep_driller: bool = False
    enable_ragflow_sync: bool = False
    enable_self_improving: bool = True
    enable_mem0: bool = True
    enable_template_expansion: bool = False
    max_candidates: int = 10
    min_market_cap: float = 100_000_000  # $100M
    target_chokepoint_weight: float = 0.30  # Chokepoint标的≥30%组合


@dataclass
class V5FinalRecommendation:
    """v5.0 综合终审结果（含图论指标和全球市场信息）"""
    ticker: str
    moment_type: ThreeMomentType = ThreeMomentType.NONE
    chokepoint: Optional[ChokepointDiagnosis] = None
    chokepoint_node: Optional[ChokepointNode] = None  # 🆕 图论输入
    six_brain: Optional[SixBrainDeepAnalysis] = None
    committee: Optional[CommitteeConsensus] = None
    recommendation: RecommendationTier = RecommendationTier.WATCHLIST
    suggested_position: float = 0.0
    key_risks: List[str] = field(default_factory=list)
    catalysts: List[str] = field(default_factory=list)
    market: str = "US"
    is_foreign_listed_on_us: bool = False

    @property
    def has_graph_validation(self) -> bool:
        """是否接收了 industry-deep-driller 的图论验证"""
        return self.chokepoint_node is not None

    @property
    def betweenness_enhanced_chokepoint(self) -> float:
        """图论增强的 Chokepoint 评分"""
        base = self.chokepoint.total_score if self.chokepoint else 0
        if self.chokepoint_node:
            graph_bonus = self.chokepoint_node.betweenness_centrality * 15  # 介数中心性贡献最高15分
            return min(100, base + graph_bonus)
        return base

    def to_summary(self) -> str:
        graph = f" | BC:{self.chokepoint_node.betweenness_centrality:.2f}" if self.chokepoint_node else ""
        return (
            f"{self.ticker} | {self.moment_type.value} | "
            f"[Graph: {self.has_graph_validation}] | "
            f"Chokepoint: {self.chokepoint.strength.value if self.chokepoint else 'N/A'}{graph} | "
            f"六大脑: {self.six_brain.overall_signal if self.six_brain else 'N/A'} | "
            f"委员会: {self.committee.bullish_votes}/11看多" if self.committee else "N/A"
        )


def classify_recommendation_v5(
    six_brain_signals: Optional[SixBrainDeepAnalysis] = None,
    committee_consensus: Optional[CommitteeConsensus] = None,
    chokepoint_strength: ChokepointStrength = ChokepointStrength.NONE,
    three_moment_type: ThreeMomentType = ThreeMomentType.NONE,
    graph_betweenness: float = 0.0,
    forensic_red_flags: int = 0,
) -> RecommendationTier:
    """
    v5.0 五层加权推荐（含图论瓶颈指数）
    权重：六大脑30% + 委员会30% + Chokepoint20% + 图论10% + 时刻10%
    """
    if forensic_red_flags >= 3:
        return RecommendationTier.WATCHLIST

    # 六大脑信号
    bullish_brains = six_brain_signals.bullish_count if six_brain_signals else 0
    bearish_brains = six_brain_signals.bearish_count if six_brain_signals else 0

    # 委员会共识
    consensus = committee_consensus.consensus_ratio if committee_consensus else 0

    # Chokepoint 强度
    chokepoint_strong = chokepoint_strength in (ChokepointStrength.EXTREME, ChokepointStrength.STRONG)
    chokepoint_extreme = chokepoint_strength == ChokepointStrength.EXTREME

    # 图论增强
    graph_strong = graph_betweenness >= 0.70  # 介数中心性极高
    graph_moderate = graph_betweenness >= 0.50

    # 时刻增强
    moment_strong = three_moment_type in (ThreeMomentType.AJI, ThreeMomentType.GATE)

    # 技术面硬止损
    if bearish_brains >= 4 and not chokepoint_strong:
        return RecommendationTier.WATCHLIST

    # 🔴 强烈推荐：全维度完美 + 图论极强
    if bullish_brains >= 5 and consensus >= 0.72 and chokepoint_extreme and graph_strong and moment_strong:
        return RecommendationTier.STRONG_BUY

    # 🟠 核心推荐
    if bullish_brains >= 4 and consensus >= 0.64 and chokepoint_strong and graph_moderate:
        return RecommendationTier.CORE_BUY
    if bullish_brains >= 3 and consensus >= 0.72 and chokepoint_strong:
        return RecommendationTier.CORE_BUY

    # 🟡 准推荐
    if chokepoint_strong and consensus >= 0.55:
        return RecommendationTier.QUALIFYING
    if bullish_brains >= 3 and consensus >= 0.55 and graph_moderate:
        return RecommendationTier.QUALIFYING

    # 🔵 次级推荐
    if consensus >= 0.45 or (chokepoint_strong and bullish_brains >= 2):
        return RecommendationTier.SECONDARY

    return RecommendationTier.WATCHLIST


def position_sizing_v5(recommendation: RecommendationTier, chokepoint_weight: bool = False) -> float:
    """v5.0 六档仓位建议（图论增强）"""
    sizes = {
        RecommendationTier.STRONG_BUY: 0.10,   # 5-10% (放松以容纳更多Chokepoint标的)
        RecommendationTier.CORE_BUY: 0.07,      # 5-8%
        RecommendationTier.QUALIFYING: 0.05,    # 3-5%
        RecommendationTier.SECONDARY: 0.03,     # 2-3%
        RecommendationTier.WATCHLIST: 0.0,
    }
    return sizes.get(recommendation, 0.0)
