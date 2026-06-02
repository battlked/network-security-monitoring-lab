# Network Security Monitoring Lab

CCNA와 정보보호 학습 내용을 바탕으로 만든 네트워크 보안 로그 분석 CLI 프로그램입니다.

## What This Program Does

이 프로젝트는 예시 보안 로그를 읽고, 탐지 규칙에 맞는 이벤트를 찾아 위험도와 설명을 출력하는 프로그램 구조입니다.

예상 기능은 다음과 같습니다.

- 로그 파일에서 SSH 스캔, 반복 HTTP 요청 같은 이벤트 탐지
- `config/rules.json`에 있는 규칙을 기준으로 위험도 계산
- 분석 결과를 JSON 리포트로 저장
- 포트폴리오 사이트가 `project.json`을 읽어 프로젝트 카드로 표시

## Repository Structure

- `src/netmon`: Python CLI 프로그램 코드
- `config`: 탐지 규칙 JSON
- `sample-logs`: 발표용 예시 로그
- `reports`: 프로그램 실행 결과 예시
- `docs`: 실행 방법과 리포트 형식 설명
- `project.json`: 포트폴리오 사이트의 Spring Boot Model이 읽는 프로젝트 데이터

## Run

```bash
python -m netmon.cli --log sample-logs/security-alerts.log --rules config/rules.json
```
