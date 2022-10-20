# 1. JavaScript를 시작하기 전에

## 1-0. JavaScript 마음가짐

- 현재 목표는 자바스크립트를 능수능란하게 사용하기보다는, JSON을 매개체로 하여 Python과 JavaScript가 서로 소통하게 만드는 쪽임
  - 그래서 JavaScript 자체를 배우는 시간보다 Vue.js를 배우는 기간이 더 길 예정
- JS뿐 아니라 다른 **제 2, 3의 언어를 배울 때는 BFS처럼**, 프레임워크를 통해서 넓게 배우는 전략을 써라!

## 1-1. JavaScript 실행 방법

- HTML 파일에 JavaScript 작성 후 웹 브라우저로 열기 - script 태그 안에 작성하면 완료

  - Chrome의 개발자 도구(F12) - Console 탭에서 결과 확인 가능

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
    <script>
      console.log('Hello, World!')
    </script>
  </body>
  </html>
  ```

- .js 확장자 파일을 만들고 JavaScript 구문을 작성 후, 그 파일을 HTML에 포함시킬 수도 있음

  ```javascript
  console.log('Hello, World!')
  ```

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
    <script type="text/javascript" src="filename.js"></script>
  </body>
  </html>
  ```

- Chrome 콘솔 창에서도 인터프리터 방식으로 JavaScript 코드를 입력할 수 있음

- 하지만 우리는 Node.js를 설치해서 VSCode로 실행할 예정

  - .js 파일을 만든 뒤 터미널에 **node (파일명).js**를 입력하여 실행함

## 1-2. JavaScript 문법 가이드

