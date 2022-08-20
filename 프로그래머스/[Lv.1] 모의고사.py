def solution(answers):
    supo1=[1,2,3,4,5]
    supo2=[2,1,2,3,2,4,2,5]
    supo3=[3,3,1,1,2,2,4,4,5,5]
    answer = list()

    ans_num = len(answers)
    
    people = 0 
    maximum = 0
    answer2= [0,0,0]
    supo1 = supo1*2000
    supo2 = supo2*1250
    supo3 = supo3*1000
    

    for i in range(ans_num):
        if supo1[i] == int(answers[i]):
            answer2[0] += 1
        if supo2[i] == int(answers[i]):
            answer2[1] += 1
        if supo3[i] == int(answers[i]):
            answer2[2] += 1
    
    for j in answer2:
        people += 1
        if j>=max(answer2):
            #maximum=j
            answer.append(people)
    return answer
