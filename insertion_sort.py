def insertion_sort(nums):
    i = 0
    while len(nums)-1 >= i:
        temp = nums[0:i+1]
        lowest_val = nums[0:i+1][0]
        for aux in range(0, len(temp)-1):
            if temp[aux] > temp[aux+1]:
                nums[aux] = temp[aux+1]
                nums[aux+1] = temp[aux]
        i += 1
    return nums

def sort_insertion(nums):
    i = 0
    while len(nums)-1 >= i:
        print(f'Index: {i}, Value: {nums[i]}: {nums[0:i+1]} ')
        i+=1
    return nums

if __name__ == '__main__':
    print(sort_insertion([5, 4, 3, 2, 1])) # Fails
