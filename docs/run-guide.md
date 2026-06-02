# Run Guide

## Requirements

- Python 3.10 이상

## Run Without Install

```bash
set PYTHONPATH=src
python -m netmon.cli --log sample-logs/security-alerts.log --rules config/rules.json
```

## Save Report

```bash
set PYTHONPATH=src
python -m netmon.cli --log sample-logs/security-alerts.log --rules config/rules.json --output reports/latest-report.json
```

## Portfolio Use

포트폴리오 사이트에서는 이 저장소의 `project.json`을 읽고, `artifactUrl` 값으로 이 실행 안내 문서를 연결합니다.
