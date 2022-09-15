import sys
sys.stdin = open('sample_input(2).txt')

t = int(input())
for cases in range(1, t + 1):                           # 이 문제는 그리디로 해결 가능.
                                                        # 갈 수 있는 정류장 중 가장 먼 곳만 골라 가면 성공
    k, n, m = map(int, input().split())
    charge = list(map(int, input().split()))
    charge.append(n)                                    # 도착 조건을 간편하게 하려고 도착점에 추가 충전소 설치
    location, charge_num, charge_idx = 0, 0, -1         # loc는 위치, c_num은 충전 횟수
                                                        # c_idx는 charge 리스트의 다음 충전소 인덱스 번호
    while location <= n - 1:                            # 버스가 도착하지 않은 동안 루프
        charge_next = -1                                # 다음으로 들를 충전소의 실제 위치
        for i in range(charge_idx + 1, len(charge)):    # c_idx 번호를 보고 지금보다 뒤에 있는 정류장만 탐색
            if charge[i] <= location + k:               # 현재 위치에서 갈 수 있는 정류장이라면
                charge_idx = i                          # 충전소 인덱스 번호 갱신
                charge_next = charge[i]                 # 충전소의 실제 위치 갱신
            else:                                       # 갈 수 없는 곳이면 탐색 중단
                break
                                                        # 루프를 돌면 가장 멀리 있는 충전소가 변수에 기록됨

        if charge_next < 0:                             # 충전소 위치가 갱신 안됐다면
            charge_num = 1                              # 갈 수 있는 곳이 없으므로 중단
            break
        else:
            location = charge_next                      # 충전소 위치를 찾았다면 현재 위치를 충전소 위치로 갱신
            charge_num += 1                             # 충전 횟수 증가

    print(f'#{cases} {charge_num - 1}')                 # 도착점에 충전소가 있다고 가정했으므로 -1을 빼야 맞음