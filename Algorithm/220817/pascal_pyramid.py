import sys
sys.stdin = open('input.txt')

def line(lst):

    if len(lst) == 0:                       # 길이가 0이라면 = 첫 줄이라면
        return [1]                          # 1만 리턴

    else:                                   # 2번째 줄 이상이라면
        lst_past = lst[:]                   # 이전 줄을 복사해서 저장, 스택의 pop 기능만 사용
        lst_now = []                        # 현재 줄을 만들어낼 준비, 스택의 push 기능만 사용
        l_top = 0                           # 파스칼 삼각형에서 '왼쪽 위' 숫자를 저장할 변수

        for num in range(len(lst)):         # 이전 줄을 다 뽑아낼 때까지 루프
            r_top = lst_past.pop()          # 이전 줄에서 하나 pop = 파스칼 삼각형에서 '오른쪽 위' 숫자
            lst_now.append(r_top + l_top)   # 두 개의 숫자를 더해서 push
            l_top = r_top                   # 오른쪽 위 숫자는 그 다음 칸에서 왼쪽 위 숫자가 됨
        lst_now.append(1)
        return lst_now

t = int(input())
for cs in range(t):

    n = int(input())
    line_past = []                          # 이전 줄의 숫자 모음을 저장할 리스트

    print(f'#{cs + 1}')
    for i in range(n):                      # 줄 길이만큼 루프
        line_now = line(line_past)          # 현재 줄의 숫자 모음을 함수로 받아와서 리스트로 저장
        print(*line_now)                    # 출력 후...
        line_past = line_now[:]             # 현재 줄을 다시 이전 줄의 리스트에 복사해서 다음 줄을 출력하도록 함