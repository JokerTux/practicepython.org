import time

#Example from the site http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

a 			   = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b 			   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#shared_numbers = []

# for number in b:
#     if number in a:
#         shared_numbers.append(number)
#         print(shared_numbers)


x = set(a).intersection(b)
print(x)



time.sleep(5)