- ASI (Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
  - JavaScript는 ;을 선택적으로 사용 가능, 없어도 ASI에 의해 알아서 삽입됨
  - JavaScript의 개발자조차도 ;을 안 쓰는 게 낫다고 했을 만큼, 안 쓰는 쪽이 현재 트렌드임
- 코드 블럭을 구분할 때는 {}로 구분함
- 코드 스타일 가이드는 Airbnb Style Guide를 기반으로 배울 것임
  - **공백, 엔터, 대소문자 하나의 차이가 가독성에 큰 영향**을 끼치므로 매우 신경써서 할 것!
  - MDN 자바스크립트 문서나, Airbnb 자바스크립트 문서를 참조할 것

# 2. JavaScript 기초 문법

## 2-1. 식별자 (Identifier)

- 변수를 구분할 수 있는 구분명. 대소문자를 구분하며, 반드시 문자나 $, _로 시작함

- 카멜 케이스 (camelCase, lower-camel-case) - 변수, 객체, 함수에 사용

  ```js
  // 변수
  let dog
  let variableName
  // 객체
  const userInfo = { name: 'Tom', age: 20}
  // 함수
  function add() {}
  function getName() {}
  ```

- 파스칼 케이스 (PascalCase, upper-camel-case) - 클래스, 생성자에 사용

  ```js
  // 클래스
  class User {
      constructor (options) {
          this.name = option.name
      }
  }
  // 생성자
  function User(options) {
      this.name = options.name
  }
  ```

- 대문자 스네이크 케이스 (SNAKE_CASE) - 상수(constants), 즉 고정 불변하는 값에 사용

  ```js
  // 상수
  const API_KEY = 'my-key'
  const PI = Math.PI
  // 재할당하지 않을 변수
  const NUMBERS = [1, 2, 3]
  ```

## 2-2. 변수

- 블록 스코프 (block scope)

  - if, for, 함수 등의 중괄호 내부를 가리킴
  - 블록 스코프를 가지는 변수는 블록 밖에서 접근 불가
  - Python의 지역변수의 조건이 조건문, 루프문까지 확대되어서 더 빡빡하게 적용되는 것과 유사함

  ```js
  let x = 1
  if (x === 1) {
      let x = 2
      console.log(x) // 2
  }
  console.log(x) // 1
  ```

- 변수 선언 키워드

  - let - 재할당 가능, 재선언 불가

  ```js
  // OK
  let number = 10
  number = 20
  ```

  ```js
  // NG
  let number = 10
  let number = 20
  ```

  - const - 재할당 불가, 재선언 불가, **Aribnb 스타일에서는 기본적으로 const 사용을 권장**

  ```js
  // NG
  const number = 10
  number = 20
  ```

  ```js
  // NG
  const number
  ```

  - var - 재할당, 재선언 가능. **ES6 이후로는 권장되지 않음** => 호이스팅 특성으로 문제 발생할 수 있음

- 호이스팅 - 변수를 선언하기 전에 참조할 수 있는 현상

  - var로 선언된 변수를 선언하기 전에 참조하면 undefined가 반환됨. JS에서 변수들은 실행시 코드 최상단으로 끌어올려지기 때문
  - let, const는 이런 경우 에러가 나오도록 되어 있음

  ```js
  console.log(name) // undefined
  
  var name = '홍길동'
  ```

  ```js
  // 위 코드를 암묵적으로 아래와 같이 처리함
  var name
  console.log(name)
  
  var name = '홍길동'
  ```

## 2-3. 데이터 타입

- 크게 원시 타입(Primitive Type)과 참조 타입(Reference Type)으로 분류됨

  - Primitive Type - Number, String, Boolean, Symbol, undefined, null
  - Reference Type - Objects(Array, Function, ...)

- Number - 정수, 실수를 표현하는 자료형

  ```js
  const a = 13
  const b = -5
  const c = 3.14
  const d = 2.998e8
  const e = -Infinity
  const f = NaN
  ```

- NaN - Number 자료형 중 숫자가 아닌 값을 나타냄
  - 숫자로서 읽을 수 없거나, 결과값이 허수거나, 식을 정의할 수 없거나 (0 / 0), 문자열에 차, 곱, 몫을 취하거나
  - Number.isNaN(변수)를 쓰면 판독 가능함

- String - 문자열을 포함하는 자료형, ''이건 ""이건 상관 없으며, 덧셈 연산만 가능함

  ```js
  const firstName = "Elon"
  const lastName = "Musk"
  const fullName = firstName + lastName
  console.log(fullName) // ElonMusk
  ```

- Template Literal - ``(백틱)을 쓰면 줄 바꿈도 되고, 사이에 ${}로 변수 삽입도 가능, Python의 f-string과 동일

  - 단, escape sequence는 사용 불가 = \n은 사용 불가

  ```js
  const sentense = `화성
  갈끄니까~`
  console.log(sentense)
  
  const age = 51
  const message = `일론 머스크는 ${age}세입니다.`
  console.log(message)
  ```

- Empty Value - 값이 없음

  - null - 값이 없음을 의도적으로 표현할 때 사용, 사용자가 직접 넣은 것
  - undefined - 값이 정의되어 있지 않음을 표현함, 직접 값을 할당하지 않으면 자동으로 할당해 두는 값

  - null은 typeof로 타입을 확인하면 object로 뜨지만, undefined는 그냥 undefined로 뜸

  ```js
  let Nothing1 = null
  console.log(Nothing1) // null
  
  let Nothing2
  console.log(Nothing2) // undefined
  ```

- Boolean - true와 false, 여기서는 **소문자로 시작**함

  | 데이터 타입 |   false    |    true     |
  | :---------: | :--------: | :---------: |
  |  undefined  | 항상 false |      X      |
  |    null     | 항상 false |      X      |
  |   Number    | 0, -0, NaN | 나머지 전부 |
  |   String    | 빈 문자열  | 나머지 전부 |
  |   Object    |     X      |  항상 true  |

- 자동 형변환

  ```js
  console.log(8 * null) // 0, null이 0으로 처리됨
  console.log('5' - 1) // 4, 문자열은 뺄셈이 안 되므로 숫자로 처리
  console.log('5' + 1) // '51', 문자열 덧셈으로 처리
  console.log('five' * 2) // NaN, 에러 대신 NaN으로 처리됨
  ```

## 2-4. 연산자

- 할당 연산자 - +=, -= 등 전부 사용 가능, ++와 --는 쓸 수는 있지만 <u>권장하지 않음</u>

- 비교 연산자 - <, >, 문자열은 사전 순서 기반으로 비교

- 동등 연산자 - **===, 웬만하면 =를 3개 써야 함**. 값과 타입이 전부 동일해야 true (객체일 경우 주소값이 동일한지로 비교함)

  - 같은 원리로 서로 다른 지를 비교하려면 **!==**로 사용해야 함
  - == 연산자는... : 비교할 때 암묵적으로 타입을 변환 후 비교

  ```js
  const a = 1
  const b = '1'
  
  console.log(a == b) // true
  console.log(a === b) // false
  console.log(a === Number(b)) // true
  
  const objA = [1, 2, 3]
  const objB = [1, 2, 3]
  const objA2 = objA
  console.log(objA === objB) // false
  console.log(objA === objA2) // true
  ```

- 논리 연산자 - &&, ||, ! 로 사용, 단축 평가 지원

- 삼항 연산자 - (조건식) ? (참일 때 반환값) : (거짓일 때 반환값)

  ```js
  const result = Math.PI > 4 ? "TRUE!" : "FALSE..."
  console.log(result) // FALSE...
  ```

## 2-5. 조건문

- if문 - **가이드라인의 공백과 줄 바꿈 조건이 빡빡하므로 매우 주의!** 여백을 최대한으로 줄인 느낌.

  ```js
  const name = 'manager'
  
  if (name === 'admin') {
    console.log('관리자님 환영합니다.')
  } else if (name === 'manager') {
    console.log('매니저님 환영합니다.')
  } else {
    console.log (`${name}님 환영합니다.`)
  }
  ```

- switch문 - **break문을 사이사이에 쓰지 않으면 그 아래의 모든 구문이 실행**된다는 점에 유의!

  ```js
  const name = '홍길동'
  
  switch(name) {
    case '홍길동': {
      console.log('관리자님 환영합니다.')
      break // break문이 없으면...?
    }
    default: {
      console.log(`${name}님 환영합니다.`) // break문이 없다면 이 구문도 같이 출력됨...
    }
  }
  ```

## 2-6. 반복문

- while, for문 : C언어의 그것과 유사함. 최초 정의한 i를 재할당하면서 사용하므로 **let만 사용 가능**함

  ```js
  let i = 0
  
  while (i < 6) {
    console.log(i)
    i += 1
  }
  
  for (let j = 0; j < 6; j++){
    console.log(j)
  }
  ```

- for of와 for in은 매 반복시 해당 변수를 새로 정의하므로 **const로 사용 가능**

- for of - Python의 for in구문과 유사. 객체 속성의 **값을 순서대로** 순회할 때 사용 -> **거의 대부분의 경우 이걸 사용함**

- for in - **객체 속성의 이름(key 값)**을 순회할 때 사용, 인덱스 **순서가 보장되지 않음**

  - 배열을 in으로 돌리면, [10, 30, 50]이라도 실제로는 {0:10, 1:30, 2:50}으로 저장되어서 0, 1, 2가 나옴

  ```js
  const numbers = [10, 20, 30]
  for (const number of numbers) {
    console.log(number) // 10 20 30
  }
  for (const number in numbers) {
    console.log(number) // 0 1 2
  }
  
  const capitals = {
    korea: '서울',
    france: '파리',
    japan: '도쿄'
  }
  for (const capital in capitals) {
    console.log(capital) // korea france japan
  }
  ```

# 3. JavaScript 함수

## 3-1. 함수 선언식과 표현식

- 함수 선언식 - 일반적인 프로그래밍 언어의 방식이나, JavaScript에서는 권장하지 X

  - 이유인 즉, var 변수처럼 **호이스팅이 발생**하기 때문. 즉 함수 호출 이후에 선언해도 동작함

  ```js
  console.log(myadd(2,7)) // 9
  
  function myadd(num1, num2) {
    return num1 + num2
  }
  ```

- 함수 표현식 - 표현식 내에서 익명 함수의 형식으로 정의, **Airbnb 가이드라인에서 사용을 권장함**

  - 함수 표현식으로 정의하면 호이스팅이 일어날 상황이라도 바로 에러로 처리되기 때문

  ```js
  const myadd = function(num1, num2) {
    return num1 + num2
  }
  
  console.log(myadd(2,7))
  ```

  - 함수 이름을 명시할 수는 있지만, 이 이름은 호출에 사용할 수 없고 디버깅 용도로만 가능

  ```js
  const myadd = function dummy(num1, num2) {
    return num1 + num2
  }
  
  console.log(myadd(2,7))
  console.log(dummy(2,7)) // ReferenceError: dummy is not defined
  ```

  - 기본 인자를 넣을 수 있고, 호출할 때 인자 개수가 불일치해도 상관 없음

  ```js
  const myadd = function (num1, num2 = 5) {
    return num1 + num2
  }
  
  console.log(myadd(2,7))
  console.log(myadd(2)) // 7
  ```

  ```js
  const myfunc = function (num1, num2) {
    return [num1, num2]
  }
  
  console.log(myfunc(1)) // [1, undefined]
  console.log(myfunc(1, 2, 3)) // [1, 2]
  ```

- 전개 구문 (Spread syntax)

  - ...  을 사용해서 배열이나 문자열처럼 반복 가능한 객체를 넣을 수 있음
  - 배열에 사용했을 때는 배열 복사를 할 수 있음 (단, 얕은 복사임. Python의 리스트 덧셈과 유사)

  ```js
  let parts = ['shoulders', 'knees']
  let lyrics = ['head', ...parts, 'and', 'toes'] // 앞, 중간, 뒤 모두 넣을 수 있음
  console.log(lyrics) // ['head', 'shoulders', 'knees', 'and', 'toes']
  ```

  - 함수에 사용했을 때는 정해지지 않은 갯수의 매개변수를 배열로 받을 수 있음 (Python의 *args)

  ```js
  const rest0pr = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
  }
  
  // restArgs 부분이 한 덩어리의 배열로 처리됨. 없으면 빈 배열로 표시
  console.log(rest0pr(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
  console.log(rest0pr(1, 2)) // [1, 2, []]
  ```

## 3-2. 화살표 함수 (Arrow Function)

- 사실 함수 표현식은 더 축약하는 것이 가능하며, 축약된 구문을 **훠어어어얼씬** 많이 쓴다.

- 화살표 함수 문법 적용 방법

  - 1단계) **function 키워드를 생략하고 대신 (인자) 뒤에 =>를 붙일 수 있음**, 가장 자주 쓰임
  - 2단계) 인자가 1개일 경우 ()를 생략 가능 (...이지만 <u>Airbnb 가이드라인에서는 권장하지 않음</u>)
  - 3단계) 함수 바디가 return을 포함해서 표현식 1개라면 **return 키워드도, {}도 생략 가능**

  ```js
  const arrow0 = function (name) {
    return `hello, ${name}`
  }
  
  // 1단계) function 키워드를 =>로 대체
  const arrow1 = (name) => { return `hello, ${name}`}
  
  // 2단계) 인자가 1개라면 () 생략 가능 (권장하지 않음)
  const arrow2 = name => {return `hello, ${name}`}
  
  // 3단계) 함수 바디가 return을 포함하여 표현식 1개라면 return과 {} 생략 가능
  const arrow3 = (name) => `hello, ${name}`
  ```

  - 인자조차 없다면 ()이나 _로 표시할 수 있음

  ```js
  let noArgs = () => 'No Args'
  noArgs = _ => 'No Args'
  ```

  - 예외 케이스 - Object를 return 한다면 return을 명시적으로 적거나 생략하는 대신 ()를 붙인다.

  ```js
  let returnObj = () => {return {key: 'value'}}
  returnObj = () => ({key: 'value'})
  ```

