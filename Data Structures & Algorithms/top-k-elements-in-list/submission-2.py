class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap={}
        solar=[]
        count=0
        sol=[]

        for i in range(len(nums)+1):
            solar.append([])
        

        for i in nums:
                hmap[i]=hmap.get(i,0)+1
        
        for n,c in hmap.items():
            solar[c].append(n)
        
        for i,v in enumerate(reversed(solar)):
                for j in v:
                    sol.append(j)
                    if len(sol)==k:
                        return sol
                    
                    
                    
                

            
        

        