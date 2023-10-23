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

class venue(WeddingItems):
    def get_recc(self):
        print("Here are some recommendations for you")


venueObject = venue("venue")
venueObject.ask_user()
print(venueObject.name)
print(venueObject.cost)


class florist (WeddingItems):
    def get_recc(self):
        print("Here are some recommendations")

floristObject = florist("florist")
floristObject.ask_user()
print(floristObject.name)
print(floristObject.cost)    