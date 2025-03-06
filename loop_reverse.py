def loop_reverse(nums):
    for index in range(len(nums)):
        last_value = nums[len(nums)-1 - index]
        print(f'Current index: {index}: last_value: {last_value}')
    return nums

if __name__ == '__main__':
    print(loop_reverse([5, 4, 3, 2, 1, 0]))
