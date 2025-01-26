def fibonacci(num):
    res = [0, 1]
    count = 1
    while (num > count):
        prevPos = count - 1
        nextPos = count
        nextVal = res[prevPos] + res[nextPos]
        res.append(nextVal)
        count = count + 1
    return res

if __name__ == '__main__':
    print(fibonacci(21))