- 즉시 실행 함수 (IIFE, Immediately Invoked Function Expression)

  - 선언하자마자 실행되는 일회용 함수, 초기화 부분에 많이 사용
  - 함수 이름 없이 내용 부분만 ()로 감싼 뒤, 바로 뒤에 (인자)를 추가하여 실행되도록 함

  ```js
  (function(num) { return num ** 3 })(2) // 8
  ((num) => {return num ** 3})(2) // 1단계 축약 적용
  ((num) => num ** 3) (2) // 3단계 축약 적용
  ```

# 4. Array와 Object

## 4-1. 배열 (Array) 과 배열 메서드

- 특별할 것 없는 그냥 배열, Python처럼 (-) 인덱스는 안 되고 array.length를 이용할 수 있음

  ```js
  const numbers = [1, 2, 3, 4, 5]
  
  console.log(numbers[0]) // 1
  console.log(numbers[-1]) // undefined
  console.log(numbers[numbers.length - 1]) // 5
  ```

- 배열 메서드 기초

  |     메서드     |                  설명                   |         비고          |
  | :------------: | :-------------------------------------: | :-------------------: |
  |    reverse     |          순서를 반대로 뒤집음           |                       |
  |   push, pop    |       가장 뒤의 요소를 추가/제거        |                       |
  | unshift, shift |       가장 앞의 요소를 추가/제거        |                       |
  |    includes    | 특정 값이 존재하는지 판별, 참/거짓 반환 |                       |
  |    indexOf     | 특정 값이 존재하는지 판별, 인덱스 반환  | 요소가 없으면 -1 반환 |
  |      join      |   모든 요소를 구분자를 이용하여 연결    |  기본값은 ','를 붙임  |

  ```js
  const numbers = [5, 4, 3, 2, 1]
  
  numbers.reverse()
  console.log(numbers) // [1, 2, 3, 4, 5]
  
  numbers.push(100)
  console.log(numbers) // [1, 2, 3, 4, 5, 100]
  
  numbers.pop()
  console.log(numbers) // [1, 2, 3, 4, 5]
  
  numbers.unshift(0)
  console.log(numbers) // [0, 1, 2, 3, 4, 5]
  
  numbers.shift()
  console.log(numbers) // [1, 2, 3, 4, 5]
  
  console.log(numbers.includes(-1)) // false
  
  console.log(numbers.indexOf(3)) // 2
  console.log(numbers.indexOf(-1)) // -1
  
  console.log(numbers.join()) // 1,2,3,4,5
  console.log(numbers.join('')) // 12345
  ```

