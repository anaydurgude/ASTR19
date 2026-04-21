class favoriteanimal:
    def __init__(self, armlength, leglength, eyes, tail, furry):
        self.armlength = armlength
        self.leglength = leglength
        self.eyes = eyes
        self.tail = tail
        self.furry =  furry
    
    def printclass(self):
        print(f"The length of the arms are: {self.armlength} meters")
        print(f"The length of the legs are: {self.leglength} meters")
        print(f"It has {self.eyes} eyes")
        print(f"Does it have a tail? {self.tail}")
        print(f"Is it furry? {self.furry}")

    

pig = favoriteanimal(0.3, 0.35, 2, True, False)

pig.printclass()