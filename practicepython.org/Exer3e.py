import time

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
lessthe = []
for items in a :
	if items < 5:
		lessthe.append(items) #Not sure if this works fine .
		print(lessthe)

time.sleep(5)		