import sys
input = sys.stdin.readline

# 스킬 차이 계산 함수
def skill_cal():
    global skill_min                                        # 스킬 차이 최소값을 저장하기 위해 전역변수를 가져옴
    s_sum, l_sum = 0, 0                                     # 스타트 팀의 스킬 합, 링크 팀의 스킬 합

    for i in range(n // 2):                                 # 각 팀의 구성원 별로 팀원끼리의 조합마다 순회
        for j in range(i, n // 2):
            s_sum += lst[team_s[i]][team_s[j]]              # 스타트 팀에서 i번째의 팀원에 대한 j번째의 팀원의 능력치 합산
            s_sum += lst[team_s[j]][team_s[i]]              # 스타트 팀에서 j번째의 팀원에 대한 i번째의 팀원의 능력치 합산
            l_sum += lst[team_l[i]][team_l[j]]              # 링크 팀도 동일하게 능력치 합산
            l_sum += lst[team_l[j]][team_l[i]]

    sum_chai = abs(s_sum - l_sum)                           # 스타트 팀과 링크 팀의 스킬 합의 차이를 구함
    if sum_chai < skill_min:                                # 이 값이 새로운 최소값이라면 갱신
        skill_min = sum_chai

# 팀배정 함수
def team_make(t):                                           # t는 현재 배정할 팀의 번호

    if t >= n:                                              # 모든 팀원 배정이 끝나면 능력치 계산 함수 호출
        skill_cal()

    else:                                                   # 아직 팀원 배정이 덜 끝난 경우
        if len(team_s) < n // 2:                            # 스타트 팀의 인원수가 아직 부족하다면
            team_s.append(t)                                # 일단 t번째 팀을 스타트 팀에 배정
            team_make(t + 1)                                # 그 다음 팀을 배정하기 위해 재귀함수 호출
            team_s.pop()                                    # 다음 경우의 수를 생각하기 위해 스타트 팀에서 뺌

        if len(team_l) < n // 2:                            # 링크 팀도 마찬가지로 계산
            team_l.append(t)
            team_make(t + 1)
            team_l.pop()

# 메인 부분
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
team_s, team_l = [], []                                     # 각 팀의 멤버를 저장할 리스트
skill_min = 999999                                          # 최대 20팀으로 400가지 조합, 능력치는 최대 100이므로 40000 이상이 초기값...?
team_make(0)                                                # 0번째 팀부터 배정 시작
print(skill_min)                                            # 능력치 조합의 차이가 가장 적은 경우를 출력