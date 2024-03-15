from getpass import getpass as gt
import sys 
import time

def game_lodaer(num_for_loader):
    chars="......"
    iteration=range(num_for_loader)
    print("Loding",end=" ")
    for i in iteration:
        for char in chars:
            sys.stdout.write( char)
            sys.stdout.flush()
            time.sleep(0.1)

def game_lodaer_short(num):
    chars="......"
    iteration=range(num)
    for i in iteration:
        for char in chars:
            sys.stdout.write( char)
            sys.stdout.flush()
            time.sleep(0.1)


print('******Welcome to  Rock , Paper and Scisscor Game********')
game_lodaer(8)
player_1=input(f'\n\nPlayer One Input your name:')
player_2=input(f'Player Two Input your name:')

options=['r','p','s']
player1_points=0
player2_points=0
round=1

print("\n*****Game has started*Valid inputs are 'r' 'p' and 's'*****")

for i in range(1,5):
    print(f"Round {round}",end=" ")
    game_lodaer_short(3)
    for i in range(1,2):
        time.sleep(1)
        selection_1=gt(f'\n\nPlayer 1: {player_1} play its your turn: ').lower()
        selection_2=gt(f'Player 2: {player_2} play its your turn: ').lower()
        print("")

        
        if selection_1 and selection_2 in options:
            ## update points
            if selection_1==selection_2:
                continue
            elif selection_1 == 'r' and  selection_2 == 'p':
                player2_points+=1
            elif selection_1 == 'p' and  selection_2 == 'r':
                player1_points+=1
            elif selection_1 == 'r' and  selection_2 == 's':
                player1_points+=1
            elif selection_1 == 's' and  selection_2 == 'r':
                player2_points+=1
            elif selection_1 == 'p' and  selection_2 == 's':
                player2_points+=1
            elif selection_1 == 's' and  selection_2 == 'p':
                player1_points+=1
        else:
            print("A player made un invald entry bye \n ***learn to follow instructions***")
            sys.exit()
            
    round+=1
    continue
print('Round is done')
print(f'****Congrajulaltions {player_1} and {player_2} the winner is..!!****')
game_lodaer_short(1)
##check
if player1_points > player2_points:
    print(f'{player_1} you win with {player1_points} point')
elif player1_points == player2_points:
    print("Opps its a draw....\n Press: 1 to play again or 0 to exit")
    play_again=input("\nEnter option: ")
    if play_again==0:
        sys.stdout.write("Bye have a good day")
        sys.exit()   
    else:
         print()      
else:
    print(f'{player_2} you win with {player2_points} points')       
