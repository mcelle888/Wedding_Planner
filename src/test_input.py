from methods import confirm_choice, guestcount, enter_year, enter_month, enter_budget
from weddingitems import WeddingItems, Venue, Florist

import pytest 

# tests that the user has inputed a valid date 

# def test():
#         assert confirm_choice() == "A" or "B" or "C" or "D" or "E"

   
    
def test_one(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "A")
        venue = Venue("venue")
        result = venue.get_recc()
        assert result == ("LuxeCraves", 10000)

def test_two (monkeypatch):
        inputs = iter(['y','Rose', 1000])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        flower = Florist("florist")
        result = flower.ask_user()
        assert result == ("Rose", 1000)

def test_three(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "B")
        result = confirm_choice()
        assert result == "B"

# def test_three(monkeypatch):
#         monkeypatch.setattr('builtins.input', lambda _: "500")
#         result = guestcount()
#         assert result == 500


# Testing WeddingItems class will create new instance 
testItem = [
        {'item_type': 'Car'},
        {'item_type': 'Favour'}
]
@pytest.mark.parametrize('itemData', testItem)
def test_item_creation(itemData):
        newItem = WeddingItems(itemData.get('item_type'))
        assert newItem.item_type != ''


