




class Solution:
    def isValid(self, s):
        #左边有多少个左括号需要匹配
        b = 0
        for a in range(len(s)-1):

            if s[a] == s[a+1]:
                b+=1
                if b == len(s)/2:
                    return True

        left = len(s)/2
        left_value = list(s)[:left]
        for i in left_value:
            if i in s[left:]:
                return True
            else:
                return False



s = Solution()
print(s.isValid(('([)]')))


