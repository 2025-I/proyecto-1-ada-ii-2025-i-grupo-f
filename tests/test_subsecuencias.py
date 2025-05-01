# tests/test_subsecuencias.py
import pytest
from src.subsecuencias import encontrar_subsecuencia

def test_encontrar_subsecuencia():
    assert encontrar_subsecuencia([1, 2, 3], [1, 2]) == True
    assert encontrar_subsecuencia([1, 2, 3], [2, 3]) == True
    assert encontrar_subsecuencia([1, 2, 3], [3, 4]) == False