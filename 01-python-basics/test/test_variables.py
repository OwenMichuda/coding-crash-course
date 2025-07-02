import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from variables import full_name, age, height, is_right

def test_full_name():
    assert isinstance(full_name, str)
    assert full_name != ""

def test_age():
    assert isinstance(age, int)
    assert age > 0

def test_height():
    assert isinstance(height, float)
    assert 0.5 < height < 3.0

def test_is_right():
    assert isinstance(is_right, bool)