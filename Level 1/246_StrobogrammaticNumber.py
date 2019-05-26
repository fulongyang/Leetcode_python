



'''
    69 return True
    88 return True
    962 return True
    将数字反转180度后是相同的，return True else return False


    数字本身是可以反转180度的
    8,0,69,1，

'''

class Solution:

    def isStrobogrammatic(self,num:str) -> bool:
        lookup = {'0':'0','8':'8','1':'1','6':'9','9':'6'}
        l = len(num)        #输入进来的有几个值
        print(num[3])


        for i in range(int((l+1)/2)):  #int(输入值+1，除以二)，浮点数变成了整数类型，如果有三个字符输入进来只会循环一次
            if num[l-1-i] not in lookup or num[i] != lookup[num[l-1-i]]:
               #num[4-1-0] not in lookup  or  num[0] != lookup[num[4-1-0]]
                return False
        return True
    #range(int((l+1)/2) :
    #num[l-1-i]         :
    #num[i]             :


if __name__ == "__main__":
    s = Solution()
    res = s.isStrobogrammatic('6969')
    print(res)














