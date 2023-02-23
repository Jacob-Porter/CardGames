import deck as _deck1
import deck as _deck2

cards1 = []
cards2 = []

deck_1 = _deck1.Deck(cards1)  
deck_2 = _deck2.Deck(cards2)

games_NameList = ['War', 'BlackJack']
games_RunningList = []

for i in range(len(games_NameList)):
    games_RunningList.append(False)
    
running = True
## ASK LOOP
while running:
    
    answer = input("________________________________________\n\nType the game would you like to play ('?' shows list of games) or 'Quit' to exit: ")

    if answer == '?': ## Help
        print('\nGames: | ', end ='')
        for i in range(len(games_NameList)):
            print(games_NameList[i], end = ' | ')
        print('\n')
    elif answer == 'Quit': ## Quit
        print('\nBye Bye :)\n')
        running = False        
    elif answer == games_NameList[0]: ## WAR
        games_RunningList[0] = True
        print('\nRunning War\n')
    elif answer == games_NameList[1]: ## BLACKJACK
        games_RunningList[1] = True
        print('\nRunning BlackJack\n')
        
    else:
        print('Error: *Not a game or incorrecly spelled*\n')
    
    
    ## GAME LOOP - BLACKJACK
    if games_RunningList[1]:
        initial_BJ = True
        played_BJ = False
        dealerTurn_BJ = False
        shuffled = False

    while games_RunningList[1]:        
        print('\n\n________________________________________\n\n')
                        
        def DisplayCards(showAllDealerCards):
            if showAllDealerCards:
                for p in range(len(playerCards)):
                    print(playerCards[p])
                print('^ Your Cards (' + str(SumOfCards(playerCards)[1]) + ') ^\n')
                
                for d in range(len(dealerCards)):
                    print(dealerCards[d])
                print('^ Dealer Cards (' + str(SumOfCards(dealerCards)[1]) + ') ^\n')
            else:              
                for p in range(len(playerCards)):
                    print(playerCards[p])
                print('^ Your Cards (' + str(SumOfCards(playerCards)[1]) + ') ^\n')
    
                for d in range(len(dealerCards)):
                    if d > 0:
                        print(dealerCards[d])
                print('^ Dealers Cards ^ *Second is Hidden*\n')
                
        def SumOfCards(cards):
            val = 0
            nums = []
            
            for i in range(len(cards)):
                temp = cards[i].GetNum() 
                if temp > 10:
                    val += 10
                else: 
                    val += temp
                
            hasAce = False
            for i in range(len(cards)):
                if cards[i].GetNum() == 1:
                    hasAce = True
            
            if hasAce:
                nums.append(val)
                if (val + 10) > 21:  
                    nums.append(val)
                else:
                    nums.append(val + 10)
                return nums ## Has ACE    
            
            nums.append(val)
            nums.append(val)     
            return nums
    
        def Play():
            ans = input("Type 'Y' to get another card\nType 'N' to hold\nType 'Exit' to go back to main menu\n")
            if ans == 'Exit':
                games_RunningList[1] = False
            elif ans == 'Y':
                playerCards.append(deck_1.GetCard(0))
                deck_1.Draw()
                return False
            elif ans == 'N':
                while SumOfCards(dealerCards)[1] < 16:
                    dealerCards.append(deck_2.GetCard(0))
                    deck_2.Draw()
                return True
       
        ## SETUP
        if initial_BJ:
           
            if shuffled == False:
                deck_1.Shuffle()
                deck_2.Shuffle()
                shuffled = True

            # count = 0                     ## Potential Bug (got aces from same suit - might be in draw()?)
            # for i in range(deck1.Size()): 
            #     print(deck1.GetCard(i))
            #     count += 1
            # print(count)
            
            playerCards = []
            dealerCards = []
            
            for i in range(0, 2):
                playerCards.append(deck_1.GetCard(0))
                deck_1.Draw()
            for i in range(0, 2):
                dealerCards.append(deck_2.GetCard(0))    
                deck_2.Draw()

            
            initial_BJ = False
           
        ## LOOP
        if not played_BJ and ((SumOfCards(playerCards)[0] == 21 or SumOfCards(playerCards)[1] == 21) and (SumOfCards(dealerCards)[0] == 21 or SumOfCards(dealerCards)[1] == 21)): ## Double BlackJack
            DisplayCards(True)
            print('! Double BlackJack !\n')
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False
            else:
                initial_BJ = True
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
        
        elif not played_BJ and (SumOfCards(dealerCards)[0] == 21 or SumOfCards(dealerCards)[1] == 21): ## Dealer BlackJack
            DisplayCards(True)
            print('! Dealer BlackJack !\n')
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False
            else:
                initial_BJ = True
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
        
        elif SumOfCards(playerCards)[0] > 21: ## Player Bust
            DisplayCards(True)
            print('! Bust !\n')
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False
            else:
                initial_BJ = True
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
            
        elif SumOfCards(dealerCards)[0] > 21: ## Dealer Bust
            DisplayCards(True)
            print('! Dealer Bust !\n')  
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False 
            else:
                initial_BJ = True 
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
                
        elif dealerTurn_BJ and SumOfCards(dealerCards)[1] == SumOfCards(playerCards)[1]: ## Push
            DisplayCards(True)
            print('! Push !\n')  
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False 
            else:
                initial_BJ = True 
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
                
        elif dealerTurn_BJ and (SumOfCards(playerCards)[1] > SumOfCards(dealerCards)[1]): ## Player wins
            DisplayCards(True)    
            print('! Player Wins !\n')
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False
            else:
                initial_BJ = True 
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
                
        elif dealerTurn_BJ and (SumOfCards(dealerCards)[1] > SumOfCards(playerCards)[1]): ## Dealer Wins
            DisplayCards(True)    
            print('! Dealer Wins !\n')
            ans = input("Enter anything to play again or type 'Exit' to leave\n")
            if ans == 'Exit':
                games_RunningList[1] = False  
            else:
                initial_BJ = True 
                played_BJ = False
                dealerTurn_BJ = False
                shuffled = False
                
        else: ## Reg
            played_BJ = True
            DisplayCards(False)
            dealerTurn_BJ = Play()
    ## END OF BLACKJACK
           
