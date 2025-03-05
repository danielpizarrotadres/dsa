def insertion_sort(nums):
    i = 0
    while len(nums)-1 >= i:
        temp = nums[0:i+1]
        lowest_val = nums[0:i+1][0]

        """
            The error happens in the for in range
            When sorting [4, 5, 3] the 3 value moves to [4, 3, 5] instead of [3, 4, 5]
        """


        for aux in range(0, len(temp)-1):
            if temp[aux] > temp[aux+1]:
                nums[aux] = temp[aux+1]
                nums[aux+1] = temp[aux]
        i += 1
    return nums

if __name__ == '__main__':
    print(insertion_sort([2, 4, 100, 1, 5, 101]))
    print(insertion_sort([3, 2, 1, 5, 4]))
    print(insertion_sort([1, 2, 3, 4, 5]))
    print(insertion_sort([5, 4, 3, 2, 1])) # Fails
    print(insertion_sort([3, -1, 2, -3, 1])) # Fails
