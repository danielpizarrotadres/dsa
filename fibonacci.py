def fibonacci(num):
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]
    if num == 2:
        return [0, 1]
    res = [0, 1] # 1
    count = 1 # 1
    while (num - 1 > count): # n
        prevPos = count - 1 # 1
        nextPos = count # 1
        nextVal = res[prevPos] + res[nextPos] # 1
        res.append(nextVal) # 1
        count = count + 1 # 1
    return res # 1

# T = 1 + 1 + 1 + 1 + 1 + 1 + 1 + n
# T = 7 + n
# T = n

def recursive_fibonacci(f, aux=1, prev=0, next=1, accum=""):
    if f == 0:
        return [0]
    if f == 1:
        return [0, 1]
    if f == 2:
        return [0, 1]
    newNext = prev + next
    newPrev = next
    aux = aux + 1
    newAccum = accum + " " + str(newNext)
    if f - 1 > aux:
        return recursive_fibonacci(f, aux, newPrev, newNext, newAccum)
    return "0 1"  + str(newAccum)

if __name__ == '__main__':
    print(fibonacci(10))
    print(recursive_fibonacci(10))
