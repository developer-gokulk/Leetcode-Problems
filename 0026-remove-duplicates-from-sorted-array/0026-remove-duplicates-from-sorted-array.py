class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        i=0
        j=1
        while j<l:
            if nums[i] !=nums[j]:
                nums[i+1]=nums[j]
                i=i+1
            j=j+1
        return i+1   

        
    
            