## 4-2. Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드, 호출 시 인자로 callback 함수를 받는 것이 특징 (함수의 인자로 함수를 넣은 것)

- 쉽게 말해 **배열을 순회하는 for문을 함수 하나로 압축한 것과 유사함**

- 종류

  - 공통적으로 콜백 함수에서 3개의 인자를 받음. array.forEach((element, index, array) => {})
  - element: 배열의 요소(<u>이 인자만 필수임</u>), index: 배열 요소의 인덱스, array: 배열 자체

  | 메서드  |                         설명                         |         비고          |
  | :-----: | :--------------------------------------------------: | :-------------------: |
  | forEach |          각 요소마다 콜백 함수 한번씩 실행           |       반환 값 X       |
  |   map   |         반환 값을 새로운 배열로 모아서 반환          |                       |
  | filter  | 반환 값이 참인 것들만 모아 새로운 배열로 모아서 반환 |                       |
  | reduce  |      반환 값들을 하나의 값(acc)에 누적 후 반환       |    추가 인자 있음     |
  |  find   |          반환 값이 참인 첫번째 요소를 반환           | 없으면 undefined 반환 |
  |  some   |       요소 중 하나라도 판별 함수를 통과하면 참       |                       |
  |  every  |         모든 요소가 판별 함수를 통과하면 참          |                       |

