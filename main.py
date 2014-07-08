from blackjack import *

global cards
global dealerWin 
global playerWin
global dealerLose
global playerLose
global playerChips
global games

def main():
    introHeader()
    globalVariables()    
    blackJackGame()        

if __name__ == '__main__':
    main()