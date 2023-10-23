from pyfiglet import Figlet
import emoji
from colorama import Fore, Back, Style
import datetime 

def introduction(): 
    user_name = input("Please enter your name: ")
    wedding_date_y = int(input("Please enter the year of the wedding (yyyy): "))
    wedding_date_m = int(input("Please enter the month of the wedding (mm): "))
    wedding_date_d = int(input("Please enter the day of the wedding (dd): "))
    # calculates total days till wedding
    today_date = datetime.date.today()
    wedding_date = datetime.date(wedding_date_y, wedding_date_m, wedding_date_d)
    diff = (wedding_date-today_date).days
   
    total_budget= int(input("Enter your budget: "))
    print(Fore.RED + "Name:", user_name, "\nDate:", wedding_date_d , wedding_date_m , wedding_date_y ,"\nTotal Budget:", total_budget)
    print(Style.RESET_ALL)
    # Checks with user if inputs are correct
    confirm = input("Are these details correct? Please type 'y' or 'n': ")
    if confirm == "n":
        print("Okay, let's try again")
        introduction() 
    elif confirm == "y": 
        print(emoji.emojize("Thanks for that:grinning_face_with_smiling_eyes: ", variant="emoji_type"))
        print("There are", diff, "days left till the wedding. Let's get planning!")

def venue():
    pass
