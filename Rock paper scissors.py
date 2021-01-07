from random import * #import
#heading and variables
print('This is Rock Paper Scissors')
opt = ['R','P','S']
player_wins = 0
comp_wins = 0
times = 1
while True:
    
    #information
    print('round: ',times)
    print('player wins: ',player_wins,'computer wins: ',comp_wins)
    
    #--MAINCODE--#
    player = input('Type R for Rock,P for Paper and S for Scissors: ').upper().strip()#player input
    choice = randint(0,2)
    chose_opt = opt[choice]
    print(chose_opt)
    
    #--Winning game--#
    if comp_wins == 3:
        print('computer wins! Better luck next time')
        break
    
    if player_wins == 3:
        print('You win! Good job')
        break
    
    #--COMBINATIONS--#
    if player == chose_opt:#tie
        print('same')
        times = times
    #winning
    if player == 'R' and chose_opt == 'S':
        print('You won')
        player_wins = player_wins + 1
        times = times + 1
        
    if player == 'P' and chose_opt == 'R':
        print('You won')
        player_wins = player_wins + 1
        times = times + 1
        
    if player == 'S' and chose_opt == 'P':
        print('You won')
        player_wins = player_wins + 1
        times = times + 1
        
    #losing
    if player == 'S' and chose_opt == 'R':
        print('You lost')
        comp_wins = comp_wins + 1
        times = times + 1
        
    if player == 'R' and chose_opt == 'P':
        print('You lost')
        comp_wins = comp_wins + 1
        times = times + 1 
        
    if player == 'P' and chose_opt == 'S':
        print('You lost')
        comp_wins = comp_wins + 1
        times = times + 1
