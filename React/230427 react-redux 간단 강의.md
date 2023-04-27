# react-redux 간단 강의

- 참고 영상 : https://youtu.be/yjuwpf7VH74
- props로만 정보를 전달하려고 하면 연결된 모든 컴포넌트에 props 구문을 달아야 하므로,컴포넌트끼리의 연결 단계가 깊어질 수록 정보 전달이 힘들어진다...
- redux를 쓰게 되면 중간 단계의 컴포넌트를 거칠 필요 없이 바로 원하는 컴포넌트에 정보를 전달할 수 있으므로, 퍼포먼스를 상승시킬 수 있다!
- 데이터를 외부에서 직접 제어할 수 없도록 만들어서, 의도치 않게 state 값이 바뀌는 문제를 차단 ⇒ 애플리케이션을 예측 가능하게 만들어 줌

## 리덕스 구문 사용법

- 먼저 redux와 react-redux 설치

```
npm install redux react-redux
```

- 코드에서 store부터 만들어주기 
  - **정보를 저장할 전역 변수**

```react
import {createStore} from 'redux';
const store = createStore();
```

- 스토어를 만들면 reducer도 만들어 줘야 함 
  - store 안의 state를 어떻게 바꿀지 설정
  - useState 만드는 것과 동일함!

```react
function reducer(currentState, action) {
    // 아직 설정되지 않았다면... 기본 값으로 number에 1 넣기.
    if (currentState === undefined) {
        return {
            number: 1,
        }
    }
    // 새로운 state를 만들 때 과거의 state를 복제, 불변성을 유지시킬 수 있음
    const newState = {...currentState};
    return newState;
}
```

- react-redux의 ~~4대장~~ 3대장
  - Provider : state를 사용할 컴포넌트 범위를 정의
  - useSelector : 어떤 state 값을 쓸 지 선택
  - useDispatch : state 값을 변경할 때 사용
  - connect : 클래스형 컴포넌트에서 컴포넌트를 특정 함수로 감싸서 값이나 함수를 props로 받아오는 거 (재사용성), 함수형 쓸 때는 Hooks 쓰면 되므로 별로 안 씀

```react
import {Provider, useSelector, useDispatch} from 'react-redux';
```

- Provider 사용
  - 필요한 컴포넌트 부분을 골라 Provider 태그로 감싸 준다.
  - 필수적으로 store라는 prop을 정의해 줘야 함, 예제에서는 createStore로 만들었던 걸 집어 넣어 줌
  - 이렇게 하면 store를 Provider 내부에서 사용할 수 있게 됨

```react
// 저쪼 위에서 만들어 뒀던 거
const store = createStore();

export default function App() {
    return (
        <div id="container">
            <h1>Root</h1>
            <div id="grid">
            	<Provider store={store}>
                	<Left1></Left1>
                    <Right1></Right1>
                </Provider>
            </div>
        </div>
    )
}
```

- useSelector 사용
  - reducer의 값을 원하는 컴포넌트에 표시할 때 사용 (읽기 기능만 쓸 때!)

```react
function Left3(props){
    // 윗 내용 요약 : store를 createStore()로 만들었음.
    // 그리고 reducer로 수정할 수 있게 만들어서 number 값 지정을 해 주었고,
    // Provider로 이 변수를 쓸 수 있게 설정해 준 다음
    // useSelector로 store 안의 state, 그 중에서도 number를 찝어낸 것!
    const number = useSelector(state=>state.number);
    return (
        <div>
            <h1>Left3 : {number}</h1>
        </div>
    )
}
```

- useDispatch 사용
  - reducer의 값을 원하는 컴포넌트에서 수정하게 만들 때 사용
  - 단, 그 변수를 직접 고칠 순 없고 reducer에 수정 '요청'을 보내면 reducer에서 구분해서 처리하는 방식
  - 선언은 useDispatch()만 써서 해 두고, 실제로 사용할 때는 dispatch()에 내부 인자로 요청 사항 정보를 넣어 주는 방식

```react
function reducer(currentState, action) {
    if (currentState === undefined) {
        return {
            number: 1,
        }
    }
    const newState = {...currentState};
    // 여기부터 추가된 코드
    if (action.type === 'ADD') {
        newState.number += 1;
    }
    return newState;
}

function Right3(props){
    const dispatch = useDispatch();
    return (
        <div>
            <h1>Right3</h1>
            <input
                type="button"
                value="+"
                onClick={() => {
                    dispatch({ type: 'ADD'});
                }}
            ></input>
        </div>
    )
}
```

