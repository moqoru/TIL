# 3. CSS(Cascading Style Sheets) 추가 내용

## 1) Float

- 용도
  - 모든 요소는 네모(박스 모델)이므로, 위->아래, 왼쪽->오른쪽으로 쌓임.
  - 다른 요소를 감싸면서 배치하거나 좌, 우측에 따로 배치하도록 함
  - 한컴오피스의 **어울림** 설정을 떠올리면 쉬움.
  
- 사용법
  
  ```html
  ...
    <style>
      /* css 작성 */
      .box {
        width: 150px;
        height: 150px;
        border: 1px solid black;
        background-color: crimson;
        margin: 20px;
      }
      .left {
        float: left;
      }
      .right {
        float: right;
      }
    </style>
  ...
  <body>
    <div class="box left">float left</div>
    <div class="box left">float left</div>
    <div class="box right">float right</div>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur veritatis, debitis vitae, est illo enim ipsum dolores, animi voluptatibus eius magnam. Reprehenderit expedita animi illo cum fugiat sint quos fugit!
    </p>
  </body>
  ```
  
  - 박스 3개가 각각 왼쪽 2개, 오른쪽 1개에 생성되고, 글자는 알아서 박스들을 피해서 배치
  
  ```html
  ...
    <style>
      .left {
        float: right;
      }
      .clearfix::after {
        content: "";
        display: block;
        clear: both;
      }
    </style>
  ...
  <body>
    <header class="clearfix">
      <div class="box1 left">box1</div>
    </header>
    <div class="box2">box2</div>
    <div class="box2">box3</div>
    <div class="box2">box4</div>
  </body>
  ```
  
  - .clearfix::after 구문으로 float 요소를 감싸면 float 이후 요소들을 정상적으로 배치 가능함.
    - clearfix 구문은 예제의 css 구문 전체가 한 덩어리라고 생각하는 게 편함.

## 2) flex

- 플렉스는 꼬치다! ~~양꼬치로 Flex!~~

  - https://flexboxfroggy.com/#ko 에서 연습하기

- 기본 구문 : **여러 요소들을 배치하는 구문은 display: flex;를 적어야 적용된다!**, 한 개는 괜찮음

  ```css
  .flex-container{
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    /*flex-flow: row wrap*/
    justify-content: space-between;
    align-items: center;
  }
  .one_only{
    order: 2;
    flex-grow: 1; 
    align-self: flex-start;
  }
  ```

  ```html
  <div class="flex-item grow-1 order-3"> <!-- html 인라인으로 쓸 경우. -->
      AAAA
  </div>
  ```

- flex-direction : Flex box의 주축(main axis)를 변경

  - row : 첫 줄은 왼쪽에서 오른쪽으로, 그 다음 줄은 아래로 붙게 배치
  - row-reverse : 첫 줄은 오른쪽에서 왼쪽으로, 그 다음 줄은 아래로 붙게 배치
  - column : 첫 줄은 위쪽에서 아래쪽으로, 그 다음 줄은 오른쪽으로 붙게 배치
  - column-reverse : 첫 줄은 아래쪽에서 위쪽으로, 그 다음 줄은 오른쪽으로 붙게 배치
  - 주축과 교차축의 가로/세로, 방향이 flex-direction에 맞춰 전부 변경됨
    - column-reverse의 경우 main axis는 아래->위, cross axis는 왼쪽->오른쪽이 됨

- flex-wrap : 여러 개의 요소들을 여러 줄에 나누어서 정렬할 지 여부 설정

  - nowrap : 기본, 한 줄에 모든 요소들을 정렬
  - wrap : 여러 줄에 걸쳐 정렬, 한 줄이 너무 길면 그 다음 요소는 다음 줄로 밀림
  - wrap-reverse : 여러 줄에 걸쳐 반대로 정렬. 첫 번째 요소가 마지막 줄 가장 첫 번째 위치로 가고, 두 번째 줄은 마지막 줄의 윗 줄로 들어간다.

- flex-flow : flex-direction-wrap를 합친 것, 인자는 direction 것과 wrap의 것 2개를 받는다.

  - flex-flow: column wrap;을 따로 풀어 쓰면?

