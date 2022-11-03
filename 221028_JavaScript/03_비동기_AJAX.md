# 8. JavaScript의 비동기 처리

## 8-1. 동기 vs 비동기

- 동기(Synchronous) : 모든 일을 순서대로 하나씩 처리하는 것, 이전 작업이 끝나야 다음 작업을 시작한다

- 비동기(Asynchronous) : 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 시작한다.

  ```python
  # 항상 동기 식인 python
  
  print('1번째 작업')
  for i in range(10):
      print('2번째 작업', i)
  print('3번째 작업')
  
  # 1번째 작업
  # 2번째 작업 0
  # 2번째 작업 1
  # ...
  # 2번째 작업 9
  # 3번째 작업
  ```

  ```javascript
  // 비동기가 될 수 있는 javascript
  
  function slowRequest(callBack) {
    console.log('1. 오래 걸리는 작업 시작...')
    setTimeout(function() {
      callBack() // 콜백 함수, 곧 2번 구문을 3000ms가 지난 뒤 실행
    }, 3000)
  }
  
  function myCallBack() {
    console.log('2. 콜백 함수 실행')
  }
  
  slowRequest(myCallBack) // 일단 1번 함수를 먼저 실행하고
  console.log('3. 다른 작업 실행') // 3번 구문 출력이 순서상으로는 나중에 나오지만...
  
  // 1. 오래 걸리는 작업 시작...
  // 3. 다른 작업 실행
  // 2. 콜백 함수 실행
  ```

- 비동기를 사용하는 이유 : 먼저 처리되는 부분부터 보여 줄 수 있으므로, 사용자 경험에 긍정적 효과

## 8-2. JavaScript의 비동기 처리

- 하지만 JavaScript는 싱글 스레드 언어라서 동시에 여러 작업을 처리할 수는 없음... 비동기 관련 작업은 브라우저나 Node 환경에서 처리
- 비동기 처리 동작 방식 = **나중에 실행할 구문끼리 비동기 구문으로 한 데 모아버린다!**
  - 일단 모든 작업은 Call Stack에 삽입해서 처리
  - Call Stack에 비동기 구문(setTimeout 등)이 들어오면 Web API에서 처리하도록 함
  - Web API에서 처리가 끝난 작업들은 Task Queue에 순서대로 삽입
  - Call Stack이 비워져야만 Event Loop에서 이것을 확인하여 Task Queue에서 빼내 Call Stack에 삽입
- 정리하면...
  - **JavaScript는 원래 싱글 스레드 언어로 Call Stack 하나만 써서 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업을 Task Queue를 거쳐, Event Loop에 의해서 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 된다.**

## 8-3. Axios

- **공식 문서와 github을 적극 참조**할 것! **사용할 때 부트스트랩처럼 기본 구문이 필요**하다!

- 비동기로 데이터 통신을 할 수 있게 해 주는 라이브러리, Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음

- get, post 등 여러 메서드를 사용 가능하며, 성공했을 때 수행할 로직은 then, 실패했을 때 수행할 로직은 catch로 작성한다.

  ```html
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
      axios.get('요청할 URL')
      	.then(성공하면 수행할 콜백함수)
      	.catch(실패하면 수행할 콜백함수)
      <!-- 사실 한 줄이지만 가독성을 위해 분할해서 적는다. -->
  </script>
  ```

