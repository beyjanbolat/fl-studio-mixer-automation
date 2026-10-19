def categorise(name):
    if "Kick" in name:
        return ("Kick", "Drums")
    elif "Hat" in name:
        return ("Hat", "Drums")
    return (name, "unknown")

