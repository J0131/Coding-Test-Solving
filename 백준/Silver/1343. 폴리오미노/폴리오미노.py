n = input() + ">"
list_n = list()
list_tem = list()

for i in n:
    if i == "X":
        list_tem.append(i)
    elif i ==">":
        if len(list_tem) % 2 != 0:
            print(-1)
        else :
            for j in range(len(list_tem) // 4 ):
                list_n.append("AAAA")
            for k in range(len(list_tem) % 4):
                list_n.append("B")
            print(''.join(s for s in list_n))
    else :
        if len(list_tem) % 2 != 0:
            print(-1)
            break
        else :
            for j in range(len(list_tem) // 4 ):
                list_n.append("AAAA")
            for k in range(len(list_tem) % 4):
                list_n.append("B")
        list_tem = list()
        list_n.append(".")