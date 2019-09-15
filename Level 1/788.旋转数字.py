





class Solution:

    @classmethod
    def rotatedDigits01(self, N: int) -> int:
        #可旋转的数
        changeDic = {
            '0': '0',
            '1': '1',
            '2': '5',
            '5': '2',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        result = 0
        #循环 1-N
        for num in range(1, N + 1):
            #将N变成字符串
            num = str(num)
            #循环变成字符串的数字，如果字符串存在于可旋转的字典中的key中，那么就获取字典中的value
            value = ''.join([changeDic[x] for x in num if x in changeDic])
            #如果结果和原始数据不同，如果结果元素长度和原始元素长度不同
            if value != num and len(value) == len(num):
                #将可能性加一
                result += 1
        return result





if __name__ == "__main__":
    N=30
    result01 = Solution.rotatedDigits01(N)
    print(result01)

    a = [1,2,3,4]
    ar = [str(ab) for ab in a]
    print(ar)

    br = [int(bc) for bc in ar]
    print(br)

















