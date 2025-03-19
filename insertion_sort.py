def insertion_sort(nums):
    for i in range(len(nums)-1):
        next_value = nums[i+1]
        temp = nums[:i+1]
        for j in range(len(temp)):
            last_value = temp[len(temp)-1 - j]
            if last_value > next_value:
                nums[len(temp)-1 - j], nums[i+1-j] = next_value, last_value
    return nums

if __name__ == '__main__':
    print(insertion_sort([5, 4, 3]))
    print(f'[5, 4, 3]/{insertion_sort([5, 4, 3])}')
    print(f'[5, 3, 4]/{insertion_sort([5, 3, 4])}')
    print(f'[5, 4, 3]/{insertion_sort([5, 4, 3])}')
    print(f'[5, 3, 4]/{insertion_sort([5, 3, 4])}')
    print(f'[-5, -3, 4]/{insertion_sort([-5, -3, 4])}')
    print(f'[3, 1, 2]/{insertion_sort([3, 1, 2])}')
    print(f'[4, 3, 2, 1]/{insertion_sort([4, 3, 2, 1])}')
    print(f'[1, 2, 3, 4] -> {insertion_sort([1, 2, 3, 4])}')
    print(f'[5, 1, 4, 2, 8] -> {insertion_sort([5, 1, 4, 2, 8])}')
    print(f'[10, -1, 2, 5, 0] -> {insertion_sort([10, -1, 2, 5, 0])}')
    print(f'[5, 4, 3]/{insertion_sort([5, 4, 3])}')
    print(f'[5, 3, 4]/{insertion_sort([5, 3, 4])}')
    print(f'[-5, -3, 4]/{insertion_sort([-5, -3, 4])}')
    print(f'[3, 1, 2]/{insertion_sort([3, 1, 2])}')
    print(f'[5, 1, 4, 2, 8] -> {insertion_sort([5, 1, 4, 2, 8])}')
    print(f'[10, -1, 2, 5, 0] -> {insertion_sort([10, -1, 2, 5, 0])}')