- justify-content : 주축(main axis, 기본은 가로)를 기준으로 요소들의 공간을 배정

  - flex-start : 요소들을 컨테이너의 시작점(기본은 왼쪽)으로 정렬
  - flex-end : 요소들을 컨테이너의 끝점(기본은 오른쪽)으로 정렬
  - center : 요소들을 컨테이너의 가운데로 정렬, 간격은 따로 더 주지 않음
  - space-around : 가운데 정렬에서 양쪽 끝 요소들과 벽 사이의 간격이 아이템들 간격의 절반이 됨, 요소끼리 가질 수 있는 영역을 균일하게 맞춤
  - space-evenly : 가운데 정렬에서 모든 요소들과 벽 사이 간격이 정확하게 같아짐
  - space-between : 가운데 정렬에서 우선 양 끝의 요소를 벽에 붙인 뒤 모든 요소들의 간격을 균일하게 함, 한 개 뿐이라면 왼쪽 벽에 붙음

- align-content : **여러 줄의** 요소들을 교차축(cross axism, 기본은 세로)를 기준으로 **공간 배정**, <u>한 줄로만 배치되는 경우 확인 불가</u>

  - justify-content와 구문은 동일함
  - flex-start는 기본이 위쪽, flex-end는 기본이 아래쪽이 됨, space 구문들은 위아래 기준

- align-items : **한 줄 안에서 여러 개의** 요소들을 교차축(cross axis)를 기준으로 **정렬**

  - flex-start : 요소들을 컨테이너의 꼭대기로 정렬, 요소들의 머리 부분이 꼭대기에 전부 닿음

  - flex-end : 요소들을 컨테이널의 바닥으로 정렬, 요소들의 끝 부분이 바닥에 전부 닿게 됨

  - center : 요소들을 컨테이너 교차축의 가운데로 정렬

  - stretch : 요소들을 컨테이너 크기에 맞도록 길게 늘임

  - baseline : 요소들을 컨테이너의 시작 위치로 정렬한다. flex-start와 유사하지만, contents의 밑줄을 기준으로 삼는다. 가령 요소들마다 글자가 들어있는데 크기와 위치가 모두 다른 경우, 글자의 바닥 부분을 일직선으로 이을 수 있게 정렬한다.

    <img src="https://i.stack.imgur.com/vxEeG.png">

- align-self : **한 개의** 요소만 교차축(cross axis)를 기준으로 **정렬**
  - align-items와 구문은 동일함
- order : **한 개의** 요소만 순서를 바꿈, 기준값은 0으로, +나 -만큼 앞이나 뒤로 밀 수 있다.
- flex-grow : 한 개의 요소가 양쪽 끝의 남은 공간을 늘려서 전부 차지하게 만듬

# 4. Bootstrap

- **꿀팁 : Bootstrap의 모든 코드는 class="" 안에 뭘 넣는지부터 시작된다!**

## 1) 기본 설명

- 일종의 오픈소스 CSS, 구글에 검색 후 사이트에 찾아가면 코드에 참조 구문 2개만 넣어주면 다양한 스킨들을 쓸 수 있게 해 준다.

  ```html
  <!--head 위치 제일 끝에 넣기-->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  <!--body 위치 제일 끝에 넣기-->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
  ```

- 다양한 상황에 대한 소스가 구비되어 있어서, 이게 있을까? 싶은 코드들은 거의 다 있다. 부트스트랩 사이트에서 검색만 잘 한다면 복붙해서 고칠 곳만 수정해서 쓰면 끝!

- 코드가 상당히 많이 축약되어서, display: flex; 같은 구문도 d-flex 정도로 짧게 줄여서 표현해버린다.

## 2) 스페이싱 (margin과 padding 여백 크기 처리 구문)과 컬러, 축약법

```html
<div class "mt-3 ms-5"> Bootstrap-spacing </div>
```

```css
/* 동일한 의미의 기존 css 구문*/
.mt-1 {
    margin-top: 1rem;
    margin-start: 3rem;
}
```

