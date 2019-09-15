





class Solution:

    @classmethod
    def rotatedDigits01(self, N: int) -> int:
        #����ת����
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
        #ѭ�� 1-N
        for num in range(1, N + 1):
            #��N����ַ���
            num = str(num)
            #ѭ������ַ��������֣�����ַ��������ڿ���ת���ֵ��е�key�У���ô�ͻ�ȡ�ֵ��е�value
            value = ''.join([changeDic[x] for x in num if x in changeDic])
            #��������ԭʼ���ݲ�ͬ��������Ԫ�س��Ⱥ�ԭʼԪ�س��Ȳ�ͬ
            if value != num and len(value) == len(num):
                #�������Լ�һ
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

















