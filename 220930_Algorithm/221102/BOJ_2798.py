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