from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = len(board)

        # ----------------- Check 1 -----------------
        for i1 in range(board_size):
            freqMap1 = defaultdict(int)
            for k1 in range(board_size):
                current = board[i1][k1]

                if current == ".":
                    continue
                
                if current in freqMap1:
                    return False

                freqMap1[current] += 1


        # ----------------- Check 2 -----------------
        for i2 in range(board_size):
            freqMap2 = defaultdict(int)
            for k2 in range(board_size):
                current = board[k2][i2]

                if current == ".":
                    continue
                
                if current in freqMap2:
                    return False

                freqMap2[current] += 1 


        # ----------------- Check 3 -----------------
        for i3 in range(board_size):
            if (i3 % 3 == 0):
                freqMap3 = defaultdict(dict)

            for k3 in range(board_size):
                current = board[i3][k3]
                
                if current == ".":
                    continue
                
                row_box = k3 // 3
                if current in freqMap3[row_box]:
                    return False
                
                freqMap3[row_box][current] = 1

        return True

