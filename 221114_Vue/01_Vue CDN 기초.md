# 1. 이론 설명

## 1-1. CSR vs SSR

- Web App : 웹 브라우저에서 실행되는 어플리케이션 소프트웨어, 마치 디바이스에 설치된 App처럼 보임
- SPA(Single Page Application) : 서버에서 최초 1장의 HTML만 전달받은 뒤 모든 요청에 대응하는 방식 -> 새로고침이 없는 페이지, CSR 방식으로 이어짐
- CSR vs SSR - 상호 보완 관계!
  - SSR(Server Side Rendering) : 서버가 사용자의 요청에 적합한 HTML을 렌더링하여 제공, 새 문서를 보내 줄 때 새로고침
  - CSR(Client Side Rendering) : 서버에서 빈 HTML 문서만 받아온 뒤 AJAX 통신을 통해 JavaScript에서 필요한 부분만 다시 렌더링하여 새로고침이 필요 없음
  - CSR을 쓰면 모든 HTML 페이지를 서버에서 받을 필요가 없고, 요청이 끊김 없이 진행 되며, Front와 Back의 작업 영역을 명확히 분리할 수 있음
  - 그러나 첫 구동시 필요한 데이터가 많으면 최초 로딩 시간이 길며, 검색 엔진 최적화(SEO, Search Engine Optimization)가 어려움. 빈 HTML부터 시작하는 CSR 특성상 검색 엔진에서 높은 순위에서 노출되기 힘듬

## 1-2. Vue 입문

- 웹 개발에서 가장 중요한 것은 **요청과 응답**이며, 이 요청과 응답 과정을 쉽게 하기 위해 Vue라는 Framework를 사용함
- Vue의 기능은 Front-end로, 우리가 보는 화면을 그려주는 기능을 함
- Vanilla JS 대신 Vue를 사용한다면, 불필요한 코드 반복이 줄어들고 변경사항을 한 번에 반영할 수 있음
- .vue 파일은 **template, script, style** 3개의 태그로 나뉘어 있고, 각각 HTML, JavaScript, CSS 구문으로 나뉘어져 있다.
- 대부분 설정들이 Vue3을 기본으로 적용되어 있지만, LTS인 Vue2 버전을 사용할 것임
- MVVM 패턴 : View, ViewModel, Model 구조로, View는 우리 눈에 보이는 DOM 부분, Model은 실제 JSON 데이터, ViewModel은 Vue를 가리키지만... 사실 Django에서의 MTV와 매우 유사함

# 2. Vue CDN 기초

## 2-1. Vue 인스턴스 만들기

- 우선 HTML 안에서 CDN만을 사용해 Vue 인스턴스를 제작하는 것부터 시작! JavaScript 내에서 간단하게 사용하기 위해 특정 기능만 골라서 쓰려는 의도이다.

- Vue2의 공식 문서에서 Delelopment version의 CDN을 복사해서 Script 태그 위에 붙인다.

- new 연산자로 Vue라는 이름의 인스턴스를 생성하고, el과 data를 설정한다.

- el : element, HTML상에서 Vue가 사용될 영역을 정하며 그 영역 밖에서는 Vue가 적용되지 않음 (Vue 인스턴스와 DOM을 mount(연결)), el : '#(HTML id)' 식으로 가리킴

- data : HTML에서 뽑아 가거나 함수에서 뽑아 쓸 수 있도록 객체나 인스턴스를 선언하는 곳, {key: value} 형태로 선언함. HTML에서 쓸 때는 {{ 변수명 }} 식으로, 다음에 나올 methods 등에서 쓸 때는 this.변수명 식으로 사용 가능

  ```HTML
  <!-- 칸 안에 글자를 입력하면 그 글자를 그대로 보여주는 구문 -->
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <div id="app"> <!-- 이 태그 안에서만 Vue가 작동함 -->
      <p id="name">name : {{ message }}</p> <!-- message 변수를 사용함 -->
      <input id="inputName" type="text" v-model="message">
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script>
      // CODE HERE
      const app = new Vue({
        el: '#app',
        data: {
          message: '',
        }
      })
    </script>
  </body>
  </html>
  ```

## 2-2. methods와 computed

- methods 

  - 호출하면 data를 변경할 수 있게 하는 함수를 작성, 실행 즉시 DOM에 변경된 결과가 반영된다. 콘솔창에서 app.함수명()을 입력하거나 HTML 안에서 JavaScript 구문을 써서 호출시킬 수 있다.
  - data의 변수를 사용할 때는 this.변수로 사용 (this는 객체 자기 자신 = new Vue, 굳이 this.data.변수로 쓸 필요는 없음)
  - 주의! methods에서는 **화살표 함수를 쓰면 안 된다!** 여기서 this를 사용해 버리면 화살표 함수의 특성상 바로 위에서 this를 사용한 것과 동일한데, **Vue 인스턴스 밖의 동명이인 변수**를 가리키게 되어버린다... 따라서 변수 값 변경이 제대로 되지 않는다.

