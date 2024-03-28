def iswhat(arms):
	a=arms[0]
	b=arms[1]
	c=arms[2]
	if a==b and b==c and c==a:
		print("Equilateral")
	elif a==b or a==c or b==c:
		print("Isoceles")
	else:
		print("No Match")

def toy_triangle(*args):
	num=args[0]
	for i in range(1,num+1):
		iswhat(args[i].split(" "))
toy_triangle(4,'36 36 30','47 8 60','46 96 90','86 86 86')