"""
11-Person Investment Committee — v4.0
Each committee member independently analyzes and votes.
Design: Divergences are often more valuable than consensus.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional


class VoteResult(Enum):
    BULLISH = "🟢 BULLISH"
    STRONG_BUY = "🔴 STRONG_BUY"
    NEUTRAL = "🟡 NEUTRAL"
    BEARISH = "🔴 BEARISH"
    LIGHT_POS = "🔵 LIGHT_POS"


@dataclass
class CommitteeVote:
    """Single committee member's vote."""
    member_name: str
    member_title: str
    investment_philosophy: str
    analysis_points: List[str]  # key check items with conclusions
    vote: VoteResult
    confidence: int  # 0-100
    rationale: str  # one-line summary with specific data


@dataclass
class CommitteeSummary:
    """Full committee voting summary for a ticker."""
    ticker: str
    votes: List[CommitteeVote]  # exactly 11

    @property
    def bullish_count(self) -> int:
        return sum(1 for v in self.votes if v.vote in (VoteResult.BULLISH, VoteResult.STRONG_BUY))

    @property
    def neutral_count(self) -> int:
        return sum(1 for v in self.votes if v.vote == VoteResult.NEUTRAL)

    @property
    def bearish_count(self) -> int:
        return sum(1 for v in self.votes if v.vote == VoteResult.BEARISH)

    @property
    def consensus_strength(self) -> str:
        """Determine consensus strength based on vote distribution."""
        pct = self.bullish_count / 11 * 100
        if pct >= 72:
            return "强共识"
        elif pct >= 55:
            return "中等共识"
        elif pct >= 36:
            return "弱共识"
        else:
            return "分歧"

    @property
    def divergences(self) -> List[str]:
        """Identify key divergences (where alpha often hides)."""
        divs = []
        bullish_votes = [v for v in self.votes if v.vote in (VoteResult.BULLISH, VoteResult.STRONG_BUY)]
        bearish_votes = [v for v in self.votes if v.vote == VoteResult.BEARISH]

        for bv in bearish_votes:
            divs.append(f"⚠️ {bv.member_name} 看空（置信度{bv.confidence}%）：{bv.rationale}")

        for bv in bullish_votes:
            if bv.confidence < 50:
                divs.append(f"⚠️ {bv.member_name} 看多但低置信度（{bv.confidence}%）：{bv.rationale}")

        return divs

    def to_markdown(self) -> str:
        """Render committee summary as Markdown table."""
        lines = [
            f"╔══════════════════════════════════════════════════════════╗",
            f"║  🗳️ {self.ticker} — 11人投资委员会投票汇总              ║",
            f"╚══════════════════════════════════════════════════════════╝",
            "",
            "┌────────────────────┬──────────────┬──────────────┐",
            "│ 委员               │ 投票          │ 置信度        │",
            "├────────────────────┼──────────────┼──────────────┤",
        ]
        for v in self.votes:
            conf_str = f"{v.confidence}%"
            lines.append(f"│ {v.member_name:<20}│ {v.vote.value:<14}│ {conf_str:<13}  │")
        lines.append("└────────────────────┴──────────────┴──────────────┘")
        lines.append("")
        lines.append(f"【委员会共识】：{self.bullish_count}/11 🟢看多 | {self.neutral_count}/11 🟡中性 | {self.bearish_count}/11 🔴看空")
        lines.append(f"  → 共识强度：{self.consensus_strength}（{self.bullish_count/11*100:.0f}%看多一致）")
        lines.append("")

        if self.divergences:
            lines.append("【主要分歧点】：")
            for d in self.divergences:
                lines.append(f"  {d}")
            lines.append("")

        return "\n".join(lines)


# Pre-defined committee members
COMMITTEE_MEMBERS = [
    {
        "name": "Warren Buffett",
        "title": "价值投资宗师",
        "philosophy": "ROE>15%, D/E<0.5, 持久护城河, 安全边际",
        "key_checks": ["ROE>15%", "D/E<0.5", "护城河评估", "安全边际IV-Price/IV>30%"],
    },
    {
        "name": "Charlie Munger",
        "title": "心智模型大师",
        "philosophy": "资本配置理性, 能力圈, 长期复利, 反向思维",
        "key_checks": ["能力圈边界", "资本配置理性", "护城河可持续年限", "管理层诚信"],
    },
    {
        "name": "Ben Graham",
        "title": "价值投资之父",
        "philosophy": "P/E<15, P/B<1.5, Current Ratio>2, 安全边际>33%",
        "key_checks": ["P/E<15", "P/B<1.5", "Current Ratio>2", "安全边际>33%"],
    },
    {
        "name": "Cathie Wood/ARK",
        "title": "颠覆性成长旗手",
        "philosophy": "AI/S曲线, 5年CAGR>25%, 技术颠覆, 可寻址市场TAM",
        "key_checks": ["5年收入CAGR>25%", "S曲线阶段t0/t1", "TAM增长空间", "分析师覆盖(关注度低=机会)"],
    },
    {
        "name": "Michael Burry",
        "title": "泡沫猎手",
        "philosophy": "泡沫信号, 会计红旗, 最坏情景压力测试, 认知差",
        "key_checks": ["估值vs历史均值", "19项法医红旗", "最坏情景跌幅", "认知差判断"],
    },
    {
        "name": "Ray Dalio",
        "title": "宏观对冲之王",
        "philosophy": "经济周期, 债务周期, 资产相关性, 全天候配置",
        "key_checks": ["经济周期阶段", "债务周期位置", "全天候角色", "地缘政治风险"],
    },
    {
        "name": "Technical Analyst",
        "title": "技术面专家",
        "philosophy": "MA排列, RSI/MACD共振, 成交量确认, 支撑阻力",
        "key_checks": ["MA排列", "RSI(14)", "MACD金叉/死叉", "成交量确认"],
    },
    {
        "name": "Earnings Analyst",
        "title": "盈利质量专家",
        "philosophy": "EPS beat rate, 盈利指引趋势, CFO/PAT, 应收风险",
        "key_checks": ["EPS beat rate(4季)", "盈利指引趋势", "CFO/PAT>0.8", "应收/营收比"],
    },
    {
        "name": "Wall St Consensus",
        "title": "华尔街共识",
        "philosophy": "分析师评级分布, 目标价均值, 覆盖分析师数, 评级变动",
        "key_checks": ["评级分布", "目标价上行空间", "覆盖分析师数", "30天评级变动"],
    },
    {
        "name": "Macro Strategist",
        "title": "宏观策略师",
        "philosophy": "VIX水平, 市场regime, FED利率路径, 地缘政治",
        "key_checks": ["VIX位置", "SPY趋势", "FED利率路径", "地缘政治风险"],
    },
    {
        "name": "Dividend Investor",
        "title": "股息投资者",
        "philosophy": "股息率, 派息比率, 股息增长历史, FCF覆盖率",
        "key_checks": ["股息率", "派息比率<60%", "股息增长连续", "FCF/股息>1.5x"],
    },
]


def create_committee_ticker(ticker: str) -> dict:
    """Initialize committee analysis for a ticker."""
    return {
        "ticker": ticker,
        "members": [{"name": m["name"], "philosophy": m["philosophy"], "status": "pending"} for m in COMMITTEE_MEMBERS],
        "consensus": None,
        "timestamp": None,
    }
