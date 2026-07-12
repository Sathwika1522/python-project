n = int(input("Enter the number of terms:"))

a = 0
b = 0

print("Fibonacci Series:")

for I in range(n):
	print(a, end=" ")
	c = a + b
	a = b
	b = c