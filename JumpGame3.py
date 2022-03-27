class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        m = [-1]*len(arr)
        def reach(arr, index):
            if index<0 or index >= len(arr):
                return False
            if m[index] == 1:
                return True
            if m[index] == 0:
                return False
            
            if(arr[index] == 0):
                return True
            m[index] = 0
            ans =  reach(arr,index+arr[index]) or reach(arr,index-arr[index])
            if(ans == True):
                m[index] = 1
                return True
            else:
                return False
        
        return reach(arr,start)

def main():
    object = Solution()
    arr = [3,0,2,1,2]
    start = 2


    print (object.canReach(arr,start))


if __name__ == "__main__":
    main() 