from pyfiglet import Figlet
import emoji
from colorama import Fore, Back, Style
import datetime 
from methods import get_details
from weddingitems import WeddingItems, Venue, Florist, Food, Decoration, MakeupHair, PhotoVideo, Dress, Cake, Ring 

# Opening App (Intro)
f = Figlet(font='contessa')
print(f.renderText('~~~ Congratulations! ~~~'))
print(emoji.emojize("Congrats on your engagement:red_heart:  Let's get you started on some planning!", variant="emoji_type"))

# Get basic user's basic information
budget = get_details()

# Venue input
venue_object = Venue("venue")
venue_object.ask_user()
print(Fore.BLUE + f"{venue_object.__dict__}") 
totalcost = int(venue_object.cost)
print(totalcost)
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
totalcost = int(venue_object.cost) + int(florist_object.cost)
print(totalcost)
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
totalcost = int(venue_object.cost) + int(florist_object.cost) + int(food_object.cost)
print(totalcost)
with open('weddingplan.txt', 'a') as f:
    f.write("\nCaterer Name: ")
    f.write(food_object.name) 
    f.write("\nCaterer Cost: $")
    f.write(str(food_object.cost))
    f.write("\n\n")

# Decor input
decoration_object = Decoration("event decorater ")
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
photo_video_object = PhotoVideo("photographer and videographer ")
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
    f.write("BUDGET")
    f.write("\n\n")

print(Style.RESET_ALL)

# Ending message
print(emoji.emojize("All done! Thank you for that :smiling_face_with_smiling_eyes:", variant="emoji_type"))
print(emoji.emojize("Now let's print out a plan for you :party_popper:", variant="emoji_type"))

# Budget Calculator for wedding plan

totalcost = int(venue_object.cost) + int(florist_object.cost) + int(food_object.cost)+ int(decoration_object.cost) + int(makeup_hair_object.cost)+ int(photo_video_object.cost) + int(dress_object.cost) + int(cake_object.cost) + int(ring_object.cost) 
print(totalcost) 
if totalcost <= budget:
    with open('weddingplan.txt', 'a') as f:
        f.write("Your total budget was: $ ")
        f.write(str(budget))
        f.write("\n")
        f.write("Your total estimated cost comes to: $ ")
        f.write(str(totalcost))
        f.write("\n")
        f.write("You are within your budget! You have excess $ ")
        f.write(str((budget - totalcost)))
        f.write(" to spend!")
else:
    with open('weddingplan.txt', 'a') as f:
        f.write("Your total budget was: $ ")
        f.write(str(budget))
        f.write("\n")
        f.write("Your total estimated cost comes to: $ ")
        f.write(str(totalcost))
        f.write("\n")
        f.write("You are over your budget! You need to cut $ ")
        f.write(str((totalcost - budget)))
        f.write(" out!")
   