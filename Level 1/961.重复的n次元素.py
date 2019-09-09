# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 11:27
# @Author  : yangfulong
# @FileName: 961.重复的n次元素.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/
# @Github  ：https://github.com/fulongyang

--------------------- 
版权声明：
原文链接：
"""


class Solution:

    '''
        输出重复多次的数字
    '''

    @classmethod
    def repeatedNTimes(self, A) -> int:
        #input :[1,2,3,3]
        #output:3
        from collections import Counter
        index = Counter(A)
        max_value = max(index.values())
        find_key = {k:v for k,v in index.items() if v ==max_value}
        result = list(find_key.keys())[0]
        print(result)
        return result


if __name__ == "__main__":
    # A = [1,2,3,3]
    A = [2,1,2,5,3,2]
    Solution.repeatedNTimes(A)