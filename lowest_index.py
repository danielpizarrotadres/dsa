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
        if current < next:
           lowest_index = aux - 1
        else:
           lowest_index = aux
        aux = aux + 1
    return lowest_index

if __name__ == '__main__':
    print(lowest_index([11, 12]))
