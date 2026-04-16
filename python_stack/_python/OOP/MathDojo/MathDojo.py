class MathDojo:
    def __init__(self):
        self.set_result(0)

    def set_result(self, result=0):
        self.result = result
        return self
    
    def add(self, num, *nums):
        for i in nums:
            self.result += i
        self.result += num
        return self
    
    def subtract(self, num, *nums):
        for i in nums:
            self.result -= i
        self.result -= num
        return self
    
# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)    # should print 5
# run each of the methods a few more times and check the result!

md2 = MathDojo()
r = md2.add(2).add(2).add(2).result
print(r)
r = md2.subtract(1).subtract(1).subtract(1).result
print(r)