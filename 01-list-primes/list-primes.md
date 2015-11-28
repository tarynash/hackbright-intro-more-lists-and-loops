List Exercises 2
=====================
*Write the code for these problems in a file called `list_primes.py` inside of the `01-list-primes` directory of this repository.*

1. Create a list called `primes` and fill it with the first two prime numbers. Hint: a prime number is a positive number that is not divisible by anything except 1 and itself.
2. Try to add the next prime number to the `primes` list by typing `primes + 5`.  What happens? 
	Error
3. If you got an error, what does this error mean? 
	Can only concatenate a list to a list, not an integer to a list
4. Commit your code.
4. Fix the error (if you got one), so that 5 will be added to the list.
5. Use the statement `primes.append(7,11)` to add the next two prime numbers to the primes list. What happens?
	Error
6. If you got an error, what does this error mean?
	Append method can only take 1 argument, and 2 arguments were given. Need to append 1 number at a time or use extend method.
7. Use the statement `primes.append([7,11])` to add the next two prime numbers to the primes list. What happens? (Hint: you may have to print primes to see)
	[7,11] is appended to the list but is considered one item instead of 2 items
8. Use the `.pop()` method on primes to remove this erroneous entry.
9. Commit your code.
9. Fix the above statement and the `.append()` method twice to properly add 7 and 11 to the primes list.
10. Use the statement `primes.extend(13,17)` to add the next two prime numbers to the primes list. What happens?
	Error
11. If you got an error, what does this error mean?
	No square brackets were used, so the extend method can only take one argument and we passed in 2 arguments.
12. Use the statement `primes.extend(13,17)` to add the next two prime numbers to the primes list. What happens? 
	Same as above
13. Fix the above statement to properly use the `.extend()` method to add 13 and 17 to the list.

*** A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
