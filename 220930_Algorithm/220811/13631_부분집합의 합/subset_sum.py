import sys
sys.stdin = open('sample_input(1).txt')

subsets = []                                        # 부분집합만 따로 담을 리스트, 이하 교재의 부분집합 코드 참조

for i in range(1 << 12):                            # 0부터 2^12 - 1까지 비트 검사 숫자를 만들어 순회
    subsets.append([])                              # 부분집합 하나마다 리스트를 따로 배정함
    for j in range(12):                             # 0부터 11까지 숫자 탐색
        if i & (1 << j):                            # i의 j번째 비트의 숫자가 1이라면 j 위치 원소를 추가해야 함
            subsets[-1].append(j + 1)               # 실제로는 1부터 12까지의 숫자이므로 1을 더하여 원소 추가

t = int(input())                                    # 케이스 수를 입력받고 그 횟수만큼 순회
for cs in range(1, t + 1):

    n, k = map(int, input().split())                # 원소의 최대 갯수와 목표 원소합 입력
    cnt = 0                                         # 조건 만족하는 조합의 갯수

    for check in subsets:                           # check에는 각 부분집합 리스트가 들어있게 됨
        if len(check) == n and sum(check) == k:     # 갯수도 맞고 총합도 맞다면
            cnt += 1                                # 조합 갯수 추가

    print(f'#{cs} {cnt}')