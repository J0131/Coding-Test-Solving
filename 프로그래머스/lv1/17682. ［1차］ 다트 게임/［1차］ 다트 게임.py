def solution(dartResult):
    answer = 0
    option = ["#","*"]
    bonus = ["S","D","T"]
    dart_len = 9

    dart_list = []

    for i in range(len(dartResult)):
        if i < len(dartResult)-1 and dartResult[i] == "1" and dartResult[i+1] == "0":
            dart_list.append("10")
        elif i > 0 and dartResult[i] == "0" and dartResult[i-1] == "1":
            continue
        else:
            dart_list.append(dartResult[i])

    while len(dart_list) < dart_len:
        dart_list.append("_")

    for i in range(dart_len):
        if i % 3 == 2:
            if dart_list[i] not in option:
                dart_list = dart_list[:i] + ["_"] + dart_list[i:]
    
    dart_list = dart_list[:9]

    n_list = []
    idx = 0

    print(dart_list)

    for i in range(len(dart_list)):
        if i % 3 == 0 :
            if i != 0:
                idx += 1
                n_list.append(sum2)
            sum2 = 0
            sum2 += int(dart_list[i])
        
        if i % 3 == 1:
            sum2 **= int(bonus.index(dart_list[i])+1)

        if i % 3 == 2 and dart_list[i] in option:
            if dart_list[i] == "*":
                sum2 *= 2
                if len(n_list) > 0:
                    n_list[idx-1] *= 2
            elif dart_list[i] == "#":
                sum2 *= -1

        if i == 8:
            n_list.append(sum2)

    print(*n_list)
    answer = sum(n_list)
    return answer