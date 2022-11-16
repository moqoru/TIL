# 9. 막간 UX / UI 분야 소개

## 9-1. UX

- User Experience, 유저가 느끼는 느낌, 태도와 행동을 디자인
- 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정이 중요

## 9-2. UI

- User InterFace, 유저에게 보여지는 화면을 디자인
- 사용자가 보다 쉽고 편리하게 사용할 수 있는 부분을 고려해서 디자인해야 함

## 9-3. Prototyping

- 개발 중인 소프트웨어 프로그램의 완성되기 전 버전을 제작하여 현재 과정을 체크
- 현재는 Figma라는 툴이 시장 점유율이 가장 높음 (실시간 협업 가능, 대부분 기능 무료)

- 프로젝트를 시작하기 전에 충분한 기획을 거쳐서 프로토타입을 설계해보는 과정이 필요함
- 어떻게 효과적으로 협업할 수 있을지 다양한 방법과 도구를 찾아보고 학습, 여러 프로젝트를 경험하는 과정이 필요함

# 10. Vue Router

## 10-1. Routing

- 네트워크에서 경로를 선택하는 프로세스를 뜻하며, 웹 서비스에서는 유저가 방문한 URL에 대해 적절한 결과를 응답하도록 함
- SSR에서는 서버가 모든 라우팅을 통제해서 URL의 결정권을 서버가 갖고 있었음
- SPA/CSR에서는 하나의 URL만 가지고 있지만, 새로고침/뒤로 가기 기능 등이 막혀 버리기 때문에 UX의 관점에서는 라우팅이 필요한 상황이 있음

## 10-2. Vue Router 기초

- Vue Router는 Vue의 공식 라우터로, SPA를 MPA처럼 **URL을 이동하면서 사용 가능**해서 뒤로가기, 새로고침 등의 기능을 문제 없이 사용할 수 있음

- **vue add router** 구문 입력 : vuex와 마찬가지로 vue 프로젝트 생성 후 입력함, 이후 물어보는 질문에는 모두 yes로 응답하면 됨

- App.vue에 router-link 요소와 router-view가 추가됨

  - router-link : a 태그와 비슷하게 URL을 이동시키는 기능, to 속성으로 지정된 목표 경로로 렌더링됨 (필요하면 다른 태그로 바꿀 수도 있음)
  - router-view : 주어진 URL과 일치하는 컴포넌트만 골라 렌더링, vuex때와 비슷하지만 어떤 컴포넌트건 **똑같은 자리에, 하나씩만 렌더링**되도록 함. 필요시 props 등의 데이터를 전달하는 것도 가능

  ```vue
  <!-- App.vue -->
  <template>
    <div id="app">
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link>
      </nav>
      <router-view/>
    </div>
  </template>
  ...
  ```

- router/index.js 파일이 생성됨 : 라우터에 관련한 정보 및 설정이 작성됨, routes에 URL과 컴포넌트를 매핑

  ```javascript
  // router/index.js => 매핑하는 부분만 따로 뽑아 옴.
  ...
  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  ]
  ...
  ```

- views 폴더가 새로 생성되어, 컴포넌트를 components 폴더와 views 폴더로 분리하여 작성

  - views/.vue : routes에 매핑되는 컴포넌트, 즉 \<router-view/> 위치에 렌더링 되는 컴포넌트만 모아둔다. 이름 구분을 위해 파일 이름을 ~View로 짓는 것을 권장
  - components/.vue : views 폴더의 컴포넌트들의 하위 컴포넌트들을 모아둠


## 10-3. Vue Router 실습

