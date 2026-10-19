def categorise(name):
    small = name.lower()
    if "kick" in small:
        return ("Kick", "Drums")
    elif "hat" in small:
        return ("Hat", "Drums")
    return (name, "unknown")

