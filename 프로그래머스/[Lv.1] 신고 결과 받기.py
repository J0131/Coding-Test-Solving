def solution(id_list, report, k):
    answer = []
    ans_dict = dict()
    ans_list = list()
    ans_dict2 = dict()
    
    for i in report:
        a,b = i.split()
        ans_dict[a] = []
        
    for i in report:
        a,b = i.split()
        if b not in ans_dict[a]:
            ans_dict[a].append(b)

    for j in id_list:
        ans_dict2[j] = 0

    for i in ans_dict.keys():        
        for j in ans_dict[i]:
            ans_dict2[j] += 1 
    
    for i in id_list:
        count = 0
        if i in ans_dict.keys():
            for j in ans_dict[i]:
                if ans_dict2[j] >= k:
                    count += 1
        answer.append(count)
    return answer
