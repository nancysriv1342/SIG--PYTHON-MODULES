print("Nancy Srivastava 1900300109006")
print("hello world")
print("enter the lengths of the triangle sides: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a == b == c:
	print("Equilateral triangle")
elif a==b or b==c or c==a:
	print("isosceles triangle")
else:
	print("Scalene triangle")