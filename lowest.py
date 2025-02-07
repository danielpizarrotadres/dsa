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

        if aux == 1:
            if current < next:
               lowest = current
            else:
               lowest = next
        else:
            if current < lowest:
                lowest = current
        aux = aux + 1
    return lowest

def lowest_index(values):
    if len(values) == 0:
        return None
    if len(values) == 1:
        return 0
    lowest_index = 0
    aux = 1
    while len(values) > aux:
        current = values[aux - 1]
        next = values[aux]
        if current < next and current <= values[lowest_index]: 
           lowest_index = aux - 1
        if next < current and next <= values[lowest_index]:
           lowest_index = aux 
        aux = aux + 1
    return lowest_index

if __name__ == '__main__':
    print(lowest([6, 9, 10, 15, 1, 17, 7, 5, 2, 3]))
    print(lowest_index([7, 3, 5, 8, 6]))
