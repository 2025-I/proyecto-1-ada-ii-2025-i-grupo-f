# tests/test_fiesta.py
import pytest
from src.fiesta import saludar

def test_saludar():
    assert saludar("Andrés") == "¡Hola, Andrés!"
    assert saludar("Ana") == "¡Hola, Ana!"