class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset=set(nums)
        maxlen=0

        if nums==[]:
            return 0

        for i in nums:
            if (i-1) not in hset:
                length=1
                while i+length in hset:
                        length+=1
                maxlen=max(maxlen,length)
        
        return maxlen