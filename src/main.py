from pyfiglet import Figlet
import emoji
from colorama import Fore, Back, Style
import datetime 
from methods import introduction
from weddingcost import WeddingItems, Venue, Florist, Food, Decoration, MakeupHair, PhotoVideo, Dress, Cake, Ring 

# Opening App
f = Figlet(font='contessa')
print(f.renderText('~~~ Congratulations! ~~~'))
print(emoji.emojize("Congrats on your engagement:red_heart:  Let's get you started on some planning!", variant="emoji_type"))


introduction()

# Venue input
venue_object = Venue("venue")
venue_object.ask_user()
print(Fore.BLUE + f"{venue_object.__dict__}") 

# Florist input
florist_object = Florist("florist")
florist_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{florist_object.__dict__}") 
 
# Catering input
food_object = Food("caterer")
food_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{food_object.__dict__}")

# Decor input
decoration_object = Decoration("event decorater ")
decoration_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{decoration_object.__dict__}")

# Beauty service input
makeup_hair_object = MakeupHair("make up and hair stylist")
makeup_hair_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{makeup_hair_object.__dict__}")

# Photographer and Videographer input
photo_video_object = PhotoVideo("photographer and videographer ")
photo_video_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{photo_video_object.__dict__}")

# Dress input
dress_object = Dress("dress and suit merchant ")
dress_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{dress_object.__dict__}")

# Cake input
cake_object = Cake("cake shop ")
cake_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{cake_object.__dict__}")

# Ring input
ring_object = Ring("wedding ring shop")
ring_object.ask_user()
print(Fore.LIGHTBLUE_EX + f"{ring_object.__dict__}")

print(Style.RESET_ALL)
print(emoji.emojize("Thank you for that :smiling_face_with_smiling_eyes:", variant="emoji_type"))
print("Now let's print out a plan for you!")
