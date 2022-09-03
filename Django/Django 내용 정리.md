# 1. Django 기본 세팅

- 장고 마음가짐
  - 장고의 대부분의 에러는 오타이거나, 파일 하나를 저장을 안한 곳에서 나온다.
  - 에러가 자세히 나오기는 하지만 너무 심하게 자세하므로 뒤에서부터 본다. (특정 에러는 어느 부분을 봐야 할지 외우는 게 좋다?)
  - 초반에는 프로젝트 하나를 만들 때마다 가상환경을 일일이 만드는 편이 연습하기엔 훨씬 좋다.
  - 장고의 url은 맨 뒤에 /가 항상 붙는다고 생각하자! 보통은 생략하지만 실제로는 /가 붙냐 안 붙냐가 서로 다른 주소를 가리킴...
  - 또한 딕셔너리에 값을 입력할 때, 항상 맨 뒤에 ,를 붙여 두자! 언제 그 뒤에 변수가 올 지 모르므로 대비하는 느낌으로 적어두자.
  - Django 프로젝트에서 html은 python 구문의 일부를 유사하게 쓸 수 있지만, 어디까지나 받아온 정보를 보여주는 방식을 다르게 할 뿐이므로 진짜 python을 돌리는 것과는 다르다. 연산을 직접 하는 것도 아니고 그냥 추가 장식 용도이므로 연산이 필요한 곳은 무조건 .py 파일들에서 다 준비해두자!
- 첫 세팅
  - VScode 상에 Django를 미리 깔아 둔다.
  - 만들려는 디렉토리 상에서 다음과 같이 진행한다.
    - mkdir (전체 폴더명)/
    - cd (전체 폴더명)/
    - python -m venv venv => 가상 환경을 처음 만들 때 쓰는 구문이다! (전체 폴더명)/venv 폴더가 만들어진다. **나중에 또 입력하면 가상환경 폴더를 또 새로 만들어버리니 주의!**
    - source venv/Scripts/activate => 가상 환경을 구동시킨다.
    - pip install django==3.2.13 => 장고 3.2.13 버전을 설치한다.
      - pip install ipython
      - pip install django-extensions
    - pip freeze > requirements.txt => 현재 pip로 설치된 모든 프로그램들을 requirements.txt에 저장하며, 나중에 가상 환경을 다시 구동할 때는 pip install requirements.txt로 텍스트 파일 안에 있던 모든 프로그램들을 한 번에 깔 수 있다.
    - django-admin startproject (프로젝트명) . => 장고 프로젝트를 생성한다.
    - python manage.py runserver
      - 결과로 나온 http://127.0.0.1:8000/ 을 ctrl+클릭하면 완성한 장고 웹페이지에 들어갈 수 있다.
      - 주소창에서 이 뒤에 index/ 등을 붙이면 코드로 구현된 웹페이지를 바로 볼 수 있다.
      - 종료할 때는 터미널 창에서 ctrl+c를 누른다.
- 디렉토리 안의 구조 설정하기
  - python manage.py startapp articles
  - python manage.py startapp pages => 이 두 구문은 **폴더를 직접 만들지 말고 무조건 이 구문으로 깔아야 한다**! 그래야 폴더 안의 각종 .py 구문들이 기본 세팅으로 들어올 수 있다.
    - vscode에서 material icon theme를 깔아주면 그냥 폴더와 startapp 구문으로 깐 디렉토리가 아이콘으로 구분이 되므로, 필수적으로 깔아두자!
  - (프로젝트명) 폴더/settings.py를 열어준 뒤...
    - INSTALLED_APPS = [] 부분을 찾아가서 설치한 라이브러리를 불러올 수 있게 하기 위해 추가해 준다. 반드시 제일 앞에 넣어줄 것! (암묵적인 정의 : 커스텀 > 서드파티 > 기본 순서대로 기록)
      - 'articles', 'django_extensions',
    - TEMPLATES = [] 부분을 찾아가서 'DIRS' : 옆에 있는 [] 안에 라이브러리를 불러오기 위해 명기해 준다.
      - 만약 templates 폴더를 아래와 같이 만들 경우, [BASE_DIR / 'templates']로 바꿔준다.
      - 원래라면 templates 폴더는 articles 폴더 아래에 있어야 하지만, 한칸 밖으로 빼내서 (전체 폴더명) 아래, 즉 (프로젝트명) 폴더와 같은 단계에 있는게 관리하기가 더 편하므로 이렇게 바꿔준다!
  - templates 폴더를 만들어준다. 이 아래에 .html 문서들이 들어간다!
    - 기본 위치는 articles 폴더 아래,
    - 위에서 TEMPLATES 설정을 바꿔준 경우에는 (전체 폴더명) 아래에 만들어준다.

