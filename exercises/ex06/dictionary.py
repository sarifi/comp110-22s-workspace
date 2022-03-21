"""Test subjects with dictionaries."""

__author__ = "730480631"   


def invert(inv: dict[str, str]) -> dict[str, str]: 
    """Inverts and returns the input."""
    empty: dict[str, str] = {} 
    for key in inv: 
        if inv[key] in empty: 
            raise KeyError("Same Key")
        value: str = inv[key] 
        empty[value] = key 
    return empty


def favorite_color(color: dict[str, str]) -> str: 
    """Returns the most common color(favorite color)."""
    fav: str = ""  
    number: dict[str, int] = {}
    for key in color:
        if color[key] in number: 
            number[color[key]] += 1 
        else:
            number[color[key]] = 1
    max: int = 0
    for key in number: 
        if number[key] > max: 
            max = number[key]
            fav = key 
    return fav 


def count(input: list[str]) -> dict[str, int]: 
    """Counts the number of items listed."""
    stored: dict[str, int] = {}
    i: int = 0
    while i < len(input): 
        if input[i] in stored: 
            stored[input[i]] += 1 
        else: 
            stored[input[i]] = 1 
        i += 1 
    return stored 