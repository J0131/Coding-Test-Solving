def solution(nums):
    answer = 0
    lens = len(nums) // 2
    nums = set(nums)
    lens2 = len(nums)
    if lens > lens2:
        answer = lens2
    elif lens <= lens2:
        answer = lens
    
    return answer
