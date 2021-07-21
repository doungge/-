#__ 두개를 붙인 변수는 인스턴스 외부에서 값을 호출하거나 바꿀수 없다.
class c:
    def __init__(self,b):
        self.__value= b
    def show(self):
        print(self.__value)

c1 =c(10)
#print(c1.__value) ## 인스턴스 변수를 외부에서 부를 수 없음
c1.show()