- 주요 문법 (+ <u>뒤쪽 Promise 내용이 섞임</u>)

  - 주로 axios({ key: value, ..., }) 이후 .then((response) => {}), .catch((error) => {}) 형식으로 사용한다.
  - catch 구문은 실행 중간에 한번이라도 실패가 나면 바로 실행된다 (if의 else구문과 유사?)
  - then 구문은 여러개 이어서 실행 가능하며(chaining), catch 구문은 then 구문 사이에도 끼여들어갈 수 있다.
  - then chaining을 할 때는, **앞쪽 then 구문의 return 값이 뒤쪽 then의 인자로 들어가게 된다**!
  - JavaScript의 특성상 뒤쪽 then 구문에서 앞쪽 then 구문에 있었던 변수를 참조할 순 없으므로, 앞쪽 then 구문에서 return을 하기 전 모든 연산을 끝내두어야 한다!

  ```javascript
  // 활용 예시
  btn.addEventListener('click', function () {
      axios({
          method: 'get',
          url: catImageSearchURL,
      })
          .then((response) => {
          const imgSrc = response.data[0].url
          return imgSrc
      })
          .then((imgSrc) => {
          const imgElem = document.createElement('img')
          imgElem.setAttribute('src', imgSrc)
          document.body.appendChild(imgElem)
      })
          .catch((error) => { 
          console.log('실패했다옹')
      })
      console.log('야옹야옹') 
  }
  ```

## 8-4. Callback vs. Promise

- 비동기 처리의 경우 모아놓고 실행하는 비동기 구문간에는 실행 순서가 불명확함

- 콜백 함수 : 다른 함수의 인자로 전달되는 함수

  - 실행 결과를 명확히 하기 위해 활용함. **함수 실행이 다 끝나야 그 함수의 결과값이 인자로 들어가는 콜백 함수가 실행**되는 원리

  ```javascript
  const btn = document.querySelector('button')
  btn.addEventListener('click', () => {
      alert('Complete!')
  })
  ```

- 콜백을 쓰면 비동기 작업을 순차적으로 만들 수 있게 되지만, 너무 과도하면 코드 가독성이 떨어짐...

  - 계속 콜백이 겹쳐지면 파이썬의 n중 포문을 연상케 하는 기다란 > 들여쓰기 형태가 된다. 콜백 지옥(Callback Hell), 파멸의 피라미드(Pyramid of doom)을 찾아볼 것

- 프로미스 객체 : 이 작업이 끝나면 실행시켜주겠다는 약속, 즉 **실행 트리거**를 만들어 준다!

  - 콜백 지옥 문제를 해결하기 위해 비동기 작업이 성공 or 실패되었는지에 따라 각기 다른 함수를 실행하는 프로미스 객체를 사용함
  - 작업이 성공하면 then(), 하나라도 실패하면 catch()를 실행하며, 이전 작업의 결과를 인자로 받아 처리함
  - axios에서 보았듯 들여쓰기가 > 형태가 아니라 일직선을 유지하여 가독성이 좋고, chaining을 사용할 수 있어 콜백의 단점을 보완할 수 있음

# X. JS 미션

- 시작 위치 : DB 4번

- 우리의 목표 : AJAX 기능 구현
  - 팔로우, 좋아요 기능을 비동기로 바꾸기! 기존 django 기반의 코드를 axios를 이용한 JS로 변환할 것
  - 페이지를 새로고침하지 않아도 서버에 요청 하고, 응답을 받아 화면의 일부만 업데이트하는 작업 수행
  
- 먼저 끝까지 순서대로 입력하되, 계속 중간중간 멈추면서 각 구문 or 변수가 뭔지 확인하기!
  - 끈질기게, 오래 한번 붙들어보라!

- 제일 큰 힌트 : 고치는 파일은 단 4개!
  - accounts/profile.html, accounts/views.py
  - articles/index.html, articles/views.py
  
- 1장씩, 다음 장을 예측해라!!!

