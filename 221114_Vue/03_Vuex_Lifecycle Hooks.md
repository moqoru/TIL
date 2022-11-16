# 6. Vuex

## 6-1. Vuex 기초

- Component의 중첩이 너무 깊어지면 데이터의 전달이 쉽지 않음, 이럴 경우 Vuex라는 중앙 저장소(store)에 데이터를 모아서 상태를 관리하도록 함 
- 필수적으로 사용할 필요는 없고, 일정 규모 이상의 SPA를 구축하는 경우 Vuex를 사용하면 더 효율적임

## 6-2. Vuex 플러그인 설치

- Vue 프로젝트 생성, 디렉토리 이동 후 **vue add vuex** 구문 입력

- src/store/index.js 파일이 만들어지며, state, getters, mutations, actions 4개의 공간이 만들어짐 (modules는 이번 과정에서는 사용하지 않음)

  ```javascript
  import Vue from 'vue'
  import Vuex from 'vuex'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    state: {
    },
    getters: {
    },
    mutations: {
    },
    actions: {
    },
    modules: {
    }
  })
  ```

- 기능 비교

  |   Vuex    | Vue 인스턴스 |          비고           |
  | :-------: | :----------: | :---------------------: |
  |   state   |    data()    |                         |
  |  getters  |   computed   |                         |
  | mutations |   methods    |    state 변경 부분만    |
  |  actions  |   methods    | 비동기 포함 나머지 전부 |

## 6-3. Vuex 사용하기

- state

  - 중앙에서 관리하는 모든 상태 정보를 저장
  - 다른 vue파일에서 쓸 때는 $store.state.변수로 사용

  ```javascript
  state : {
      message: 'message in store',
  },
  ```

  ```vue
  <!-- 다른 vue 함수에서 -->
  <script>
  	export default {
          computed: {
              message() {
                  return this.$store.state.message
              }
          }
      }
  </script>
  ```

- actions

  - methods와 비슷하게 각종 함수가 들어가지만 state를 직접적으로 변경하지는 않으며, 비동기 작업이 들어올 수 있음
  - 주로 연산을 진행하다가 state를 건드리는 부분에서만 mutations를 호출하는 방식으로 사용, store.js의 모든 요소와 메서드를 탐색(만)할 수 있음
  - 소속 함수의 인자
    - context : 정의할 때는 store 내부의 다른 요소나 메서드를 탐색하는 용도로 사용, 다른 vue 파일에서 호출할 때는 사용하고자 하는 actions 함수 이름을 ''로 감싸서 적는다
    - payload : 다른 vue 파일에서 보내고 받는 데이터
  - 다른 vue 파일에서 호출할 때는 this.$store.dispatch('함수명', 데이터) 메서드로 호출, actions 안에서 다른 actions를 호출할 때도 this.dispatch(...)로 호출하면 된다!

  ```javascript
  actions : {
      changeMessage(context, message) {
          console.log(context.state) // 이런 방식으로 store.js의 다른 요소와 메서드 탐색 가능
          console.log(mesage)
      },
  },
  ```

  ```vue
  <!-- 다른 vue 함수에서 -->
  <script>
  	export default {
          methods: {
              changeMessage() {
                  const newMessage = "payload"
                  this.$store.dispatch('changeMessage', newMessage)
              }
          }
      }
  </script>
  ```

- mutations

  - state를 직접적으로 변경하는 함수가 들어가며, 동기적인 함수만 들어감
  - 여기에 소속된 함수만 특별 취급으로 UPPER_SNAKE_CASE로 작성
  - 소속 함수의 인자
    - state : 말 그대로 모든 상태 정보가 저장된 state 자신을 가리킴, 이를 이용해서 state의 값을 변경
    - payload : getters에서 보내주는 데이터
  - actions에서 호출할 때는 context.commit('함수명', 데이터) 메서드로 호출

  ```javascript
  mutations : {
      CHANGE_MESSAGE(state, message) {
          state.message = message
      },
  },
  actions : {
      changeMessage(context, message) {
          context.commit('CHANGE_MESSAGE', message)
      },
  },
  ```

