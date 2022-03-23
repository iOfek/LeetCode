import re


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # first we find pivot index:
        n= len (nums)
        l= 0
        r = n -1
        
        while l < r:
            mid = (r +l) // 2
            if nums[mid] >  nums[r]:
                l=mid+1
            else:
                r =mid
                
        if nums[l] == target: return l
        if nums[l]< target and target <= nums[n-1]: 
            l = l +1
            r = n-1
        else:
            l=0
            r = r-1
        while l <= r:
            mid = (r +l) // 2
            
            if nums[mid] ==  target:
                return mid
            if nums[mid] >  target:
                r = mid-1
            else:
                l = mid+1
                
        return -1
        
def main():
    object = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 7
    print (object.search(nums,target))


if __name__ == "__main__":
    main() 