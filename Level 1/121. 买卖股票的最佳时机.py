# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/12 10:11
# @Author  : yangfulong
# @FileName: 121. 买卖股票的最佳时机.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/
# @Github  : https://github.com/fulongyang

--------------------- 
版权声明：
原文链接：
"""


class Solution:


    @classmethod
    def maxProfit(self, prices) -> int:
        #动态规划
        min_p, max_p = 999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        print(max_p)
        return max_p




if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    # prices = [1,2]
    Solution.maxProfit(prices)
    pass