- getters

  - computed와 비슷하게 계산된 값을 얻는 함수가 들어가며, state의 값은 바꾸지 않음
  - 소속 함수의 인자
    - state : 마찬가지로 state 자신을 가리킴
    - getters : 추가 인자로 getters를 받으면 같은 위치의 또 다른 함수를 콜백으로 호출해서 연산하는 것도 가능

  ```javascript
  getters : {
      messageLength(state) {
          return state.message.length
      },
      messageLengthDouble(state, getters) {
          return getters.messageLength * 2
      }
  }
  ```

  ```vue
  <!-- 다른 vue 함수에서 -->
  <script>
  	export default {
          computed: {
              messageLength() {
                  return this.$store.getters.messageLength
              }
          }
      }
  </script>
  ```

# 7. Lifecycle Hooks

- 각 Vue 인스턴스는 생성과 소멸 과정 사이에 단계별 초기화 과정을 거치고, 이 단계를 트리거로 특정 로직을 수행할 수 있음
- 부모-자식 관계에 따라 순서가 정해져있지는 않음
- 각 Vue 파일의 export default 안에서 사용 가능 (data나 methods와 같은 레벨)
- created()
  - Vue Instance 생성 후 호출, '첫 실행시'등의 조건에 어울림
  - 아직 mount되지 않아 요소에 접근할 수는 없음
- mounted()
  - Vue Instance가 요소에 mount 된 뒤 호출됨
  - DOM 접근이 가능해서 요소를 조작할 수 있음
- updated()
  - 데이터가 변경되어 DOM에 변화를 줄 때 호출

# 8. Todo List 실습

- 시간상의 이유로 CRUD + 로컬 스토리지 기능이 완성된 코드만 업로드

- Local Storage와 관련 메서드

  - 브라우저를 종료하고 다시 실행해도 데이터가 보존되는 공간, 검색 이력 기능 등 데이터 보존용으로 사용 가능
  - setItem(key, value) : key, value 형태로 데이터 저장
  - getItem(key) : key에 해당하는 아이템 조회
  - 데이터가 문자열 형태로 저장되므로 JSON.stringify와 JSON.parse로 문자열 변환 작업 필요

- vuex-persistedstate

  - vuex state를 자동으로 브라우저의 Local Storage에 저장해주고 다시 state로 불러와 주는 라이브러리
  - npm i vuex-persistedstate로 설치

