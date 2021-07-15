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


    #def use(self, Player):



apple = BaseItem('Apple', 'A bruised red apple', 'Eat', 1)

pear = BaseItem()


class Player:
    name = 'BLANK'
    life = 100
    #HUNGER = 100
    #THIRST = 100
    player_inventory = []
    location = 'Starting Room'
    
    # Player constructor
    def __init__(self, name, life, inventory):
        self.name = name
        self.life = life
        self.inventory = inventory
    
    def add_to_inventory(BaseItem, item_to_give):
        if check_item(item, Item):
            inventory.append(item)
        
    

        
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
        
        

