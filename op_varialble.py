class c(object):
    def __init__(self, v1):
        self.value = v1
    def show(self):
        print(self.value)

    def getValue(self):
        return self.value
    def setValue(self, v):
        self.value = v

c1 = c(10)
print(c1.getValue())  
c1.setValue(20)
print(c1.getValue())
