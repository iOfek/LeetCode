class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        
        
        def solve(len,l,r,i,str):
            if r > l :
                return False
            if i ==len :
                if l ==r :
                    ans.append(str)
                    return True
                return False
            if i < len and l >=r:
                solve(len,l+1,r,i+1,str+"(") 
                solve(len,l,r+1,i+1,str+")")
            return False    
                
        solve((n*2),l=0,r=0,i=0,str="")
        return ans



def main():
    object = Solution()
    n = 3
    print (object.generateParenthesis(n))
   

if __name__ == "__main__":
    main() 