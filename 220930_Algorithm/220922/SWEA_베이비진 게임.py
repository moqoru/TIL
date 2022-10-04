import sys
sys.stdin = open('input.txt')

def win_check(deck):
    # run 체크, 같은 카드 3장만 있으면 된다.
    if 3 in deck:
        return True
    # triplet 체크, 연속된 카드 3종이 모두 1장 이상이면 된다.
    else:
        for i_w in range(8):
            if deck[i_w] and deck[i_w + 1] and deck[i_w + 2]:
                return True
        return False

t = int(input())
for cs in range(t):
    lst = list(map(int, input().split()))
    # p1과 p2의 각 숫자별 카드 장수 저장
    p1, p2 = [0] * 10, [0] * 10
    winner = 0
    for i in range(0, 12, 2):
        # p1 차례, 카드를 기록하고 이겼는지 체크
        p1[lst[i]] += 1
        if win_check(p1):
            winner = 1
            break
        # p2 차례, 카드를 기록하고 이겼는지 체크
        p2[lst[i + 1]] += 1
        if win_check(p2):
            winner = 2
            break

    print(f'#{cs + 1} {winner}')
