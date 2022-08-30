# 1. HTML(Hyper Text Markup Language)

## 1) 태그 사용 기초

- 시작하기
  - 맨 처음 시작할 때는 html 파일을 만들고 VSCode를 연다. 그리고 !를 치고 탭을 치면 기본 틀이 완성된다.
  - 이와 비슷한 방식으로, 가령 \<div>를 만들려면 div를 치고 탭을 치면 자동으로 열고 닫는 태그가 완성된다.
  - 저장한 뒤 실행시키면 인터넷 창에서 열 수 있으며, 크롬 브라우저에서 F12를 누른 뒤 개발자 도구를 이용하여 각 요소를 전체 / 실제 적용 부분 별로 확인할 수 있다. (각각 styles, computed) 또한 Element에서 해당 태그를 체크 설정 / 해제하면서 비교할 수 있다.
  - HTML 문서에 대한 모델을 구성한 트리를 DOM(Document Object Model) 트리라고 함
- 태그의 사용법
  - 보통 열고 닫는 사이에 내용을 감싸는 것으로 표현, 간혹 내용이 없어 닫는 태그가 없는 img, input, link 등의 태그도 있다.
  - <>로 둘러싸인 속성 안에서는 보통 (뭐시기="") 식으로 쓰며, 한 요소 안에서는 띄어쓰기를 쓰지 않는다! 요소끼리 구분하거나 여러 요소가 함께 들어갈 때 띄어쓰기를 쓴다.
  - 태그 안에 태그를 중첩하는 식으로 작성하며, 
- 태그의 종류
  - \<head> 부분에는 문서를 꾸밀 \<style>을 넣거나 참조할 CSS 주소를 \<link>로 넣고, \<body> 부분의 대부분의 내용이 들어간다. 
  - \<div>는 가장 많이 쓰는 태그로, **글상자 취급되는** 기본 블록 레벨 컨테이너를 뜻한다.
  - \<span>은 인라인 컨테이너를 뜻한다.
  - \<h1>, \<h2>, ...는 헤더 태그로, 제목 부분을 표시한다. \<p>는 한 줄 단위의 글이다.
  - \<a>는 하이퍼링크를 생성하는 태그이다.
  - \<img>(닫는 태그 없음!)는 이미지를 표현하는 태그이다.
  - \<form>은 정보를 서버에 제출할 때 사용하는 태그
  - \<input>(닫는 태그 없음!)은 데이터를 입력하는 태그이다.
  - \<hr>은 수평선을 생성하는 태그이다.
- 시맨틱 태그 - HTML 5에서 추가된 의미를 담은 태그들, 보통 이 태그들 안에 \<div>, \<hn>,  \<img> 등의 태그를 넣어 본문으로 작성한다.
  - \<header> - 문서 전체의 머리말 부분
  - \<nav> - 좌측 사이드(네비게이션) 부분
  - \<aside> - 우측 사이드 부분
  - \<footer> - 문서의 꼬리말, 마지막 부분
  - \<section> - 문서의 중앙 메인 부분, 컨텐츠의 그룹을 표현
    - section 안에도 header와 footer 부분이 있다.
    - \<article> - 독립적으로 구분되는 알짜배기 중앙 영역

## 2) 각 태그들의 사용 방법

```html
<div class="box black" id="red"></div>
```

- 기본적으로 div에는 자신을 가리킬 수 있는 class와 id 정보를 넣어주고, 나중에 이걸 가리켜서 꾸밀 수 있게 해 준다.
  - box black으로 클래스를 작성하면 나중에 box 클래스 따로, black 클래스 따로 스타일을 지정해서 중첩시킬 수 있다.
  - class는 같은 이름을 중복해서 계속 쓸 수 있지만, id는 같은 이름은 한 번만 쓸 수 있다.

```html
<h1 style="color: blue; font-size: 100px">Hello</h1>
```

- 태그 안에 직접 style 속성을 활용한 것이며, 이를 인라인 스타일이라고 한다.

```html
<style>
    class1, class2
    class3 {
        color: red;
    }
</style>
```

- \<head> 부분 안에서 \<style>에 클래스 이름을 적고 {}로 감싸 꾸며줄 수 있다.
  - 이를 내부 참조라고 하며, 한번에 여러 클래스를 지정할 때는 ,로 구분한다.

```html
<link rel="stylesheet" href="aaa.css">
```

- \<head> 부분에 넣어 html과 css를 연결시키는 코드이며, href에 css 파일명을 넣는다.
  - 위의 \<style> 부분을 css 파일에 따로 적는 개념이며, 이것을 외부 참조라고 한다.

```html
<form action="/search" method="GET">
    <input type="text" name="q">
</form>
```

