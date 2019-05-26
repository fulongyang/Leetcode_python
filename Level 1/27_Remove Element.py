



class Solution:
    def removeElement(self, nums, val):
        # setp1 -------------------------以递归的形式实现
        '''
        解释：
            如果是空数组，返回空数组
            如果val存在于nums,那么就将它移除，如果val 不存在nums了，那么就返回这个列表的长度，不然就再次返回给自己调用
        '''

        if not nums:
            return 0
        elif val in nums:
            nums.remove(val)
            return len(nums) if val not in nums else self.removeElement(nums,val)
        else:
            return len(nums)



# class Solution:
#     def removeElement(self, nums, val):
#
#         #setp2------------------- 以循环的方式实现
#
#         '''
#             解释:
#                 如果val存在于nums里面，就将他移除，持续下去
#
#             问题：
#                 使用remove会不会达不到O(1)的复杂度，还是需要使用Pop?
#                 是的，列表中使用pop能达到O(1)的效果，使用方法list.pop(2)
#         '''
#         while val in nums:
#             nums.remove(val)
#         return len(nums)



# class Solution:
#     def removeElement(self, nums, val):
#         n=0
#         while n<=len(nums) and len(nums) !=1:
#             if nums[n] ==val:
#                 nums.pop(n)
#             n+=1
#         return len(nums)



if __name__ == "__main__":
    s = Solution()
    res = s.removeElement([2],3)
    print(res)








'''

给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1:

给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。


'''
















