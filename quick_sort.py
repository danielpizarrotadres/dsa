# TODO: Implement quick_sort()

# 1- Create a variable `pivot`
# 2- Assign a value to variable `pivot` It should be the last number from list of numbers
# 3- Loop over the list of numbers
# 4- For each number, validate:
# 4.1- If current number is greater than `pivot` and 
# 4.2- If curret number is greater than next number
# 5- Swap doesn't work, I should use the `remove` and `insert` approach

def quick_sort(nums):
    for index in range(1, len(nums)-1):
        current = nums[index]
        previous = nums[index-1]
        print(f'Printing index: {index} Printing current: {current} Printing previous {previous}')
    return nums

if __name__ == '__main__':
    print(f'[4, 13, 2, 3, 10, 6, 1, 5]/{quick_sort([4, 13, 2, 3, 10, 6, 1, 5])}')
