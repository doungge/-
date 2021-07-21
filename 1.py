

class cal(object):
# 생성자, constructor 객체를 만들때 초기화를 해야하는데 init을 사용한다. 
# 파이썬은 첫번째 매개변수를 꼭정해야되고 첫번째 매개변수는 언제나 인스턴스가 된다. 인스턴스를 가르키는 값이 첫번째 매개변수의 값으로 들어오게된다.
# 인스턴스.메서드()’냐 ‘클래스.메서드(인스턴스)
    def __init__(self, v1, v2):
        print(v1, v2)
        self.v1=v1  # 매개변수를 통해 인스턴스를 정의할 수 있음 첫번째 인자가 인스턴스를 가르키는 것이다. self = instance 변수
        self.v2=v2

    def add(self):
        return self.v1+self.v2
    def subtract(self):
        return self.v1-self.v2
   
c1 = cal(10,10)
print(c1.add())
print(c1.subtract())

c2 = cal(30,20)
print(c2.add())
print(c2.subtract())