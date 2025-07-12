def cal(a,b):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    print("Addition",add())
    print("subtract",sub())
    print("product",mul())
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
cal(a,b)


def mul_by(n):
    def inner(x):
        return x*n
    return inner
times_2=mul_by(2)
times_3=mul_by(3)
print(times_2(5))
print(times_3(10))


def titled(title):
    def greet(name):
        return f"Hello,{title}{name}"
    return greet                         
mr_greet=titled("Mr.")
dr_greet=titled("Dr.")
print(mr_greet("Vijay"))
print(dr_greet("Jason"))



x=100
y=10
def display():
    x=22
    print("x=",x)
    print("locally",x+y)
display()
print("x=",x)
y=10
y=25
print("latest value of y globally:",y)
print("globally",x+y)