- forEach - **Airbnb 가이드라인에서는 for of 구문보다도 더 권장**하는 방식! 단 break, continue 사용 불가

  ```js
  const colors = ['red', 'blue', 'green']
  
  // 함수를 따로 만들어 넣을 경우
  printFunc = function(color) {
    console.log(color)
  }
  colors.forEach(printFunc) // red blue green
  
  // 함수 정의를 인자로 넣을 경우
  colors.forEach(function (color) {
    console.log(color)
  })
  
  // 축약 1단계
  colors.forEach((color) => {return console.log(color)})
  
  // 축약 3단계
  colors.forEach((color) => console.log(color))
  ```

- map - forEach + return 과 유사함

  ```js
  const numbers = [1, 2, 3]
  
  // 일단 사용해보기
  const doubleFunc = function (number) {
    return number * 2
  }
  console.log(numbers.map(doubleFunc)) // [2, 4, 6]
  
  // 바로 최종 단계로 축약하면?
  console.log(numbers.map((number) => number * 2))
  ```

- filter

  ```js
  const fruits = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'}
  ]
  
  // 1단계로 축약할 경우
  console.log(fruits.filter((product) => {return product.type === 'fruit'}))
  // [ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]
  ```

- reduce - array.reduce((acc, element, index, array) => {}, initialValue) 식으로 사용

  - acc라는 인자에는 이전 callback 함수의 반환 값이 누적됨. (acc + 0번째 반환값 + 1번째 반환값 + ...)
  - initialValue는 함수 첫 호출시 acc에 저장될 초기값이며, 기본적으로는 배열의 첫번째 값이 들어감
  - initialValue는 굳이 안 적어도 되지만 빈 Value의 경우에는 안 적으면 에러가 남

  ```js
  const tests = [90, 90, 80, 77]
  
  let mySum = tests.reduce(function (total, x) {
    return total + x
  }, 0)
  console.log(mySum) // 337
  
  // 화살표 함수로 축약
  mySum = tests.reduce((total, x) => {return total + x}, 0)
  console.log(mySum)
  
  const myAver = tests.reduce((total, x) => total + x, 0) / tests.length
  console.log(myAver) // 84.25
  ```

