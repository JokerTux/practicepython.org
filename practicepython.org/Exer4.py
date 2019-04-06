import time

Num = int(input("Please give me a number : "))

Divi=[]
x = range(1,Num+1)

for element in x:
	if Num%element == 0:
		Divi.append(element)
		print (Divi)

	
time.sleep(5)