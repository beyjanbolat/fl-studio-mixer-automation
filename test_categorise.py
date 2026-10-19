from categorise import categorise

def test_kick():
    assert categorise("ThaiKick_01_SP") == ("Kick", "Drums")


def test_unknown():
    assert categorise("Serum") == ("Serum", "unknown")


def test_hat_loop():
    assert categorise("Hat LOOP 91 BPM") == ("Hat", "Drums")

def test_hat_loop_uppercase():
    assert categorise("HAT LOOP 91 BPM") == ("Hat", "Drums")