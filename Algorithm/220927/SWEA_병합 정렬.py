import sys
sys.stdin = open('input.txt')

# 왼쪽 마지막 원소가 오른쪽 마지막 원소가 큰 경우의 수를 찾으려면...
# 먼저 왼쪽 원소가 오른쪽 원소보다 '작거나 같은' 경우에는 왼쪽 원소가 복사되도록 한다.
# 즉, 오른쪽 원소가 더 작을 경우에만 오른쪽 원소가 들어가게 될 것이다.
# !!!! 자, 그러면 '왼쪽에만 원소가 남는 경우' 는 어떤 경우가 될까?
# 왼쪽 마지막 원소가 오른쪽 원소들보다 더 큰 경우와 동일해진다! 여기에서 카운트를 올려주면 된다!!!!

def merge_sort(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])
    l_cur, r_cur = 0, 0 # pop을 안 쓰는 대신 left와 right의 어느 위치를 가리키는지를 정해 주었다.
    res = []

    # 아래 루프문은 예시 코드에서 pop을 쓰지 않고 if문의 순서가 바뀌었을 뿐 기본적으로는 동일하다.
    while l_cur + r_cur < len(left) + len(right):
        if r_cur >= len(right):
            res.extend(left[l_cur:])
            cnt += 1 # 오른쪽이 비어버려서 왼쪽만 남은 경우에만 카운트를 올려주면 된다.
            break
        elif l_cur >= len(left):
            res.extend(right[r_cur:])
            break
        elif left[l_cur] <= right[r_cur]:
            res.append(left[l_cur])
            l_cur += 1
        else:
            res.append(right[r_cur])
            r_cur += 1
    return res

    # 1, 2일 때 => left가 먼저 복사됨, right만 남아 있음, cnt 안 올라감
    # 1, 1일 때 => left가 먼저 복사됨, right만 남아 있음, cnt 안 올라감
    # 2, 1일 때 => right가 먼저 복사됨, left만 남아 있음, cnt 올라감

t = int(input())
for cs in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    print(f'#{cs + 1} {merge_sort(lst)[n//2]} {cnt}')