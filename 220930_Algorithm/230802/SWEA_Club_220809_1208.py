import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

# 핵심 : 일단 정렬을 시킨 후, 정렬된 상태를 계속 유지하면서 평탄화 작업 진행
# 양 끝 지점의 차이가 1 이하라면 평탄화 작업이 끝난 것, 아니라면 두 지점의 차이가 곧 높이 차이

for cs in range(1, 11):
    d = int(input())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True) # 역순 정렬

    for i in range(d):
        # 만약 나라시 작업이 전부 끝났다면 바로 종료
        if lst[0] - lst[99] < 2:
            break
        # 가장 큰 숫자 중 제일 마지막, 작은 숫자 중 제일 첫번째 위치 탐색
        maxLast, minFirst = 0, 99
        for j in range(99):
            if lst[j] > lst[j + 1]:
                maxLast = j
                break
        for j in range(99, 0, -1):
            if lst[j - 1] > lst[j]:
                minFirst = j
                break
        lst[maxLast] -= 1
        lst[minFirst] += 1

    print(f'#{cs} {lst[0] - lst[99]}')