- find, some, every

  ```js
  const tests = [90, 90, 80, 77]
  
  console.log(tests.find((score) => score < 90)) // 80
  console.log(tests.find((score) => score === 100)) // undefined
  console.log(tests.some((score) => score === 100)) // false
  console.log(tests.every((score) => score > 80)) // false
  ```

## 4-3. 객체 (Object)

- Python의 객체와는 다른 개념이며, 오히려 딕셔너리와 더 유사함

- 속성의 집합이며, {} 내부에 key와 value의 쌍으로 표현됨

  - key는 문자열 타입만 가능, ''를 쓰지 않아도 되지만 띄어쓰기 등이 있으면 ''로 묶어서 표현
  - value는 함수를 포함하여 모든 타입 가능

- 객체 요소에 접근할 때는 .key나 [key] 사용 가능, key에 띄어쓰기 등이 있으면 []만 사용 가능

- 객체 사용 예시

  ```js
  const my_info = {
    name: 'billy',
    phoneNum: '01012345678',
    'samsung products': {
      buds: 'Galaxy Buds pro 99',
      phone: 'Galaxy Z Z Flip Flip Flip',
    },
  }
  
  console.log(my_info.name) // billy
  console.log(my_info['name']) // billy
  console.log(my_info['samsung products']) // { buds: 'Galaxy Buds pro 99', phone: 'Galaxy Z Z Flip Flip Flip' }
  // console.log(my_info.samsung products) // 에러 발생
  console.log(my_info['samsung products'].buds) // Galaxy Buds pro 99
  ```

