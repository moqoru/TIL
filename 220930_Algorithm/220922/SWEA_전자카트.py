import sys
sys.stdin = open('input.txt')

# 이전에 방문했던 노드의 정보를 계속 함수의 인자로 넘겨주게 함, 이것으로 다음에 방문할 노드 사이의 거리를 입력받은 리스트에서 검색
# now_chk를 스택으로 사용하여 이전까지 방문한 노드의 정보를 계속 담고 있도록 하고, 아직 방문하지 않은 노드만 방문하도록 함

def npr(depth, now_sum, b_node): # 인자는 각각 깊이, 현재 거리 총합, 이전에 방문한 노드
    global min_sum, n
    if depth >= n - 1: # 이제 마지막으로 1번 노드로 돌아오기만 하면 된다면
        min_sum = min(min_sum, now_sum + lst[b_node][0]) # 1번 노드로 되돌아왔을 때의 거리가 최소 거리보다 작다면 갱신
    elif now_sum < min_sum: # 가지치기 테스트? 총합이 이미 넘어가 버린다면 방문 필요 X
        for i in range(1, n): # 1번 노드는 어차피 시작점이므로 방문 필요 없음(리스트의 인덱스는 0부터 시작)
            if i not in now_chk:
                now_chk.add(i)
                npr(depth + 1, now_sum + lst[b_node][i], i) # 각 인자의 정보를 갱신해서 재귀 호출
                now_chk.remove(i)


t = int(input())
for cs in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    now_chk = set()
    min_sum = n * 100 + 1
    npr(0, 0, 0)
    print(f'#{cs + 1} {min_sum}')