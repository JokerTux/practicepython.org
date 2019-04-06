import time


name = input ("Enter your name : ")
age  = int (input ("Please enter your age (0-99) :"))
till = 100 - age

print ("Welcome ",name,"your ",age," years old . In ",till," you will be 100 years old." )
time.sleep(5)
