- 순열과 조합이 헷갈린다?

```python
import sys
input = sys.stdin.readline

ansSum = -1

# N개의 카드 중에서 3장을 뽑는 코드
def nCr(idx, cnt, nowSum): # 직전 단계에 선택한 카드 번호, 고른 카드 장 수, 현재 총합
    if cnt >= 3: # 3장을 뽑았다면
        global ansSum
        if M - nowSum < M - ansSum: # 카드의 총합을 갱신할 수 있다면 갱신
            ansSum = nowSum
    else: # 아직 덜 뽑았다면
        for i in range(idx + 1, N - 2 + cnt):
            if nowSum + Deck[i] <= M: # 이번 카드를 뽑았을 때 현재 총합이 한계치보다는 아래라면
                nCr(i, cnt + 1, nowSum + Deck[i]) # 현재 총합을 갱신하여 재귀 함수 호출

N, M = map(int, input().split())
Deck = list(map(int, input().split()))
nCr(-1, 0, 0)
print(ansSum)
```

- 이 코드에서 다음 부분을 주목해보자.

```python
    else: # 아직 덜 뽑았다면
        for i in range(idx + 1, N - 2 + cnt):
```

- i 루프의 시작점이 idx + 1, 즉 현재까지 뽑은 숫자보다 뒤에서부터 시작된다. 이 경우, **뒤에 뽑힌 숫자가 앞에 뽑힌 숫자보다 더 크다는 게 무조건 보장된다.** 따라서 이건 **조합**이다!
  - 그럼 순열로 만들려면? i루프의 **시작점은 항상 0번으로 고정**되고, **현재 뽑히지 않은 숫자만 다음 순열로 들어갈 수 있게** 만들어야 할 것이다!