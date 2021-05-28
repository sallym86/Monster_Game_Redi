# Monster_Game_Redi
# Use variables and Python data types that we learned in class to create and store player information
# (name, attack, health and heal) and monster information (name, attack, and health).

player_name = 'John'
player_attack = 100
player_health = 1000
player_heal = 50

monster_name = 'limolimo'
monster_attack = 80
monster_health = 1000
print ('Welcome to the Monster Game')
print('Hallo,' + player_name + ' I am the ' + monster_name + ' the worst enemy ever, '
                                                             'if you attack me ' + str(
    player_attack) + ' times ' + 'I will attack you back ' + str(monster_attack) + ' times ,' + ' So be careful!!')

while monster_health > 0  and player_health > 0  :

    player_action = input('Attack or Heal?')
    if player_action.lower() == 'attack':
        monster_health = monster_health - player_attack
        print('the monster health ' + str(monster_health))
        print('After you attacked ' + monster_name + ' will attack you back')
        player_health = player_health - monster_attack
        print('Player health now = ' + str(player_health))
    elif player_action.lower() == 'heal':
        print('Enough is Enough :)')
    else:
        print('try again')
    if player_health <= 0 :
        print ('Hard luck ! ')
        print('Would you like to try again!')
    if monster_health <=0 :
        print('Congrats, You win')


#1-heal,2-exit the game,3-game over,4-new game when the game overed
