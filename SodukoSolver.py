

from math import floor


class Solution(object):
    
    backtracks =0
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        def isValidSudoku(board):
            """
            :type board: List[List[str]]
            :rtype: bool
            """
            
            
            def checkRow(i,j,value, map):
                rowIndex= 'row'+str(i+1)
                row = map.get(rowIndex)
                if value in row:
                    return False
                row.append(value)
                return True  
            
            def checkCol(i,j,value, map):
                colIndex= 'col'+str(j+1)
                col = map.get(colIndex)
                if value in col:
                    return False
                col.append(value)
                return True  
                
            def checkBox(i,j,value, map):
                row = floor(i/3) +1
                col = floor(j/3) +1
                
                box = col
                if(row == 2): box +=3
                elif row == 3: box+=6
                box = int(box)
                boxIndex= 'box'+str(box)
                mapBox = map.get(boxIndex)
                if value in mapBox:
                    return False
                mapBox.append(value)
                return True  
                
            map = {}
            for i in range(1,10):
                map['row'+str(i)] = []
                map['col'+str(i)] = []
                map['box'+str(i)] = []

            for i in range(9):
                for j in range(9):
                    value = board[i][j] 
                    if value == ".": 
                        continue
                    value = int(value)
                    if  value > 9 or value < 1:
                        return False
                    if not checkRow(i,j,value,map) or not checkCol(i,j,value,map)  or not checkBox(i,j,value,map):
                        return False 
            return True
    
        def findNextCelltoFill(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return i , j
            return -1 , -1    
        
        
        def solve(board,i,j):
        
            i,j = findNextCelltoFill(board)
            
            if i == -1:
                return True
            
            for value in range(1,10):
                board[i][j] = value
                if isValidSudoku(board):
                    if solve(board,i,j):
                        return True
                # undo
                self.backtracks+=1
                board[i][j] = '.'
            
            return False
            
        return solve(board,0,0)
def main():
    board = [["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]]
    object = Solution()
    
    print (object.solveSudoku(board))
    for row in board:
        print ( row)
    

if __name__ == "__main__":
    main() 