import sys
input = sys.stdin.readline

x, y = map(int, input().split())
k = int(input())

if k > x * y:
    print(0)

else:

    dx, dy = x, y + 1
    di, cnt, loop = 0, 0, 1

    while dx > 0 and dy > 0:

        if di == 0:                             # 위로 가는 경우
            dy -= 1
            cnt += dy
            if cnt >= k:
                print(loop, dy - (cnt - k) + loop - 1)
                break

        elif di == 1:                           # 오른쪽으로 가는 경우
            dx -= 1
            cnt += dx
            if cnt >= k:
                print(dx - (cnt - k) + loop, y - loop + 1)
                break

        elif di == 2:                           # 아래로 가는 경우
            dy -= 1
            cnt += dy
            if cnt >= k:
                print(x - loop + 1, cnt - k + loop)
                break

        else:                                   # 왼쪽으로 가는 경우
            dx -= 1
            cnt += dx
            if cnt >= k:
                print(cnt - k + loop + 1, loop)
                break

        di += 1
        if di >= 4:
            loop += 1
            di = 0