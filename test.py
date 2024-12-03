
a = 10
b = 5

def Deduct(a:int,b:int):
    return a - b

def Count(a:int,b:int):
    return a + b

def Sum() -> int:
    return Count(a,b) + Deduct(a,b)

print(f"Sum is: {Sum()}")