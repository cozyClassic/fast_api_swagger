# INBODY 코딩테스트 과제

## 서버 실행방법
- $uvicorn app.main:app --reload
- api_docs: [swagger](http://127.0.0.1:8000/docs)

### 가정한 내용
- 체중, 골격근량, 체지방량, 체지방률: 소수점1자리까지 가능
- 최고혈압, 최저혈압, 맥박 : 자연수로만 가능
- 체중,골격근량,체지방량,체지방률,최고혈압,최저혈압,맥박 모두
- 값이 null로 input 되는 상황이 있을 수 있음

### 기타 설명
- user/시간(연월일시분초)이 body_monitor의 unique값인데, 0.5초는 반올림 적용
- database에 unique 처리를 할까 했으나, internal Error(500)이 뜨는게 싫어서 논리로만 적용
- controller 분리할까 했으나, 분량이 많지 않아 보기 편하시라고 합쳐둠

