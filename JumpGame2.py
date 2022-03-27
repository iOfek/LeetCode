class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        end, furthest =  0, 0  
        jumps = 0
        for i in range(len(nums)-1):
            furthest = max(furthest,i+nums[i])
            if i == end:
                jumps+=1
                end = furthest    
                
        return jumps 
                
def main():
    object = Solution()
    # nums = [1,1,1,1]
    nums = [2,3,0,1,4]
    # nums = [2,3,1,1,4]
    # nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]


    print (object.jump(nums))


if __name__ == "__main__":
    main() 