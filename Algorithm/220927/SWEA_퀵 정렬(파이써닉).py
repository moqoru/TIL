import sys
sys.stdin = open("input.txt")

# 파이써닉한 방법으로 퀵소트 구현.
def q_sort_pythonic(arr):
    # 먼저 맨 앞, 가운데, 맨 뒤 중에서 중앙값을 pivot으로 설정
    pv_start, pv_mid, pv_end = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = pv_start + pv_mid + pv_end - max(pv_start, pv_mid, pv_end) - min(pv_start, pv_mid, pv_end)
    # pivot보다 작은 값, pivot보다 큰 값만 모은 2개의 리스트를 만듦
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    # pivot과 같은 값이 여러개일 수도 있으므로 left와 right의 원소의 갯수를 이용해서 pivot과 동일한 값의 갯수를 구함
    pivot_num = len(arr) - len(left) - len(right)
    # left와 right가 길이가 2 이상이라면 재귀함수로 호출하도록 함
    if len(left) > 1:
        left = q_sort_pythonic(left)
    if len(right) > 1:
        right = q_sort_pythonic(right)
    # 재귀적으로 정렬된 left와 right 사이에 pivot 값을 갯수만큼 붙여서 리턴
    return left + [pivot] * pivot_num + right

t = int(input())
for cs in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    print(f'#{cs + 1} {q_sort_pythonic(lst)[n//2]}')