- computed

  - 안에 적히는 구문은 함수이지만 실제 사용은 변수처럼 뒤에 () 없이 쓰게 된다. 연산 '완료된' 것을 바로 캐시로 쓰게 해서 좀 더 효율적으도 동작하게 됨

  - 데이터를 가공해서 새로운 값으로 보여주고 싶은 상황에서만 사용, 나머지는 그냥 methods를 쓰면 된다

- 실 사용 비교(단, 변수를 바꾸는 구문은 없음)

  - method는 HTML 쪽에서 전체 데이터를 받아와서 실행, 그래서 HTML쪽에서 데이터를 직접 보내준 것을 인자를 통해 받아서 처리했다.
  - computed는 Vue 쪽에서 갖고 있는 데이터로 실행. 따로 받은 인자 없이 this에서 가리켜진 내부 인자를 받아 계산 완료된 것을 바로 HTML로 전송했다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <div id="app">
      <div v-for="value1 in getOddNumsMethods(nums)">
        <p>{{ value1 }}</p>
      </div>
      <div v-for="value2 in getOddNumsComputed">
        <p>{{ value2 }}</p>
      </div>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          nums : [1, 2, 3, 4, 5, 6]
        },
        methods: {
          // getOddNumsMethods: function(numbers) {
          //   const oddNums = numbers.filter((num) => {
          //     return num % 2
          //   })
          //   return oddNums
          // }
          getOddNumsMethods(numbers) {
            return numbers.filter(number => number % 2 !== 0)
          }
        },
        computed: {
          // getOddNums: function() {
          //   const oddNums = this.nums.filter((num) => {
          //     return num % 2
          //   })
          //   return oddNums
          getOddNumsComputed() {
            return this.nums.filter(number => number % 2 !== 0)
          }
        }
      })
    </script>
  </body>
  </html>
  ```

## 2-3. v-syntax로 HTML에서 JS 구문 사용하기

- 렌더링 된 DOM을 Vue에 선언적으로 바인딩할 수 있게 HTML 기반의 template syntax를 사용

- v-syntax의 구조
  - (v-접두사):전달인자.특수속성="변수"
  - :를 통해 전달 인자를 받고, .으로 표시되는 특수 속성 사용할 때도 있음
  - 예시) v-on:submit.prevent="onSubmit"
  
- 이하 구문들은 편의를 위해 Vue 인스턴스 안에서 data: { 변수: ??? }로 선언되었다는 가정하에 작성

- Text Interpolation : {{ value를 출력할 변수 }}, 가장 기본적인 방법이며 {{ 변수.split('') }} 등 JS 식도 작성 가능

- v-text : <태그 v-text="value를 출력할 변수"></태그>, {{}}와 거의 동일하므로 둘 중 취향껏 사용

- v-html : <태그 v-html="html 구문 value가 있는 변수"></태그>, RAW HTML을 표현하기 위해 Vue가 제공하는 특수 속성 값으로 작성

- v-show : <태그 v-show="boolean value가 있는 변수"> 보이냐? </태그>, 일단 DOM에 렌더링은 다 해놓고 boolean 값이 true이면 태그 안쪽의 값을 보여주고, false이면 안 보이게 함

- v-if : <태그 v-if="boolean value가 있는 변수"> 보이냐고. </태그>, false일 경우 아예 DOM에서 지워버린다. v-else-if나 v-else 형태도 사용 가능하며, **웬만하면 v-if를 쓰고, 필요할 때만 v-show를 사용**

- v-for : JavaScript의 for in 구문과 유사함

  - <태그 v-for="blah in 객체":key="구분 지을 이름"> (루프 돌 곳) </태그>
  - 문자열, 배열, 객체 등에 모두 사용 가능하며, 객체의 경우 blah.name 등으로 내부 값 조회도 가능
  - key와 value를 출력하고 싶을 경우 (value, key) 식으로 순서를 뒤바꾸어 넣어야 함, **단, Vue Cli에서는 무조건 사용해야 함!**
  - 특수 속성 key는 **Vue Cli에서는 필수적으로 작성, key 부분에 쓴 변수를 통째로 포함하고 있어야 한다!**
  - 주의! **v-if와 v-for는 절대 1개의 HTML 태그 안에 몰아 쓰지 말 것**! Vue 2와 Vue 3의 동작이 다르다!

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
  </head>
  <body>
    <!-- 3. v-for -->
    <div id="app">
      <h2>String</h2>
      <!-- 이 구문은 Vue CDN에서만 사용 가능합니다. -->
      <div v-for="char in myStr">
        {{ char }}
      </div>
      <div v-for="(char, index) in myStr" :key="index">
        <p>{{ index }}번째 문자열 {{ char }}</p>
      </div>
  
      <h2>Array</h2>
      <div v-for="(item, index) in myArr" :key="`ssafy-${index}`">
        <p>{{ index }}번째 아이템 {{ item }}</p>
      </div>
  
      <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
        <p>{{ index }}번째 아이템</p>
  		  <p>{{ item.name }}</p>
      </div>
  
      <h2>Object</h2>
      <div v-for="value in myObj">
        <p>{{ value }}</p>
      </div>
  
      <div v-for="(value, key) in myObj" :key="key">
        <p>{{ key }} : {{ value }}</p>
      </div>
    </div>
  
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app',
        data: {
          // 1. String
          myStr: 'Hello, World!',
  
          // 2-1. Array
          myArr: ['python', 'django', 'vue.js'],
  
          // 2-2. Array with Object
          myArr2: [
            { id: 1, name: 'python', completed: true},
            { id: 2, name: 'django', completed: true},
            { id: 3, name: 'vue.js', completed: false},
  			  ],
          
          // 3. Object
          myObj: {
            name: 'harry',
            age: 27
          },
        }
      })
    </script>
  </body>
  </html>
  ```