- 사실 배열도 객체다?

  - 반복문에서 for in 구문을 사용했을 때 봤던 것처럼, 배열도 사실 인덱스를 키로 가지는 객체이다.
  - [10, 30, 50]으로 정의해도 실제로는 { '0': 10, '1': 30, '2': 50 } 형식으로 처리됨

## 4-4. 객체 관련 문법

- 이하 내용은 ES6에 새로 도입된 문법들임 (흔히 ES6+로 표기)

- 속성명 축약 - 객체를 정의할 때 key와 변수 이름이 같으면 축약 가능

  ```js
  const books = ['Jump to Python', 'Club JavaScript']
  const magazines = ['Vogue', 'Science']
  
  const bookShop = {
    // ES5 문법
    // books: books,
    // magazines: magazines,
    // ES6+ 문법
    books,
    magazines,
  }
  
  console.log(bookShop)
  // {
  //   books: [ 'Jump to Python', 'Club JavaScript' ],
  //   magazines: [ 'Vogue', 'Science' ]
  // }
  ```

- 메서드명 축약 - 메서드 선언시 function 키워드 생략 가능, 이 경우 화살표 함수보다도 더 축약됨

  ```js
  const obj = {
    // ES5 문법
    // greeting: funtion () {
    // greeting: () => {
    // ES6+ 문법
    greeting() {
      console.log('Hi!')
    }
  }
  obj.greeting() // Hi!
  ```

- 계산된 속성 - 객체를 정의할 때 key의 이름을 표현식을 써서 동적으로 생성 가능

  ```js
  const myKey = 'country'
  const myValue = ['한국', '미국', '일본']
  
  const myObj = {
    [myKey]: myValue,
  }
  
  console.log(myObj) // { country: [ '한국', '미국', '일본' ] }
  console.log(myObj.country) // [ '한국', '미국', '일본' ]
  ```

- 구조 분해 할당 - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

  - 여러 속성을 key 값과 같은 이름을 가진 변수에 한 번에 할당 가능

  ```js
  const userInfo = {
    name: 'ssafy kim',
    userId: 'ssafyStudent1234',
    phoneNumber: '010-1234-5678',
    email: 'ssafy@ssafy.com'
  }
  
  // ES5 문법
  // const name = userInfo.name
  
  // ES6+ 문법
  // const {name} = userInfo
  // const {userId} = userInfo
  // const {phoneNumber} = userInfo
  // const {email} = userInfo
  // console.log(name, userId, phoneNumber, email)
  
  // ES6+ 문법으로 한 방에 해결하기
  const {name, userId, phoneNumber, email} = userInfo
  console.log(name, userId, phoneNumber, email)
  // ssafy kim ssafyStudent1234 010-1234-5678 ssafy@ssafy.com
  ```

- Spread syntax - 배열과 마찬가지로 ... 기호를 통해 객체 내부에 객체를 얕은 복사 할 수 있음

  ```js
  const obj = {b: 2, c: 3}
  const newObj = {a: 1, ...obj, d: 4}
  console.log(newObj) // { a: 1, b: 2, c: 3, d: 4 }
  ```

## 4-5. JSON 변환법

- JSON (JavaScript Object Notation)

  - JS의 Key-Value 형태로 이루어진 자료 표기법
  - Object와 유사한 구조이지만 JSON은 그냥 형식이 있는 문자열에 불과함
  - JSON <-> Object 변환 작업이 필요

- JSON <-> Object 변환

  ```js
  const jsObject = {
    coffee: 'Americano',
    iceCream: 'MintChoco',
  }
  
  // Object -> JSON
  const objToJson = JSON.stringify(jsObject)
  console.log(objToJson) // {"coffee":"Americano","iceCream":"MintChoco"}
  console.log(typeof objToJson) // string
  
  // JSON -> Object
  const jsonToObj= JSON.parse(objToJson)
  console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'MintChoco' }
  console.log(typeof jsonToObj) // object
  ```

  