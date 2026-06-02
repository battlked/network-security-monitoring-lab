from netmon.analyzer import DetectionRule, analyze_logs, count_by_severity


def test_analyze_logs_detects_matching_keyword():
    rules = [
        DetectionRule(
            name="Possible SSH Scan",
            keyword="ssh scan",
            severity="HIGH",
            description="SSH scan detected",
        )
    ]
    lines = ["2027-04-10 alert Possible SSH scan from 10.0.0.15"]

    events = analyze_logs(lines, rules)

    assert len(events) == 1
    assert events[0].severity == "HIGH"


def test_count_by_severity_counts_events():
    rules = [
        DetectionRule("SSH", "ssh scan", "HIGH", "SSH scan"),
        DetectionRule("HTTP", "http request", "MEDIUM", "HTTP request"),
    ]
    lines = ["ssh scan", "http request", "ssh scan"]

    events = analyze_logs(lines, rules)
    result = count_by_severity(events)

    assert result["HIGH"] == 2
    assert result["MEDIUM"] == 1
