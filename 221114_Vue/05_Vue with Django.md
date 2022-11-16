# 1114 수업자료

- 장고 스켈레톤 코드만 일단 볼 것임
- 뷰까지 보기에는 시간이 없어서 어쩔 수 없다... 따라서 **장고와 연결되는 부분 위주로 볼 것!**


## ~20p

- json 파일을 그대로 가져와서 loaddata하는 구문
- 이때 json 파일 구조와 models 파일 구조는 **완벽하게 동일해야 함**, 하나라도 다르면 오류 뜨더라...
- 그래서 일단 유저 등 모델이 다른 곳은 전부 주석처리로 빼냄. **나중에 해제될 예정**
- serializer는 아직 뭔지는 감을 못잡았지만 views에 serializer 헤더가 있는 걸로 봐선 무조건 써야 할 것으로 예상됨 (데이터를 모아서 한 덩어리로 만드는 느낌?)
- 왜 urls.py에 app 이름을 따로 적어놓지 않았을까? **이걸 어떤건 안 적고 어떤 건 적어도 되나???**
- 더미 json 데이터 가져와서 DRF로 확인하는 작업까진 완료

## ~37p

- 뷰에서 받는 구문
- axios 구문을 이용해 장고 URL을 입력해서 요청 보내서 받는 식임

## ~55p

- SOP이 데이터 교환을 막는다. SOP같은 철통보안!!!!!!!!!!!
- 한마디로 http, localhost, : 8000까지는 동일해야 함
- CORS - 교차 출처 리소스 공유
  - 추가 HTTP 헤더를 써서, 다른 출처의 자원에 접근 가능한 권한을 부여
- django-cors-headers 라이브러리를 사용해서 CORS 헤더를 응답에 추가해줌
  - pip install django-cors-headers
  - pip freeze
  - settings.py에서 **좀 많이** 설정을 바꿔줌
  - 이렇게 하면 Vue에서 데이터를 정상적으로 받을 수 있음
  - 단, django에서 **serializers.py에서 2중 클래스 안의 fields**에 적혀 있는 것만 읽을 수 있음

## ~84p

- Article Read : articles/로 GET 요청을 보내서 받아옴
- Article Create : articles/로 POST 요청을 보내서 받아옴 (하지만 약간 비효율적인 면이? 70p 보기.)
- Article Detail : articles/pk/로 GET 요청

## ~94p

- DRF가 공식적으로 인증하는 방식 중 하나인 TokenAuthentication을 쓸 것!
- INSTALLED_APPS에 rest_framework.authtoken을 등록
- **Token 주는 건 알아서 해야함**. 젠장!!!! 사용법만 알려줬음.
  - **<u>여기까지 했음.</u>**

## ~112p

- dj-rest-auth를 쓰면 회원가입, 인증, 비밀번호 설정, 회원정보 수정 등 REST API end point 제공
- 이거 설치하는 법 나옴, 놀랍게도 view에 뭐 적을 필요 없음 (= **추가 기능 달려면 개고생 당첨!!!!**)
- signup, 비번변경

## ~122p

- 권한 세부 설정
- 드디어 Article List Read : 로그인 필요한 페이지;; 잘 될까? 무슨 페이지인지 보기.

- Article Create
- Article Detail Read
- **122p ㅈㄴ 중요!!!!**
- ...이후 160페이지까지는 계속 Vue였다가 다시 장고로 쭉 나옴.