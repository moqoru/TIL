# 3. Vue Cli 기초

## 3-1. Vue Cli 설치 (반드시 VSCode의 터미널에서 진행!)

- npm install -g @vue/cli 입력 (Node.js가 설치되어 있어야 하며, npm은 패키지를 설치하는 구문임)
- vue create (프로젝트명)
- Vue 버전을 방향키와 Enter로 Vue 2를 선택 (Bash로는 키보드 입력이 안 먹힌다!)
- cd (프로젝트명)
- npm run serve : 프로젝트를 실행시키는 구문 (장고의 python manage.py runserver)
- 주소를 ctrl+클릭 하면 브라우저로 실행 가능

## 3-2. Vue Cli 프로젝트 구조

- node_modules : 각종 모듈이 들어있으며 파이썬의 venv와 유사, vue 프로젝트를 생성하면 자동으로 추가됨
- Babel : JavaScript의 최신 코드를 구버전으로 변환해주는 도구
- Webpack : 모듈을 하나로 묶어서 몇 개의 파일로 만드는 도구(Bundler), 모듈 의존성 문제를 해결해 줌. 그래서 npm install 한번만 해 주면 다양한 모듈을 한 번에 설치할 수 있음
- package.json : 프로젝트의 종속성 목록과 브라우저 구성 옵션이 들어 있음
- package-lock.json : node_modules에 설치된 모듈의 의존성을 설정 및 관리, 장고의 requirements.txt
- public/index.html : Vue 앱의 뼈대가 되는 html 파일 (프로젝트 만들 때 직접 건드릴 일은 잘 없음)
- src/ 디렉토리
  - assets : 정적 파일을 저장
  - **components** : 하위 컴포넌트들이 위치, HelloWorld.vue가 기본으로 들어 있음
  - **App.vue** : 최상위 컴포넌트, index.html로 연결됨
  - main.js : index.html과 App.vue를 연결시킴, Vue 전역에서 사용할 모듈을 등록 가능

## 3-3. SFC (Single File Component)

- 한 개의 .vue 파일이 곧 하나의 Vue instance이고, 하나의 컴포넌트에 해당됨
- 이전 차시에서 new Vue()로 HTML 파일 안에 집어넣던 것을 HTML + CSS + JavaScript 묶음으로 이루어진 기능 단위의 한 파일로 독립시키는 것
- Component : UI를 기능별로 분화한 코드 조각이며, 보편적으로는 컴포넌트들을 tree로 중첩시켜 하나의 app으로 구성함. 카드 뉴스 등 반복되는 UI 구성이 쉬워져서 **유지보수가 쉽고 재사용성에서도 강력함**

# 4. Vue Cli 실습

## 4-1. Vue Component 구조

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
- 최상단의 component가 App.vue
- 기본적으로 HelloWorld.vue 컴포넌트가 생성되어 있고 App.vue의 하위 component로 연결되어 있음
- 컴포넌트 끼리의 데이터 연결이 완전히 자유롭지는 않고, **부모-자식 관계에서만 데이터 주고받기가 가능** => 데이터 흐름 파악이 용이하고, 유지 보수가 쉬워짐

## 4-2. 새로운 vue 파일 만들고 상위 컴포넌트와 연결

- src/components/ 안에 .vue 파일을 만듬
- vue 치고 엔터 치면(vue with default vue) template, script, style이 자동완성됨
- template에 적어도 1개 이상의 태그가 있어야 함. 그냥 div를 넣는 것을 추천
  - 부모 컴포넌트에서 연결할 때 <파일명/> 태그 부분에 자식 파일의 template - /template 부분이 통째로 들어가는 것. **자식 파일의 내용이 통째로 들어가게 '태그 구멍'을 뚫어 놨는데 정작 들어갈 태그가 없으면 안 된다**는 의미
- script의 export default 안에 name : '파일명' 적기
- 자식 컴포넌트를 등록하는 3단계 (App.vue 파일에 연결)
  - **불러오기** : script 태그 안에 import 파일명 from '파일주소'를 적기, 파일주소는 src의 단축기호로 @/를 쓸 수 있고 .vue는 생략 가능
  - **등록하기** : export default 안에 components : { 파일명 }을 추가하기
  - **보여주기** : template 태그 안에 <파일명/>의 형태로 사용, 여러 번 사용하는 것도 가능함
  - 이 3개 과정 중 하나라도 완성되지 않으면 오류가 남
- **여기까지의 과정은 파일 하나 만들 때마다 필수적으로 진행!**

```vue
<!-- TestComponent.vue -->
<template>
  <div>
    <h1> Test </h1>
  </div>
</template>

<script>
export default {
  name : "TestComponent"
}
</script>

<style>

</style>
```

```vue
<!-- App.vue -->
<template>
  <div id="app">
    <!-- 3단계 사용하기, 여러 번 사용 가능 -->
    <TestComponent/>
    <TestComponent/>
  </div>
</template>

<script>
// 1단계 등록하기
import TestComponent from '@/components/TestComponent'

// 2단계 불러오기
export default {
  name: 'App',
  components: {
    TestComponent
  }
}
</script>
...
```

# 5. 부모-자식 Component 간 데이터 전달

## 5-1. Pass Props (부모 => 자식)

- 모든 props는 부모 => 자식 방향으로만 동작하며, 부모 속성이 업데이트되면 자식 컴포넌트의 prop이 전부 새로고침되지만 자식 쪽에서 prop을 변경할 수는 없음

