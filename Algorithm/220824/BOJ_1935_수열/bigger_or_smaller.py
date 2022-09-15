import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
greater, lesser = [], []                    # 커지는 수열, 작아지는 수열 저장
ans = 0                                     # 가장 긴 수열 길이

for val in lst:                             # 입력받은 수열 순회

    if greater and greater[-1] > val:       # 커지는 수열에 숫자가 들어 있고 그 수열이 끊기게 되면

        if ans < len(greater):              # 길이를 체크해서 수열 길이 최대치 갱신
            ans = len(greater)

        greater.clear()                     # 수열이 끊겼으므로 비워서 새로운 수열 만들 준비

    greater.append(val)                     # 커지는 수열에 이번 숫자를 새로 삽입

    if lesser and lesser[-1] < val:         # 작아지는 수열에 숫자가 들어 있고 그 수열이 끊기게 되면

        if ans < len(lesser):               # 길이를 체크해서 수열 길이 최대치 갱신
            ans = len(lesser)

        lesser.clear()                      # 수열이 끊겼으므로 비워서 새로운 수열 만들 준비

    lesser.append(val)                      # 작아지는 수열에 이번 숫자를 새로 삽입

if ans < len(greater):                      # 맨 마지막 숫자까지 돌았을 때 수열이 안 끊기고 남아있을 수 있으므로
    ans = len(greater)                      # 루프가 끝나고 나서 마지막으로 최대값 한번 더 갱신
if ans < len(lesser):
    ans = len(lesser)

print(ans)