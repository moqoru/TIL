# OpenVidu 리액트로 열기 연습

https://docs.openvidu.io/en/stable/tutorials/openvidu-library-react/

- 도커를 다운받아 둔 뒤, 다음 구문을 실행한다

  ```
  docker run -p 4443:4443 --rm -e OPENVIDU_SECRET=MY_SECRET openvidu/openvidu-dev:2.25.0
  ```

- ~~도커가 **더럽게** 실행이 안 되므로 로그인을 해 주고, 컴을 계속 껐다 켰다 해 준다~~

- python3이 설치되어 있는지 확인 하고, python 구문들을 실행시켜 준다

  - 이때 가상 환경 실행 구문은 source venv/Scripts/activate로, python 실행 구문은 python app.py로 실행시킨다

- 나중에 끌 때는 도커 데스크탑을 직접 켜서 중지 버튼을 눌러주면 서버가 멈춰진다

## 리액트 구조

- 기본적으로 import OpenViduSession from 'openvidu-react' 라이브러리를 불러온다
- \<OpenViduSession /> 구문으로 활성화한다
  - 이때 세션과 토큰 정보가 필요하다
  - 이것저것 필요한건 그냥 통째로 긁어오자

## 추가 데모

https://docs.openvidu.io/en/stable/demos/openvidu-call-react/

- 리액트로 짜여 있으며, 채팅, 음성, 영상 ON/OFF 설정이 가능하게 되어 있다
- 아직 테스트해보진 않음