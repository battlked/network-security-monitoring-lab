from dataclasses import dataclass
from typing import Iterable


@dataclass
class DetectionRule:
    name: str
    keyword: str
    severity: str
    description: str


@dataclass
class SecurityEvent:
    rule_name: str
    severity: str
    description: str
    raw_log: str


def analyze_logs(lines: Iterable[str], rules: Iterable[DetectionRule]) -> list[SecurityEvent]:
    events: list[SecurityEvent] = []

    for line in lines:
        lowered_line = line.lower()
        for rule in rules:
            if rule.keyword.lower() in lowered_line:
                events.append(
                    SecurityEvent(
                        rule_name=rule.name,
                        severity=rule.severity,
                        description=rule.description,
                        raw_log=line.strip(),
                    )
                )

    return events


def count_by_severity(events: Iterable[SecurityEvent]) -> dict[str, int]:
    result: dict[str, int] = {}

    for event in events:
        result[event.severity] = result.get(event.severity, 0) + 1

    return result
