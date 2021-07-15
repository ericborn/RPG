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

class BaseItem:

    # base item constructor
    def __init__(self, name, description, useAction, quantity):
        self.name = name
        self.description = description
        self.useAction = useAction
        self.quantity = quantity

    # set the items quantity
    def setQuantity(self, quantity):
        if self.quantity + quantity >= 0:
            self.quantity = self.quantity + quantity
        else:
            return('Invalid amount')

    # used to get the items quantity
    def getQuantity(self):
        return self.quantity
    
    # checks if an item is valid
    def check_if_item(item):
        return isinstance(item, BaseItem)

# item tests
'''
apple = BaseItem('Apple', 'A bruised red apple', 'Eat', 1)

apple.getQuantity()

apple.setQuantity(1)

apple.getQuantity()

apple.setQuantity(-2)

apple.getQuantity()

#pear = BaseItem()

apple.check_if_item()

'''

# Create functions
# ModifiyHealth 
# Killed
# ShowDeathScreen

class Player:
    
    # Player constructor
    def __init__(self, name, health = 100, inventory = []):
        self.name = name
        self.health = health
        self.inventory = inventory
    
    # add an item to the players inventory
    def Add_to_inventory(self, item_to_give):
        if BaseItem.check_if_item(item_to_give):
            self.inventory.append(item_to_give)
        else:
            return('Invalid item')
    
        # returns
    def Get_Inventory(self):
        if len(self.inventory) > 0:
            print('print ' + str(self.inventory))
            # for item in range(len(self.inventory)):
            #     print('print ' + str(self.inventory[item].name))
            #     return('return ' + str(self.inventory[item].name))
                   
    # killed the player
    def Killed(self, damage_event, damage_causer):
        print("dead")
        #return("Dead")
        #ShowDeathScreen(damage_causer)
    
    # set the players health
    def Set_Health(self, change_amount):
        self.health = self.health + change_amount
        
    # damage the player    
    def Take_Damage(self, damage_event, change_amount, damage_causer): 
        self.Set_Health(change_amount)
        
        if self.health <= 0:
            self.Killed(damage_event, damage_causer)

    # check the players health    
    def Get_health(self):
        return self.health

Tim = Player('Tim')

Tim.Get_health()

Tim.Take_Damage('Slash', -10, 'dragon')

#Tim.Take_Damage('Slash', -100, 'dragon')

Tim.Get_health()

apple = BaseItem('Apple', 'A bruised red apple', 'Eat', 1)

Tim.Add_to_inventory(apple)
Tim.Add_to_inventory(apple)

# !!! TODO !!!
# figure out how to print the name of the base item, not the object itself
Tim.Get_Inventory()

test_list = ['apple', 'apple', 'apple']
print(test_list)


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
        
        

