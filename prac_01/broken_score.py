"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# score must be [0,100], >=90 is excellent, >=50 is pass, <50 is bad

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")
