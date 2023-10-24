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
        
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 1 or index == 2 or index ==3:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
        print("Option D.  Randomly select one for me! \nOption E.  Leave blank (an average price of $15,000 will be used to calculate the final cost estimate)")
        print(Style.RESET_ALL)
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")
        if choice == 'A': 
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index ==1: 
                     self.name = row[1]
                     self.cost = row[2]
                    
        elif choice == 'B':
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index ==2: 
                     self.name = row[1]
                     self.cost = row[2]
        elif choice == 'C':
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index ==3: 
                     self.name = row[1]
                     self.cost = row[2]
        elif choice == 'D':
            pass
        elif choice == 'E':
            self.name = "Undecided"
            self.cost = 15000

# FLORIST
class Florist(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 7 or index == 8 or index == 9 :
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
        print("Option D.  Randomly select one for me! \nOption E.  Leave blank (an average price of $15,000 will be used to calculate the final cost estimate)")
        print(Style.RESET_ALL)
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")
        
        if choice == 'A': 
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index == 7: 
                     self.name = row[1]
                     self.cost = row[2]

        elif choice == 'B':
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index == 8 : 
                     self.name = row[1]
                     self.cost = row[2]
        elif choice == 'C':
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index == 9: 
                     self.name = row[1]
                     self.cost = row[2]
        elif choice == 'D':
            pass
        elif choice == 'E':
            self.name = "Undecided"
            self.cost = 15000        
   


# CATERING
class Food(WeddingItems):
    def get_recc(self):
        num_people = int(input('How many guests are attending? '))
        print ("Here are some recommendations for you")
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 4 or index == 5 or index == 6:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1], "' which costs: $",row[2],"pp. They",row[3])
        print("Option D. Randomly select one for me! \nOption E. Leave blank (an average price of $15,000 will be used to calculate the final cost estimate)")
        print(Style.RESET_ALL)
        choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ")
        if choice == 'A': 
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index == 4: 
                     self.name = row[1]
                     self.cost = int(row[2]) * num_people 
                
        elif choice == 'B':
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index == 5: 
                     self.name = row[1]
                     self.cost = int(row[2]) * num_people 
        elif choice == 'C':
            with open('recc.csv') as f:
                csv_reader = csv.reader(f)
                for index, row in enumerate(csv_reader):
                    if index == 6: 
                     self.name = row[1]
                     self.cost = int(row[2]) * num_people 
        elif choice == 'D':
            pass
        elif choice == 'E':
            self.name = "Undecided"
            self.cost = num_people * 90 
      


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