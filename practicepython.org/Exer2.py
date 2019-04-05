import time  


Num = int(input("1st number : "))
Num2 = int(input("2nd number : "))

if Num % 2 == 0 :
	print("the first number is even")
elif Num % 4 == 0 :
	print("the first number is also even when devided by 4")
else :
	print("the first number is odd.")

if Num % Num2 ==0 :
	print("the devided numbers are even.")		

time.sleep(5)	
