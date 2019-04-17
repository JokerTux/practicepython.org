# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Rock Paper Scissors - I made it a bit different.
# Exercise 8 (and Solution)

# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

#     -Rock beats scissors
#     -Scissors beats paper
#     -Paper beats rock


import random



while True :

	def game_start():
		print("Lets play some Rock Paper Scissors game !")
		figure     = input("choose a figure (Rock=r , Paper=p ,Scissors=s) :")
		if figure == "r":
			figure = 1
		elif figure == "p":
			figure = 2
		elif figure == "s":
			figure = 3		
		else :
			print("Wrong key , try again .")	



		figure_ran = random.randrange(1, 4,+1)
		# print ("you : " , figure , ", comp : " , figure_ran) # just checking if the random works 1=rock , 2=paper ,3=scissors
		
		if figure == figure_ran :
			print ("you : " , figure , ", comp : " , figure_ran)
			print ("Tie")
		# 1st 
		if figure == 1 and figure_ran == 2:
			print ("your choice was :Rock ,the opponent chosed :Paper ")
			print ("you lose ...")	
		if figure == 2 and figure_ran == 1:
			print ("your choice was :Paper ,the opponent chosed :Rock ")
			print ("You won !")		
		# 2nd	
		if figure == 2 and figure_ran == 3:
			print ("your choice was :Paper ,the opponent chosed :Scissors ")
			print ("you lose ...")
		if figure == 3 and figure_ran == 2:
			print ("your choice was :Scissors ,the opponent chosed :Paper ")
			print ("You won !")	
		# 3rd
		if figure == 1 and figure_ran == 3:
			print ("your choice was :Rock ,the opponent chosed :Scissors ")
			print ("You won !")
		if figure == 3 and figure_ran == 1:
			print ("your choice was :Scissors ,the opponent chosed :Rock ")
			print ("you lose ...")	


	game_stop = input('Type "q" to exit the game ,for start press "s":')

	if game_stop == "q" :
		break
	elif game_stop == "s" :
		print("[[[[[[[[[[[[ Starting the game ]]]]]]]]]]]]]]]]]")
		game_start()	
	else :	
		print("Wrong key , try again .")	

