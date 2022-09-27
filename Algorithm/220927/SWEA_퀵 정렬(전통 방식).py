import sys
sys.stdin = open('input.txt')

# 호어 파티션 알고리즘. 사실 그냥 구현하라하면 잘 못할 거 같은 느낌...
def hoare_partition(arr, l, r):
    pivot = arr[l]
    i = l
    j = r
    # while문 중첩이 까다로워 보임;
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j

def q_sort(arr, l, r):
    if l < r:
        pivot = hoare_partition(arr, l, r)
        q_sort(arr, l, pivot - 1)
        q_sort(arr, pivot + 1, r)

t = int(input())
for cs in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    q_sort(lst, 0, n-1)
    print(f'#{cs + 1} {lst[n//2]}')