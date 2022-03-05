

from math import floor


class Solution(object):
    complete = {"1","2","3","4","5","6","7","8","9"}
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
        
        def getBox(boxNumber):
            boxIndexes=[]
            colAdd=0
            rowAdd=0
            if(boxNumber in {1,4,7}):
                colAdd = 3
            if(boxNumber in {2,5,8}):
                colAdd = 6    
            if(boxNumber in {3,4,5}):
                rowAdd = 3
            if(boxNumber in {6,7,8}):
                rowAdd = 6
            for i in range (3):
                for j in range (3):                    
                    boxIndexes.append((i+rowAdd,j+colAdd))
            return boxIndexes
        
        def makeImplications(board):
            impl = []
            changed = True
            # while changes are available
            while changed:
                changed = False
                # for each box
                for i in range(9):
                    # get box Indexes
                    box = getBox(i)
                    
                    # initialize box values
                    missingBoxValues = self.complete.copy()
                    # contains info for each index in box
                    boxInfo = []
                    # find missing box values and 
                    for index in box:
                        i,j = index
                        value = board [i][j]
                        if value != ".":
                            missingBoxValues.remove(value)
                    # save copy missing values for each empy index in box
                    for index in box:
                        i,j = index
                        value = board [i][j]
                        if value == ".":
                            boxInfo.append((i,j,missingBoxValues.copy()))
                    
                    for element in boxInfo:
                        left = set()
                        # get row numbers
                        row = element[0]
                        rowValues = set()
                        for value in  board[row]:
                            if value != '.':
                                rowValues.add(value)
                        left = element[2].difference(rowValues)
                        
                        # get col numbers
                        col = element[1]
                        colValues = set()
                        for i in  range(9):
                            value = board[i][col]
                            if value != '.':
                                colValues.add(value)
                        left = element[2].difference(colValues)
                                                
                        # check if left is singleton
                        if len(left)== 1:
                            val = left.pop()
                            board[row][col] = str(val)
                            if isValidSudoku(board):
                                impl.append((row,col,val))
                                changed = True
                            else:
                                board[row][col] = "."
                                        
            return impl
        
        def undoImplications(board, impl):
            for element in impl:
                i,j=element[0],element[1]
                board[i][j] = "."
            return
        
        def solve(board,i,j):
            i,j = findNextCelltoFill(board)
            
            if i == -1:
                return True
            
            for value in range(1,10):
                board[i][j] = str(value)
                # impl = []
                if isValidSudoku(board):
                    impl = makeImplications(board)
                    
                    if solve(board,i,j):
                        return True
                # undo
                    self.backtracks+=1
                    undoImplications(board,impl)
                board[i][j] = "."
            
            return False
            
        solve(board,0,0)
        return self.backtracks
def main():
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    object = Solution()
    
    print (object.solveSudoku(board))
    for row in board:
            print ( row)  

if __name__ == "__main__":
    main() 