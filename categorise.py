Drums = ["Kick", "Hat", "Snare", "Rim", "Ride", "Cymbal"]

def categorise(name):
    for Drum in Drums:
        small = name.lower()
        if Drum.lower() in small:
            return (Drum, "Drums")
    return (name, "unknown")