from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResearchRequest:
    topic: str
    depth: str = "interview-prep"
    fail_agent_once: str | None = None


@dataclass
class ResearchPlan:
    topic: str
    depth: str
    agents: list[str] = field(default_factory=list)


@dataclass
class AgentTask:
    topic: str
    depth: str
    agent: str
    fail_agent_once: str | None = None


@dataclass
class AgentResult:
    agent: str
    finding: str
    evidence: list[str]


@dataclass
class SynthesisInput:
    topic: str
    depth: str
    results: list[AgentResult]


@dataclass
class ResearchBrief:
    topic: str
    depth: str
    summary: str
    findings: list[str]
    retry_lesson: str
