from fakeapp import fakeapp
import pytest

def test_main():
    print(fakeapp)
    assert fakeapp.fake() == 'a'
