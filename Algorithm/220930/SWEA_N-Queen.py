# 풀이 핵심 : nxn인 판에 n개의 퀸을 올려놓는 것이므로, 각 가로줄과 세로줄에는 각각 1개씩의 퀸을 놓을 수밖에 없다.
# 1차원 리스트 순열을 생성하면 가로와 세로가 겹치지 않는 퀸의 배치를 만들 수 있다.
# place 리스트의 인덱스 번호를 가로 좌표, 그 위치의 값을 세로 좌표가 되게 배치한다.
# 예시 [2, 0, 3, 1] => 퀸을 각각 (0, 2), (1, 0), (2, 3), (3, 1)에 배치한 것으로 생각한다.
# 순열의 길이가 1개 늘어날 때마다 대각선으로 겹치지 않는 배치인지 고려해서, n 길이의 순열을 완성한 순간 정답 케이스 1개를 추가해주면 된다.

def crosscheck(depth):                                      # 대각선끼리 겹치는지 확인하는 함수

    for i in range(depth):                                  # i는 depth 바로 직전 원소까지 순회

        x1, y1 = i, lst[i]                                  # 리스트의 i, depth 인덱스와 기록된 값을 x, y 좌표에 대응시킨다.
        x2, y2 = depth, lst[depth]

        if x2 - x1 == y2 - y1 or x2 - x1 == y1 - y2:        # x좌표의 차이와 y 좌표의 차이가 일치하면 같은 대각선상에 있는 것이다.
            return False                                    # 대각선으로 겹치면 False를 리턴한다.

    return True                                             # 대각선으로 겹치지 않으면 True를 리턴한다.

def permutation(depth):                                     # 순열을 만드는 함수, place는 만든 순열을 들고 다님

    ans = 0                                                 # ans는 재귀함수를 호출하는 동안 쭉 해답 가짓수를 받아와 저장함

    if depth == n:                                          # 길이에 맞게 대각선으로도 안 겹치는 순열을 완성했다면
        ans += 1                                            # 정답 가짓수가 1 늘어남

    else:                                                   # 아래 구문은 for문을 n개 중첩한 것을 재귀함수로 만든 것과 같다.
        for i in range(n):                                  # n까지의 모든 숫자에 대해 루프
            if i not in lst[:depth]:                        # 지금까지 리스트에 넣어둔 숫자를 보고 겹치지 않는 숫자라면
                lst[depth] = i                              # 리스트 맨 뒤에 숫자를 넣어줌
                if crosscheck(depth):                       # 지금까지 만든 퀸의 배치가 대각선 방향으로 겹치는지 판별해본 후
                    ans += permutation(depth + 1)           # 재귀함수 호출, 정답 가짓수를 받아오는 구문까지 같이 적음

    return ans                                              # 정답 가짓수를 리턴해 줌

t = int(input())
for cs in range(t):

    n = int(input())                                        # 판의 크기 n은 전역변수로써 순열의 길이로도 사용
    lst = [-1] * n
    print(f'#{cs + 1} {permutation(0)}')