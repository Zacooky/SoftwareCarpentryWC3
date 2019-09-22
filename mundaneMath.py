#Sum of even numbers between 1 and 100 (including 100)

SUM = 0

for i in range(1,101):
	if i %2 ==0:
		SUM = SUM + i
		i = i + 1

print(SUM)