- 주소를 이동하는 방법은 선언적 방식과 프로그래밍 방식이 있음

  - 선언적 방식 네비게이션
    - 먼저 import로 컴포넌트의 주소를 명시해 주고, routes 안에서 router-link의 to 속성으로 주소 전달
    - router/index.js에서 routes에 name 인자로 지정을 해두면 v-bind를 이용해서 동적인 값을 사용하는 것도 가능


  ```javascript
  // router/index.js
  ...
  import HomeView from '../views/HomeView.vue'
  import AboutView from '@/views/AboutView' // 파일의 경로를 명시해 주어야 함
  ...
  const routes = [
    {
      path: '/', // 선언적 방식에서는 path를 직접 쓰거나...
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about', // name을 쓰는 방법을 이용할 수 있음
      component: AboutView
    },
  ]
  ...
  ```

  ```vue
  <!--App.vue-->
  <template>
    <div id="app">
      <nav>
        <!-- 선언적 방식 -->
        <router-link to="/">Home</router-link> |
        <router-link :to="{ name: 'about' }">About</router-link> |
      </nav>
      <router-view/>
    </div>
  </template>
  ```

  - 프로그래밍 방식
    - vue 인스턴스 내부에서는 라우터 인스턴스에 $router로 접근할 수 있음
    - 이를 이용해 this.$router.push(...) 구문으로 선언적 방식과 똑같은 효과를 낼 수 있음
    - push라는 이름에 맞게, history stack에 이동할 URL을 넣는 방식, 방문 기록이 남기 때문에 브라우저의 뒤로 가기 버튼 기능을 구현할 수 있음

  ```vue
  <!--views/AboutView.vue-->
  <template>
    <div class="about">
      <h1>This is an about page</h1>
      <button @click="toHome"> 홈으로 </button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutView',
    methods: {
      toHome() {
        this.$router.push({name: 'home'})
      }
    }
  }
  </script>
  ```

- Dynamic Route Matching

  - router/index.js에 route를 추가할 때 (:변수명)으로 인자를 명시해 둠
  - vue 인스턴스 내부에서는 this.$route.params.변수명으로 선언한 뒤 사용 가능
  - 철자 주의! **route**, 지금 접속하는 사이트 하나에만 해당되는 것이라서 **s가 빠진다**고 생각하자!

  ```javascript
  // router/index.js
  import HelloView from '@/views/HelloView'
  ...
  const routes = [
      ...
      {
      path: '/hello/:userName', // 이런 방식으로 명시해 두고...
      name: 'hello',
      component: HelloView
    },
  ]
  ```

  ```vue
  <!-- view/HelloView.vue -->
  <template>
    <div>
      <h1>hello, {{ userName }} </h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloView',
    data() {
      return {
        userName: this.$route.params.userName
      }
    }
  }
  </script>
  ```

- Dynamic Route Matching을 네비게이션에 사용하기

  - 선언적 방식 네비게이션에서는 params를 사용해서, "{ name: "hell", params: {userName: Kitty} }"식으로 사용하면 된다.
  - 마찬가지로 프로그래밍 방식 네비게이션에서는 this.$router.push()에서 () 안에 위 구문을 똑같이 집어넣으면 동작하며, vue 인스턴스 내부의 변수 값을 이용해서 입력값에 따라 주소값이 달라지게 하는 식으로도 쓸 수 있다.

  ```vue
  <!-- App.vue, 선언적 방식의 예시 -->
  <template>
    <div id="app">
      <nav>
        ...
        <router-link :to="{ name: 'hello', params: { userName: 'Billy'} }">Hello</router-link>
      </nav>
      <router-view/>
    </div>
  </template>
  ```

  ```vue
  <!-- views/AboutView.vue, 프로그래밍 방식의 예시 -->
  <template>
    <div class="about">
      <!--v-bind로 입력값과 변수를 바인딩-->
      <input
        type="text"
        @keyup.enter="goToHello"
        v-model="inputData"
      >
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutView',
    data() {
      return {
        inputData: null
      }
    },
    methods: {
      goToHello() {
        // 입력받은 변수 데이터의 값에 따라 URL이 동적으로 바뀌도록 함
        this.$router.push({ name: 'hello', params: { userName: this.inputData} })
        // 이건 보너스, 같은 구문을 이렇게도 표현 가능
        // this.$router.push( { path: `hello/${this.inputData}`} )
      }
    }
  }
  </script>
  ```

- lazy-loading

  - 모든 파일을 한번에 로드하지 않고, 해당 라우터가 동작할 때 해당 컴포넌트의 코드만 따로 렌더링하는 방식. 최초 로드 시간이 빨라짐
  - 해당 부분은 import 구문을 따로 작성하지 않고, route 안에 한 번에 적음

  ```javascript
  // router/index.js
  const routes = [
    ...
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
  ]
  ```

