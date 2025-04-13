def quick_sort(nums):
    limit = len(nums)-1
    pivot = nums[limit]
    min_len = 2
    count_greaters = 0
    for index in range(limit):
        print(nums)
        current_index = limit-(index+1)
        prev_index = limit-(index+2)
        next_index = current_index+1
        if limit > min_len and (prev_index < 0 or current_index < 0):
            break
        current_val = nums[current_index]
        prev_val = nums[prev_index]
        if current_val < pivot and current_val < prev_val:
            nums[current_index], nums[prev_index] = nums[prev_index], nums[current_index]
        if nums[current_index] > pivot:
            count_greaters += 1            
        if nums[current_index] > pivot and nums[next_index] < pivot:
            temp_index = (limit) - count_greaters
            nums[current_index], nums[temp_index] = nums[temp_index], nums[current_index]
    return nums

if __name__ == '__main__':
    print(f'[4, 13, 2, 3, 10, 6, 1, 5]/{quick_sort([4, 13, 2, 3, 10, 6, 1, 5])}')
