"""Test subjects with lists."""


__author__ = "730480631"  


def only_evens(numbers: list[int]) -> list[int]: 
    """Returns only even numbers."""
    even: list[int] = []
    i: int = 0 
    while i < len(numbers): 
        if numbers[i] % 2 == 0: 
            even.append(numbers[i]) 
        i += 1 
    return even 


def sub(btwn: list[int], start: int, end: int) -> list[int]: 
    """Returns items between first and end index."""
    btwn_numbers: list[int] = []
     
    if start < 0: 
        start = 0 
    if end > len(btwn):
        end = len(btwn)
    # if len(btwn) == 0 or start > len(btwn) or end <= 0: 
    # return btwn_numbers
    i: int = start 
    while i < end: 
        btwn_numbers.append(btwn[i])
        i += 1 
    return btwn_numbers    


def concat(first: list[int], second: list[int]) -> list[int]:  
    """Concatenates two lists."""
    new_list: list[int] = []  
    new_list = first 
    i: int = 0
    while i < len(second): 
        new_list.append(second[i])
        i += 1 
    return new_list 