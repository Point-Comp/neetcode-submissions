class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=True
        seen1={}
        seen2={}

        for i in range(len(s)):
            seen1[s[i]]=seen1.get(s[i],0)+1
        
        for j in range(len(t)):
            seen2[t[j]]=seen2.get(t[j],0)+1

        print(seen1)
        print(seen2)
        return seen1==seen2
