# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 9:26
# @Author  : yangfulong
# @FileName: 高度检查器.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/

--------------------- 
版权声明：
原文链接：
"""






class Solution:

    '''
        请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 非递减 高度排列的必要移动人数。

    input:[1,1,4,2,1,3]
    output:3

    '''

    @classmethod
    def heightChecker01(self, heights) -> int:
        #思路：先将列表小到大排序，然后与排序后的列表进行对比看哪个不一样，输出False数字
        #[1, 1, 4, 2, 1, 3]
        #[1, 1, 1, 2, 3, 4]
        #[False, False, True, False, True, True]
        #3
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


    @classmethod
    def heightChecker02(self, heights) -> int:
        pass






if __name__ == "__main__":
    heights = [1,1,4,2,1,3]
    Solution.heightChecker01(heights)



















