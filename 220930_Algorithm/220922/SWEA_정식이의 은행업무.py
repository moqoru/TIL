import sys
sys.stdin = open('input.txt')

# 풀이법 : int() 구문을 쓸 때, int(str, 2)로 써주면 2진법으로 쓰여진 문자열 str을 10진법으로 바꿔 줍니다.
# 이걸 이용해서 먼저 입력값을 전부 문자열로 받은 뒤, 한 글자씩 보면서 2진법상에서 1글자씩만 바뀐 숫자를
# 10진법으로 변환해서 set을 만들어서 전부 넣어줍니다.
# set에 2진법 숫자에서 헷갈렸을 모든 경우의 수가 저장되어 있으므로, 3진법 숫자를 전부 1글자씩만 바꿔 주면서
# in set 연산으로 있는지 확인해주면 끝입니다.

# 문자열에서 딱 1글자만 특정 숫자로 바꾼 것을, 원하는 진법으로 보고 10진법 숫자로 리턴하는 함수
def one_replaced(arr, where, lett, digit):
    return int(arr[0:where] + lett + arr[where + 1: len(arr)], digit)

t = int(input())
for cs in range(t):
    two = input()
    three = input()
    two_set = set()
    # 2진법 숫자에서 헷갈릴 수 있는 모든 경우의 수를 set에 삽입
    for i in range(len(two)):
        if two[i] == "0":
            two_set.add(one_replaced(two, i, "1", 2))
        else:
            two_set.add(one_replaced(two, i, "0", 2))

    # 3진법 숫자에서 헷갈릴 수 있는 모든 경우의 수에 대해 set에 있는지 체크
    flag = False
    ans = None
    # 앞에서부터 한 자리씩 봄
    for i in range(len(three)):
        # 그 자릿수를 3번 바꿔 봄
        for j in ["0", "1", "2"]:
            ans = one_replaced(three, i, j, 3)
            # 보고 있는 자릿수가 바뀐 게 맞고, 바꿔본 숫자가 set에 있으면
            if three[i] != j and ans in two_set:
                flag = True
                break
        if flag:
            break
    print(f'#{cs + 1} {ans}')