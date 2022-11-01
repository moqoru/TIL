# 1. 이론 설명

# 2. Vue 문법 기초

## 2-1. Vue의 기본 구조

new Vue



- 어제꺼 실습
  - HTML에서는 id로 나타내 준 것을 Vue에서 #을 써서 가리킬 수 있음
  - 반대로 Vue에서 data에 {key : value} 형태로 넣어준 것은 HTML에서 {{ key }} 형태로 가리킬 수 있음



- computed 특징 : 함수인데 변수처럼 사용

  - method는 HTML 쪽에서 전체 데이터를 받아와서 실행.

  - computed는 Vue 쪽에서 갖고 있는 데이터로 실행.

- 메서드명 축약? 자스 01의 4-4를 잘 되짚어보자. 있었다...

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
    <div v-for="value in getOddNums">
      <p>{{ value }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        nums : [1, 2, 3, 4, 5, 6]
      },
      computed: {
        // getOddNums: function() {
        //   const oddNums = this.nums.filter((num) => {
        //     return num % 2
        //   })
        //   return oddNums
        getOddNums() {
          return this.nums.filter(number => number % 2 !== 0)
        }
      }
    })
  </script>
</body>
</html>
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
  <div id="app">
    <div v-for="value in getOddNums(nums)">
      <p>{{ value }}</p>
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
        // getOddNums: function(numbers) {
        //   const oddNums = numbers.filter((num) => {
        //     return num % 2
        //   })
        //   return oddNums
        // }
        getOddNums(numbers) {
          return numbers.filter(number => number % 2 !== 0)
        }
      }
    })
  </script>
</body>
</html>
```

