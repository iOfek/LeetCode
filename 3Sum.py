

class Solution(object):
    
    def threeSum(self, nums:list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        s = []
        nums.sort()
        for i in range(len(nums)):
            first = nums[i]
            if first in s: continue
            s.append(first)
            l = i+1
            r = len(nums) -1
            while l < r:
                sum = first + nums[l] +nums[r] 
                if sum == 0:
                    sequence = [first, nums[l], nums[r]]
                    sequence.sort()
                    if(sequence not in ans): 
                        ans.append(sequence)
                    l+=1
                    r-=1
                elif sum < 0:
                    l+=1
                else:
                    r-=1
            
            
            
            
        return ans
def main():
    nums = [-1,0,1,2,-1,-4]
    object = Solution()
    print(object.threeSum(nums))


if __name__ == "__main__":
    main()           