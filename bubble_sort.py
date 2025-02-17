from lowest import lowest_index
from highest import highest

# This code depends on `lowest_index` and `highest` functions
# Also this algorithm is selection_sort because it finds the lowest value
# def bubble_sort(nums):
#     numbers = nums
#     temp = []
#     aux = 0
#     while len(nums) > 0:
#         lowest_idx = lowest_index(nums)
#         temp.insert(aux, nums[lowest_idx])
#         nums.pop(lowest_idx)
#         aux = aux + 1
#     return temp

def bubble_sort(nums):
    for i, num in enumerate(nums):
        for j in range(len(nums) - 1):
            aux = nums[j]
            if nums[j] > nums[j+1]:
                aux = nums[j]
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
    
if __name__ == '__main__':
    print(bubble_sort([7, 3, 5, 8, 6]))
