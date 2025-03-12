def selection_sort(nums):
    temp = nums.copy()
    i = 0
    while len(nums) > i:
        j = 0
        lowest_value = temp[0]
        lowest_index = 0
        while len(temp)-1 > j:
            if temp[j] > temp[j+1] and temp[j+1] <= lowest_value:
                lowest_value = temp[j+1]
                lowest_index = j+1
            j+=1
        temp.pop(lowest_index)
        nums[i] = lowest_value
        i+=1
    return nums

def selection_sort_swaping(nums):
    i = 0
    while len(nums) > i:
        lowest_index = i
        for j in range(i, len(nums)-1):
            if nums[j] > nums[j+1] and nums[j+1] <= nums[lowest_index]:
                lowest_index = j+1
        nums[i], nums[lowest_index] = nums[lowest_index], nums[i]
        i += 1
    return nums

if __name__ == '__main__':
    print(f'[5, 4, 3]/{selection_sort([5, 4, 3])}')
    print(f'[5, 3, 4]/{selection_sort([5, 3, 4])}')
    print(f'[-5, -3, 4]/{selection_sort([-5, -3, 4])}')
    print(f'[3, 1, 2]/{selection_sort([3, 1, 2])}')
    print(f'[4, 3, 2, 1]/{selection_sort([4, 3, 2, 1])}')
    print(f'[1, 2, 3, 4] -> {selection_sort([1, 2, 3, 4])}')
    print(f'[5, 1, 4, 2, 8] -> {selection_sort([5, 1, 4, 2, 8])}')
    print(f'[10, -1, 2, 5, 0] -> {selection_sort([10, -1, 2, 5, 0])}')
    print(f'[5, 4, 3]/{selection_sort_swaping([5, 4, 3])}')
    print(f'[5, 3, 4]/{selection_sort_swaping([5, 3, 4])}')
    print(f'[-5, -3, 4]/{selection_sort_swaping([-5, -3, 4])}')
    print(f'[3, 1, 2]/{selection_sort_swaping([3, 1, 2])}')
    print(f'[5, 1, 4, 2, 8] -> {selection_sort_swaping([5, 1, 4, 2, 8])}')
    print(f'[10, -1, 2, 5, 0] -> {selection_sort_swaping([10, -1, 2, 5, 0])}')
