# War game
import random
import itertools

# Version with one colour
def WarOne(Cards):
    player1Cards = Cards.copy()
    player2Cards = Cards.copy()
    # shuffle Cards
    random.shuffle(player1Cards)
    random.shuffle(player2Cards)
    # extra variable
    player1 = 0
    player2 = 0
    i = 0
    answer = 0
    while (answer != 'N') & (i <= (len(Cards) - 1)):
        print( 'Round: ' + str(i) )
        # show card from the top
        print('Player 1 card: ' + str(player1Cards[i]))
        
        # check which card is a letter
        if (player1Cards[i] == 'W'):
            player1Cards[i] = 10
        elif (player1Cards[i] == 'D'):
            player1Cards[i] = 11
        elif (player1Cards[i] == 'K'):
            player1Cards[i] = 12
        elif (player1Cards[i] == 'A'):
            player1Cards[i] = 13

        print('Player 2 card: ' + str(player2Cards[i]))
        if (player2Cards[i] == 'W'):
            player2Cards[i] = 10
        elif (player2Cards[i] == 'D'):
            player2Cards[i] = 11
        elif (player2Cards[i] == 'K'):
            player2Cards[i] = 12
        elif (player2Cards[i] == 'A'):
            player2Cards[i] = 13

        # check value of cards
        if (player1Cards[i] > player2Cards[i]):
            print('Player 1 wins!')
            player1 += 1
        elif (player1Cards[i] < player2Cards[i]):
            print('Player 2 wins!')
            player2 += 1
        else:
            print('Draw!')
        
        i += 1  # iteration index

        if (i == (len(Cards)) ):
            print('Thank you for game!')
        else:
            answer = input('Do you want to play one more time? Y/N')
            if (answer == 'n'):
                print( 'Score: ')
                print( 'P1:  ' + str(player1) + ' P2: ' + str(player2) )
                break
    return

# version with four colours
def WarFour(Cards, Colours):
    player1Cards = []
    player2Cards = []
    #   
    for card in Cards:
        for colour in Colours:
            tup1 = (card, colour)
            player1Cards.append(tup1)
            player2Cards.append(tup1)
    
    # shuffle
    random.shuffle(player1Cards)
    random.shuffle(player2Cards)
    # extra variable
    player1 = 0
    player2 = 0
    i = 0
    answer = 0
    while (answer != 'N') & (i <= (len(Cards) - 1)):
        print( 'Round: ' + str(i) )
        
        # check value
        (value1, colour1) = player1Cards[i]
        (value2, colour2) = player2Cards[i]
        # check the top card
        print( "Player 1: " + str(value1) + str(colour1) ) 
        print( "Player 2: " + str(value2) + str(colour2) ) 
        # value for W, D, K, A
        # check which card is a letter
        if (value1 == 'W'):
            value1 = 10
        elif (value1 == 'D'):
            value1 = 11
        elif (value1 == 'K'):
            value1 = 12
        elif (value1 == 'A'):
            value1 = 13

        if (value2 == 'W'):
            value2 = 10
        elif (value2 == 'D'):
            value2 = 11
        elif (value2 == 'K'):
            value2 = 12
        elif (value2 == 'A'):
            value2 = 13
        # comparison of value
        if (value1 > value2):
            print('Player 1 wins!')
            player1 += 1
        elif (value1 < value2):
            print('Player 2 wins!')
            player2 += 1
        else:
            print('Draw!')

        i += 1  # iteration index

        if (i == (len(player1Cards)) ):
            print('Thank you for game!')
        else:
            answer = input('Do you want to play one more time? Y/N')
            if (answer == 'n'):
                print( 'Score: ')
                print( 'P1:  ' + str(player1) + ' P2: ' + str(player2) )
                break

    return

Cards = [2, 3, 4, 5, 6, 7, 8, 9, 'W', 'D', 'K', 'A']
Colours = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
WarFour(Cards, Colours);
