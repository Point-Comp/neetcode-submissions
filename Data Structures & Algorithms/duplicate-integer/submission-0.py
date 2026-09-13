class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        flag=False

        for i in nums:
            if i in seen:
                flag=True
            seen.add(i)
        
        return flag
