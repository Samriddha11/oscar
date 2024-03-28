def iswhat(arms):
	a=arms[0]
	b=arms[1]
	c=arms[2]
	if a==b and b==c and c==a:
		print("Equi")
	elif a==b or a==c or b==c:
		print("Iso")
	else:
		print("No Match")

def toy_triangle(string,num):
	splits=string.split(" ")
	print(splits)
	for i in range(0,num):
		iswhat(splits[i])
    #return newstring
#toy_triangle("2 2 1",'3 3 3','6 5 7', 3)
toy_triangle("221 333 657", 3)
print("Done")