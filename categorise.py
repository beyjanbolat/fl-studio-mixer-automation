sounds = ["Track 1(consolidated)", "Track 1(consolidated)#2", "Serum", "Track 1(consolidated)", 
          "PL_TS_Snare_One", "CleanHat_01_SP", "DreamyBrazilianHat","LightCrispyRide_01_SP",
          "ThaiKick_01_SP", "HAT LOOP 91 BPM", "Kontakt 7", "Serum #2", "Analog Lab V"]


Drums = ["Kick", "Hat", "Snare", "Rim", "Ride", "Cymbal"]

def categorise(name):
    for Drum in Drums:
        small = name.lower()
        if Drum.lower() in small:
            return (Drum, "Drums")
    return (name, "unknown")