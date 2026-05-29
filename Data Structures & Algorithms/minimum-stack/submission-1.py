class MinStack:

    def __init__(self):
        self.a = []
        

    def push(self, val: int) -> None:
        if len(self.a)<1:
            self.a.append([val, val])
            return
        self.a.append([val, min(self.a[-1][1], val)])
        

    def pop(self) -> None:
        self.a.pop()
        

    def top(self) -> int:
        return self.a[-1][0]
        

    def getMin(self) -> int:
        return self.a[-1][1]
        
