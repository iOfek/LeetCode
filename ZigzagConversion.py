class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans= ""
        if numRows == 1 : return s
        if(numRows == 2):
            ans = s[::2]
            ans += s[1::2]
            return ans
        test = [""] * numRows
        count=0
        flag = False        
        for i in range(len(s)):
            if(not flag):
                test[count] += s[i]
                count +=1
                if(count == numRows): 
                    flag =True
                    count-=1
            else:
                count -= 1
                test[count] += s[i]
                
                if count ==1:
                    count =0
                    flag =False
            
        for str in test:
            ans += str
            
        return ans
def main():
    
    object = Solution()
    print(object.convert("PAYPALISHIRING", numRows = 2))


if __name__ == "__main__":
    main()  