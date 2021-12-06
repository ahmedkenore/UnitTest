import pytest
@pytest.mark.numbers
def test_add():
     assert 1 + 3 == 4
 
@pytest.mark.numbers
def test_mult():
     assert 8*2 == 16
 
@pytest.mark.strings
def test_startswith():
     assert "abcd".startswith("a")
 
@pytest.mark.strings
def test_endsswith():
     assert "abcd".endswith("d")