class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # first binary search the rows  =
        u = 0
        d = len(matrix)-1
        while u<=d:
            mid = (u + d) // 2
            if matrix[mid][0] == target: 
                return True
            if matrix[mid][0] >  target: 
                d = mid -1
            else:
                u = mid+1
        if matrix[mid][0] <  target:
            row = mid
        else:
            row = mid -1
        
        l,r = 0, len(matrix[0])-1
        while l<=r:
            mid = (l + r) // 2
            if matrix[row][mid] == target: 
                return True
            if matrix[row][mid] >  target: 
                r = mid -1
            else:
                l = mid+1
        return False
        
        
        
def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]

    target = 13
    object = Solution()
    print(object.searchMatrix(matrix,target))


if __name__ == "__main__":
    main()  