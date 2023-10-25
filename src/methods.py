import emoji
from colorama import Fore, Back, Style
import datetime 

def confirm_yesno():
    response = None   
    while response is None:     
        try: 
            response = input(" Please type 'y' or 'n': ").lower() 
            if  response !='y' and response !='n':
                raise ValueError      
        except ValueError:
            response = None
            print("try again")
    return response
   
 

def get_details(): 
    user_name = input("Please enter your name: ")
    
    wedding_date_y = int(input("Please enter the year of the wedding (yyyy): "))   
    wedding_date_m = int(input("Please enter the month of the wedding (mm): "))
    wedding_date_d = int(input("Please enter the day of the wedding (dd): "))

  
    # calculates total days till wedding
    today_date = datetime.date.today()
    wedding_date = datetime.date(wedding_date_y, wedding_date_m, wedding_date_d)
    diff = (wedding_date-today_date).days
   
    total_budget = int(input("Enter your budget: "))
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
            f.write("Name:")
            f.write(user_name)
            f.write("\nDate of Wedding: ")
            f.write(str(wedding_date))
            f.write('\n')
            f.write(str(diff))
            f.write(" days until the wedding!")
            f.write('\n \n')
            f.write("BUDGET PLAN")
    return total_budget

 
def confirm_choice():
    choice = None   
    while choice is None:     
        try: 
            choice = input("Please enter 'A' or 'B' or 'C' or 'D' or 'E': ").upper()
            if  choice !='A' and choice !='B' and choice !='C' and choice !='D' and choice !='E':
                raise ValueError      
        except ValueError:
            choice = None
            print("Invalid input, please type 'A' or 'B' or 'C' or 'D' or 'E'")
    return choice
