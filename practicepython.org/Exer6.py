# Exercise 6 
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
import time

Inpu = input("Please enter a word : ")
print ("Your wrote : ",Inpu)	


# c   = 0 #counter for the letters
# pal = []

# for a in Inpu:
# 	c +=1 
# 	pal.append(a)

# print(pal[0:c])	
# print(c)

if str(Inpu) == str(Inpu)[::-1]:
	print("This word is a palindrome")

time.sleep(5)	