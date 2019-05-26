






class Solution(object):
  def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    for i in range(0, len(nums)):
      if i > 0 and nums[i] == nums[i - 1]:
        continue
      target = 0 - nums[i]
      start, end = i + 1, len(nums) - 1
      while start < end:
        if nums[start] + nums[end] > target:
          end -= 1
        elif nums[start] + nums[end] < target:
          start += 1
        else:
          res.append((nums[i], nums[start], nums[end]))
          end -= 1
          start += 1
          while start < end and nums[end] == nums[end + 1]:
            end -= 1
          while start < end and nums[start] == nums[start - 1]:
            start += 1
    return res


  def threeSum2(self, nums):
      length = len(nums)
      resultList = []
      for i in range(0, length):
          for j in range(i + 1, length):
              for k in range(j + 1, length):
                  tSum = nums[i] + nums[j] + nums[k]
                  if tSum == 0:
                      result = []
                      result.append(nums[i])
                      result.append(nums[j])
                      result.append(nums[k])
                      result.sort()
                      if result not in resultList:
                          resultList.append(result)
      return resultList


  def threeSum3(self, nums):
      length = len(nums)
      resultList = []
      nums.sort()
      for i in range(0, length - 2):
          j = i + 1
          k = length - 1
          while (j < k):
              sum0 = nums[i] + nums[j] + nums[k]
              if (sum0 == 0):
                  result = []
                  result.append(nums[i])
                  result.append(nums[j])
                  result.append(nums[k])
                  if result not in resultList:
                      resultList.append(result)
                  j += 1
              if (sum0 < 0):
                  j += 1
              if (sum0 > 0):
                  k -= 1
      return resultList


  def threeSum4(self, nums):
      len_nums = len(nums)
      for l in range(len_nums-2):
          i = l+1
          r = len_nums-1
          while (i<r):
              sum0 = nums[l]+nums[i]+nums[r]
              if sum0 == 0:
                  lista = [nums[l],nums[i],nums[r],]




if __name__ == "__main__":
    s = Solution()
    # res = s.threeSum([1,2,3])
    # res = s.threeSum([-1, 0, 1, 2, -1, -4])
    # res = s.threeSum2([-1, 0, 1, 2, -1, -4])
    res = s.threeSum3([-1, 0, 1, 2, -1, -4])
    print(res)

