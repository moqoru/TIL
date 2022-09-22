import sys
sys.stdin = open('input.txt')

# 그리디로 풀 수 있지만, 큰 짐부터 실어야 쉽게 풀리는 문제(작은 짐부터 실으면 조건이 너무 복잡함)
# 컨테이너, 트럭 둘 다 큰 것부터 내림차순 정렬시킴
# 다음과 같은 순서로 while문을 돌며, 트럭이나 컨테이너 둘 중 하나라도 끝까지 오면 종료
# 현재의 짐 무게가 트럭 제한과 같거나 더 가볍다면 : 트럭에 짐을 바로 싣고 총 무게 증가, 컨테이너와 트럭 모두 다음 번호로 넘김
# 더 무겁다면 : 트럭은 그대로 두고, 컨테이너만 다음 번호로 넘김

t = int(input())
for cs in range(t):
    n, m = map(int, input().split()) # n이 짐, m이 트럭 갯수
    load = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    load.sort(reverse=True)
    trucks.sort(reverse=True)
    l_cur, t_cur, max_sum = 0, 0, 0
    while l_cur < n and t_cur < m:
        if load[l_cur] <= trucks[t_cur]:
            max_sum += load[l_cur]
            t_cur += 1
        l_cur += 1
    print(f'#{cs + 1} {max_sum}')