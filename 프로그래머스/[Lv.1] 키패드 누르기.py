import math

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 11
    distance_list = [[0,4,3,4,3,2,3,2,1,2],
                    [4,0,1,2,1,2,3,2,3,4],
                    [3,1,0,1,2,1,2,3,2,3],
                    [4,2,1,0,3,2,1,4,3,2],
                    [3,1,2,3,0,1,2,1,2,3],
                    [2,2,1,2,1,0,1,2,1,2],
                    [3,3,2,1,2,1,0,3,2,1],
                    [2,2,3,4,1,2,3,0,1,2],
                    [1,3,2,3,2,1,2,1,0,1],
                    [2,4,3,2,3,2,1,2,1,0],
                    [1,2,4,5,2,3,4,1,2,3],
                    [1,5,4,2,4,3,2,3,2,1]]
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        elif i == 3 or i == 6 or i == 9:    
            answer += 'R'
            right = i
        else :
            if abs(distance_list[left][i]) > abs(distance_list[right][i]):
                answer += 'R'
                right = i
            elif abs(distance_list[left][i]) < abs(distance_list[right][i]):
                answer += 'L'
                left = i
            else :
                if hand == 'left':
                    answer += 'L'
                    left = i
                else :
                    answer += 'R'
                    right = i
    return answer
