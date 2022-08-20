def solution(participant, completion):
    answer = ''
    answer_dict = dict()
    
    for i in participant:
        answer_dict[i] = 0 

    for j in participant:
        answer_dict[j] += 1
    
    for i in completion:
        answer_dict[i] -= 1

    for key,value in answer_dict.items():
        if value == 1:
            answer = key
            return answer
