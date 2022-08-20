def solution(lottos, win_nums):
    answer = []
    max_count = 0
    min_count = 0
    
    for i in range(6):
        if win_nums[i] in lottos and win_nums[i] != 0:
            max_count += 1
            min_count += 1
    
    max_count += lottos.count(0)
    
    if max_count < 2:
        answer.append(6)
    elif max_count == 2:
        answer.append(5)
    elif max_count == 3:
        answer.append(4)
    elif max_count == 4:
        answer.append(3)
    elif max_count == 5:
        answer.append(2)
    elif max_count == 6:
        answer.append(1)
    
    if min_count < 2:
        answer.append(6)
    elif min_count == 2:
        answer.append(5)
    elif min_count == 3:
        answer.append(4)
    elif min_count == 4:
        answer.append(3)
    elif min_count == 5:
        answer.append(2)
    elif min_count == 6:
        answer.append(1)
        
    return answer
