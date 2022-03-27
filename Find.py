

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ans0,ans1 = -1,-1
        l= 0
        r = len(nums)-1
        # first find right index of target
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] == target and ( mid==len(nums)-1 or nums[mid+1]> target ) :
                ans1 = mid
                break
            if nums[mid] > target:
                r= mid -1  
            else:
                l= mid +1
                
    
        l= 0
        r = len(nums)-1
        # then find left index of target        
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] == target and ( mid==0 or nums[mid-1]< target ) :
                ans0 = mid
                break 
            if nums[mid] < target:
                l= mid +1
            else:
                r= mid -1

        return [ans0, ans1]

def main():
    object = Solution()
    nums = [2,2]
    target = 2
    print(object.searchRange(nums, target))

if __name__ == "__main__":
    main()        