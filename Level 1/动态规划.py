


'''
    动态规划算法是自下而上的收集子问题的过程
    求解决策过程中最优解的数据方法


    动态规划解决问题：
        寻求已知数据的最优解
        降低时间复杂度





'''


class Dp:


    def o2n(self,n):
        #这里的时间复杂度是O(2n) 属于高度重复计算
        if n <=1:return 1
        return self.o2n(n-1)+self.o2n(n-2)


    def on(self,n):
        #这里的时间复杂度是O(n),中度复杂
        mem = []
        if n <1:return 1
        if n not in mem:
            mem[n] =self.on(n-1)+self.on(n-2)
        return mem[n]


    def on_(self,n):
        #这里的时间复杂度是O(n)  ,中度复杂
        #区别：
        dp = [1]*(n+1)
        for i in range(2,n+1):
            dp[i] =dp[i-1]+dp[i-2]
        return dp[n]


    def o1(self,n):
        #这里的时间复杂度是O(1)，低度复杂，高效率
        dp1,dp2 = 1,1
        for i in range(2,n+1):
            dp2,dp1 = dp1+dp2,dp2
        return dp2























