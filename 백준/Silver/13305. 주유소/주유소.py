n = int(input())

dist_list = list(map(int,input().split()))
value_list = list(map(int,input().split()))
price = 0
min_value = 1000000000

for i in range(len(dist_list)):
    if value_list[i] < min_value:
        min_value = value_list[i]
        price += dist_list[i] * value_list[i]

    elif value_list[i] >= min_value:
        price += dist_list[i] * min_value

print(price)