import random

# Startvärdena väljer du själv.
spelare_hp = 100
fiende_hp = 80

# Ditt första kort börjar här.
spelare_namn = input("Vad heter du?")

print("Du vaknar i en öken mitt i ingenstans. Hur kom du hit? Varför är du här? Vad ska du göra nu? Är några frågor som du ställer dig själv.")
print("Du ser ett gäng skorpioner gå på led åt samma håll och bestämmer dig för att följa efter. Utan att du märker går du in i en grotta och med en smäll blockeras ingången")
print("???: Ser man på, vad har mina skorpioner släpat hit idag då? Det spelar ingen roll vem du är, skorpioner, attackera dem!!\n    Ajdå.\n Innan skorpionerna når dig hittar du ett bortglömt svärd att använda.")

while True:
    print(f"{spelare_namn}{spelare_hp} VS Skorpion {fiende_hp}")
    fråga = input("Vad gör du nu? 1. Slåss       2. Hela     3. Fly").lower()
    if fråga == 3 or "fly":
    