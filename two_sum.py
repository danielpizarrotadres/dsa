class Solution:
  def two_sum(self, nums, target):
    result = []
    for i, num in enumerate(nums):
      for j, pair in enumerate(nums):
        if (i != j) and (num + pair == target):
          result.append(i)
          result.append(j)
          return result
    return result

if __name__ == "__main__":
  sol = Solution()
  print(sol.two_sum([2, 7, 11, 15], 9))
