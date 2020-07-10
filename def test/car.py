class Car:
    color=""
    speed=0
    
    def speedUp(self, value):
        self.speed+=value
    def speedDown(self, value):
        self.speed-=value
    
myCar=Car()
myCar.speedUp(39)
myCar.speedDown(3)
print(myCar.speed)
myCar.color="red"
print(myCar.color)