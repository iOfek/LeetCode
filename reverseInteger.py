class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        sign = 1 if x >= 0 else-1
        x = abs(x)
        # while x !=0:
        #     ans *= 10
        #     ans += (x%10)
        #     x = int(x/10)
       
        string = ""
        while x !=0:
            
            string += str(x%10) 
            x = int(x/10)
        if string=="":
            ans =0
        else:
            ans = int(string)
        
        return (sign * ans) if (-2**31 <= (sign*ans)  <= 2**31 - 1) else 0

def main():
    object = Solution()
    # print(object.reverse(-123))
    print(object.reverse(0))


if __name__ == "__main__":
    main()