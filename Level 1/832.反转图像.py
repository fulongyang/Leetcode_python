




class Solution:
    # def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    @staticmethod
    def flipAndInvertImage(A):
        #input  [[1,1,0],[1,0,1],[0,0,0]]
        #putput [[1,0,0],[0,1,0],[1,1,1]]
        #输入: [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
        #输出: [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
        result = list(map(lambda A:[a-1 if a ==1 else a+1 for a in A[::-1]],A))
        return result



if __name__ == "__main__":
    # A = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    A = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
    Solution.flipAndInvertImage(A)






