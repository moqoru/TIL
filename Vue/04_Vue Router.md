# 9. 막간

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

- 

## 10-2. Vue Router 기초

- 

## 10-3. Vue Router 실습

- 

# 11. Navigation Guard

- Vue Router를 통해 특정 URL에 접근할 때 해당 URL로의 접근을 막는 방법
- ex) 로그인이 안 되어 있으면 특정 페이지에 접근할 때 자동으로 로그인 페이지로 리다이렉트

## 11-1. 전역 가드

- 

## 11-2. 라우터 가드

- 

## 11-3. 컴포넌트 가드

- 

# 12. 최종 정리 + Aritcles App 제작 실습

- vue add vuex, vue add router, vue add axios

components - 기능을 분화한 하위 파일들

views - 직접 보여주는 파일들

router - URL 분화, url과 파일을 연결함

store - vuex 기능에서 사용, 모든 vue파일들이 내려받아 사용

src에 기본으로 있는 App.vue - 모든 vue 파일들을 제어, 라우터와 연결하는 실질적인 메인 파트

- 추가 : .?

- 제작 실습

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

  