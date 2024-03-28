numbers = eval(input())

output = ([], [])

for number in numbers:
    output[0 if number % 2 == 0 else 1].append(number)

print(output)
