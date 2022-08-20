def solution(board, moves):
    answer = 0
    answer_list = []
    n = len(board)
    a = [[] for _ in range(n)]

    for i in range(len(board)):
        for j in reversed(range(len(board))):
            a[i].append(board[j][i])

    for k in range(n):
        while 0 in a[k]:
            a[k].remove(0)


    for i in moves:
        if not answer_list and a[i-1]:
            answer_list.append(a[i-1].pop())

        else : 
            if a[i-1]:
                if a[i-1][-1] != answer_list[-1]:
                    answer_list.append(a[i-1].pop())
                    
                else :
                    answer += 2
                    a[i-1].pop()
                    answer_list.pop()           
            
    return answer
