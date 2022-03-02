## -----------define the generator function:----------------
# def numbers_generator(start,end):
# 	num  = start
# 	while num<=end:
# 		# yield is almost like return, but it freezes the execution
# 		yield num
# 		num += 1

# numbers = numbers_generator(1,10)
# # iterate over our generator:
# for i in numbers:
# 	print(i)

### -----------  define the even numbers generator function:----------------

def even_numbers_generator(start,end):
    num  = start
    while num<=end:
        if num%2==0: 
		# yield is almost like return, but it freezes the execution
            yield num
            num += 1
        else:
            num += 1
            continue
        
       

even_numbers = even_numbers_generator(1,10)

# iterate over our generator:
for i in even_numbers:
	print(i)
