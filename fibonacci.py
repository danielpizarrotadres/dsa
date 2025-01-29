def fibonacci(num):
    res = [0, 1] # 1
    count = 1 # 1

    while (num > count): # n
        prevPos = count - 1 # 1
        nextPos = count # 1
        nextVal = res[prevPos] + res[nextPos] # 1
        res.append(nextVal) # 1
        count = count + 1 # 1

    return res # 1

# T = 1 + 1 + 1 + 1 + 1 + 1 + 1 + n
# T = 7 + n
# T = n

def recursive_fibonacci(f, aux=0, current=0, prev=0, next=0):
    aux = aux + 1
    if f > aux:
        return True
    return recursive_fibonacci(f, aux)

if __name__ == '__main__':
    print(fibonacci(7))
    print(recursive_fibonacci(5))
