def selection_sort(nums):
    sorted_nums = []
    temp = nums
    aux = 0
    lowest_val = nums[0]
    lowest_pos = 0
    while len(nums) > aux:
        temp = temp[0:len(temp)]
        for index in range(len(temp)-1):
            if temp[index] < temp[index+1] and temp[index] <= lowest_val:
                lowest_val = temp[index]
                lowest_pos = index
        sorted_nums.append(lowest_val)
        temp.pop(lowest_pos)
        if len(temp) > 0:
            lowest_val = temp[0]
            lowest_pos = 0
        aux += 1
    return sorted_nums

# def sort_selection(nums):
#     for index, num in enumerate(nums):
#         print(f'Current [{index}/{num}]')

#         for item in range(index, len(nums)):
#             print(item)

#         print('\n')
#     return nums

def sort_selection(nums):
    i = 0
    for num in nums:
        lowest_val = num
        lowest_pos = i
        j = i
        for item in range(i,len(nums)-1):
            if nums[item] < nums[item+1] and nums[item] <= lowest_val:
                lowest_val = nums[item]
                lowest_pos = j
            j+=1
        nums.pop(lowest_pos)
        nums.insert(i, lowest_val)
        i+=1
    return nums

if __name__ == '__main__':
    nums = [2, 4, 100, 1, 5, 101]
    print(selection_sort(nums))
    print(sort_selection(nums))
