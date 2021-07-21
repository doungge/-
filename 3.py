## set, get 메소드를 사용하는 이유는 외부로부터 변수값에 직접적으로 접급하는 것을 막기 위해서다.

class cal(object):

    def __init__(self, v1, v2):
        if isinstance(v1,int):
            self.v1=v1  
        if isinstance(v2,int):
            self.v2=v2

    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
    ## 원하는 변수가 다른 데이터 타입으로 들어오는 것을 방지하고 싶을때 하는 방법
    def setV1(self, v):
        if isinstance(v,int): # v값이 정수 인지 아닌지 비교하는 함수 `isinstance(a,자료형)`
            self.v1 =v

    def getV1(self):
        return self.v1

c1 = cal(10,10)
print(c1.add())
print(c1.subtract())

c1.setV1('one')
c1.v2 = 30

print(c1.add())
print(c1.subtract())