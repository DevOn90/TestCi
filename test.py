
a = 10
b = 5

def Deduct(a:int,b:int):
    return a - b

def Count(a:int,b:int):
    return a + b

def Sum() -> int:
    return Count(a,b) + Deduct(a,b)

print(f"The result is: {Count(2,3)}")
print(f"The relsutl deduct is: {Deduct(10,8)}")
print(f"Sum is: {Sum()}")