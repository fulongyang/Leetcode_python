











class Solution:
    def climbStairs(self, n):
        '''
            解题思路
            1.递归方式实现

            2.斐波那契数实现

        '''
        #return 1 if n == 0 or n == 1 else self.climbStairs(n - 1) + self.climbStairs(n - 2)


        #func 2
        x,y = 1,1
        for _ in range(n):
            x,y =y,x+y
            print(_,x,y)
        return x

        #func 3
        # max,b,c =0,1,1
        # while max<n:
        #     yield c
        #     b,c = b,b+c
        #     max = max+1
        #     print(max)




if __name__ == "__main__":
    s = Solution()
    r = s.climbStairs(3)











'''

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶


'''








