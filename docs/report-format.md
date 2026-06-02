# Report Format

CLI 프로그램은 다음 형태의 JSON 리포트를 출력합니다.

```json
{
  "sourceLog": "sample-logs/security-alerts.log",
  "totalEvents": 3,
  "severitySummary": {
    "HIGH": 1,
    "MEDIUM": 1,
    "LOW": 1
  },
  "events": []
}
```

## Fields

- `sourceLog`: 분석한 로그 파일 경로
- `totalEvents`: 탐지된 이벤트 개수
- `severitySummary`: 위험도별 이벤트 개수
- `events`: 탐지 규칙과 원본 로그 목록
