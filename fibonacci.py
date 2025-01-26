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

if __name__ == '__main__':
    result = fibonacci(5)
    expect = [0, 1, 1, 2, 3, 5]
    success = result == expect
    print(success)
