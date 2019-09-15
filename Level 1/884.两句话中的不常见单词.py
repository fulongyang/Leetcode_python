





class Solution:
    # def uncommonFromSentences(self, A: str, B: str) -> List[str]:

    @classmethod
    def uncommonFromSentences01(self, A: str, B: str):
        from collections import Counter
        return [k for k,v in Counter(A.split(' ')+B.split(' ')).items() if v ==1]


    @classmethod
    def uncommonFromSentences02(self, A: str, B: str):
        pass





if __name__ == '__main__':
    #quertion:寻找列表中只出现过一次的单词
    # A = 'this apple is sweet'
    # B = 'this apple is sour'
    A = 'apple apple'
    B = 'banana'
    result01 = Solution.uncommonFromSentences01(A,B)
    print(result01)





