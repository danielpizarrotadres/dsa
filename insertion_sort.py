def insertion_sort(nums):
    for i in range(len(nums)-1):
        next_value = nums[i+1]
        temp = nums[:i+1]
        for j in range(len(temp)):
            last_value = temp[len(temp)-1 - j]
            if last_value > next_value:
                nums[len(temp)-1 - j], nums[i+1] = next_value, last_value    
    return nums

if __name__ == '__main__':
    print(insertion_sort([5, 4, 3]))
