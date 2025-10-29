class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=0
        x=str(x)
        j=len(x)-1
        flag=False
        while i<=j:
            if x[i] == x[j]:
                i=i+1
                j=j-1
                flag=True
            else:
                flag=False
                return flag
        return flag    

        