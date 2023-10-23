from colorama import Fore, Back, Style


class WeddingItems:
    name = None
    cost = None
    def __init__(self,item_type):
        self.item_type = item_type
    def ask_user(self):
        confirm = input(Fore.RED + f"Have you chosen a {self.item_type}? Please enter 'y' or 'n' ")
        print(Style.RESET_ALL)
        # confirm = input(f"Have you chosen a {self.item_type}? Please enter 'y' or 'n': ")
        if confirm == "y":
            self.name = input(f"Please enter your {self.item_type} name: ") 
            self.cost = input(f"Please enter your {self.item_type} cost: ")
        
           
            
        elif confirm == "n":
            self.get_recc()
    # def get_recc():
    #     pass

# Instances of Wedding Items 

# VENUE
class Venue(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you")

# FLORIST
class Florist(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")


# CATERING
class Food(WeddingItems):
    def get_recc(self):
        print ("Here are some recommendations for you")


# DECOR
class Decoration(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")

# BEAUTY SERVICES
class MakeupHair(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")

# PHOTO AND VIDEO
class PhotoVideo(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")

# CLOTHES
class Dress(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")

# CAKE
class Cake(WeddingItems): 
    def get_recc(self):
        print("Here are some recommendations for you")
