def selection_sort(nums):
    lowest_value = 0
    lowest_pos = 0
    temp = []
    for i, num in enumerate(nums):
        print(f'Current: {i}')

        # Find lowest
        for j, item in enumerate(nums):

            print(f'Current j: {j}')

            if j == 0:
                if nums[j] > nums[j+1]:
                    lowest_value = nums[j+1]
                    lowest_pos = j+1
                if nums[j+1] > nums[j]:
                    lowest_value = nums[j]
                    lowest_pos = j

            if j+1 == len(nums):
                print(f'Current j: {j} is equal to len(nums): {len(nums)}')
                continue

            if j > 0:
                if nums[j] > nums[j+1] and lowest_value >= nums[j+1]:
                    lowest_value = nums[j+1]
                    lowest_pos = j+1
                if nums[j+1] > nums[j] and lowest_value >= nums[j]:
                    lowest_value = nums[j]
                    lowest_pos = j

        print(f'lowest_value: {lowest_value}')
        print(f'lowest_pos: {lowest_pos}')
    return nums

if __name__ == '__main__':
    nums = [2, 4, 100, 1, 5, 101]
    # nums.pop(0)
    print(selection_sort(nums))
