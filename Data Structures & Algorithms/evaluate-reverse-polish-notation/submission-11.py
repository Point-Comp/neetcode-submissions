class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for i in tokens:
            if i in "+-/*":
                if i=='*':
                    temp=int(stack.pop())*int(stack.pop())
                elif i=='/':
                    a=stack.pop()
                    b=stack.pop()
                    temp=int(b/a) #// doesnt work cause that rounds -neg values down, not towards 0
                elif i=='+':
                    temp=int(stack.pop())+int(stack.pop())
                
                elif i=='-':
                    temp=-(int(stack.pop())-int(stack.pop()))
                stack.append(temp)
                
            else:
                stack.append(int(i))
                
        

        return int(stack.pop())
        