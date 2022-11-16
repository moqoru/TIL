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

## ~112p

- signup, 비번변경 등 accounts를 한방에 해결해주는 pip install

- dj-rest-auth를 쓰면 회원가입, 인증, 비밀번호 설정, 회원정보 수정 등 REST API end point 제공

- 이거 설치하는 법 나옴, 놀랍게도 view에 뭐 적을 필요 없음 (= **추가 기능 달려면 개고생 당첨!!!!**)

- DB 한번 리셋, AUTH_USER_MODEL = 'accounts.User'로 적용

- pip install dj-rest-auth

- settings.py에 INSTALLED_APPS에 'dj_rest_auth', 추가

- 그런데 accounts 모델에 추가 정보가 있는데, 괜찮을까? 일단 DB 다시 migrate

- **100p 꼭 보기! url이 꼭 dj_rest_auth.urls여야만 한다!!**

- pip install 'dj-rest-auth[with_social]'

- settings.py에... 좀 넣을 거 많음

  ```python
  INSTALLED_APPS = [
  	'django.contrib.sites',
      'allauth',
      'allauth.account',
      'allauth.socialaccount',
      'dj_rest_auth.registration',
  ]
  
  SITE_ID = 1 # 다수의 도메인이 하나의 DB에 등록, 현재 프로젝트가 1번째 사이트
  ```

- urls.py에 이거 추가하고, 또 migrate...

  ```py
      path('accounts/', include('dj_rest_auth.urls')),
      path('accounts/signup/', include('dj_rest_auth.registration.urls')),
  ```

- 이제 /accounts/로 들어가거나 /accounts/signup/으로 들어가면...?

- 비번 변경은 어케 하죠? 일단 settings.py에...

  ```python
  REST_FRAMEWORK = {
      # Authentication
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ],
  ```

- 이후 accounts/password/change/로 들어가면? 이건 POSTMAN으로 해야함! 걍 교재봐...

## ~122p

- 권한 세부 설정

- 드디어 Article List Read : 로그인 필요한 페이지;; 잘 될까? 무슨 페이지인지 보기.

- 일단 setting에서...

  ```python
      # permission
      'DEFAULT_PERMISSION_CLASSES': [
          # 'rest_framework.permissions.IsAuthenticated',
          'rest_framework.permissions.AllowAny',
      ],
  ```

- 그리고 views.py에 데코레이터를 붙이면...?

  ```python
  # permission Decorators
  from rest_framework.decorators import permission_classes
  from rest_framework.permissions import IsAuthenticated
  
  @api_view(['GET', 'POST'])
  @permission_classes([IsAuthenticated])
  def article_list(request):
      if request.method == 'GET':
          # articles = Article.objects.all()
          articles = get_list_or_404(Article)
          serializer = ArticleListSerializer(articles, many=True)
          return Response(serializer.data)
      ...
  ```

- 이제 로그인 해야 article read가 가능!!!

- Article Create
- Article Detail Read
- **122p ㅈㄴ 중요!!!!**

## 164~p

- 드디어 model.py를 고쳐도 됨. 이건 아직 안 했음
- 그 상태에서 makemigrations 해주면 드디어 에러가 안 남
- serializer.py와 view.py를 수정

- ...이후 160페이지까지는 계속 Vue였다가 다시 장고로 쭉 나옴.

## 175~p

- SWAG 넘치는 기능 ~~아님~~
- pip install drf-spectacular

- setting 바꾸기

  ```python
  INSTALLED_APPS = [
      # OpenAPI 3.0
      'drf_spectacular',
  ]
  
  REST_FRAMEWORK = {
      # Authentication
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework.authentication.TokenAuthentication',
      ],
      
      # permission
      'DEFAULT_PERMISSION_CLASSES': [
          # 'rest_framework.permissions.IsAuthenticated',
          'rest_framework.permissions.AllowAny',
      ],
  
      # spectacular Settings
      'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
  }
  
  SPECTACULAR_SETTINGS = {
      'TITLE': 'Your Project API',
      'DESCRIPTION': 'Your project description',
      'VERSION': '1.0.0',
      'SERVE_INCLUDE_SCHEMA': False,
      # OTHER SETTINGS
  }
  ```

- 그 다음에 community/urls.py에...

  ```python
  from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
  
  urlpatterns = [
  
      path('schema/', SpectacularAPIView.as_view(), name='schema'),
      # # optional UI
      path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
  ]
  ```

- http://127.0.0.1:8000/community/swagger/