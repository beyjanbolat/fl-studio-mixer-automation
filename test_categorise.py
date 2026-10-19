from categorise import categorise

def test_kick():
    assert categorise("ThaiKick_01_SP") == ("Kick", "Drums")


def test_unknown():
    assert categorise("Serum") == ("Serum", "unknown")