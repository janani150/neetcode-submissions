class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        flag=True
        rows=len(board)
        cols=len(board[0])

        for row in range(rows):
            seen=set()
            for col in range(cols):
                
                if board[row][col] != ".":
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    elif board[row][col] in seen:
                        flag= False
                        
        for col in range(cols):
            seen=set()
            for row in range(rows):
                
                if board[row][col] != ".":
                    if board[row][col] not in seen:
                        seen.add(board[row][col])
                    elif board[row][col] in seen:
                        flag= False
                        
                        
        
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()
                for i in range(box_row,box_row+3):
                    for j in range(box_col,box_col+3):
                        if board[i][j] != ".":
                            if board[i][j] not in seen:
                                seen.add(board[i][j])
                            elif board[i][j] in seen:
                                flag= False
                                

        return flag



        