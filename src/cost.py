
def get_recc():
    pass



class WeddingItems:
    name = None
    cost = None
    has_vendor = False
    def ask_user():
        confirm = input("Have you chosen a venue? Please enter 'y' or 'n': ")
        if confirm == "y":
            has_vendor = True
            name = input("Please enter your venue name: ") 
            venue_cost =("Please enter your venue cost:")
        elif confirm == "n":
            get_recc()
    def get_recc():
        pass

def cost_input():

    confirm = input("Have you chosen a venue? Please enter 'y' or 'n': ")
    if confirm == "y":
        chosen_venue = input("Please enter your venue name: ") 
        venue_cost =("Please enter your venue cost:")
    elif confirm == "n":
        pass

    confirm1 = input ("Have you chosen a catering service? Please enter 'y' or 'n': ")
    if confirm1 == "y":
        chosen_food = input("Please enter your catering name: ") 
        food_cost =("Please enter your catering cost")
    elif confirm1 == "n":
        pass

    
    confirm3 = input ("Have you chosen a florist? Please enter 'y' or 'n': ")
    if confirm3 == "y":
        chosen_food = input("Please enter your florists name: ") 
        food_cost =("Please enter your florists cost")
    elif confirm3 == "n":
        pass


    venue = WeddingItems(chosen_venue, venue_cost)
    catering = WeddingItems(chosen_food, food_cost)
    florist = WeddingItems(chosen_flower, flower_cost)
    decoration = WeddingItems(chosen_deco, deco_cost) 
    beauty = WeddingItems(chosen_beauty, beauty_cost)
    photo = WeddingItems(chosen_photo, photo_cost)
    dress = WeddingItems(chosen_dress, dress_cost)
    cake = WeddingItems(chosen_cake, cake_cost)


a = [florist, "catering", "venue"]
b = []
c = [] 

for item in a: 
    answer = input ("Have you chosen a {item} ? Please enter 'y' or 'n': ")
    if answer == "y":
        b.append(input("Please enter your {item} name: "))
        c.append(("Please enter your {item} cost:"))
    elif answer == "n":
        chosen = "name"
        chosen_cost = 150
    venue = WeddingItems(chosen_venue, venue_cost)

venue = (b[0], c[0])
    




