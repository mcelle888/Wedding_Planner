class WeddingItems:
    name = None
    cost = None
    def __init__(self,item_type):
        self.item_type = item_type
    def ask_user(self):
        confirm = input(f"Have you chosen a {self.item_type}? Please enter 'y' or 'n': ")
        if confirm == "y":
            self.name = input(f"Please enter your {self.item_type} name: ") 
            self.cost = input(f"Please enter your {self.item_type} cost:")
        elif confirm == "n":
            self.get_recc()
    # def get_recc():
    #     pass



# Instances of Wedding Items 

# VENUE
class Venue(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you")

venue_object = Venue("venue")
venue_object.ask_user()
print(venue_object.__dict__)
 

# FLORIST
class Florist(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")

florist_object = Florist("florist")
florist_object.ask_user()
print(florist_object.__dict__) 

# CATERING
class Food(WeddingItems):
    def get_recc(self):
        print ("Here are some recommendations for you")

food_object = Food("caterer")
food_object.ask_user()
print(food_object.__dict__)

# DECOR
class Decoration(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")

decoration_object = Decoration("event decorater ")
decoration_object.ask_user()
print(decoration_object.__dict__)

# BEAUTY SERVICES
class MakeupHair(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")

makeup_hair_object = MakeupHair("make up and hair stylist")
makeup_hair_object.ask_user()
print(makeup_hair_object.__dict__)

# PHOTO AND VIDEO
class PhotoVideo(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")
photo_video_object = PhotoVideo("photographer and videographer ")
photo_video_object.ask_user()
print(photo_video_object.__dict__)

# CLOTHES
class Dress(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you ")
dress_object = Dress("dress and suit merchant ")
dress_object.ask_user()
print(dress_object.__dict__)

# CAKE
class Cake(WeddingItems): 
    def get_recc(self):
        print("Here are some recommendations for you")
cake_object = Cake("cake shop ")
cake_object.ask_user()
print(cake_object.__dict__)
