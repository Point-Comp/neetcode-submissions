class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        pro=[]
        prod=1
        solar=[]

        pre.append(1)
        for i in range(len(nums)):
            prod*=nums[i]
            pre.append(prod)
        prod=1
        
        for j in reversed(range(len(nums))):
            prod*=nums[j]
            pro.append(prod)
        pro.reverse()
        pro.append(1)

        for k in range(len(nums)):
            solar.append(pre[k]*pro[k+1])


        return solar



        

