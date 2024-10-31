class Solution:
  def two_sum(self, nums, target):
    result = [] // 1
    for i, num in enumerate(nums):
      for j, pair in enumerate(nums): // n
        if (i != j) and (num + pair == target): // 1
          result.append(i) // 1
          result.append(j) // 1
          return result // 1
    return result // 1

// T = 1 + 1 + 1 + 1 + 1 + 1 + n
// T = 6 + 2 * n
// T = 6 + 2n
// T = 2n

if __name__ == "__main__":
  sol = Solution()
  print(sol.two_sum([2, 7, 11, 15], 9))
