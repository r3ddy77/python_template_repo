from core.logic import oblicz_wynik

def test_oblicz_wynik():
    assert oblicz_wynik(2, 3) == 5
    assert oblicz_wynik(-1, 1) == 0