- 구글 검색창 부분의 코드이다.
  - form에서 action은 데이터를 보낼 곳의 URL, method는 사용할 HTTP 메서드를 뜻한다.
  - enctype은 데이터의 유형을 뜻한다.
  - input에서 name은 form control에 적용되는 이름, value는 적용되는 값

```html
<label for="agreement"> 개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - label의 for 속성과, input의 id 속성을 일치시켜 연관시킴

```html
<a href="#women" class="text-grey">Women's</a>
...
<div class="section-aside" id="women"></div>
```

- 마찬가지로 파일 하나의 내부에도 하이퍼링크를 나타내는 a의 # class와 div의 id를 맞추면 클릭했을 때 본문의 해당 부분으로 이동하는 코드를 짤 수 있다.
  - **이후의 많은 구문에서도 가리키는 구문의 class와 호출되는 구문의 id 맞추기는 중요!**


```html
<img src="./images/women.PNG" class="img-width" alt="women img">
```

- \<img>에서 src에는 이미지 주소(온라인 상의 주소를 쓸 수도 있다), class는 생략, alt는 오류났을 때 대체해서 표시할 텍스트를 기록한다.

# 2. CSS(Cascading Style Sheets)

- 칙칙한 HTML을 좀 더 있어보이게 꾸며준다.

- **모든 요소는 박스 모델(네모)이고, 위에서 아래로, 왼쪽부터 오른쪽으로 쌓인다.**

- 기본 구문

  ```css
  h1, h2{
      color: blue;
      font-size: 15px;
  }
  ```

  - h1, h2를 선택자, : 부분을 속성, ; 부분을 값이라고 한다.

- 선택자

  ```css
  <style>{
      /*전체 선택자*/
  }
  h1{
      /*요소 선택자*/
  }
  .box{
      /*클래스 선택자*/
  }
  #idw{
      /*id 선택자*/
      color: black !important;
  }
  ```

  - 요소 선택자 : HTML 태그를 직접 선택한다. 예시) \<style> {}, h1 {}
  - 클래스 선택자 : . 사용, 해당 클래스를 선택한다. 예시) .box {}
  - id 선택자 : # 사용, 해당 아이디가 적용된 항목을 선택한다. 예시) #idw {} 

  - 우선순위: !important > 인라인 스타일 > id 선택자 > class 선택자 > 요소 선택자 > 순서
    - !important를 ;가 나오기 전에 덧붙이면 다른 모든 것보다 우선하게 되고, 범위가 좁은 것이 우선순위가 높다.
    - 여기서 코드 순서는 css 상에서 작성된 순서가 더 뒤인 것이 우선으로, html에서 class="2 1"로 2개 클래스를 같이 적었더라도 **css에서 .1{} .2{} 순서대로 적었다면 2가 우선이다!!!**

- 상속

  - html 코드상에서 중첩되어 들어간 코드는 상위 요소의 일부 속성들을 하위 요소에서 상속받아 그대로 이용할 수 있다.
  - 속성 중에서 text 관련 요소는 상속되지만, box model과 position 관련 요소는 상속되지 않는다.

- 크기 단위

  ```css
  .myclass{
      width: 300px;
      height: 50vw;
      margin: auto;
      padding: 70%;
      font-size: 2rem;
  }
  ```

  - px : 픽셀, 고정적인 단위
  - % : 백분율, 가변 레이아웃에서 사용
  - em : 배수 단위, 상속의 영향을 받으며 요소에 지정된 사이즈 기준 상대적 크기
  - rem : 배수 단위, 상속 없이 최상위 요소(html) 기준 상대적 크기
  - vw : viewport, 픽셀처럼 사용하지만 인터넷 창의 크기에 따라 가변적으로 변함
  - **값을 어떻게 할 지 모를 경우 auto도 사용할 것!**

- 색상 단위

  ```css
  .article {
      background-color: white;
      color: black; /* '글상자' 취급이라서 text-color가 아니라 그냥 color가 글자 색상이다.*/
  }
  ```

  - black; 등으로 직접 키워드 쓸 수 있음
  - #000000; rgb(0, 0, 0);
  - hsl(120, 100%, 0); 색상, 채도, 명도
  - rgba 나 hsla는 4번째 항목으로 투명도를 더 지정할 수 있음

- 결합자

  ```css
  div span { color: red; } /* 자손 결합자*/
  div > span { color: red; } /* 자식 결합자*/
  p ~ span { color: red; } /* 일반 형제 결합자 */
  p + span { color: red; } /* 인접 형제 결합자 */
  ```

  - 자손 결합자(space) : A 하위의 모든 B 요소를 선택 **(A 안에 C 안에 B여도 B 적용 가능)**
  - 자식 결합자(>) : A 바로 하위 단계의 B 요소만 선택 **(A 안에 C 안에 B면 B 적용 불가)**
  - 일반 형제 결합자(~) : A의 형제 요소(같은 들여쓰기) 중 뒤에 있는 모든 B 요소를 선택
  - 인접 형제 결합자(+) : A의 형제 요소(같은 들여쓰기) 중 바로 뒤에 있는 B 요소만 선택

- box model

  ```css
  .box {
      width: 100px;
      margin-left: 10px;
      padding: 20px;
      border: 1px solid black; /* dashed나 dotted도 있음 */
      border-radius: 4px; /* 테두리를 둥글게 깎는 코드 */
  }
  ```

  - Margin(외부 여백, 색 지정 불가) > Border(테두리) > Padding(내부 여백, 배경색이나 이미지 적용 가능) > Content (내부 실제 내용)
  - Margin이나 Padding은 4개까지 적을 수 있지만 더 적게 적을 수도 있는데, 시계방향으로 돌면서 부족한 개수는 대칭으로 맞춰 들어간다고 생각하면 된다.
  - 또한 margin-left, padding-bottom 등으로 세부적으로 지정할 수도 있다.

- display

  ```css
  .classA {
      display: inline-block;
      /*display: inline;*/
      /*display: block;*/
      font-size: 0;
  }
  ```

  - block 요소

    - 한 줄 전체를 차지하며 줄 바꿈이 일어나고, 각종 속성 지정이 가능하다.
    - 블록 안에 인라인이 들어갈 수 있다.
    - div, form 등

  - inline 요소

    - content 너비만큼만 가로 폭을 차지하며 줄 바꿈이 일어나지 않고, 폭, 너비, margin의 상하 속성 지정이 불가능하다.
    - img, a, span 등

  - inline-block 요소

    - 퓨전! inline처럼 한 줄에 여러 개 표시할 수 있으면서도 속성 지정에 제한이 없다.
    - 사실상 가장 많이 쓴다.

    - 이 형식이 원래 글상자용이라, **글자가 하나도 없어도 font-size: 0; 구문을 넣어줘야 한다. 아니면 글자 들어갈 약간의 여백이 지워지지 않고 남는다!**

  - none, hidden

    - none은 아예 없는 취급이고, hidden은 렌더링은 되어 있어서 다른 게 자리차지 못하게 와드는 남아 있는 상태

- position

  ```css
  #bepis{
      position: absolute;
      top: 200px;
      left: 200px;
      /*position: relative;*/
      /*position: fixed;*/
      /*position: sticky;*/
      /*bottom: 0;*/
      /*right: 0;*/
  }
  ```

  - relative : 스태틱 위치 또는 부모 요소의 기준 위치(좌측 최상단)에 와드 하나 박고 이동함, 와드 박힌 위치에는 딴 게 못 옴, normal flow 유지됨
    - 다른 게 와드에 막혀 밀려날 때는 보통 바로 아래로 밀려나는데, 블록 레벨 요소라서 같은 줄에는 못 들어가기 때문이다.
  - absolute : 무조건 가장 가까이 있는 부모 요소나 브라우저 화면 기준으로 이동, normal flow에서 벗어나서 상속 같은 것도 새로 지정해줘야 함
  - fixed : 스크롤을 해도 항상 같은 곳에 위치, 마찬가지로 normal flow에서 벗어남
  - sticky : 스크롤에 따라 static -> fixed로 변경, 스크롤 위치가 임계점에 다다르면 fixed처럼 화면에 고정할 수 있음
  - 보통은 relative를 많이 쓰고, 필요한 경우에만 absolute와 fixed를 사용

- 그 외

  ```css
  #etc {
      vertical-align: top;
      text-align: center;
      background-image: url("chess_img/black_pawn.png");
      background-size: contain;
      opacity: 80%;
      font-family: Arial; /*family = 글꼴*/
    	font-size: 20px; /*size = 크기*/
    	font-weight: bold; /*weight = 굵게, 이탤릭체는 style로 하는듯*/
  }
  ```

  - vertical-align으로 세로 방향의 위치도 정렬 가능, 가로도 될듯?
  - text-align으로 글자의 위치 정렬 가능, 참고로 세로도 따져서 top이나 bottom을 써야함
  - background image를 넣을 때는 url("참조 주소")로 적은 뒤, 배경 size를 적어 줘야 이미지가 안에 깔끔하게 맞춰서 들어갈 수 있다.
  - opacity는 전체의 투명도를 조절한다.
  - font에서 family가 글꼴, size는 크기, weight는 굵게 여부를 조절한다. 이탤릭체는 style을 사용한다.



