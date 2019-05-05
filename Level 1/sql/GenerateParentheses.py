




class Solution:


    def generateParentheis(self,n):
        if n == 0:
            return []
        result = []
        self.helpler(n,n,'',result)
        return result

    def helpler(self,l,r,item,result):
        #(()))) )(
        if r<l:
            return
        if l == 0 and r==0:
            result.append(item)    #？？？为啥这里会让l,r变回了2??

        if l >0:#是否已经用完了
            self.helpler(l-1,r,item+'(',result)
        if r >0:
            self.helpler(l,r-1,item+')',result)

r = Solution()
res = r.generateParentheis(2)
print(res)