- 참고 : mutations의 UPDATE_TODO_STATUS의 원리?

  - todo 리스트 중 특정 항목만 isCompleted를 반대로 뒤집는 기능임
    - 반복을 돌면서 바꿀 todo만 찾아서
    - 바꿀 todo의 참/거짓 값을 바꿔 주고
    - 나온 결과를 다시 todos로 할당시킨 뒤
    - 원하는 부분만 바꾼 걸 하나의 배열로 모아서 반환하면 다시 통째로 보여주는 식
  - 왜 이렇게 복잡한가?
    - TodoListItem이라는 똑같은 객체를 반복해서 넣는 식이라 하나만 똑 떼서 고칠 수가 없음...
    - 여러 개를 복붙하다보니 내용물을 직접 들여다보지 않으면 구분하는 게 불가능하다!
    - 그래서 싸그리 돌려서 요청 보낸 거랑 일치하는 것을 찾아 바꾸는 식으로 구현하는 것.

  ```javascript
  // store/index.js
  import Vue from 'vue'
  import Vuex from 'vuex'
  import createPersistedState from 'vuex-persistedstate'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    plugins: [
      createPersistedState(),
    ],
    state: {
      todos: [],
    },
    getters: {
      allTodosCount(state) {
        return state.todos.length
      },
      completedTodosCount(state) {
        // 1. 완료된 투두만 모아놓은 새로운 배열을 생성
        const completedTodos = state.todos.filter((todo) => {
          return todo.isCompleted === true
        })
        // 2. 그 새로운 배열의 길이를 반환
        return completedTodos.length
      },
      unCompletedTodosCount(state, getters) {
        return getters.allTodosCount - getters.completedTodosCount
      },
    },
    mutations: {
      CREATE_TODO(state, todoItem) {
        state.todos.push(todoItem)
      },
      DELETE_TODO(state, todoItem) {
        const index = state.todos.indexOf(todoItem)
        state.todos.splice(index, 1)
      },
      UPDATE_TODO_STATUS(state, todoItem) {
        console.log(todoItem)
        // todos 배열에서 선택된 todo의 is_completed값만 토글한 후
        // 업데이트 된 todos 배열로 되어야 함
  
        // made by 승태
        // const index = state.todos.indexOf(todoItem)
        // state.todos[index].isCompleted = !state.todos[index].isCompleted
  
        state.todos = state.todos.map((todo) => {
          if (todo === todoItem) {
            todo.isCompleted = !todo.isCompleted
          } 
          return todo
        })
      },
      // LOAD_TODOS(state) { 
      //   const localStorageTodos = localStorage.getItem('todos')
      //   const parsedTodos = JSON.parse(localStorageTodos)
      //   // console.log(parsedTodos)
      //   state.todos = parsedTodos
      // },
    },
    actions: {
      createTodo(context, todoTitle) {
        // Todo 객체 만들기
        const todoItem = {
          title: todoTitle,
          isCompleted: false,
        }
        // console.log(todoItem)
        context.commit('CREATE_TODO', todoItem)
        // context.dispatch('saveTodosToLocalStorage')
      },
      deleteTodo(context, todoItem) {
        context.commit('DELETE_TODO', todoItem)
        // context.dispatch('saveTodosToLocalStorage')
      },
      updateTodoStatus(context, todoItem) {
        context.commit('UPDATE_TODO_STATUS', todoItem)
        // context.dispatch('saveTodosToLocalStorage')
      },
      // saveTodosToLocalStorage(context) {
      //   const jsonTodos = JSON.stringify(context.state.todos)
      //   localStorage.setItem('todos', jsonTodos)
      // },
      // loadTodos(context) {
      //   context.commit('LOAD_TODOS')
      // }
    },
    modules: {
    }
  })
  ```

  ```vue
  <!-- App.vue -->
  <template>
    <div id="app">
      <h1>Todo List</h1>
      <h2>모든 Todo 개수: {{ allTodosCount }}</h2>
      <h2>완료된 Todo 개수: {{ completedTodosCount }}</h2>
      <h2>미완료된 Todo 개수: {{ unCompletedTodosCount }}</h2>
      <TodoList/>
      <TodoForm/>
      <!-- <button @click="loadTodos">Todo 불러오기</button> -->
    </div>
  </template>
  
  <script>
  import TodoList from '@/components/TodoList'
  import TodoForm from '@/components/TodoForm'
  
  export default {
    name: 'App',
    components: {
      TodoList,
      TodoForm,
    },
    computed: {
      allTodosCount() {
        return this.$store.getters.allTodosCount
      },
      completedTodosCount() {
        return this.$store.getters.completedTodosCount
      },
      unCompletedTodosCount() {
        return this.$store.getters.unCompletedTodosCount
      }    
    },
    methods: {
      loadTodos() {
        this.$store.dispatch('loadTodos')
      }
    }
  }
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  ```

  ```vue
  <!-- components/TodoForm.vue -->
  <template>
    <div>
      <input 
        type="text"
        v-model.trim="todoTitle"
        @keyup.enter="createTodo"
      >
    </div>
  </template>
  
  <script>
  export default {
    name:'TodoForm',
    data() {
      return {
        todoTitle: null,
      }
    },
    methods: {
      createTodo() {
        // console.log(this.todoTitle)
        if (this.todoTitle) {
          this.$store.dispatch('createTodo', this.todoTitle)
        }
        this.todoTitle = null
      }
    }
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  <!-- components/TodoList.vue -->
  <template>
    <div>
      <TodoListItem
        v-for="(todo, index) in todos"
        :key="index"
        :todo="todo"
      />
    </div>
  </template>
  
  <script>
  import TodoListItem from '@/components/TodoListItem'
  
  export default {
    name: 'TodoList',
    components: {
      TodoListItem,
    },
    computed: {
      todos() {
        return this.$store.state.todos
      }
    },
  }
  </script>
  
  <style>
  
  </style>
  ```

  ```vue
  <!-- components/TodoListItem.vue -->
  <template>
    <div>
      <span 
        @click="updateTodoStatus"
        :class="{ 'is-completed': todo.isCompleted }"
      >
        {{ todo.title }}
      </span>
      <button @click="deleteTodo">Delete</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TodoListItem',
    props: {
      todo: Object,
    },
    methods: {
      deleteTodo() {
        // console.log('삭제 메서드 호출!!')
        this.$store.dispatch('deleteTodo', this.todo)
        // this.$store.commit('DELETE_TODO', this.todo)
      },
      updateTodoStatus() {
        this.$store.dispatch('updateTodoStatus', this.todo)
      },
    }
  }
  </script>
  
  <style>
    .is-completed {
      text-decoration: line-through;
    }
  </style>
  ```