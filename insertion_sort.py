def insertion_sort(nums):
    i = 0
    while len(nums)-1 >= i:
        temp = nums[0:i+1]
        last_value = temp[len(temp)-1]
        print(f'\nCurrent temp: {temp}, printing last value: {last_value}')
        for index in range(len(temp)):
            print(f'Current index: {index}')
        i += 1
    return nums

if __name__ == '__main__':
    # print(insertion_sort([5, 4, 3, 2, 1])) # Fails
    # print(insertion_sort([3, -1, 2, -3, 1])) # Fails
    print(insertion_sort([5, 4, 3]))
