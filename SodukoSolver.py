

from math import floor
import re


class Solution(object):
    complete = {"1","2","3","4","5","6","7","8","9"}
    backtracks =0
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        rows = []
        columns = []
        boxes = [[[], [], []], [[], [], []], [[], [], []]]
        
        rowsEmptyIndexes =[]
        colsEmptyIndexes =[]
        boxesEmptyIndexes =[[[], [], []], [[], [], []], [[], [], []]]
        for i in range(9):
            row = []
            rowEmptyIndexes =[]
            for j in range(9):
                if (board[i][j] != "."):
                    row.append(board[i][j])
                else:
                    rowEmptyIndexes.append((i,j)) 
            rows.append(row)
            rowsEmptyIndexes.append(rowEmptyIndexes)
        for j in range(9):
            column = []
            colEmptyIndexes =[]
            for i in range(9):
                if (board[i][j] != "."):
                    column.append(board[i][j])
                else:
                    colEmptyIndexes.append((i,j)) 
            columns.append(column)
            colsEmptyIndexes.append(colEmptyIndexes)
        for i in range(9):
            for j in range(9):
                if (board[i][j] != "."):
                    boxes[i // 3][j // 3].append(board[i][j])
                else:
                    boxesEmptyIndexes[i // 3][j // 3].append((i,j))
        
        
        def isValid(row,col,value):
            """
            :type board: List[List[str]]
            :rtype: bool
            """
            
            def checkRow(row,value):
                if value in rows[row]:
                    return False
                return True
            
            def checkCol(col,value):
                if value in columns[col]:
                    return False
                return True 
                
            def checkBox(row,col,value):
                if value in boxes[row // 3][col // 3]:
                    return False
                return True
                
                
            if not checkRow(row,value) or not checkCol(col,value)  or not checkBox(row,col,value):
                return False 
            return True

        def findNextCelltoFill(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i , j
            return -1 , -1    
        
        
        def makeImplications(board,i,j,val):
            board [i][j] =val
            rows[i].append(val)
            columns[j].append(val)
            boxes[i//3][j//3].append(val)
            boxesEmptyIndexes[i//3][j//3].remove((i,j))
            impl = []
            impl.append((i,j,val))
            i=0
            j=0
            changed = True
            # while changes are available
            while changed:
                changed = False
                # for each box
                for i in range(3):
                    for j in range(3):
            #             # initialize box values
                        missingBoxValues = self.complete.copy()
            #             # find missing box values 
                        # boxValues = set(boxes[i][j])
                        missingBoxValues = missingBoxValues.difference(set(boxes[i][j]))
                    
            #             # save copy missing values for each empy index in box
                        for index in boxesEmptyIndexes[i][j]:
                            r,c = index
                            rowValuesSet = set(rows[r])
                            left = missingBoxValues.difference(rowValuesSet)
                            colValuesSet = set(columns[c])
                            left = left.difference(colValuesSet)
                                                
                            # check if left is singleton
                            if len(left)== 1:
                                val = str(left.pop())
                                if isValid(r,c,val):
                                    board[r][c] = val
                                    impl.append((r,c,val))
                                    rows[r].append(val)
                                    columns[c].append(val)
                                    boxes[r//3][c//3].append(val)
                                    boxesEmptyIndexes[r//3][c//3].remove((r,c))
                                    changed = True
                            
                                        
            return impl
        
        def undoImplications(board, impl):
            for element in impl:
                val =element[2]
                i,j=element[0],element[1]
                board[i][j] = "."
                rows[i].remove(val)
                columns[j].remove(val)
                boxes[i//3][j//3].remove(val)
                boxesEmptyIndexes[i//3][j//3].append((i,j))
            return
        
        def solve(board,i,j):
            i,j = findNextCelltoFill(board)
            if i == -1:
                return True
            
            for value in range(1,10):
                val = str(value)
                # impl = []
                if i == 0 and j ==2 and val == '4':
                    print()
                if isValid(i,j,val):
                    
                    impl = makeImplications(board,i,j,val)
                    if solve(board,i,j):
                        return True
                    # undo
                    self.backtracks+=1
                    undoImplications(board,impl)
                    
                    
            return False
        
        
        solve(board,0,0)
        return self.backtracks

def main():
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    object = Solution()
    
    print (object.solveSudoku(board))
    for row in board:
            print ( row)  

if __name__ == "__main__":
    main() 