def highest(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]
    highest = 0
    aux = 1
    while len(values) > aux:
        current = values[aux - 1]
        next = values[aux]
        if current > next:
           highest = current
        else:
           highest = next
        aux = aux + 1
    return highest

if __name__ == '__main__':
    print(highest([11, 12, 15, 1]))
