def solution(sizes):
    answer = 0
    garo_list = []
    sero_list = []
    min_list = []
    
    for i in range(len(sizes)):
        garo_list.append(sizes[i][0])
        sero_list.append(sizes[i][1])
        min_list.append(min(sizes[i]))
    
    max_value = max([max(garo_list), max(sero_list)])

    answer = max_value * max(min_list)    
    return answer
