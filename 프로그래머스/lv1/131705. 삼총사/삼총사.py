import itertools

def solution(number):
    answer = 0
    n_list = list(itertools.combinations(number,3))

    for i in n_list:
        if sum(i) == 0:
            answer += 1

    return answer