num_list = [1, 2, 3, 4, 5, 6]

print(num_list)

index = 0
sum = 0
while index < len(num_list):
    sum = num_list[index] + sum
    index += 1

print(sum) 