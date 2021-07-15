# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:44:42 2021

@author: Eric Born

!!! TODO !!!
create room class which stores description text and inventory list for items 
to be taken by player
"""
#import inspect


room_text = []

game_active = True

# checks if an item is valid
def check_item(item):
    return isinstance(item, BaseItem)

class BaseItem:

    def __init__(self, name, description, useAction, quantity):
        self.name = name
        self.description = description
        self.useAction = useAction
        self.quantity = quantity

    def setQuantity(self, quantity):
        if self.quantity + quantity >= 0:
            self.quantity = self.quantity + quantity
        else:
            return('Invalid amount')

    def getQuantity(self):
        return self.quantity

# item tests
'''
apple = BaseItem('Apple', 'A bruised red apple', 'Eat', 1)

apple.getQuantity()

apple.setQuantity(1)

apple.getQuantity()

apple.setQuantity(-2)

apple.getQuantity()

#pear = BaseItem()

'''

# Create functions
# ModifiyHealth 
# Killed
# ShowDeathScreen

class Player:
    name = 'BLANK'
    health = 100
    #HUNGER = 100
    #THIRST = 100
    player_inventory = []
    location = 'Starting Room'
    
    # Player constructor
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
    
    def Add_to_inventory(BaseItem, item_to_give):
        if check_item(item_to_give, Item):
            inventory.append(item_to_give)
        
    def Take_Damage(Damage, DamageEvent, DamageCauser):
        damage_Dealt = ModifyHeath(-Damage)
        
        if health <= 0:
            Killed(DamageEvent, DamageCauser)
            
    def Killed(target):
        if isinstance(target, Player):
            ShowDeathScreen()
            

        
#     def use_item(self)
 
# def return_status():
#     print('Your name is ' + str(PLAYER_NAME) + 
#           'Your location is ' + str(LOCATION) + 
#           '\nYour life is ' + str(LIFE) +
#           '\nYour hunger is ' + str(HUNGER) + 
#           '\nYour thirst is ' + str(THIRST))

# def player_command():
#     command = input('Please choose a command: ')
#     if command == 'quit':
#         quit_command()
 
    

        


    
# def move_player(room_selection):
#     print(room_text)

# def quit_command():
#     game_active = False
    

# while game_active: 
#         PLAYER_NAME = input('Please choose a name or enter "quit": ')
#         if PLAYER_NAME == 'quit':
#             print('Please play again soon!')
#             game_active = False
#         else:
            
#             return_status()
#             print('You must journey to the final room and defeat the dragon to' 
#                   'win the game. \nCollect items along the way to aid you in'
#                   'your quest. \nType look around to examine the room you''re'
#                   'in. \nType "quit" to exit')
        
        

