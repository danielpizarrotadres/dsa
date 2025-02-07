from lowest import lowest_index
from highest import highest

def bubble_sort(nums):
    numbers = nums
    temp = []
    aux = 0
    while len(nums) > 0:
        print("Printing current nums: ", nums)
        lowest_idx = lowest_index(nums)
        print("Printing lowest_idx: ", lowest_idx)
        temp.insert(aux, nums[lowest_idx])
        nums.pop(lowest_idx)
    return temp
 
if __name__ == '__main__':
    print(bubble_sort([7, 3, 5, 8, 6]))
