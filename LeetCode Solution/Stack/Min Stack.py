class MinStack:

    def __init__(self):
        self.res_list = []
        
    def push(self, val: int) -> None:
        self.res_list.append(val) 

    def pop(self) -> None:
        if self.res_list:
            self.res_list.pop()
        
    def top(self) -> int:
        if self.res_list:
            return self.res_list[-1]
        

    def getMin(self) -> int:
        if self.res_list:
            return min(self.res_list)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(10)
obj.push(2)
# obj.pop()
param_3 = print(obj.top())
param_4 = print(obj.getMin())