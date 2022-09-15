def star(n):
    field = []
    if n <= 3:                                                                          # 상하좌우 크기가 젤 작으면
        for i in range(0, 3):                                                           # 3x3 크기의 표를 2중 리스트로 만들어 줌
            field_oneline = []                                                          # 한 줄짜리 리스트
            for j in range(0, 3):
                if i == j == 1:                                                         # 가운데만 공백
                    field_oneline += [' ']
                else:                                                                   # 나머지는 별로 채움
                    field_oneline += ['*']
            field.append(field_oneline)                                                 # 2중 리스트이므로 한 줄씩 따로 붙여줘야 함
        return field                                                                    # [* * *][* ' ' *][* * *]
        # return [['*','*','*'],['*',' ','*'],['*','*','*']]                            # 완전 축약하면 이런 느낌
    else:
        smol_field = star(n // 3)                                                       # 가로세로 크기가 1/3인 표 정보를 받아옴
                                                                                        # 다음과 같이 진행
                                                                                        # [1 2 3] => 1/3 크기의 표를 한 줄씩 잘라서, 3번 반복한 것을 한 줄로 만들어 붙임
                                                                                        # [4 5 6] => 4, 6 부분은 1/3 크기의 표를 붙임, 5 부분은 그 크기만큼 공백으로 만듬
                                                                                        # [7 8 9] => 123 부분과 동일
        for i in range(0, n // 3):                                                      # [1 2 3] 부분
            field.append(smol_field[i][:] * 3)                                          # 참조가 되지 않도록 [:]로 얕은 복사
        for i in range(0, n // 3):                                                      # [4 5 6] 부분
            field.append(smol_field[i][:] + [' '] * (n // 3) +smol_field[i][:])
        for i in range(0, n // 3):                                                      # [7 8 9] 부분
            field.append(smol_field[i][:] * 3)
        return field

n = int(input())
field = star(n)
for i in range(n):
    for j in range(n):
        print(field[i][j], end='')                                                      # 2중 포문으로 예쁘게 프린트
    print()