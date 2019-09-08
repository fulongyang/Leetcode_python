




class Solution:

    @classmethod
    def majorityElement(self, nums) -> int:
        nums.sort()
        result = nums[int(len(nums)/2)]
        return result




if __name__ == "__main__":
    # nums = [2,2,1,1,1,2,2]
    nums = [-1,2147483647]
    Solution.majorityElement(nums)





















