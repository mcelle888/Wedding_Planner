import csv 
import pandas as pd 
from colorama import Fore, Back, Style
import emoji
 
 
# print((line))
# print((line2)) 
 
# with open("recc.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(" ".join(row))

 
# df = pd.read_csv('recc.csv',
#         sep='[:, |_]',
#         header=0,
#         usecols=["Option", "Name", "Price", "Description"],
#                 nrows=3)

# print(df)

# with open('recc.csv') as f:
#    csv_reader = csv.reader(f)
#    for index, row in enumerate(csv_reader):
#       if index == 1:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
#       elif index == 2:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
#       elif index == 3:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],". It is",row[3])
       
#    print("Option D. Randomly select one for me! \nOption E. Leave blank (an average price of $`15000 will be used to calculate the final cost estimate)")
     

# with open('recc.csv') as f:
#    csv_reader = csv.reader(f)
#    for index, row in enumerate(csv_reader):
#       if index == 5 or index == 6 or index ==7:
#          print("Option", row[0], "is at '", row[1], "' which costs: $",row[2],"pp. They",row[3])
# print("Option D.  Randomly select one for me! \nOption E.  Leave blank (an average price of $`15000 will be used to calculate the final cost estimate)")


# data = {} 
# with open('recc.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)    

# DATAFRAME
# dataFrame = pd.read_csv('recc.csv')
# print("Data",dataFrame)



# wedding_date_y = int(input("Please enter the year of the wedding (yyyy): "))
# result = None
# while result is None:
#     try:    
#         result = int(wedding_date_y)
#     except ValueError:
#         print("Please enter date using numbers")
#     except ValueError:
#         print("Please enter a valid date")
#     # if len(wedding_date_y) > 4:
#     #         raise ValueError("Please enter a valid date")


# result = None 
# while result == None:
#     try:
#         wedding_date_y = int(input("Please enter the year of the wedding (yyyy): "))
#         if (wedding_date_y) != int(wedding_date_y):
#             raise ValueError
#     except ValueError:
#         print ("Must enter a number, please try again")
#     # return wedding_date_y
 

# def get_date():
    
#     result = None
#     while result is None:
#         try:
#             wedding_date_y = int(input("Please enter the year of the wedding (yyyy): "))   
#             wedding_date_m = int(input("Please enter the month of the wedding (mm): "))
#             wedding_date_d = int(input("Please enter the day of the wedding (dd): "))
#             if wedding_date_y != int(wedding_date_y):
#                 raise ValueError
#             if wedding_date_m != int(wedding_date_m):
#                 raise ValueError
#             if wedding_date_d != int(wedding_date_d):
#                 raise ValueError
#         except ValueError:
#             print ("Must enter a number, please try again")
#         return result
    
# get_date()
 
# def confirm():
    
#     answer = None
#     while answer is None:
#         response = input("Are these details correct? Please type 'y' or 'n': ")
#     try:     
#         answer = response 
#     except ValueError:
#         print("Please type 'y' or 'n")
 
#     return answer
# confirm()





# while True:
#     try:
#         confirm = input("Are these details correct? Please type 'y' or 'n': ").lower()
#         if confirm !='y' or confirm !='n':
#             raise ValueError
#     except ValueError:
#         print("Please type 'y' or 'n")


# confirm = input("Are these details correct? Please type 'y' or 'n': ")
# try:
#     if confirm !='y' or confirm !='n':
#         raise ValueError  
# except ValueError as error:
#     print("try again")
 

# def confirm_yesno():
#     response = None   
#     while response is None:     
#         try: 
#             response = input("Are these details correct? Please type 'y' or 'n': ") 
#             if  response !='y' and response !='n':
#                 raise ValueError      
#         except ValueError:
#             response = None
#             print("try again")
#     return response

 
# # confirm_yesno()
# #print(confirm_yesno())






# class WeddingItems:
#     name = None
#     cost = None
#     def __init__(self,item_type):
#         self.item_type = item_type
#     def ask_user(self):
#         confirm = confirm_wedding_item (self.item_type)
#         print(Style.RESET_ALL)
#         if confirm == "y":
#             self.name = input(f"Please enter your {self.item_type} name: ") 
#             self.cost = confirm_cost(self.item_type)          
#         elif confirm == "n":
#             self.get_recc()

# def confirm_wedding_item(item_type):
#     response = None   
#     while response is None:     
#         try: 
#             response = input(Fore.RED + f"Have you chosen a {item_type}? Please enter 'y' or 'n' ")
#             if  response !='y' and response !='n':
#                 raise ValueError      
#         except ValueError:
#             response = None
#             print("Please enter 'y' or 'n' ")
#     return response


# def confirm_cost(item_type):
#     response = None
#     while response is None:
       
#         try:
#             response = input(f"Please enter your {item_type} cost: ") 
#             response = int(response)
#         except ValueError:
#             response = None
#             print("wrong")
#     return response

# newitem = WeddingItems("venue")
# newitem.ask_user()


# def enter_budget():
#     response = None
#     while response is None:
#         response = input("Please enter your budget: ") 
#         try:
#             response = int(response)
#         except ValueError:
#             response = None
#             print(Fore.RED + "Invalid input, please enter a number for your budget")
#             print(Style.RESET_ALL)
#     return response
import datetime

# def enter_day():
#     response = None
#     while response is None:
#         response = (input("Please enter the day of the wedding (dd): "))
#         try:
#             if response == int(response):
#                raise ValueError
            
#             if int(response) > 31 or int(response) < 1:
#                 raise ValueError     
#         except ValueError:
#             response = None
#             print(Fore.RED + "Invalid input, please enter a number value for the day")
#             print(Style.RESET_ALL)
#     return response
     
# print(enter_day())
# wedding_date_y = int(input("Please enter the year of the wedding (yyyy): "))   
# wedding_date_m = int(input("Please enter the month of the wedding (mm): "))
# wedding_date_d = int(input("Please enter the day of the wedding (dd): "))


# calculates total days till wedding
# today_date = datetime.date.today()
# wedding_date = datetime.date(wedding_date_y, wedding_date_m, wedding_date_d)
# diff = (wedding_date-today_date).days

# def enter_year():
#     response = None
#     while response is None:
#         response = (input("Please enter the year of the wedding (yyyy): "))  
#         try:
#             if response == int(response):
#                 raise ValueError
            
#             if len(response) != 4:
#                 raise ValueError
            
#             if int(response) < datetime.date.today().year:
#                 raise ValueError
            
#         except ValueError:
#             response = None
#             print(Fore.RED + "Invalid input, please enter a 4 digit number for a future date")
#             print(Style.RESET_ALL)
#     return response

# enter_year()
 