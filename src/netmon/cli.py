import argparse
import json
from pathlib import Path

from netmon.analyzer import DetectionRule, analyze_logs, count_by_severity


def load_rules(path: Path) -> list[DetectionRule]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return [DetectionRule(**item) for item in data]


def build_report(log_path: Path, rule_path: Path) -> dict:
    lines = log_path.read_text(encoding="utf-8").splitlines()
    rules = load_rules(rule_path)
    events = analyze_logs(lines, rules)

    return {
        "sourceLog": str(log_path),
        "totalEvents": len(events),
        "severitySummary": count_by_severity(events),
        "events": [event.__dict__ for event in events],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Network security log monitoring CLI")
    parser.add_argument("--log", required=True, help="Path to security log file")
    parser.add_argument("--rules", required=True, help="Path to detection rule JSON")
    parser.add_argument("--output", default="", help="Optional output report JSON path")
    args = parser.parse_args()

    report = build_report(Path(args.log), Path(args.rules))
    report_json = json.dumps(report, ensure_ascii=False, indent=2)

    if args.output:
        Path(args.output).write_text(report_json, encoding="utf-8")
    else:
        print(report_json)


if __name__ == "__main__":
    main()
