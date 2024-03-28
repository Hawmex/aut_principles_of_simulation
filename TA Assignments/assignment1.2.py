n, q, l = map(lambda i: int(i), input().split(" "))

dictionary = {}

for i in range(n):
    bin, label = input().split(" ")

    dictionary[bin] = label

outputs = []

for i in range(q):
    bin = input()

    if bin in dictionary.keys():
        outputs.append(dictionary[bin])
    else:
        outputs.append("Unknown")

for output in outputs:
    print(output)
