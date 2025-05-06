def plus_minus(nums):
    count_positive_values, count_negative_values, count_zeros = 0, 0, 0
    for i in range(len(nums)):
        if nums[i] > 0:
            count_positive_values += 1
        elif nums[i] < 0:
            count_negative_values += 1
        else:
            count_zeros += 1
    print(f"{count_positive_values / len(nums):.6f}")
    print(f"{count_negative_values / len(nums):.6f}")
    print(f"{round(count_zeros / len(nums), 6):.6f}")

if __name__ == '__main__':
    plus_minus([1, 1, 0, -1, -1])
    plus_minus([-4, 3, -9, 0, 4, 1])