- margin과 padding 구문을 단 3글자로 축약해서 표현한다.
  - 첫 번째 글자 : property(종류)
    - m : margin
    - p : padding
  - 두 번째 글자 : sides(지정할 부분)
    - t : top
    - b : bottom
    - s : left (start라서, 아랍어 같은 경우에는 오른쪽이 됨)
    - e : right (end이므로, 마찬가지로 오른쪽이 먼저일 경우 왼쪽이 됨)
    - x : left + right
    - y : top + bottom
  - '-' 이후 세 번째 숫자 : 자세한 설정
    - 0 : 0 rem, 0 px
    - 1 : 0.25 rem, 4 px
    - 2 : 0.5 rem, 8 px
    - **3 : 1 rem, 16 px**
    - 4 : 1.5 rem, 24 px
    - 5 : 3 rem, 48 px
    - auto : **값을 최대한 많이 주고 알아서 이뻐 보이게 정렬! x-auto면 좌우 가운데 정렬, s-auto면 오른쪽 정렬이 됨(왼쪽에 여백을 최대로 줌)**

```html
<div class="d-block p-2 bg-primary text-center-white fw-bold">
    d-block
</div>
```

- display: block; font-weight: bold; text-align: center; 등의 구문은 짧게 축약됨
- primary, secondary, success, info, warning, danger, light, dark 등의 색상이 미리 들어 있음.
- 부트스트랩 축약법 정리 \<div class = "<u>여기 안에 들어갈 거</u>">
  - <u>d-block</u> = display: block;
  - <u>fixed-bottom</u> = position: fixed; bottom: 0;
  - <u>d-flex flex-row</u> = direction: flex; flex-direction: row;
  - <u>bg-red</u> = background: red;
  - <u>text-blue</u> = color: blue;
  - <u>text-center</u> = text-align: center;
  - <u>fst-italic</u> = font-style: italic;
  - <u>w-100</u> = width: **100%**; **백분율이므로 주의!!!!**
  - <u>align-self-start</u> = align-self: flex-start;

## 3) Grid System

- 사용방법 - container, row, col 3단계를 순서대로 감싸기!

  ```html
  <div class="container">
      <div class="row justify-content-center">
          <div class="box col-3 align-self-start"></div>
          <div class="box col-6 offset-4"></div>
          <div class="box col-3 col-lg-12"></div>
      </div>
  </div>
  ```

  - container : 전체 덩어리
  - row : 한 줄에 들어갈 요소들
    - row 안에 다시 col을 넣고 row를 넣으면 요소 안에 요소들을 겹쳐 넣을 수 있음, 액자식 디자인 느낌
  - col : 한 줄에서 한 개씩 자리 잡을 요소
    - col 뒤에 붙는 숫자는 한 줄을 12로 나눈 뒤 n/12만큼 영역을 차지하는 식, row 안에 같이 든 요소들이 왼쪽 끝부터 차례대로 붙어서 나옴
    - 12번째 칸을 넘게 될 경우 그 요소는 다음 줄에 들어감, 바로 윗 줄과 딱 붙어 있음
    - offset을 넣으면 n/12만큼 간격을 띄운 뒤 위치하게 됨
  - col, 혹은 offset과 숫자 사이에 특정 단어를 넣으면 화면 크기에 따라 요소 크기가 달라지게 할 수 있음, breakpoint를 잡아주는 셈. 이걸로 반응형 웹 페이지 제작 가능
    - \-sm-, -md-, -lg, -xl-, -xxl-이 있으며, 그 기준보다 화면이 클 경우 적용됨
    - col-3 col-lg-12의 경우, lg 화면 크기보다 작으면 3/12칸, 크면 12/12칸을 차지함
  - row나 col에 각각 flex 구문의 여러 요소 배치 구문 / 개별 요소 배치 구문을 넣으면 좀 더 다양한 위치에 배치 가능

## 4) 기타

- class="d-none", 즉 display: none을 사용하면 특정 상황에서 아예 요소를 숨겨버릴 수 있음
- class="img-fluid", 혹은 "container-fluid" 등을 사용하면 상위 속성 안에 딱 맞게 들어가는 사이즈가 됨 (여백 없이 정확하게 딱 맞음)
- Bootstrap 말고도 다양한 css 소스들이 많음, 상황에 맞게 찾아 쓰는 연습!
