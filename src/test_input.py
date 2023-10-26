from weddingitems import WeddingItems, Venue, Florist, Dress, PhotoVideo

import pytest

# TEST ONE: Testing the get_recc function to see that user input is drawing the
# correct data from the csv file


# Testing to see that once venue instance is created, if the user inputs A for
# get_recc function, the correct data is returned, in this case option A is
# LuxeCraves which costs 10,000
def test_get_recc_venue(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "A")
    venue = Venue("venue")
    result = venue.get_recc()
    assert result == ("LuxeCraves", 10000)


# Testing to see that once Dress instance is created, if user inputs option C
# for get_recc function, the correct data is returned, in this case option C
# is BlancCouture which costs 5000
def test_get_recc_dress(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "C")
    dress = Dress("dress")
    result = dress.get_recc()
    assert result == ("BlancCouture", 5000)


# TEST TWO: Testing to see that ask.user function will
# return user input for supplied vendors (i.e if they answer 'y' to
# "do you have a vendor?",their inputed vendor will be returned)

# Testing to see that when user decides to add their own vendor to
# 'Florist', in this case they enter 'y' to own vendor
# and 'Rose' to name of vendor and '1000' for cost of vendor,
# the function will return "Rose" and "1000"
def test_ask_user(monkeypatch):
    inputs = iter(['y', 'Rose', 1000])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    flower = Florist("florist")
    result = flower.ask_user()
    assert result == ("Rose", 1000)


# Testing to see that when user decides
def test_ask_user_y(monkeypatch):
    inputs = iter(['y', 'SnapShot', 2000])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    photo = PhotoVideo("photographer and videographer")
    result = photo.ask_user()
    assert result == ("SnapShot", 2000)


# TEST THREE: # Testing creating new instances of WeddingItems
# class will produce a result (i.e will not return nothing).

# Creating instances of WeddingItems with item_type Car will
# result in item.type of the newItem = Car

testItem = [
        {'item_type': 'Car'}

           ]


@pytest.mark.parametrize('itemData', testItem)
def test_item_creation(itemData):
    newItem = WeddingItems(itemData.get('item_type'))
    assert newItem.item_type == 'Car'
