from methods import confirm_choice, guestcount, enter_year

import pytest 

# tests that the user has inputed a valid date 

# def test():
#         assert confirm_choice() == "A" or "B" or "C" or "D" or "E"

   
    
def test_one(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "A")
        result = confirm_choice()
        assert result == "A"

def test_two(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "B")
        result = confirm_choice()
        assert result == "B"

def test_three(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "500")
        result = guestcount()
        assert result == 500

# def test_four(monkeypatch):
#     with pytest.raises(ValueError):        
#         enter_year()
#         monkeypatch.setattr('builtins.input', lambda _: "45")

# def test_five(monkeypatch):
#         monkeypatch.setattr('builtins.input', lambda _: "2024")
#         result = enter_year()
#         assert result == "2024"


 