# 2. Django 파일 구조

## 2-1. 기본 폴더 위치대로 만들기

- 기본 구조 짜기 : 항상 urls.py -> views.py -> .html로 이어진다!

- 먼저 templates 폴더를 (프로젝트명) 폴더 아래에 만드는 경우로 설명.

  - 일단은 (프로젝트명)/urls.py에 from articles import views를 적어주고, urlpatterns = 안에 path('index/', views.index),를 적어준다.

    ```python
    # pjt/urls.py
    from django.contrib import admin
    from django.urls import path
    from articles import views
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('index/', views.index),
    ]
    ```

  - 그 다음, articles/views.py에 아래와 같이 적는다.

    ```python
    # articles/views.py
    from django.shortcuts import render
    
    def index(request):
        foods = ['apple', 'banana', 'coconut',]
        info = {
            'name': 'Moqoru'
        }
        context = {
            'foods': foods,
            'info': info,
        }
        return render(request, 'index.html', context)
    ```

    - render(request, template_name, context)
      - request는 요청 객체, template_name은 템플릿 경로, context는 템플릿에서 쓸 데이터이다.
      - context는 딕셔너리 타입으로 적어야 하며, 생략할 수도 있다.

  - articles 폴더 밑에 templates 폴더를 만들고 html 문서를 만든다.

    ```django
    <!-- articles/templates/index.html -->
    <!-- 느낌표 치고 Tab 치기! -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <p> 안녕하세요 제 이름은 {{ info.name }} 입니다. </p>
      <p> 제가 가장 좋아하는 과일은 {{ foods.0 }} 입니다. </p>
    </body>
    </html>
    ```

  - 이제 http://127.0.0.1:8000/index/ 로 접속하면...?

