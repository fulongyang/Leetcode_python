




class Solution:

    @classmethod
    def majorityElement01(self, nums) -> int:
        nums.sort()
        result = nums[int(len(nums)/2)]
        # print(result)
        return result

    @classmethod
    def majorityElement02(self, nums) -> int:
        result = sorted(nums)[len(nums)//2]
        # print(result)
        return result




if __name__ == "__main__":
    # nums = [2,2,1,1,1,2,2]
    nums = [-1,2147483647]
    Solution.majorityElement01(nums)
    Solution.majorityElement02(nums)





















