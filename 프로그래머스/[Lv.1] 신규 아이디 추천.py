def solution(new_id):
    
    answer = []
    new_id = new_id.lower()
    new_id = [i for i in new_id]
    dot_count = 0

    for i in new_id:
        if i.isdigit() or i.islower() or i == '-' or i == '_':
            answer.append(i)
            dot_count = 0
        elif i == '.':
            dot_count += 1
            if dot_count < 2:
                answer.append(i)

    if answer and answer[0] == '.':
        answer.pop(0)

    if answer and answer[-1] == '.':
        answer.pop()

    if not answer:
        answer.append("a")

    if len(answer) >= 16:
        answer = answer[0:15]
        if answer[14] == ".":
            answer.pop()
    
    if len(answer) <= 2:
        while len(answer) < 3:
            answer.append(answer[-1])

    answer = ''.join(answer)
    return answer
