def solution(numbers):
    answer = ''
    new = list(map(str,numbers))

    new.sort(key = lambda x : x*3 , reverse=True)
    return str(int(''.join(i for i in new)))