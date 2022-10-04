import sys
input = sys.stdin.readline

def num_check(n):
    for k in range(5):
        if n in garo[k]:
            garo[k][garo[k].index(n)] = 0
        if n in sero[k]:
            sero[k][sero[k].index(n)] = 0
        if n in daegak1:
            daegak1[daegak1.index(n)] = 0
        if n in daegak2:
            daegak2[daegak2.index(n)] = 0

def cross_check():
    cnt = 0
    for k in range(5):
        if sum(garo[k]) == 0:
            cnt += 1
        if sum(sero[k]) == 0:
            cnt += 1
    if sum(daegak1) == 0:
        cnt += 1
    if sum(daegak2) == 0:
        cnt += 1
    return cnt

garo = [list(map(int, input().split())) for _ in range(5)]
sahueja = [list(map(int, input().split())) for _ in range(5)]
sero, daegak1, daegak2 = [], [], []

for j in range(5):
    tmp_lst = []
    for i in range(5):
        tmp_lst.append(garo[i][j])
    sero.append(tmp_lst)

for i in range(5):
    daegak1.append(garo[i][i])
    daegak2.append(garo[i][4 - i])

bingo_3rd = False
for i in range(5):
    for j in range(5):
        num_check(sahueja[i][j])
        if cross_check() >= 3:
            print(i * 5 + j + 1)
            bingo_3rd = True
            break
    if bingo_3rd:
        break
