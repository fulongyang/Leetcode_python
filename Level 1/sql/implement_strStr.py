





class Solution:

    def strStr(self,haystack,needle):

        result = 0
        #print(len(haystack),len(needle)+1)
        for i in range(len(haystack)-len(needle)+1):
            # if haystack[i:i+len(needle)]
            print(haystack[i:i+len(needle)])
            print(i,i+len(needle))

        print(haystack[4:9])




'hello need ll return 2'

if __name__ == "__main__":
    s = Solution()
    s.strStr('hessfsfas','llsaa')









