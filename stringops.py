def slicedice(word):
	print(f"Word is :-{word}-")
	print(f"this is word[2:5]:- {word[2:5]}")
	print(f"this is word[:5]:- {word[:5]}")
	print(f"this is word[:-5]:- {word[:-5]}")
	print(f"this is word[-4:-1]:- {word[-4:-1]}")
  	
def modify(word):
	re=word.replace("w","j")
	print(f"Replaced String:-{re}")
	print(f"Upper Cased:- {word.upper()}")
	print(f"Remove Whitespaces:-{word.strip()}")
	#cr=word.split(",")
	#print(f"Split on comma:{cr}")
	sp=word.split(" ")
	print(f"Split on space:{sp}")
	print(f"First word after split using index:	{sp[0]}")

def concatestrings(word,nextword):
	c=word+nextword
	print(f"Concatenated string: {c}")
	addspace=word+" "+nextword
	print(f"Adding a space between: {addspace}")
	addcomma=word+","+nextword
	print(f"Adding a comma:-{addcomma}")

def formatstring(word,nextword,num,num2,num3):
	txt="and am spread across {} billion light years with {} trillion galaxies"
	txt2="What is {2} in a  {0} number {1}"
	injected=format(txt.format(num,num2))
	ordered=format(txt2.format(num,num2,num3))
	print(f"Ordered Line: {ordered}")
	print(f"Inserting Number: {word} {nextword} {injected}")
	
    
w="World is not enough"
u="so Hello Universe!"
v=93
x=2
y=12
slicedice(w)
modify(w)
concatestrings(w,u)
formatstring(w,u,v,x,y)

———————————