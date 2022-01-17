class Hello:

    def __init__(self,a,b):
        self.nm=a
        self.date=b

    def hello1(self):
        return print(f"hello1{self.nm}")
    def hello2(self):
        print(f"hello2{self.nm}")
    def hello3(self):
        print(f"hello3{self.nm}. today is {self.date}")

a=input("1~3を入力してください。：")
HelloTom=Hello("Tom","July")

if int(a)==1:
    HelloTom.hello1()
if int(a)==2:
    HelloTom.hello2()
if int(a)==3:
    HelloTom.hello3()

