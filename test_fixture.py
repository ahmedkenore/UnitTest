import pytest
@pytest.fixture
def initialisation():
     valeur = 100
     return valeur
 
def test_superieur(initialisation):
     assert 150 > initialisation 
 
def test_inferieur(initialisation):
     assert 50 < initialisation