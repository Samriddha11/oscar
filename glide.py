def glide(s2,dictionary,size):
    valid_subsets=[]
    for word in dictionary:
        #if set(word).issubset(set(s2)): 
        if set(word)<=set(s2):
            valid_subsets.append(word)
    if valid_subsets:
        wordis=min(valid_subsets)
        print(wordis)
    else:
        return "No Valid"
s="ocbms"
dictionary=["rdnothix","obms","qhlrpiaiv","ms","jaupx"]
size=5
glide(s,dictionary,size)
