class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        sign = 1
        ans = 0
        firstNonZero = False
        count=0
        for i in range(len(s)):
            if count>1: return 0
            if(s[i] == "-" or s[i]=="+"): 
                count+=1 
            if(s[i] == " " and firstNonZero): break
            if(s[i] == " " or s[i]=="+"): 
                continue
            if(s[i] == "-"): 
                sign *= -1
                continue
            if(s[i] == "0" and not firstNonZero): continue
            if not (ascii("0")<=ascii(s[i])<= ascii("9")) and not firstNonZero: return 0
            if s[i]=="." : break
            if(ascii("0")<=ascii(s[i])<= ascii("9")):
                if(s[i] != "0"): firstNonZero=True
                ans*=10
                ans += int(s[i])
            if not (ascii("0")<=ascii(s[i])<= ascii("9")) and  firstNonZero: return 0
     
        if (-2**31 <= (sign*ans)  <= 2**31 - 1):
            return (sign * ans) 
        else:
            if(sign ==-1):
                return -2**31
            else:
                return 2**31 - 1
            
def main():
    
    object = Solution()
    print(object.myAtoi("woe 4193 with words"))


if __name__ == "__main__":
    main()        