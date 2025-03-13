def insertion_sort(nums):
    i = 0
    while len(nums) > i:
        temp = nums[:i+1]
        print(f'Current index: {i}, temp: {temp}')
        i += 1
    return nums

if __name__ == '__main__':
    print(insertion_sort([5, 4, 3]))
