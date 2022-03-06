## a program which will output in the console only the words that starts with letter 't' and are longer than 3 symbols

quotes = [
	'Nothing travels faster than the speed of light, with the possible exception of bad news, which obeys its own special laws',
	'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.'
]

s2=str(quotes).strip("[]")
s3=((str(s2).replace(",","")).replace(".","")).replace("'","")
s1=str(s3).split()

# print(s2)
# print(s3)
# print(s1)

def foo(name):
	if len(name)>3:
		# print(name)
		return name[0]=='t'
	return False

t_quotes=filter(foo,s1)

print(list(t_quotes))