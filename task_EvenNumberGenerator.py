#define the generator function:
def even_numbers_generator(start,end):
	num  = start+1
	while num<=end:
		# yield is almost like return, but it freezes the execution
		yield num
		num += 2

even_numbers = even_numbers_generator(1,10)
# iterate over our generator:
for i in even_numbers:
	print(i)