- DTL (Django Template Language)

  - html 안에서 python과 유사한 구문을 쓸 수 있지만, 실제 파이썬 구문은 아니니 주의!
    - 그냥 파이썬 스럽게 스킨을 살짝 씌우는 수준이므로 진짜 파이썬 코드가 필요하면 .py 구문들에서 작성하자.
  - 이하 모든 구문은 기존 html처럼 영어 부분만 적고 Tab을 치면 자동완성으로 미리 만들어주니 적극 활용!
  - {{ variable }}
    - 말 그대로 변수이며, 아까 views.py에서 딕셔너리로 넘겨준 context 값 중 딕셔너리의 key 부분을 변수명으로 사용할 수 있음
    - variable.0 같은 식으로 쓰면 딕셔너리의 value 부분이 리스트일 떄 그 리스트나 딕셔너리의 인덱스까지 참조할 수 있음
    - | filter 식으로 변수에 필터를 걸 수 있다. |lower나 |upper, |truncatechar: 5 식으로 쓸 수 있음.
  - {% tag %}
    - if나 for 등의 구문을 쓸 수 있음
    - 종료 구문이 필요한 경우가 있어, endif 같은 구문도 사용
  - {# 주석 #}
    - 주석 구문
    - 여러줄 주석의 경우 {% comment %} 줄과 {% endcomment %} 줄 사이에 입력

## 2-2. 파일 분할하고 폴더 위치 이리저리 옮겨보기

- DTL에서 계속... 먼저 html부터 분할하려면?

  - {% extends 'base.html' %}

    - 자식 html 파일의 최상단에 작성되어야 함
    - 자식 템플릿이 부모 템플릿을 상속받아 확장할 수 있음

  - {% block content %} 와 {% endblock content %}

    - 둘 사이는 자식 템플릿이 재정의할 수 있는 공간
    - 부모 템플릿은 block과 endblock 사이를 뻥 비워서 전체적인 틀로 활용하고, 자식 템플릿은 extends와 block 구문만 넣고 block 구문 사이에 자세한 내용을 입맛에 맞게 적어넣는 식으로 사용!

  - .html 파일 분할하기

    ```django
    <!-- articles/templates/base.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      {% block content %}
      
      {% endblock content %}
    </body>
    </html>
    ```

    ```django
    <!-- articles/templates/index.html -->
    {% extends 'base.html' %}
    {% block content %}
      <p> 안녕하세요 제 이름은 {{ info.name }} 입니다. </p>
      <p> 제가 가장 좋아하는 과일은 {{ foods.0 }} 입니다. </p>
    {% endblock content %}
    ```

    - 이때, **부모 템플릿은 따로 urls.py와 views.py에 추가해서 넣을 필요는 <u>없다</u>!**
      - 위 예시로 들면 index는 정보를 넣어줘야 하지만 base는 딱히 명기 안 해 줘도 돌아간다!

- template 폴더를 옮기려면?

  - 1번 항목에서...

    ```
    만약 templates 폴더를 아래와 같이 만들 경우, [BASE_DIR / 'templates']로 바꿔준다.
    ```

    라고 했던 것 기억나는가? 바로 해보자!

    ```python
    # pjt/settings.py
    ...
    INSTALLED_APPS = [
        'articles',
        'django_extensions',
        ...
    ]
    ...
    TEMPLATES = [
        {
            ...
           'DIRS': [BASE_DIR / 'templates'],
            ...
        }
    ]
    ```

  - settings.py를 바꿔 줬다면 이제 templates 폴더를 (전체 폴더명) 밑으로, 즉 최상위로 빼낼 수 있다!

- url.py 분할하기

  - url을 분할하면 각 app(아이콘 달린 폴더들) 별로 url 스킨을 위탁할 수 있음

  - pages, articles에 urls.py를 각각 추가로 만들고 원래의 (프로젝트명)의 urls.py까지 순차적으로 수정

    ```python
    # articles/urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('index/', views.index),
    ]
    ```

    ```python
    # pages/urls.py
    from django.urls import path
    #from . import views => pages의 views는 미작성 상태이므로
    
    urlpatterns = [
    	# 적어도 빈 리스트라도 있어야 에러가 안 남!!!
    ]
    ```

    ```python
    # pjt/urls.py
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('articles/', include('articles.urls')),
        path('pages/', include('pages.urls')),
    ]
    ```

    - 이때, 아쉽게도 pages와 articles에 먼저 쓰고 (프로젝트명)의 urls.py를 수정해야 한다...
      - 자식 먼저, 부모를 나중에 수정하기!

  - 이렇게 하면 메인 페이지의 주소가 http://127.0.0.1:8000/articles/index/ 로 바뀜. articles가 추가되었음!

    - 그러면... 주소 하나 바꿀 때마다 html 안에서 하이퍼링크로 썼던 주소들을 다 찾아가서 바꿔야 하나...?

  - 그래서 urls.py에서 path를 적을 때 name을 추가로 적어준다!

    ```python
    # articles/urls.py
    from django.urls import path
    from . import views
    
    urlpatterns = [
        path('index/', views.index, name='index'),
    ]
    ```

  - 그리고 html 파일에서는 {% url '' %}을 써서 받아온 변수명을 url 주소로 쓸 수 있다!

    ```django
    <!-- articles/templates/index.html -->
    {% extends 'base.html' %}
    {% block content %}
      <p> 안녕하세요 제 이름은 {{ info.name }} 입니다. </p>
      <p> 제가 가장 좋아하는 과일은 {{ foods.0 }} 입니다. </p>
      <a href="{% url 'index' %}"> 인덱스 페이지 </a>
    {% endblock content %}
    ```

    - 저 index라는 변수가 articles/index를 저절로 가리키게 된다!

  - throw랑 catch는 좀 나중에 하자...