# ------------------------------------------------------------------------------------------           
           
    ## GAME LOOP - WAR
    if games_RunningList[0]:
        deck1_Shuffled_War = False
        deck2_Shuffled_War = False 
  
    while games_RunningList[0]:
        
        print('\n\n________________________________________\n\n')
        
        ## Shuffle Decks
        if deck1_Shuffled_War == False and deck2_Shuffled_War == False:
            deck_1.Shuffle()
            deck1_Shuffled_War = True
            deck_2.Shuffle()
            deck2_Shuffled_War = True
        
        ## Play
        if deck_1.Size() > 0 and deck_2.Size() > 0: ## Draw and compare
            temp1 = deck_1.GetCard(0)
            temp2 = deck_2.GetCard(0)
            deck_1.PrintCard(0)
            num1 = deck_1.Draw()
            print('^ Your Card ^\n')
            deck_1.PrintCard(0)
            num2 = deck_2.Draw()
            print('^ Computer Card ^\n')
            
        elif deck_1.Size() == 0: ## Computer Wins Case
            print('Computer Wins!')
            games_RunningList[0] = False
            running = True
            break
        else: ## Player Win Case
            print('You Win!')
            games_RunningList[0] = False
            running = True
            break

        if(num1 > num2): ## Player Wins Round
            print("~ Winner ~")
            deck_1.Add(temp1)
            deck_1.Add(temp2)
            print('\nPlayer Deck Size: ' + str(deck_1.Size()) + '\n')
            print('Computer Deck Size: ' + str(deck_2.Size()) + '\n')
        if (num1 < num2): ## Comp Wins Round
            print("~ Loser ~")
            deck_2.Add(temp1)
            deck_2.Add(temp2)
            print('\nPlayer Deck Size: ' + str(deck_1.Size()) + '\n')
            print('Computer Deck Size: ' + str(deck_2.Size()) + '\n')
        elif(num1 == num2): ## Tie Round
            print("~ Tie ~")
            deck_1.Add(temp1)
            deck_2.Add(temp2)
            print('\nPlayer Deck Size: ' + str(deck_1.Size()) + '\n')
            print('Computer Deck Size: ' + str(deck_2.Size()) + '\n')
        
        ans = input("Press 'Enter Key' to play next card or type 'Exit' to go back to main menu\n")
        if ans == 'Exit':
            games_RunningList[0] = False
    ## END OF WAR
    