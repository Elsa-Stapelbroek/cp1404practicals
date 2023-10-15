"""
CP1404/CP5632 Practical 5 - Intermediate exercise
Hex colour-codes in a dictionary
https://www.color-hex.com/color-names.html
"""
NAME_TO_CODE = {"cadmium orange": "#ed872d", "international orange": "#ff4f00", "light orange": "#fed8b1",
                "orange (crayola)": "#ff5800", "orange peel": "#ff9f00", "orange soda": "#fa5b3d",
                "outrageous orange": "#ff6e4a", "persian orange": "#d99058", "portland orange": "#ff5a36",
                "red orange": "#ff5349", "burnt orange": "#cc5500", "carrot orange": "#ed9121",
                "spanish orange": "#e86100", "tart orange": "#fb4d46", "yellow orange": "#ffae42"}
# orange you glad I left out the other oranges?

name = input("Colour name: ").lower()
while name != '':
    try:
        print(NAME_TO_CODE[name])
    except KeyError:
        print("Invalid colour!")
    name = input("Colour name: ").lower()
