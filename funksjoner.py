def multiply(a,b):
   return a*b

def divide(a,b):
   return a/b

a = float(input("a: "))
b = float(input("b: "))


print(f"{a}*{b} = {round(multiply(a,b), 2)}")
print(f"{a}/{b} = {round(divide(a,b), 2)}")

