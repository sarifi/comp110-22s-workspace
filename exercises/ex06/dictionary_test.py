"""Unit tests for function in dictionary.py."""


__author__ = "730480631"   

from dictionary import invert
from dictionary import count
from dictionary import favorite_color   


def test_invert_one() -> None: 
    """Test one for invert."""
    inv: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(inv) == {'z': 'a', 'y': 'b', 'x': 'c'}  


def test_invert_two() -> None: 
    """Test two for invert."""
    inv: dict[str, str] = {'apple': 'cat'}
    assert invert(inv) == {'cat': 'apple'}


def test_invert_three() -> None: 
    """Test three for invert."""
    inv: dict[str, str] = {}
    assert invert(inv) == {}


def test_favorite_color_one() -> None: 
    """Test one for favorite color."""
    fav: dict[str, str] = {'sahra': 'green', 'lillian': 'pink', 'Mia': 'green', 'lauren': 'green'}
    assert favorite_color(fav) == 'green'


def test_favorite_color_two() -> None: 
    """Test one for favorite color."""
    fav: dict[str, str] = {"sahra": "green", "lillian": "yellow", "bintou": "yellow"}
    assert favorite_color(fav) == "yellow"


def test_favorite_color_three() -> None: 
    """Test one for favorite color."""
    fav: dict[str, str] = {}
    assert favorite_color(fav) == "" 


def test_count_one() -> None: 
    """Test one for count."""
    stored: list[str] = ["1", "1", "2"]
    assert count(stored) == {"1": 2, "2": 1}


def test_count_two() -> None: 
    """Test two for count."""
    stored: list[str] = ["5", "4", "5", "4", "20", "10", "5"]
    assert count(stored) == {"5": 3, "4": 2, "20": 1, "10": 1} 


def test_count_three() -> None: 
    """Test three for count."""
    stored: list[str] = []
    assert count(stored) == {} 