- 전체 흐름 

  - 부모 script의 data()에서 데이터를 선언
  - 부모 template에서 자식 컴포넌트로 데이터 전달
  - 자식 script의 props에서 데이터 타입 명시
  - 자식 template에서 받은 데이터 사용

- 부모에서 자식쪽으로 컴포넌트를 전달 할 때는...

  - <(자식 파일명) :pass-props="부모 변수"/>
  - 앞쪽 pass-props는 반드시 kebab-case로 작성하며, 자식 쪽에서 받을 때는 camelCase로 **자동으로 케이스 변환**되므로 주의!
  - 뒤쪽 "부모 변수"가 data()에서 선언되었던 변수

- 적용 예제

  ```vue
  <!-- App.vue -->
  <template>
    <div id="app">
      <!-- 2. 내려보냄 -->
      <TestComponent
        :pass-props="passProps"
      />
    </div>
  </template>
  
  <script>
  import TestComponent from '@/components/TestComponent'
  
  export default {
    name: 'App',
    data(){
      return {
        // 1. 선언
        passProps : "내려보내는 데이터"
      }
    },
    components: {
      TestComponent
    }
  }
  </script>
  ...
  ```

  ```vue
  <!-- TestComponent.vue -->
  <template>
    <div>
      <!-- 4. 사용 -->
      <h1> {{ passProps }} </h1>
    </div>
  </template>
  
  <script>
  export default {
    name : "TestComponent",
    props : {
      // 3. 받은 데이터 타입 명시
      passProps: String,
    }
  }
  </script>
  ...
  ```

## 5-2. Emit Event (자식 => 부모)

- 자식에서 부모 쪽으로 보낼 때는 데이터를 직접 보내는 것이 아닌, 자식 쪽에서 데이터를 담은 emit 이벤트를 발생시키면 부모가 그 이벤트를 듣고 데이터를 받는 방식

- 전체 흐름

  - 자식 template에서 특정 트리거가 발생하면 함수를 실행
  - 자식 methods에서 this.$emit을 이용해 보낼 데이터를 담은 이벤트를 발생시킴
  - 부모 template에서 자식 컴포넌트에서 올라온 이벤트를 듣고 함수를 호출
  - 부모 methods에서 이벤트에 들어있던 데이터를 받아 연산 수행

- 자식 컴포넌트에서의 emit 구문의 이벤트 이름은 부모 컴포넌트에서 감지하는 이벤트 이름과 일치해야 함

- 적용 예제

  ```vue
  <!-- TestComponent.vue -->
  <template>
    <div>
      <!-- 1. 트리거 발생 감지 -->
      <input
        type="text"
        v-model="emitInputData"
        @keyup.enter="emitInput"
      >
    </div>
  </template>
  
  <script>
  export default {
    name : "TestComponent",
    data() {
      return {
        emitInputData: null,
      }
    },
    methods: {
      // 2. 보낼 데이터를 담은 이벤트를 발생시킴
      emitInput() {
        this.$emit('emit-input', this.emitInputData)
        this.emitInputData = ""
      }
    }
  }
  </script>
  ...
  ```

  ```vue
  <!-- App.vue -->
  <template>
    <div id="app">
      <h1> {{ childData }} </h1>
      <!-- 3. 자식 쪽의 이벤트를 감지 -->
      <TestComponent
        @emit-input="getEmitData"
      />
    </div>
  </template>
  
  <script>
  import TestComponent from '@/components/TestComponent'
  
  export default {
    name: 'App',
    components: {
      TestComponent
    },
    data() {
      return {
        childData : ""
      }
    },
    methods: {
      // 4. 받은 데이터로 연산
      getEmitData(payload) {
        this.childData = payload
      }
    }
  }
  </script>
  ```

## 5-3. 코드가 헷갈릴 때를 위한 파트별 총 복습

- 각 Vue 파일의 script 안에서

  - import : 자식 파일의 정보를 불러오고 선언하는 곳, 추후 axios 등의 기능도 호출 가능


  - components : 자식 파일을 쓸 수 있게 등록하는 곳
  - data() : 해당 파일 안에서 사용할 데이터를 선언하는 곳

  - props : 부모 파일에서 받은 데이터 형식을 등록하는 곳 

  - methods : 각종 함수를 작성하는 곳. 부모 파일에게 보낼 이벤트를 this.$emit으로 발생시키기도 함. data 또는 props에서 선언(등록)된 파일을 건드릴 때는 this.변수명으로 사용 

  - props와 emit을 동시에 사용할 때는 필연적으로 methods에서 props의 데이터를 사용하게 될 것임
  - 필요시 computed나 watch 등을 methods 대신 사용할 수도 있음

- template 안에서

  - {{ 변수명 }}으로 script 부분에서 선언된 파일 사용 가능
  - @ (v-on)를 붙여서 이벤트 조건을 충족하면 = "특정 함수를 실행 가능"
  - : (v-bind)를 붙이면 =""를 문자열에서 JavaScript 구문으로 바꿀 수 있음

- 추가로, Vue 파일의 이름은 파스칼 케이스로 반드시 2단어 이상으로 작성되어야 하며, 부모-자식 파일의 이름은 MyData - MyDataDetail 식으로 자식 파일의 이름 안에 부모 파일의 이름이 온전히 들어가도록 하는 것을 권장 