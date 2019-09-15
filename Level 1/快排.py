# _*_ encoding:utf-8 _*_
"""
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 16:13
# @Author  : yangfulong
# @FileName: 快排.py.py
# @Software: PyCharm
# @Blog    ：https://www.yangfulong.top/

--------------------- 
版权声明：
原文链接：
"""


quick_sort01 = lambda array: array if len(array) <= 1 else quick_sort01([item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort01([item for item in array[1:] if item > array[0]])


def quick_sort02(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort02(array, low, left - 1)
    quick_sort02(array, left + 1, high)







def quick_sort03(array, l, r):
    if l < r:
        q = partition03(array, l, r)
        quick_sort03(array, l, q - 1)
        quick_sort03(array, q + 1, r)




def partition03(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1






if __name__ == "__main__":
    pass











