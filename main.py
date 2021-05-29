# Use variables and Python data types that we learned in class to create and store player information
# (name, attack, health and heal) and monster information (name, attack, and health).
from random import randint

from random import randint
player_name = 'John'
player_attack = 100
player_health = 1000
player_heal = 50

monster_name = 'limolimo'
monster_attack = 80
monster_health = 1000
print ('Welcome to the Monster Game')
print('Hallo,' + player_name + ' I am the ' + monster_name + ' the worst enemy ever, '
                                                             'if you attack me hard' + ' I will attack you harder ' + ' So be careful!!')




while monster_health > 0  and player_health > 0  :

    player_attack = randint(100, 200)
    monster_attack = randint(80, 150)
    print('player has attack:', player_attack)
    print('monster has attack:', monster_attack)

    player_action = input('1 or 2 ')
    Attack=1
    Heal=2
    if player_action.lower() == '1':
        monster_health = monster_health - player_attack
        print('the monster health ' + str(monster_health))
        print('After you attack! ' + monster_name + ' will punch you ')
        player_health = player_health - monster_attack
        print('Player health now = ' + str(player_health))
    elif player_action.lower() == '2':
        print('Enough is Enough :)')
        print('Player health now = ' + str(player_health))
        print('the monster health ' + str(monster_health))

    else:
        print('try again')
    if player_health <= 0 :
        print ('Hard luck ! ')
        print('Would you like to try again!')
    if monster_health <=0 :
        print('Congrats, You won')
        print('Lets Play again')


#1-heal,2-exit the game,3-game over,4-new game when the game overed
