def crosscheck(place):                                      # 대각선끼리 겹치는지 확인하는 함수

    for i in range(len(place)):                             # i는 리스트의 전 원소를 순회
        for j in range(i + 1, len(place)):                  # j는 i번 다음 번째 원소부터 순회

            x1, y1 = i, place[i]                            # 리스트의 i, j 인덱스와 기록된 값을 x, y 좌표에 대응시킨다.
            x2, y2 = j, place[j]

            if x2 - x1 == y2 - y1 or x2 - x1 == y1 - y2:    # x좌표의 차이와 y 좌표의 차이가 일치하면 같은 대각선상에 있는 것이다.
                return False                                # 대각선으로 겹치면 False를 리턴한다.

    return True                                             # 대각선으로 겹치지 않으면 True를 리턴한다.

def permutation(place):                                     # 순열을 만드는 함수, n은 크기, place는 만든 순열

    ans = 0                                                 # ans는 재귀함수를 호출하는 동안 쭉 해답 가짓수를 받아와 저장함

    if len(place) == n:                                     # 길이에 맞게 대각선으로도 안 겹치는 순열을 완성했다면
        ans += 1                                            # 정답 가짓수가 1 늘어남

    else:                                                   # 아래 구문은 for문을 n개 중첩한 것을 재귀함수로 만든 것과 같다.
        for i in range(n):                                  # n까지의 모든 숫자에 대해 루프
            if i not in place:                              # 겹치지 않는 숫자라면
                place.append(i)                             # 리스트 맨 뒤에 숫자를 넣어준 뒤
                if crosscheck(place):                       # 지금까지 만든 퀸의 배치가 대각선 방향으로 겹치는지 판별해본 후
                    ans += permutation(place)               # 재귀함수 호출, 정답 가짓수를 받아오는 구문까지 같이 적음
                place.pop()                                 # 다시 빼서 다음 순열의 경우의 수를 고려함

    return ans                                              # 정답 가짓수를 리턴해 줌

t = int(input())
for cs in range(t):

    n = int(input())                                        # 판의 크기 n은 전역변수로써 순열의 길이로도 사용
    print(f'#{cs + 1} {permutation([])}')