def lowest(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]
    lowest = 0
    aux = 1
    while len(values) > aux:
        current = values[aux - 1]
        next = values[aux]
        if current < next:
           lowest = current
        else:
           lowest = next
        aux = aux + 1
    return lowest

if __name__ == '__main__':
    print(lowest([11, 12, 15, 1]))
