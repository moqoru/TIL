import sys
sys.stdin = open('sample_in.txt')

def bus_check(start, end, stp):

    global station                                                  # 본문의 for문 안에서 선언한 리스트이지만 글로벌로 불러올 수 있음!

    station[start] += 1                                             # 먼저 시작점과 끝점은 무조건 서야 하므로 서는 버스 종류를 1씩 더해 줌
    if start != end:                                                # 정말 만의 하나라도 시작점과 끝점이 동일한 경우가 있을 수 있으므로...
        station[end] += 1
                                                                    # 사이의 정류장들을 찾아가는 경우의 수들을 1개로 합쳐본 결과
    first_stp = stp if stp == 1 or stp == 2 else stp - start % stp  # 광역 급행만 그 다음 정류장을 3 or 4의 배수로 맞추고, 나머지는 시작점 1 or 2칸 뒤부터 시작

    for j in range(start + first_stp, end, stp):                    # start + first_stp이 항상 사이의 정류장들 중 조건에 맞는 첫번째 정류장이 되게 맞춤
        if j % 10 or stp != 3:                                      # 광역 급행이 시작점이 홀수일 때만 10의 배수 조건이 추가로 붙음
            station[j] += 1                                         # 루프를 돌면서 조건에 맞는 정류장에 서는 버스 대수를 1씩 더함

t = int(input())
for cs in range(t):

    n = int(input())
    station = [0] * 1001

    for i in range(n):
        ty, a, b = map(int, input().split())

        if ty != 3 or a % 2:                                        # 일반 or 광역 or 광역급행인데 시작점이 홀수
            bus_check(a, b, ty)                                     # 일반, 광역버스는 시작점부터 1 or 2칸씩(= ty) 떨어진 정류장마다 섬
                                                                    # 광역급행, 시작점이 홀수라면 3칸(= 또 ty) 떨어진 정류장마다
        else:                                                       # 광역급행인데 시작점이 짝수인 경우
            bus_check(a, b, ty + 1)                                 # 4(= ty + 1)의 배수 정류장마다 섬

    print(f'#{cs + 1} {max(station)}')
