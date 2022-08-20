def solution(survey, choices):
    answer = ''
    answer_dict = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 
                   'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(survey)):
        if choices[i] < 4:
            answer_dict[survey[i][0]] += 4-choices[i]
            
        elif choices[i] > 4:
            answer_dict[survey[i][1]] += choices[i]-4
    
    if answer_dict['R'] >= answer_dict['T']:
        answer += 'R'
    elif answer_dict['R'] < answer_dict['T']:
        answer += 'T'
        
    if answer_dict['C'] >= answer_dict['F']:
        answer += 'C'
    elif answer_dict['C'] < answer_dict['F']:
        answer += 'F'
        
    if answer_dict['J'] >= answer_dict['M']:
        answer += 'J'
    elif answer_dict['J'] < answer_dict['M']:
        answer += 'M'
        
    if answer_dict['A'] >= answer_dict['N']:
        answer += 'A'
    elif answer_dict['A'] < answer_dict['N']:
        answer += 'N'
        
           
    return answer
