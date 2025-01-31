from lowest import lowest_index
from highest import highest

def bubble_sort(nums):
    numbers = nums
    temp = []
    index = 0
    while len(nums) > 0:
        low_index = lowest_index(nums)
           print('Printing low_index: ' + str(low_index))
        nums.pop(low_index)
        index = index + 1
        temp.append()
    return nums
 
if __name__ == '__main__':
    print(bubble_sort([7, 3, 5, 8, 6]))
