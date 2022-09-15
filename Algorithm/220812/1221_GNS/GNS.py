import sys, functools
sys.stdin = open('GNS_test_input.txt')

m_order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', \
           'FIV', 'SIX', 'SVN', 'EGT', 'NIN']               # 화성(?)의 숫자 순서 저장

def m_check(m1, m2):                                       # 화성의 숫자 순서대로 앞쪽 값이 더 작은 숫자인지 검사
    return m_order.index(m1) - m_order.index(m2)

t = int(input())

for cs in range(t):
    sharp, n = map(str, input().split())
    lst = list(map(str, input().split()))                   # 일단 입력을 통째로 리스트에 저장
    n = int(n)                                              # 전체 케이스 개수는 정수형 변환 필요

    lst_srt = sorted(lst, key=cmp_to_key(m_check))

    print(sharp)                                            # 결과 출력
    print(*lst)