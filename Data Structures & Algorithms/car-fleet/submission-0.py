class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        stack=[]

        cars= list(zip(position,speed))
        cars=sorted(cars, reverse=True)
        stack.append((target-cars[0][0])/cars[0][1])
        for i in cars:
            if ((target-i[0])/i[1])>stack[-1]:
                stack.append((target-i[0])/i[1])
            else:
                continue
                
        

        return len(stack)