# 11. Navigation Guard

- Vue Router를 통해 특정 URL에 접근할 때 해당 URL로의 접근을 막는 방법
- ex) 로그인이 안 되어 있으면 특정 페이지에 접근할 때 자동으로 로그인 페이지로 리다이렉트

## 11-1. Global Before Guard(전역 가드)

- 애플리케이션 전역에서 동작하며, 따라서 다른 URL 주소로 이동할 때 매번 실행된다.

- router/index.js에 router.beforeEach()를 사용하여 설정하며, 다음 3개의 인자를 받는다.

  - to : 이동할 URL 정보가 담긴 Route 객체, '목적지'
  - from : 현재 URL 정보가 담긴 Route 객체, '출발지'
  - next : 지정한 URL로 이동하기 위해 호출하는 함수, '조건'

- beforeEach 안에서 next()가 호출되지 않으면 화면이 전환되지 않으며, 호출되어야만 화면이 전환됨. 단, 딱 한 번만 호출되어야 함

- 기본적으로는 to의 사이트로 이동하지만, 선언적 방식 네비게이션을 이용해서 강제로 다른 특정 사이트로 이동시킬 수도 있음

  ```javascript
  // router/index.js
  // LoginView 페이지를 'login'이라는 이름으로 만들었다고 가정
  ...
  router.beforeEach((to, from, next) => {
    const isLoggedIn = true // 로그인 여부
    const authPages = ['hello'] // 로그인 필요 페이지
    const isAuthRequired = authPages.includes(to.name) // to가 로그인 필요 사이트인가?를 확인
  
    if (isAuthRequired && !isLoggedIn) {
      next({ name: 'login'}) // 로그인 사이트로 쫓아냄
    } else {
      next() // to 사이트로 그대로 이동
    }
  })
  ```

## 11-2. Router Guard(라우터 가드)

- 특정 URL에서만 동작하는 가드를 만들고 싶을 때 사용

- beforeEnter()를 사용하며, 인자는 beforeEach와 동일하다.

- 매개변수, 쿼리, 해시 값 변경시에는 실행되지 않고, 오로지 다른 경로에서 탐색할 때만 실행

  ```javascript
  // router/index.js
  // LoginView로 들어가려고 할 때 이미 로그인 된 경우 HomeView로 이동하기
  import LoginView from '@/views/HelloView'
  ...
  const isLoggedIn = true
  
  const routes = [
    ...
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter(to, from, next){
        if (isLoggedIn === true) {
          next({ name: 'home'}) // 이미 로그인 된 상태일 경우
        } else {
          next()
        }
      }
    }
  ]
  ```

## 11-3. Component Guard(컴포넌트 가드)

- 특정 컴포넌트 안에서 가드를 지정할 때 사용

- beforeRouteUpdate()를 사용하며, 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행된다. 물론 인자는 동일하게 to, from, next이다.

- 예를 들어 About 페이지에서 'Kitty'를 입력 후 '/hello/:userName' 페이지로 이동하게 되는 경우,

  - 주소창에는 hello/Kitty, 인터넷 창의 내용에도 똑같이 hello, Kitty라고 되어 있다.
  - 하지만 여기서 Hello 이동 버튼을 누르면...? (/hello/Billy로 바인딩 되어 있다)
  - 주소창은 Billy로 변하지만, 인터넷 창의 내용은 Kitty로 그대로다...?!
  - 이는 라우터가 효율 때문에 컴포넌트를 그냥 재사용해버려서 데이터를 새로 가져오지 않기 때문이다.
  - 이를 컴포넌트 가드로 방지할 수 있으며, 변경시 인터넷 창의 내용도 함께 바뀐다.

  ```vue
  <template>
    <div>
      <h1>hello, {{ userName }} </h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HelloView',
    data() {
      return {
        userName: this.$route.params.userName
      }
    },
    // 가드 사용 부분.
    beforeRouteUpdate(to, from, next){
      this.userName = to.params.userName
      next()
    }
  }
  </script>
  ```

## 11-4. 404 Not Found

