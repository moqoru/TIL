# print(int("0x1D", 2))

import sys
sys.stdin = open("input.txt")

# 정말 다행히도, 정상적인 16진수 숫자 안에 2진수 숫자가 일부만 끼어들어가는 경우는 없음.
# 하지만 비정상 코드의 조건이 무엇인지 헷갈린다... 56글자가 아니라 57글자인 경우도 나온다는 건가?

num_dict = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}

def decode(cod):

    cod_multi = len(cod) // 56
    bitchk_lst, numchk_lst = [], []

    for i_d in range(cod % 8, len(cod), 7 * cod_multi):
        zero_flag = True  # 0부터 시작하므로...
        num_cnt = 0

        for j_d in range(i_d, i_d + 7 * cod_multi):
            if cod[j_d] == "0":
                if zero_flag:
                    num_cnt += 1
                else:
                    bitchk_lst.append(num_cnt // cod_multi)
                    zero_flag = True
                    num_cnt = 1
            else:
                if not zero_flag:
                    num_cnt += 1
                else:
                    bitchk_lst.append(num_cnt // cod_multi)
                    zero_flag = False
                    num_cnt = 1

        bitchk_lst.append(num_cnt // cod_multi)
        numchk_lst.append(num_dict[set(bitchk_lst)])

    odd_chksum, even_chksum = 0, 0
    for i_d in range(0, 7, 2):
        odd_chksum += 3 * numchk_lst[i_d]
    for i_d in range(1, 7, 2):
        even_chksum += numchk_lst[i_d]

    return sum(numchk_lst) if not odd_chksum + even_chksum % 10 else 0


t = int(input())
for cs in range(t):
    n, m = map(int, input().split())
    lst = [input().strip() for _ in range(n)]
    code_dict = dict() # 코드 원본 : 실제 값 순서대로 저장
    end, start = -1, -1
    now_bin = ""
    for i in range(n):
        j = m
        while j > 0:
            j -= 1
            if lst[i][j] != "0":
                change_flag, zero_cnt, one_cnt = 0, 0, 0
                while True: # 1이었다가 다시 0이었다가 다시 1인 지점을 찾아서 0과 1의 수를 세어야 함... 그것도 16진수를 2진수로 변환해 넣으면서!
                    # 젠장. 결국 0이 아닌 수는 전부 볼 수밖에 없잖아...
                    onebit_bin = bin(int("0x" + lst[i][j], 16))[2:]
                    if change_flag == 0 and "0" in onebit_bin:
                        change_flag = 1
                        one_cnt = 3 - onebit_bin.index("1") + len(now_bin)
                    now_bin = onebit_bin + now_bin


        # for j in range(m, -1, -1):
        #     if not flag and lst[i][j] != '0':
        #         flag = True
        #         end = j + 1 # 슬라이싱 연산을 편하게 하기 위해서...
        #     elif flag and lst[i][j] == '0':
        #         flag = False
        #         start = j + 1 # 0이 나오면 그 뒷 글자까지가 코드 부분이기 때문.
        #         code_orig = bin(int("0x" + lst[i][start: end], 16))[2:]
        #         if code_orig not in code_dict:
        #             code_num = decode(code_orig)
        #             code_dict[code_orig] = code_num
        #
        # if flag:
        #     if start == -1: # 하필이면 맨 처음 숫자까지도 코드의 일부일 경우
        #         code_orig = bin(int("0x" + lst[i][0: end], 16))[2:]
        #         if code_orig not in code_dict:
        #             code_num = decode(code_orig)
        #             code_dict[code_orig] = code_num

    ans = 0
    for val in code_dict.values():
        ans += val
    print(f'#{cs + 1} {val}')



