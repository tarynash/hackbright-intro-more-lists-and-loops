#for i in range(1,21):
#	if i == 13:
#		print "hello",
#	print i,

#for i in range(1,10,2):
#	print i,

#for i in range(10,-1,-1):
#	if i == 0:
#		print "Blastoff!",
#	else:
#		print i,

#fruits = ["apples", "oranges" ,"bananas"]

#for item in fruits:
#	print item,

#for item in range(len(fruits)):
#	print fruits[item],

#def sum_nums(num):
#	sum = 0
#	for i in range(num):
#		sum = i + sum
#	return sum
#print sum_nums(3)

#def sum_nums(num):
#	sum = 0
#	for i in range(num+1):
#		sum = i + sum
#	return sum
#print sum_nums(3)

#def sum_nums2(num):
#	if num < 0:
#		sum = 0
#		for i in range(0,num-1,-1):
#			sum = i + sum
#		return sum
#	else:
#		sum = 0
#		for i in range(num+1):
#			sum = i + sum
#		return sum
#print sum_nums2(3)

def fizz_buzz():
	for i in range(1,101):
		if(i%3==0 and i%5==0):
			print "FizzBuzz"
		elif(i%3==0):
			print "Fizz"
		elif(i%5==0):
			print "Buzz"
		else:
			print i

