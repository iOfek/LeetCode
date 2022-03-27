

class Solution(object):
    
    
    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # last_index = 0 
        # for i in range (len(nums)):
        #     if i > last_index:
        #         return False
        #     last_index = max(last_index, i+nums[i])   
        # return True 
        last_index =  len(nums)-1  
        for i in range(last_index-1,0-1,-1):
            if i+nums[i] >= last_index:
                last_index = i
        return last_index == 0    
        
        
        
        
    
        
        
        
def main():
    object = Solution()
    nums1 = [3,2,1,0,4]
    print (object.canJump(nums1))


if __name__ == "__main__":
    main() 
        