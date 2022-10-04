import sys
input = sys.stdin.readline

s = input().rstrip()                                        # rstrip을 하지 않으면 맨 끝에 \n이 추가로 붙어버립니다.
stk_gob, stk_numlen = [], [0]                               # stk_gob은 '(' 바로 앞의 문자열 곱하는 횟수를 저장하는 스택입니다.
                                                            # stk_numlen은 ()가 한 단계씩 깊어질 때마다 그 단계의 문자의 길이를 저장하는 스택입니다.
                                                            # 단, 첫번째 원소는 괄호 밖의 문자 길이가 되므로 초기값을 따로 줬습니다.

for idx, val in enumerate(s):                               # s 문자열을 한 글자씩 탐색합니다.

    if val == '(':                                          # 여는 괄호를 만났다면
        stk_numlen[-1] -= 1                                 # 괄호 바로 앞이 문자열 곱하는 횟수이므로 괄호 바깥쪽 단계의 숫자의 길이를 1 줄입니다.
                                                            # (압축을 풀었을 때 사라져버리는 숫자이기 때문입니다.)
        stk_gob.append(int(s[idx - 1]))                     # 괄호 바로 앞의 곱하는 횟수를 스택에 push 합니다.
        stk_numlen.append(0)                                # 괄호 안쪽 단계의 글자 길이를 계산하기 위해 스택에 push 합니다.

    elif val == ')':                                        # 닫는 괄호를 만났다면
        unpack_numlen = stk_gob.pop() * stk_numlen.pop()    # 이번 단계의 문자열 곱하는 횟수와, 괄호 사이에 있는 글자 길이를 스택에서 pop 해서 곱합니다.
        stk_numlen[-1] += unpack_numlen                     # 이제 바로 윗 단계의 문자 길이에, 압축을 푼 글자 길이를 더해줍니다.

    else:                                                   # 그냥 숫자라면
        stk_numlen[-1] += 1                                 # 현재 단계의 숫자의 길이를 1 늘립니다.

print(stk_numlen[0])                                        # 무사히 성공했다면 stk_numlen에는 가장 바깥쪽 단계의 문자 길이만 남아 있을 것이므로, 출력하면 됩니다.
