from ast import List
from os import remove


class Solution:
    def merge(self, intervals):
        ans= []
        intervals.sort()
        i = list()
        while len(intervals) != 0:
            first  = intervals.pop(0)
            for interval in intervals.copy():
                if first[1]>= interval[0]:
                    first[1] = max(first[1],interval[1])
                    intervals.remove(interval)
                else:
                    break
            ans.append(first)
        return ans
        
    
def main():
    object = Solution()
    intervals = [[1,4],[0,2],[3,5]]
    print (object.merge(intervals))


if __name__ == "__main__":
    main() 