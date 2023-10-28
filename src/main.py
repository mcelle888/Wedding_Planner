from pyfiglet import Figlet
import emoji
from colorama import Fore, Style
from methods import get_details
import subprocess
import datetime
from weddingitems import (Venue, Florist, Food, Decoration,
                          MakeupHair, PhotoVideo, Dress, Cake, Ring)


# Opening App (Intro)
f = Figlet(font='contessa')
print(f.renderText('~~~ Congratulations! ~~~'))
print(emoji.emojize("Congrats on your engagement:red_heart: ",
                    variant="emoji_type"))
print("Let's get you started on some planning!")

# Get basic user's basic information
user_details = get_details()


# Venue input
venue_object = Venue("venue")
venue_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{venue_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nVenue Name: ")
    f.write(venue_object.name)
    f.write("\nVenue Cost: $") 
    f.write(str(venue_object.cost))
    f.write("\n\n")

# Florist input
florist_object = Florist("florist")
florist_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{florist_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nFlorist Name: ")
    f.write(florist_object.name)
    f.write("\nFlorist Cost: $")
    f.write(str(florist_object.cost))
    f.write("\n\n")

# Catering input
food_object = Food("caterer")
food_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{food_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nCaterer Name: ")
    f.write(food_object.name) 
    f.write("\nCaterer Cost: $")
    f.write(str(food_object.cost))
    f.write("\n\n")

# Decor input
decoration_object = Decoration("event decorater")
decoration_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{decoration_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nDecor Name: ")
    f.write(decoration_object.name) 
    f.write("\nDecor Cost: $")
    f.write(str(decoration_object.cost))
    f.write("\n\n")

# Beauty service input
makeup_hair_object = MakeupHair("make up and hair stylist")
makeup_hair_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{makeup_hair_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nBeauty Service Name: ")
    f.write(makeup_hair_object.name) 
    f.write("\nBeauty Service Cost: $")
    f.write(str(makeup_hair_object.cost))
    f.write("\n\n")

# Photographer and Videographer input
photo_video_object = PhotoVideo("photographer and videographer")
photo_video_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{photo_video_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nPhotographer and Videographer Name: ")
    f.write(photo_video_object.name) 
    f.write("\nPhotographer and Videographer Cost: $")
    f.write(str(photo_video_object.cost))
    f.write("\n\n")

# Dress input
dress_object = Dress("dress and suit merchant ")
dress_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{dress_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nDress Shop Name: ")
    f.write(dress_object.name) 
    f.write("\nDress Cost: $")
    f.write(str(dress_object.cost))
    f.write("\n\n")

# Cake input
cake_object = Cake("cake shop ")
cake_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{cake_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nCake Shop Name: ")
    f.write(cake_object.name) 
    f.write("\nCake Cost: $")
    f.write(str(cake_object.cost))
    f.write("\n\n")

# Ring input
ring_object = Ring("wedding ring shop")
ring_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{ring_object.__dict__}")
with open('weddingplan.txt', 'a') as f:
    f.write("\nRing Shop Name: ")
    f.write(ring_object.name) 
    f.write("\nRing Cost: $")
    f.write(str(ring_object.cost))
    f.write("\n\n")
    f.write("~ BUDGET ~ \n\n")
   

print(Style.RESET_ALL)

# Ending message with final budget
print(emoji.emojize(
    "All done! Thank you for that :smiling_face_with_smiling_eyes:",
    variant="emoji_type"
    ))

# Budget Calculator for wedding plan
totalcost = (
            int(venue_object.cost) 
            + int(florist_object.cost) 
            + int(food_object.cost) 
            + int(decoration_object.cost) 
            + int(makeup_hair_object.cost) 
            + int(photo_video_object.cost)
            + int(dress_object.cost) 
            + int(cake_object.cost) 
            + int(ring_object.cost)
            )

difference = user_details[0] - totalcost

print(Fore.LIGHTMAGENTA_EX 
      + f"Your budget was $ {user_details[0]}")
print(f"Your estimated cost is $ {totalcost}")
if totalcost <= user_details[0]: 
    print(f"You are within your budget! You have excess $ {difference}")
else:
    print(f"You are over your budget! You have to cut $ {difference * - 1}")          
print(Style.RESET_ALL)

# Printing message

print(emoji.emojize("Now let's print out a plan for you :party_popper:", 
                    variant="emoji_type"))

if totalcost <= user_details[0]:
    with open('weddingplan.txt', 'a') as f:
        f.write("Your total budget was: $ ")
        f.write(str(user_details[0]))
        f.write("\n")
        f.write("Your total estimated cost comes to: $ ")
        f.write(str(totalcost))
        f.write("\n")
        f.write("You are within your budget! You have excess $ ")
        f.write(str((user_details[0] - totalcost)))
        f.write(" to spend!")
else:
    with open('weddingplan.txt', 'a') as f:
        f.write("Your total budget was: $ ")
        f.write(str(user_details[0]))
        f.write("\n")
        f.write("Your total estimated cost comes to: $ ")
        f.write(str(totalcost))
        f.write("\n")
        f.write("You are over your budget! You need to cut $ ")
        f.write(str((totalcost - user_details[0])))
        f.write(" out!\n\n")

# Calculates and prints scheduled to do list 

task_one = (round(user_details[1] * 0.1))
task_two = (round(user_details[1] * 0.25))
task_three = (round(user_details[1] * 0.4))
task_four = (round(user_details[1] * 0.6))
task_five = (round(user_details[1] * 0.7))
task_six = (round(user_details[1] * 0.8))
task_seven = (round(user_details[1] * 0.9))
task_eight = (round(user_details[1] * 1))

today = datetime.date.today()
end_date_one = (today + datetime.timedelta(days=task_one)).strftime("%Y-%m-%d")
end_date_two = (today + datetime.timedelta(days=task_two)).strftime("%Y-%m-%d")
end_date_three = (today + datetime.timedelta(days=task_three)).strftime("%Y-%m-%d")
end_date_four = (today + datetime.timedelta(days=task_four)).strftime("%Y-%m-%d")
end_date_five = (today + datetime.timedelta(days=task_five)).strftime("%Y-%m-%d")
end_date_six = (today + datetime.timedelta(days=task_six)).strftime("%Y-%m-%d")
end_date_seven = (today + datetime.timedelta(days=task_seven)).strftime("%Y-%m-%d")
end_date_eight = (today + datetime.timedelta(days = task_eight)).strftime("%Y-%m-%d")

with open('weddingplan.txt', 'a') as f:
    f.write("\n\n ~ PLANNING CHECKLIST ~\n\n")
    f.write(end_date_one)
    f.write("\n")
    f.write("Start looking for vendors\n\n")
    f.write(end_date_two)
    f.write("\n")
    f.write("Hire/Book all suppliers and vendors\n\n")
    f.write(end_date_three)
    f.write("\n")
    f.write("Send out invitations\n\n")
    f.write(end_date_four)
    f.write("\n")
    f.write("Food Tasting\n")
    f.write("Call vendors to confirm\n\n")
    f.write(end_date_five)
    f.write("\n")
    f.write("Hair and Makeup Trial\n")
    f.write("Dress collection and last alterations\n\n")
    f.write(end_date_six)
    f.write("\n")
    f.write("Organise Final payments for vendors\n")
    f.write("Final guest count and plean table arrangements\n")
    f.write("Plan accommadation and transport\n\n")
    f.write(end_date_seven)
    f.write("\n")
    f.write("Ceremony and Reception rehearsals\n\n")
    f.write(end_date_eight)
    f.write("\n")
    f.write("D-DAY: GET MARRIED!")



# Opens a text file of the wedding plan for the user to save
subprocess.call(['notepad.exe', 'weddingplan.txt'])

print(emoji.emojize("""Thanks for using the Wedding App :smiling_face_with_hearts:"""
                    """\nHappy planning!:confetti_ball:""", variant = "emoji_type"))