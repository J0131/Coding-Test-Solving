def solution(s):
    answer = ''
    a = ''
    
    for i in s:
        if i.isdigit():
            answer += str(i)
        elif i.islower():
            a += i
            if a == 'zero':
                a = ''
                answer += '0'
            elif a == 'one':
                a = ''
                answer += '1'
            elif a == 'two':
                a = ''
                answer += '2'
            elif a == 'three':
                a = ''
                answer += '3'
            elif a == 'four':
                a = ''
                answer += '4'
            elif a == 'five':
                a = ''
                answer += '5'
            elif a == 'six':
                a = ''
                answer += '6'
            elif a == 'seven':
                a = ''
                answer += '7'
            elif a == 'eight':
                a = ''
                answer += '8'
            elif a == 'nine':
                a = ''
                answer += '9'
    
    answer = int(answer)
    return answer
            
    return answer
