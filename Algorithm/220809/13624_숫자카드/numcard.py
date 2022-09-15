import sys
sys.stdin = open('1.txt')

t = int(input())

for cases in range(1, t + 1):
    n = int(input())
    cards = list(map(int, input()))             # 49679가 [4, 9, 6, 7, 9]로 분할되어 들어 온다.

    num_srt = [0] * 10
    for i in cards:
        num_srt[i] += 1                         # 카운팅 정렬로 저장해 둔다.

    max_num, max_cnt = -1, 0
    for i in range(10):
        if max_cnt <= num_srt[i]:               # 개수가 같다면 더 큰 숫자가 우선인 점에 주의!
            max_num = i
            max_cnt = num_srt[i]

    print(f'#{cases} {max_num} {max_cnt}')
