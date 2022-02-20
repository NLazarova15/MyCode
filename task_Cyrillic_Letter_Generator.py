# define the generator function:
def cyrillic_letter_generator(start,end):
	cyr_char  = start
	while cyr_char<=end:
		# yield is almost like return, but it freezes the execution
		yield cyr_char
		cyr_char += 1

cyr_char = cyrillic_letter_generator(1040,1071)

# iterate over our generator:
for i in cyrillic_letter_generator(1040,1071): 
	print(chr(i))