left_column = eval(input())
right_column = eval(input())

result = 0

for i in range(8):
    if left_column[i] == 1 and right_column[i] == 1:
        result += 1

print(result)
