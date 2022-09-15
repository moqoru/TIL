import sys
sys.stdin = open('s_input.txt')

t = int(input())
for cs in range(t):

    bus_stop = [0] * 5001                   # 5000개의 버스 정류장을 리스트에 통째로 저장
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())    # 버스 정보를 입력받을 때마다
        for j in range(a, b + 1):           # 루프를 돌려 지나는 정류장마다 전부 노선 개수를 1씩 추가
            bus_stop[j] += 1

    p = int(input())
    print(f'#{cs + 1}', end = ' ')
    for i in range(p):
        c = int(input())                    # 출력을 원하는 정류장 번호를 입력 받으면
        print(bus_stop[c], end = ' ')       # 그 정류장의 노선 개수를 바로바로 출력
    print()