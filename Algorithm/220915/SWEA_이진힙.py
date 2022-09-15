import sys
sys.stdin = open("input.txt")

def hipify(num):                                                # heapify 하는 함수
    while (num):                                                # num이 0이 되면 탈출 (1번 노드보다 위로 올라가거나,)
        if hip[num // 2] > hip[num]:                            # 부모 노드보다 현재 노드 값이 작다면
            hip[num // 2], hip[num] = hip[num], hip[num // 2]   # 교환하고 부모 노드로 옮겨서 계속 진행
            num //= 2
        else:                                                   # 2번째 탈출 조건 : heapify가 끝난 경우
            num = 0

def ans_search(num):                                            # 부모따라 쭉 올라가면서 합산해서 결과값 출력
    ans_sum = 0
    num //= 2
    while (num):
        ans_sum += hip[num]
        num //= 2
    return ans_sum

t = int(input())
for cs in range(t):
    n = int(input())
    in_lst = list(map(int, input().split()))
    hip = [0] * (n + 1)

    for i, val in enumerate(in_lst):
        hip[i + 1] = val
        hipify(i + 1)

    print(f'#{cs + 1} {ans_search(n)}')
