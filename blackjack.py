import random

def globalVariables():	
	global cards
	global dealerWin 
	global playerWin
	global dealerLose
	global playerLose
	global playerChips
	global games 
	
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]	
	dealerWin = 0  	
	playerWin = 0  	
	dealerLose = 0  	
	playerLose = 0  	
	playerChips = 100	
	games = 1
	

def introHeader():
	print
	print " -----------------------------------------------------------------------------"
	print " |                * Welcome to the Insight Data Engineering *                |"
	print " |                               BLACKJACK                                   |"
	print " |                                                                           |"
	print " |       You have 100 free chips for playing at our data-driven Casino       |"
	print " |                                              created by: @dmartincc       |"
	print " -----------------------------------------------------------------------------"


def newGameHeader(games):
	print
	print " ---------------------------------- HAND #%d -----------------------------------"% (games)

def gameOverHeader():
	print
	print " --------------------------------- GAME OVER -----------------------------------"

def shuffle(cards):    
    card = random.randint(0,12)
    return cards[card]

def countPoints(hand):    
    aces = hand.count(11)
    points = sum(hand)
    if points > 21 and aces > 0:
        while aces > 0 and points > 21:
            points -= 10
            aces -= 1
    return points

def stats(games,playerWin,dealerWin,playerLose,dealerLose,playerChips):
	print 
	print " ----------------------------- STATS after %d hands ---------------------------"% (games)
	print
	print "                  Player %  Dealer %"
	print " Wins   -            %d        %d" % (playerWin*100/games, dealerWin*100/games)	
	print " Chips  -           %d " % (playerChips)
	print 

def blackJackGame():	
	global cards
	global dealerWin 
	global playerWin
	global dealerLose
	global playerLose
	global playerChips
	global games

	while True: 

		player = []
		dealer = []

		playerBust = False
		dealerBust = False 

		newGameHeader(games)
		
		player.append(shuffle(cards))
		player.append(shuffle(cards))
		
		dealer.append(shuffle(cards))
		
		if playerChips == 0:
			print " You have run out of chips. More luck next time!"
			gameOver()
			False
			break
		
		print
		playerBet = raw_input(" How many chips do you want to bet from your %d chips (default = 1 chip): "% (playerChips))		
		if playerBet:
			try:
				if int(playerBet)>1 and int(playerBet)< playerChips:
					playerBet= int(playerBet)
				elif int(playerBet)>playerChips:
					playerBet = raw_input(" Please bet less than your %d chips:"% (playerChips))
					playerBet= int(playerBet)
				else:
					playerBet=1
			except:
				playerBet = raw_input(" Please enter a numeric number and bet less than your %d chips: "% (playerChips))
				playerBet= int(playerBet)
		else:
			playerBet = 1  

		while True:
		    playerPoints = countPoints(player) 
		    dealerPoints = countPoints(dealer)   
		    print                  
		    print " Player has these cards %s with a total value of %d" % (player, playerPoints)
		    print " Dealer has these cards %s with a total value of %d" % (dealer, dealerPoints)
		    print
		    if playerPoints > 21:
		        print " --> Player is busted!"
		        playerBust = True                
		        break
		    elif playerPoints == 21:
		        print "\a --> BLACKJACK!!!"                             
		        break
		    else:
		        hitOrStand = raw_input(" (H)it or (S)tand (type 'h' or 's'): ").lower()
		        if 'h' in hitOrStand:
		            player.append(shuffle(cards))
		        else:
		            break
		while True:		    
		    dealer.append(shuffle(cards))

		    while True:
		        dealerPoints = countPoints(dealer)                
		        if dealerPoints < 17:
		            dealer.append(shuffle(cards))
		        else:
		            break
		    
		    print
		    print " The dealer has %s for a total of %d" % (dealer, dealerPoints)
		    print

		    if dealerPoints > 21:
		        print " --> Dealer is busted!"
		        dealerBust = True
		        if playerBust == False:
		            print " --> Player wins!"
		            playerChips = playerChips + playerBet
		            playerWin += 1
		            dealerLose += 1  

		    elif dealerPoints > playerPoints:
		        print " --> Dealer wins!"
		        playerChips = playerChips - playerBet
		        dealerWin += 1
		        playerLose += 1

		    elif dealerPoints == playerPoints:
		        print " It's a draw!"

		    elif dealerPoints < playerPoints:
		        if playerBust == False:
		            print " --> Player wins!"
		            playerChips = playerChips + playerBet
		            playerWin += 1
		            dealerLose += 1

		        elif dealerBust == False:
		            print " --> Dealer wins!"
		            playerChips = playerChips - playerBet
		            dealerWin += 1
		            dealerLose += 1
		    break  
		 
		stats(games,playerWin,dealerWin,playerLose,dealerLose,playerChips)
		games += 1

		exit = raw_input(" Press Enter or type (Q)uit: ").lower()
		if str(exit) == 'q':
		    break