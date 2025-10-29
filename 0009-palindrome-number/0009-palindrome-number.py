class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=0
        x=str(x)
        j=len(x)-1
        while i<=j:
            if x[i] != x[j]:
                return False
            i=i+1
            j=j-1
        return True
   

        