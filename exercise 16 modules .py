import game.characters.player
import game.characters.enemy
import game.weapons.gun
import game.weapons.knife
from os import system
system("cls")

#import game.characters
#import game.weapons


player_1= game.characters.player.player
player_1.name='Hero'
print (player_1.name)

gun_1= game.weapons.gun.gun()
gun_1.rounds()

for i in range(7):
    gun_1.shoot_1()

player_2=game.characters.player.player()
player_2.name='Side Kick'

print (player_2.name)

knife_1 = game.weapons.knife.knife()
knife_1.dagger()

player_3=game.characters.enemy.enemy()
player_3.name='Villan'
print(player_3.name)

