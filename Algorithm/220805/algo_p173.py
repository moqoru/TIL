def brute_force(nums, target):                                          # O(n^2) => Big O의 핵심 : 루프를 최대한 덜 중첩시켜라!
    
    for i in range(len(nums)):
        
        for j in range(i+1, len(nums)):
            
            if nums[i] + nums[j] == target:                             # 해시 : 암호를 풀어 정답 가진 사람을 찾아간다. 하지만 동명이인은 무조건 정해진 한 명만 찾아간다.
                return [i, j]
    return None

def in_search(nums, target):                                            # O(n^2)... 지만 더 빠르다.
    
    for i in range(len(nums)):

        if (target - nums[i]) in nums:                                  # for문 하나를 in으로 대체해버리면?
                                                                        # ...근데 in만 쓰면 있다는 것만 확인 가능하지, 어디 있는지는 모르잖아요?
            return [i, nums.index(target-nums[i])]                      # index를 쓰시면 됩니다.
                                                                        # 교재에서는 nums 대신 nums[i+1:]을 썼는데, i 뒷부분만 검사해서 시간을 절반으로 줄이는 방법입니다.
    return None

def in_dict_search(nums, target):                                       # O(n)?! 이건 컨닝했습니다.
    nums_dict = {}                                                      # 사실 in 연산은 튜플과 딕셔너리에서는 정말 무지하게 빠릅니다! 단 O(1)밖에 안 돼요!
                                                                        # 파이썬 in 연산자 시간복잡도를 검색해보시길...
    for i, num in enumerate(nums):                                      # 딕셔너리 탐색은 기본적으로 key로 찾기 때문에 그 쪽에 맞춰서 값을 넣어줍니다.
        nums_dict[num] = i                                              # key는 값, value는 위치로 넣어 줍니다.
    
    for i, num in enumerate(nums):                                      # 이 코드에서는 실수로 같은 위치를 2번 가리키는 경우를 배제했습니다.
        if (target - num) in nums_dict and i != nums_dict[target - num]:# [0,1,3,3]인데 합이 6인걸 찾는 경우... 딕셔너리는 같은 값을 2번 가리킬 수도 있거든요.
            return [i, nums_dict[target - num]]                         # 딕셔너리는 중복된 넘버(= 키)는 1개만 저장되므로, 리스트가 다른 위치를 가리켜야 성공입니다.


nums = [2, 7, 11, 15]
target = 9
print(brute_force(nums, target))
print(in_search(nums, target))





def L_R_gop(nums):
    outL, outR, out = [], [], []

    p = 1
    for i in range(0, len(nums)):
        outL.append(p)
        p = p * nums[i] # [1, 2, 6, 24]

    p = 1
    for i in range(len(nums)-1, -1, -1):
        outR.append(p)
        p = p * nums[i] # [24, 24, 12, 4] 순서는 오른쪽 끝에서 왼쪽으로.

    for i in range(0, len(nums)):
        if i == 0: # 왼쪽 끝의 값은 outR의 바로 오른쪽 옆자리 값만 읽는다.
            out.append(outR[i+1])
        elif i == len(nums) - 1: # 오른쪽 끝의 값은 outL의 바로 왼쪽 옆자리 값만 읽는다.
            out.append(outL[i-1])
        else: # 사이에 끼인 값은 outL의 바로 왼쪽 자리 값, outR의 바로 오른쪽 자리 값을 서로 곱한다.
            out.append(outL[i-1]*outR[i+1]) # [24, 1*12 = 12, 2*4 = 8, 6]

    return out
            