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

def lowest_index(values):
    if len(values) == 0:
        return 0
    if len(values) == 1:
        return values[0]
    lowest_index = 0
    aux = 1
    while len(values) > aux:
        current = values[aux - 1]
        next = values[aux]
        if current < next:
           lowest_index = aux - 1
        else:
           lowest_index = aux
        aux = aux + 1
    return lowest_index

if __name__ == '__main__':
    print(lowest([11, 12, 15, 1]))
    print(lowest_index([11, 12, 15, 1]))
