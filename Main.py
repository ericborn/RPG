# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:44:42 2021

@author: Eric Born

!!! TODO !!!
create room class which stores description text and inventory list for items 
to be taken by player
"""
#import inspect

location_dict = {'start': 'This is the starting room, choose to inspect the room',
                 'north': 'The north side of the castle, you can move south',
                 'east': 'The east side of the castle, you can move west',
                 'south': 'The south side of the castle, you can move north',
                 'west': 'The west side of the castle, you can move to the end',
                 'end': 'The dragon'}

game_active = True

class BaseItem:

    # base item constructor
    def __init__(self, name, description, use_action, quantity):
        self.name = name
        self.description = description
        self.use_action = use_action
        self.quantity = quantity

    # set the items quantity
    def set_quantity(self, quantity):
        if self.quantity + quantity >= 0:
            self.quantity = self.quantity + quantity
        else:
            return('Invalid amount')

    # used to get the items quantity
    def get_quantity(self):
        return self.quantity
    
    # checks if an item is valid
    # def check_if_item(item):
    #     return isinstance(item, BaseItem)
    
    def use_item(item):
        return()
            
class FoodItem(BaseItem):
    #def __init__(self, name, description, use_action, quantity, heal_amount):
    #super().__init__(name, description, use_action, quantity)
        #self.use_action = 'Consume'
    heal_amount = 5
    def use_item(self, Player, item):
        # check for valid
        if(Player and Player.inventory.Find_Item(item)):
            Player.Set_Health(self.heal_amount)
        else:
            return()


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
# Find_Item # looks for item of same class 
# Killed
# ShowDeathScreen
# Restart

class Inventory:
    def __init__(self):
        self.item_list = []
        
    # try to add an item to the players inventory
    # just performs checks then performs add to inventory if successful
    def Try_Add_Item(self, item_to_give):
        if (item_to_give.get_quantity() > 0):
            self.Add_Item(item_to_give)
        else:
            return('Invalid item')
    
    # add the item to the players item list
    def Add_Item(self, item):
        new_item = item
        new_item.set_quantity(item.get_quantity())
        self.item_list.append(new_item)
        return(new_item)
    
    # returns all inventory items
    def Get_Inventory(self):
        if len(self.item_list) > 0:
            for item in self.item_list:
                print(item.name)
        else:
            print('No items')
            
    def Find_Item(self, item):
        if len(self.item_list) > 0:
            for inv_item in self.item_list:
                if item == inv_item:
                    print(item.name)
                    return(inv_item)
        else:
            print('No Items')

class Player:
    
    # Player constructor
    def __init__(self, name, location = 'Start', health = 100):
        self.name = name
        self.health = health
        self.inventory = Inventory()
        self.location = location
    
    # used to move the player
    def Set_Location(self, location):
        if location in location_dict:
            self.location = location
            return('Moved to the ' + str(location))
        else:
            return('Invalid move')
    
    # used to find where the player currently is
    def Get_Location(self):
        return(self.location.lower())
    
    def Inspect_Room(self):
        print(location_dict[self.Get_Location()])
    
    # used to pick up items
    def Loot_Item(self, item_to_give):
        self.item_list.append(item_to_give)
    
    # kill event for the player
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
        return(self.health)
    
    # use item and call remove_item
    def Use_Item(self, item):
        if self.inventory.Find_Item(item):
            item.use_item(self, item)
            self.Remove_Item(item)
        else:
            return('No item')
        
    # removes an item from the item_list
    def Remove_Item(self, item):
        self.inventory.item_list.remove(item)

Tim = Player('Tim')

Tim.Get_health()

Tim.Take_Damage('Slash', -10, 'dragon')

#Tim.Take_Damage('Slash', -100, 'dragon')

Tim.Get_health()

apple = FoodItem('Apple', 'A bruised red apple', 'Eat', 1)

Tim.inventory.Try_Add_Item(apple)

Tim.inventory.Get_Inventory()

Tim.Use_Item(apple)

Tim.Inspect_Room()

Tim.Set_Location('west')


# test_list = [apple, apple, 'apple']
# print(test_list[0].name)

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
        
        

