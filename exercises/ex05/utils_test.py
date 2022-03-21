"""Unit test for functions in utils.py."""


__author__ = "730480631" 

from utils import only_evens
from utils import sub 
from utils import concat


def test_only_even_one() -> None: 
    """Test one for only evens."""
    numbers: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(numbers) == [2, 4, 6] 
 

def test_only_even_two() -> None:
    """Test two fot only evens."""
    numbers: list[int] = [12, 14, 16, 18, 20]
    assert only_evens(numbers) == [12, 14, 16, 18, 20]   


def test_only_even_three() -> None:
    """Test three for only evens."""
    numbers: list[int] = [3, 5, 7, 9, 11]
    assert only_evens(numbers) == [] 


def test_sub_one() -> None:
    """Test one for sub."""
    btwn: list[int] = [20, 30, 40, 50, 60]
    assert sub(btwn, 1, 3) == [30, 40]


def test_sub_two() -> None: 
    """Test two for sub."""
    btwn: list[int] = []
    assert sub(btwn, 1, 2) == [] 


def test_sub_three() -> None: 
    """Test three for sub."""
    btwn: list[int] = [1, 2, 3, 4, 5]
    assert sub(btwn, 5, 6) == [] 


def test_concat_one() -> None: 
    """Test one for concat."""
    first: list[int] = []
    second: list[int] = [1, 2]
    assert concat(first, second,) == [1, 2]


def test_concat_two() -> None: 
    """Test two for concat."""
    first: list[int] = []
    second: list[int] = []
    assert concat(first, second,) == []


def test_concat_three() -> None: 
    """Test three for concat."""
    first: list[int] = [1, 2, 4, 6]
    second: list[int] = [8, 10, 12, 14, 16]
    assert concat(first, second,) == [1, 2, 4, 6, 8, 10, 12, 14, 16]