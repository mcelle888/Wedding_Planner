import emoji
from colorama import Fore, Style
import datetime 
 
 
def get_details(): 
    user_name = input("Please enter your name: ")
    
    wedding_date_y = int(enter_year())   
    wedding_date_m = int(enter_month())
    wedding_date_d = int(enter_day())

  
    # calculates total days till wedding
    today_date = datetime.date.today()
    wedding_date = datetime.date(wedding_date_y, wedding_date_m, wedding_date_d)
    diff = (wedding_date-today_date).days
   
    total_budget = int(enter_budget())
    print(Fore.LIGHTMAGENTA_EX + "Name:", user_name, "\nDate:", wedding_date_d , wedding_date_m , wedding_date_y ,"\nTotal Budget:", total_budget)
    print(Style.RESET_ALL)
    # Checks with user if inputs are correct
    print("Are these details correct?")
    answer = confirm_yesno()
    if answer == "n":
        print("Okay, let's try again")
        get_details() 
    elif answer == "y": 
        print(emoji.emojize("Thanks for that:grinning_face_with_smiling_eyes: ", variant="emoji_type"))
        print("There are", diff, "days left till the wedding. Let's get planning!")



        # Printing to the end wedding plan text file
        with open('weddingplan.txt', 'w') as f:
            f.write("Name: ")
            f.write(user_name)
            f.write("\nDate of Wedding: ")
            f.write(str(wedding_date))
            f.write('\n')
            f.write(str(diff))
            f.write(" days until the wedding!")
            f.write('\n')
            f.write("Budget: ")
            f.write(str(total_budget))
            f.write('\n \n')
            f.write("BUDGET PLAN")
    return total_budget



# Error handling methods

# For entering the date of wedding
def enter_year():
    response = None
    while response is None:
        response = (input("Please enter the year of the wedding (yyyy): "))  
        try:
            if response == int(response):
                raise ValueError
            
            if len(response) != 4:
                raise ValueError
            
            if int(response) < datetime.date.today().year:
                raise ValueError
            
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter a 4 digit number for a future date")
            print(Style.RESET_ALL)
    return response

def enter_month():
    response = None
    while response is None:
        response = (input("Please enter the month of the wedding (mm): "))
        try:
            if response == int(response):
               raise ValueError
            
            if int(response) > 12 or int(response) < 1:
                raise ValueError     
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter a number between 1 and 12")
            print(Style.RESET_ALL)
    return response

def enter_day():
    response = None
    while response is None:
        response = (input("Please enter the day of the wedding (dd): "))
        try:
            if response == int(response):
               raise ValueError
            
            if int(response) > 31 or int(response) < 1:
                raise ValueError     
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter a number value for the day")
            print(Style.RESET_ALL)
    return response



# For entering budget
def enter_budget():
    response = None
    while response is None:
        response = input("Please enter your budget: ") 
        try:
            response = int(response)
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter a number for your budget")
            print(Style.RESET_ALL)
    return response
         
# For confirming information entered 
def confirm_yesno():
    response = None   
    while response is None:     
        try: 
            response = input(" Please type 'y' or 'n': ").lower() 
            if  response !='y' and response !='n':
                raise ValueError      
        except ValueError:
            response = None
            print(Fore.RED+"Invalid input, please try again with 'y' or 'n' ")
            print(Style.RESET_ALL)
    return response

# Asking if they have a wedding item or not
def confirm_wedding_item(item_type):
    response = None   
    while response is None:     
        try: 
            response = input(Fore.LIGHTMAGENTA_EX + f"Have you chosen a {item_type}? Please enter 'y' or 'n' ").lower()
            if  response !='y' and response !='n':
                raise ValueError      
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter 'y' or 'n' ")
            print(Style.RESET_ALL)
    return response


# Confirming costs of self input
def confirm_cost(item_type):
    response = None
    while response is None:
        response = input(f"Please enter your {item_type} cost: ") 
        try:
            response = int(response)
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter a number for the cost")
            print(Style.RESET_ALL)
    return response

# For multiple choice reccommendations 
def confirm_choice():
    choice = None   
    while choice is None:     
        try: 
            choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ").upper()
            if  choice !='A' and choice !='B' and choice !='C' and choice !='D' and choice !='E':
                raise ValueError      
        except ValueError:
            choice = None
            print(Fore.RED + "Invalid input, please type 'A' or 'B' or 'C' or 'D' or 'E'")
            print(Style.RESET_ALL)
    return choice


# Confirming number of guests
def guestcount():
    response = None
    while response is None:
        response = input("How many guests are attending? ") 
        try:
            response = int(response)
        except ValueError:
            response = None
            print(Fore.RED + "Invalid input, please enter a number for the guest")
            print(Style.RESET_ALL)
    return response

