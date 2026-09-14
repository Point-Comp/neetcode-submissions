class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff=0
        seen={}

        for i,v in enumerate(nums):
            diff=target-v

            if diff in seen:
                return [seen.get(diff,0),i]
            
            seen[v]=i


        

        