from pathlib import Path


def read_alerts(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    return [line for line in lines if "alert" in line.lower()]


if __name__ == "__main__":
    for alert in read_alerts("sample-logs/security-alerts.log"):
        print(alert)
