from collections import deque
import itertools

def solution(queue1, queue2):
    answer = 0

    dq1 = deque(queue1)
    dq2 = deque(queue2)

    sum1 = sum(dq1)
    sum2 = sum(dq2)

    num = (sum1 + sum2) / 2

    if (sum1 + sum2) % 2 == 1:
        answer = -1
        return answer

    #1
    for i in range(len(dq1)):
        if dq1[i] > num:
            answer = -1
            return answer 
        if dq2[i] > num:
            answer = -1 
            return answer


    for i in range(len(queue1)*4):

        if sum1 == num:
            break
        
        if sum1 > num:
            ele1 = dq1.popleft()
            dq2.append(ele1)
            sum1 -= ele1
            sum2 += ele1
            answer += 1
        else :
            ele2 = dq2.popleft()
            dq1.append(ele2)
            sum1 += ele2
            sum2 += ele2
            answer += 1
        
        if i == len(queue1)*4-1:
            answer = -1

    return answer