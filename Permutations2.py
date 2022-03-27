class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        n = len(nums)
        def rec( nums,group ):
                if len(group) == n:
                    ans.append(group)
                    return
            
                for i in range(len(nums)):
                    if  i>0 and nums[i] == nums[i-1]:
                        continue
                    num = nums.pop(i)
                    newGroup = list(group)
                    newGroup.append(num)
                    rec(nums, newGroup )
                    nums.insert(i,num)
                    newGroup = list(group)
                    
            

        nums.sort()
        group = []
        rec(nums, group)
        return ans
    
def main():
    object = Solution()
    nums = [1,1,2]
    print (object.permuteUnique(nums))


if __name__ == "__main__":
    main() 