- 유효하지 않은 페이지로의 접근을 막고 데이터가 없음을 명시한다.

- 예를 들어 /article/40을 요청을 보냈는데 40번 게시글이 없다면, /article/:id/로만 작성한 경우 억지로 렌더링하려고 하게 된다. 이런 경우를 404로 막는 것

- 또한 간혹 페이지를 /404-NF/로 했는데 하필 /:id/로 가는 사이트가 더 있을 경우, 404 쪽이 더 위로 가지 않으면 :id 쪽에 씹혀서 404 사이트로 제대로 가지 않는다! 숫자에 한해서만 우선순위가 뒤집힐 수 있다는 사실을 명심할 것.

- redirect 기능을 활용하여 path에 '*' 기호를 쓸 수 있는데, 반드시 routes의 최하단에 작성해야 함에 주의할 것! (/aticles/\* 같은 식으로도 쓸 수 있다, / 갯수가 다르면 서로 다른 것으로 판정)

  ```javascript
  // router/index.js
  const routes = [
    ...
    {
      path: '/404-NF',
      name: 'NotFound404',
      component: NotFound404
    },
    {
      path: '/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '*',
      redirect: { name: 'NotFound404' }
    },
  ]
  ```

  ```javascript
  <!--vue 인스턴스에서 $router.push 구문을 이용할 경우, axios 설치 필요-->
  axios({
    ...
  })
  .then((response) => {
    ...
  })
  .catch((error) => {
    this.$router.push('/404-NF')
    console.log(error)
  })
  ```

# 12. 최종 정리 + 게시판 사이트 제작 실습

- 처음 시작할 때는...

  - vue create (프로젝트명)
  - cd (프로젝트명)
  - vue add vuex, vue add router, vue add axios (import axios from 'axios' 구문 필요)
  - npm run serve

- 프로젝트 파일 구조

  - App.vue : 최상위 부모 vue 파일
  - views : URL 마다 하나씩 매핑된 vue 파일들이 들어감
  - components : 기능이 분화된 하위 vue 파일들이 들어감
  - router/index.js : router 설치시 사용, URL을 분화하고 각 파일들과 연결함

  - store/index.js : vuex 설치시 사용, 모든 vue파일들이 함께 쓰는 데이터의 중앙 저장소
  - assets : 정적 파일들을 저장

- 추가 정보 : **Optional Chaining**

  - .이 들어갈 자리에 ?. 기호를 사용

  - **?. 기호 앞의 객체 값이 undefined이거나 null이면 에러 없이 undefined를 반환**

  - 예를 들어 아래와 같은 상황에서 article에 데이터가 제대로 들어오지 못해서 값이 null인 경우, 그냥 렌더링 되지 않도록 처리함

  ```vue
  <!--views/DetailView.vue-->
  <template>
    <div>
      <h1>Detail</h1>
      <p>글 번호 : {{ article?.id }}</p>
      <p>글 제목 : {{ article?.title }}</p>
      <p>글 내용 : {{ article?.content }}</p>
      ...
    </div>
  </template>
  ```

