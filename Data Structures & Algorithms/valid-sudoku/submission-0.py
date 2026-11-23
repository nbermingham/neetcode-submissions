class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        return whether a sudoku board is valid.

        1. check if each row has duplicate values
        2. check if each column has duplicate values
        3. check if each box has duplicate values
        """

        # check rows
        for i in range(9):
            found = set([])
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] not in found:
                    found.add(board[i][j])
                else:
                    return False

        # check columns
        for i in range(9):
            found = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] not in found:
                    found.add(board[j][i])
                else:
                    return False

        # check boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                found = set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] == ".":
                            continue
                        if board[r+i][c+j] not in found:
                            found.add(board[r+i][c+j])
                        else:
                            return False

        return True