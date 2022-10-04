N = int(input())
# 별 담을 시작 판
board = [['*']]

#처음 시작 그냥 3으로 잡음
number = 3

def star(number):
    # 숫자가 들어 왔을 때 삼등분 해서 앞에 앞에 (O/X/X) 맨 앞 덩어리 두번 붙이기
    for j in range(2):
        for i in range(number//3):
            board.append(board[i])
    print(board)
    # number 범위만큼 삼등분해서
    for i in range(number):
        # i가 맨처음 등분에 포함되면 세번 곱하기
        if i // (number//3) == 0:
            board[i] = board[i]*3
            print(i, board[i])
        # 세번째도 세번 곱하기
        elif i // (number//3) == 2:
            board[i] = board[i]*3
            print(i, board[i])
        # 두번쨰 등분이면 더하고 / 3등분 길이만큼 빈공간 더하고 /또 더하기
        else:
            board[i] = board[i] + list(' '*(number//3)) + board[i]
            print(i, board[i])
    # 이렇게 해서 원하는 숫자까지 그리면 리턴
    if number == N:
        return board
    # 아니면 숫자에 3곱해서 새로운 board 기준으로 더 새로운 보드 기리기
    else:
        return star(number*3)

# 함수 돌리고
star(number)

# 다 붙여서 프린트하기
for i in range(N):
    print(''.join(board[i]))