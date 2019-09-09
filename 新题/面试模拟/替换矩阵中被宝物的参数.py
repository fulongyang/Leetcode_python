






class Solution:

    @classmethod
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''
        [
        ['x','x','x,'x'],
        ['x','0','0,'x'],
        ['x','x','0,'x'],
        ['x','0','x,'x'],
        ]
        '''
        array2 =[
        ['x','1','1','x'],
        ['x','0','0','x'],
        ['x','x','0','x'],
        ['x','0','x','x'],
        ]

        #6,7,10,11,    16  6,7,10,11,14,15, 20
        i = 0
        array3 = [[c for c in a] for a in array2]
        print(array3)


        catH = list(map(lambda x:x[1:-1:],array2[1:-1:]))
        # catL = list(map(lambda x:x[1:],array2[1:]))
        # catR = list(map(lambda x:x[:],array2[1:]))
        print(catH)
        print(array2[0])
        result =''





if __name__ == "__main__":
    Solution.solve('')









