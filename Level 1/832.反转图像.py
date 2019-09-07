




class Solution:
    # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    @staticmethod
    def flipAndInvertImage01(A):
        #input  [[1,1,0],[1,0,1],[0,0,0]]
        #putput [[1,0,0],[0,1,0],[1,1,1]]
        #输入: [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        #输出: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        result = list(map(lambda A:[a-1 if a ==1 else a+1 for a in A[::-1]],A))
        return result


    @staticmethod
    def flipAndInvertImage02(A):
        alter = lambda x: 1 if x==0 else 0
        result = [[alter(b) for b in a[::-1]] for a in A]
        return result


if __name__ == "__main__":
    # A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    A = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    Solution.flipAndInvertImage01(A)
    Solution.flipAndInvertImage02(A)






