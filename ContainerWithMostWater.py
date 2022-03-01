class Solution(object):
    
    
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_container = 0
        l = 0
        r = len(height) -1        
        while l < r:
            width = abs(l-r)
            area = min(height[l],height[r]) * width                   
            max_container =max(max_container,area)
            if (height[l] <= height[r]):
                l+=1
            else :r-=1
         
        return max_container
    
            
def main():
    height = [2,3,4,5,18,17,6]
    object = Solution()
    print(object.maxArea(height))


if __name__ == "__main__":
    main()   