- 그리고 긴 구문을 입력할 때, 한번씩 끊으면서 이게 무슨 값인지 출력 구문으로 체크해보라!

  ```
  1트
  
  <팔로우의 django 구문을 JS 구문으로 대체>
  83, 84p
  - base.html에 block 추가해서 구멍 뚫기
  - profile.html에 자스 구문 쓸 수 있게 block 넣어서 추가, axios 쓸 수 있게 준비
  
  85, 86p
  - 팔/언팔 부분의 form 태그 부분에서 주소 가리키고 요청 받는 부분은 싹 비우고
  대신 가리킴 당할 수 있게 id만 달아줌
  - script에서 쿼리 셀렉터로 id를 가리켜 줌
  - 쿼리 셀렉터가 나왔으면 뭐다? 이벤트 리스너다!
  
  87p
  - 리스너 안에 axios 요청을 준비해 준다. axios는 보낼 방식(method)와
  보낼 주소 (url)로 구성된다.
  
  막간
  - 자 그럼 POST 요청을 보내기 위해 필요한 것은?
  - 85p에서 지워버렸던 그 부분이 필요하다! user pk와 csrf token 처리를 어쩌지?
  
  90p, 92p
  - 85p에 추가로 data-뭐시기와 {{}}로 감싼 변수를 넣어주자!
  - 변수 설정은 어디에서? 아까 만든 이벤트 리스너 안에! (이 변수 이름은 암기만으론 힘듬)
  - 여기서 뭐시기는 HTML 안이니까 케밥 케이스지만, url 작성을 자스에서 옮겨와서 할 땐
  자스 문법대로 카멜 케이스로 변경됨. (HTML : data-user-id => JS : userId)
  * 못 믿겠으면 console.log(event.target.dataset)을 사이에 껴 넣어보자.
  
  96p
  - 이제 csrf token을 넣어주려면... 크롬의 개발자 도구에 들어가서
  hidden 타입으로 숨어 있는 input 태그를 뒤져보자. name="csrfmiddlewaretoken" 발견! 
  - 상수 하나를 선언해서 쿼리 셀렉터로 [name=csrfmiddlewaretoken]을 선택 후 .value로
  값을 발굴해 준다.
  
  97p
  - 이걸 axios 요청으로 같이 보내야 할 테니, axios의 인자로 같이 넣으면 되겠지?
  - headers를 이용, 장고 문서대로 따라한다.
  * 이렇게 하면 일단 팔로우 클릭하면 새로고침 하면 팔로우 내역 변경이 된다.
  
  <팔로우 기능을 비동기로 전환>
  99p
  - view.py에서 제이슨 응답 헤더를 추가하고, 팔로우 여부 확인용 변수를 추가해 준다.
  - 제이슨 응답에 이 변수를 제이슨 형식(py 딕셔너리 형식)으로 바꾸어 담아 리턴해 준다.
  
  100p
  - 버튼 토글 기능을 추가해 주기 위해 이제 드디어! profile.html의 axios에 .then 구문을 담아 준다.
  - then 구문은 받아온 응답을 이용해 연산을 하는데, 이 값은 바로 99p에서 보내준 제이슨 데이터!
  - 쿼리 셀렉터로 딱 정확하게 팔로우/해제 버튼을 가리켜 준 뒤...
  - 버튼.value 의 값을 지정해 주면 끝!
  
  103p, 104p
  - 버튼은 바뀌지만 팔로우 숫자가 안 바뀐다...
  - 팔로워 : 팔로잉 : 부분을 자스에서 선택할 수 있게 span 태그로 id를 부여
  - axios안에서 같이 처리하면 되므로 쿼리 셀렉터로 또 찝어준다.
  
  105p, 106p
  - 마찬가지로 인원수 연산은 일단 view.py에서 진행함, 보낼 JSON 데이터에 추가해준다.
  - 또 마찬가지로 profile.html로 와서 받은 걸 처리하는 JS 구문을 추가해준다.
  - 109p를 같이 봐야함! 우변에 뭘 넣는지 선언하는 구문이 빠짐.
  ```

- 즉, HTML로 처리하던 부분을 자스 부분을 추가해서 받아와서 queryselector와 eventlistener로 처리.
- 파이썬에서 원하는 자료를 보낼 때는 JSON 파일로 담아서 보낸 뒤 받을 때는 axios 안에서 response.으로 찾는다.