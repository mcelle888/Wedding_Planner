from colorama import Fore, Back, Style
import csv


class WeddingItems:
    name = None
    cost = None
    def __init__(self,item_type):
        self.item_type = item_type
    def ask_user(self):
        confirm = input(Fore.RED + f"Have you chosen a {self.item_type}? Please enter 'y' or 'n' ")
        print(Style.RESET_ALL)
        if confirm == "y":
            self.name = input(f"Please enter your {self.item_type} name: ") 
            self.cost = input(f"Please enter your {self.item_type} cost: ")
        
           
            
        elif confirm == "n":
            self.get_recc()

# Instances of Wedding Items 

# VENUE
class Venue(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you")
        
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")
        if choice == 'A':
            pass
        elif choice == 'B':
            pass
        elif choice == 'C':
            pass
        elif choice == 'D':
            pass
        elif choice == 'E':
            pass

# FLORIST
class Florist(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")


# CATERING
class Food(WeddingItems):
    def get_recc(self):
        print ("Here are some recommendations for you")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")


# DECOR
class Decoration(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")

# BEAUTY SERVICES
class MakeupHair(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")

# PHOTO AND VIDEO
class PhotoVideo(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")

# CLOTHES
class Dress(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")
        

# CAKE
class Cake(WeddingItems): 
    def get_recc(self):
        print("Here are some recommendations for you")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")

# RING
class Ring(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you")
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")


def Calculator():
    pass