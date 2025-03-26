def quick_sort(nums):
    pivot = nums[len(nums)-1]
    limit = len(nums)-1
    for index in range(limit):
        current = nums[index]
        if current >= pivot:
            nums.pop(index)
            nums.append(current)
    return nums

if __name__ == '__main__':
    print(f'[4, 13, 2, 3, 10, 6, 1, 5]/{quick_sort([4, 13, 2, 3, 10, 6, 1, 5])}')
