# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html | Exercise 7 Num%element == 0:
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

import time

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



for even in a : 
	if even%2 == 0:
		print(even)

evennr = [even for even in a if even%2 == 0]
print (evennr)


time.sleep(5)		