- v-on : JavaScript의 querySelector와 addEventListener를 한 덩어리로 통째로 묶은 것

  - <(button) v-on:click="각종 JS 구문"> 나 버튼 </(button)>
  - 매우 많이 쓰므로 **'v-on:'까지를 묶어서 @ 기호로 축약 가능**! @click=... => 귀를 본따서 @라나...?
  - : 뒤에 넣을 구문을 통해 이벤트의 트리거 설정 가능 (click이나 keyup 등...)
  - 각종 구문 앞에 : 를 붙이면 원래는 ="" 안의 ""가 문자열이지만, **: 를 붙이는 순간 JS 구문으로 변신**함, **태그 안에 JS 구문을 넣고 싶다면 거의 필수!**
  - JS 구문 자리에는 변수를 넣어도 되고, 메서드나 객체 등등 뭐든 넣어도 됨. <u>데이터 조작도 가능</u>

- v-bind : HTML 기본 속성에 Vue data를 연결
  - <(a) v-bind:href="url"> 하이퍼링크 </(a)>
  - 역시 매우 많이 쓰므로 **'v-bind:'까지를 묶어서 그냥 : 하나로 축약함**. : class 라던가...
  - ""안에는 class가 들어가는데, 조건부 바인딩으로 "{'class 이름' : 표현식}"을 쓰거나, 다중 바인딩으로 "[JS 구문1, 구문2, ...]" 식으로 사용할 수도 있음
  - Vue data의 변화에 따라 DOM에 유동적으로 반영 가능

- v-model : Vue instance와 DOM을 양 방향으로 바인딩
  - <(input) v-model="myMessage" type="text">
  - Vue data를 바꾸면 v-model로 연결된 사용자 입력 element에도 변경 사항이 적용된다.
  - v-on의 단방향 연결보다 좋아보이지만, 한글이나 한자 등의 완성형 문자의 경우 한 글자가 완성되어야 변경 내역이 감지된다는 단점이 있어서 취사선택할 필요가 있음

## 2-4. 기타 내용

- Vue 구문을 작성할 때는 3박자를 따르자! **HTML, data의 변수, method나 computed의 함수**
- watch : { 감시할 변수 : function(변동 전 data, 변동 후 data) {...} }, Vue 인스턴스 안에 methods와 비슷하게 작성하며, 특정 변수의 변화를 감지할 때 사용한다. 각종 객체의 내부 요소 변경을 감지하려면 deep 속성이 필요함
- filters : ~~{{ 변수 }}나 v-bind를 쓸 때 '|' 기호를 써서 {{ 변수 | 거르는 함수1 | 거르는 함수2 }} 식으로 적고, 거르는 함수는 Vue 인스턴스 안에 filters : {} 식으로 따로 선언해 준다.~~ ...methods나 computed에서 처리하는게 훨씬 낫다.
- Vue Style Guide : 위의 v-if와 v-for 동시 사용 금지 외에도 몇 가지 추가 가이드가 있으므로 인터넷 문서를 참조할 것. 특히 적극 권장(Strongly Recommended)는 한 번쯤 보자.
