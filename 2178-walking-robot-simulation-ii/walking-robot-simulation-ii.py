class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0,0]
        self.cur = 0
        self.dirs = ["East", "North", "West", "South"] 
        self.vals = [[1, 0], [0, 1], [-1, 0], [0, -1]]     

    def step(self, num: int) -> None:
        num = num % ( 2 * (self.width + self.height - 2))
        if num == 0 and self.pos[0] == 0 and self.pos[1] == 0:
            self.cur = 3
        while num > 0:
            x, y = self.pos
            mul_x, mul_y = self.vals[self.cur]
            final_x, final_y = x + mul_x * num, y + mul_y * num
            if final_x < 0:
                final_x = 0
            if final_x >= self.width:
                final_x = self.width - 1
            
            if final_y < 0:
                final_y = 0
            if final_y >= self.height:
                final_y = self.height - 1
            
            steps_taken = abs(final_x - x) + abs(final_y - y)
            self.pos = [final_x, final_y]
            num -= steps_taken
            if num > 0:
                self.cur = (self.cur + 1) % 4
        
        

    def getPos(self) -> List[int]:
        return self.pos
        

    def getDir(self) -> str:
        return self.dirs[self.cur]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()