- 게시판 사이트 제작 실습

  ```javascript
  // router/index.js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import IndexView from '../views/IndexView.vue'
  import CreateView from '../views/CreateView.vue'
  import DetailView from '../views/DetailView.vue'
  import NotFound404 from '../views/NotFound404.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/',
      name: 'index',
      component: IndexView
    },
    {
      path: '/create',
      name: 'create',
      component: CreateView
    },
    {
      path: '/404-not-found',
      name: 'NotFound404',
      component: NotFound404
    },
    {
      path: '/:id',
      name: 'detail',
      component: DetailView
    },
    {
      path: '*',
      redirect: { name: 'NotFound404' }
    },
  ]
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router
  ```

  ```javascript
  // store/index.js
  import Vue from 'vue'
  import Vuex from 'vuex'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    state: {
      article_id: 3,
      articles: [
        {
          id: 1,
          title: 'title',
          content: 'content',
          createdAt: new Date().getTime(),
        },
        {
          id: 2,
          title: 'title2',
          content: 'content2',
          createdAt: new Date().getTime(),
        }
      ]
    },
    getters: {
    },
    mutations: {
      CREATE_ARTICLE(state, article) {
        state.articles.push(article)
        state.article_id = state.article_id + 1
      },
      DELETE_ARTICLE(state, article_id) {
        state.articles = state.articles.filter((article) => {
          return !(article.id === article_id)
        })
      },
    },
    actions: {
      createArticle(context, payload) {
        const article = {
          id: context.state.article_id,
          title: payload.title,
          content: payload.content,
          createdAt: new Date().getTime()
        }
        context.commit('CREATE_ARTICLE', article)
      }
    },
    modules: {
    }
  })
  ```

  ```vue
  <!--App.vue-->
  <template>
    <div id="app">
      <router-view/>
    </div>
  </template>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  
  nav {
    padding: 30px;
  }
  
  nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  nav a.router-link-exact-active {
    color: #42b983;
  }
  </style>
  ```

  ```vue
  <!--components/ArticleItem.vue-->
  <template>
    <div @click="goDetail(article.id)">
      <p>글 번호 : {{ article.id }}</p>
      <p>글 제목 : {{ article.title }}</p>
      <hr>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ArticleItem',
    props: {
      article: Object,
    },
    methods: {
      goDetail(id) {
        this.$router.push({ name: 'detail', params: {id}})
        // this.$router.push({ name: 'detail', params: {id: `${this.article.id}` }})
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  <!--views/CreateView.vue-->
  <template>
    <div>
      <h1>게시글 작성</h1>
      <form @submit.prevent="createArticle">
        <input type="text" v-model.trim="title"><br>
        <textarea v-model.trim="content"></textarea>
        <input type="submit">
      </form>
      <router-link :to="{ name: 'index' }">뒤로가기</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CreateView',
    data() {
      return {
        title: null,
        content: null,
      }
    },
    methods: {
      createArticle() {
        const title = this.title
        const content = this.content
        const payload = {
          title, content
        }
        this.$store.dispatch('createArticle', payload)
        this.$router.push({ name: 'index' })
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  <!--views/DetailView.vue-->
  <template>
    <div>
      <h1>Detail</h1>
      <p>글 번호 : {{ article?.id }}</p>
      <p>글 제목 : {{ article?.title }}</p>
      <p>글 내용 : {{ article?.content }}</p>
      <!-- <p>글 작성시간 : {{ article?.createdAt }}</p> -->
      <p>작성시간 : {{ articleCreatedAt }}</p>
      <button @click="deleteArticle">삭제</button><br>
      <router-link :to="{ name: 'index' }">뒤로가기</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'DetailView',
    data() {
      return {
        article: null,
      }
    },
    computed: {
      articles() {
        return this.$store.state.articles
      },
      articleCreatedAt() {
        const article = this.article
        const createdAt = new Date(article?.createdAt).toLocaleString()
        return createdAt
      },
    },
    methods: {
      getArticleById(id) {
        // const id = this.$route.params.id
        for (const article of this.articles) {
          if (article.id === Number(id)) {
            this.article = article
            break
          }
        }
        if (this.article === null) {
          this.$router.push({ name: 'NotFound404' })
        }
      },
      deleteArticle() {
        this.$store.commit('DELETE_ARTICLE', this.article.id)
        this.$router.push({ name: 'index' })
      }
    },
    created() {
      this.getArticleById(this.$route.params.id)
    }
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  <!--views/IndexView.vue-->
  <template>
    <div>
      <h1>Articles</h1>
      <router-link :to="{ name: 'create' }">게시글 작성</router-link>
      <ArticleItem 
        v-for="article in articles"
        :key="article.id"
        :article=article
      />
    </div>
  </template>
  
  <script>
  import ArticleItem from '@/components/ArticleItem'
  
  export default {
    name: 'IndexView',
    components: {
      ArticleItem,
    },
    computed: {
      articles() {
        return this.$store.state.articles
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  <!--views/NotFound404.vue-->
  <template>
    <div>
      <h1>404 Not Found</h1>
    </div>
  </template>
  
  <script>
  export default {
    name: 'NotFound404',
  }
  </script>
  
  <style>
  
  </style>
  ```

  