from colorama import Fore, Style
import csv
import pandas as pd
import random
import emoji
from methods import (confirm_choice, confirm_wedding_item,
                     confirm_cost, guest_count)


class WeddingItems:
    name = None
    cost = None

    def __init__(self, item_type):
        self.item_type = item_type

    def ask_user(self):
        confirm = confirm_wedding_item(self.item_type)
        print(Style.RESET_ALL)
        if confirm == "y":
            self.name = input(f"Please enter your {self.item_type} name: ")
            self.cost = confirm_cost(self.item_type)
        elif confirm == "n":
            self.get_recc()
        return self.name, self.cost

# Instances of Wedding Items

# VENUE


class Venue(WeddingItems):
    def get_recc(self):
        print(emoji.emojize("""Here are some recommendations for you :house:""",
                            variant="emoji_type"))

        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 1 or index == 2 or index == 3:
                    print(Fore.BLUE + "Option", row[0], "is at '",
                          row[1], "' which costs: $", row[2],
                          ". It is", row[3]
                          )
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[0, 1]
            self.cost = dataFrame.iloc[0, 2]

        elif option == 'B':
            self.name = dataFrame.iloc[1, 1]
            self.cost = dataFrame.iloc[1, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[2, 1]
            self.cost = dataFrame.iloc[2, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
            print(Fore.LIGHTGREEN_EX + "You got", self.name,
                  "which costs $ ", self.cost)
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 15000
        return self.name, self.cost

# FLORIST


class Florist(WeddingItems):
    def get_recc(self):
        print(emoji.emojize("Here are some recommendations for you :bouquet:",
                            variant="emoji_type"))
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 7 or index == 8 or index == 9:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2],
                          ". They offer a ", row[3]
                          )
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[6, 1]
            self.cost = dataFrame.iloc[6, 2]

        elif option == 'B':
            self.name = dataFrame.iloc[7, 1]
            self.cost = dataFrame.iloc[7, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[8, 1]
            self.cost = dataFrame.iloc[8, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 1500
        return self.name, self.cost

# CATERING


class Food(WeddingItems):
    def get_recc(self):
        num_people = int(guest_count())
        print(emoji.emojize("Here are some recommendations for\
                             you :fork_and_knife:", variant="emoji_type"))
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 4 or index == 5 or index == 6:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], "pp. They", row[3])
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[3, 1]
            self.cost = int(dataFrame.iloc[3, 2]) * num_people
        elif option == 'B':
            self.name = dataFrame.iloc[4, 1]
            self.cost = int(dataFrame.iloc[4, 2]) * num_people
        elif option == 'C':
            self.name = dataFrame.iloc[5, 1]
            self.cost = int(dataFrame.iloc[5, 2]) * num_people
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 70 * num_people
        return self.name, self.cost

# DECOR


class Decoration(WeddingItems):
    def get_recc(self):
        print(
            emoji.emojize("Here are some recommendations for you :balloon:",
                          variant="emoji_type"
                          )
             )
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 10 or index == 11 or index == 12:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], ". They", row[3]
                          )
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[9, 1]
            self.cost = dataFrame.iloc[9, 2]
        elif option == 'B':
            self.name = dataFrame.iloc[10, 1]
            self.cost = dataFrame.iloc[10, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[11, 1]
            self.cost = dataFrame.iloc[11, 2]
        elif option == 'D':
            multi = ['A', 'B', 'C']
            number = random.choice(multi)
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 1800
        return self.name, self.cost

# BEAUTY SERVICES


class MakeupHair(WeddingItems):
    def get_recc(self):
        print(
            emoji.emojize("Here are some recommendations for you :lipstick:",
                          variant="emoji_type")
             )
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 13 or index == 14 or index == 15:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], ". They offer", row[3]
                          )
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[12, 1]
            self.cost = dataFrame.iloc[12, 2]
        elif option == 'B':
            self.name = dataFrame.iloc[13, 1]
            self.cost = dataFrame.iloc[13, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[14, 1]
            self.cost = dataFrame.iloc[14, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 800
        return self.name, self.cost

# PHOTO AND VIDEO


class PhotoVideo(WeddingItems):
    def get_recc(self):
        print(emoji.emojize("Here are some recommendations for you :camera:",
                            variant="emoji_type"
                            )
              )
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 16 or index == 17 or index == 18:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], ". They offer", row[3]
                          )
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[15, 1]
            self.cost = dataFrame.iloc[15, 2]
        elif option == 'B':
            self.name = dataFrame.iloc[16, 1]
            self.cost = dataFrame.iloc[16, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[17, 1]
            self.cost = dataFrame.iloc[17, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 3500
        return self.name, self.cost

# CLOTHES


class Dress(WeddingItems):
    def get_recc(self):
        print(emoji.emojize("Here are some recommendations for you :dress:",
                            variant="emoji_type"
                            )
              )
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 19 or index == 20 or index == 21:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], ". They ", row[3])
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[18, 1]
            self.cost = dataFrame.iloc[18, 2]
        elif option == 'B':
            self.name = dataFrame.iloc[19, 1]
            self.cost = dataFrame.iloc[19, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[20, 1]
            self.cost = dataFrame.iloc[20, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 3000
        return self.name, self.cost

# CAKE


class Cake(WeddingItems):
    def get_recc(self):
        print(emoji.emojize("Here are some recommendations\
                             for you :shortcake:", variant="emoji_type"))
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 22 or index == 23 or index == 24:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], ". They ", row[3])
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[21, 1]
            self.cost = dataFrame.iloc[21, 2]
        elif option == 'B':
            self.name = dataFrame.iloc[22, 1]
            self.cost = dataFrame.iloc[22, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[23, 1]
            self.cost = dataFrame.iloc[23, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 600
        return self.name, self.cost

# RING


class Ring(WeddingItems):
    def get_recc(self):
        print(emoji.emojize("Here are some recommendations for you :ring:",
                            variant="emoji_type"))
        with open('recc.csv') as f:
            csv_reader = csv.reader(f)
            for index, row in enumerate(csv_reader):
                if index == 25 or index == 26 or index == 27:
                    print(Fore.BLUE + "Option", row[0], "is at '", row[1],
                          "' which costs: $", row[2], ". They ", row[3])
        print("""Option D.  Randomly select one for me! \nOption E."""
              """Leave blank (an average price will be used to calculate"""
              """the final cost estimate)""")
        print(Style.RESET_ALL)
        option = confirm_choice()
        dataFrame = pd.read_csv('recc.csv')
        if option == 'A':
            self.name = dataFrame.iloc[24, 1]
            self.cost = dataFrame.iloc[24, 2]
        elif option == 'B':
            self.name = dataFrame.iloc[25, 1]
            self.cost = dataFrame.iloc[25, 2]
        elif option == 'C':
            self.name = dataFrame.iloc[26, 1]
            self.cost = dataFrame.iloc[26, 2]
        elif option == 'D':
            number = random.choice([0, 1, 2])
            self.name = dataFrame.iloc[number, 1]
            self.cost = dataFrame.iloc[number, 2]
        elif option == 'E':
            self.name = "Undecided*"
            self.cost = 2500
        return self.name, self.cost
