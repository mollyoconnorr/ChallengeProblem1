"""
Montana Counties License Plate Lookup

Author: Molly O'Connor
Date: 1/22/2026
Description:
    This program allows users to look up Montana counties based on
    the numeric license plate prefix. Users can query any valid
    prefix (1-56) and choose whether to display the County name,
    the County seat, or both. The program reads county data from
    a CSV file and stores it in a dictionary for fast lookup.
"""

import csv

# Load Montana county data into a dictionary

# Dictionary structure: {prefix: (county_name, county_seat)}
# Advantages:
# - Fast lookups O(1)
# - Ensures prefixes are unique
# - Scales well if dataset grows

counties = {}

with open("MontanaCounties.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        county = row["county"]
        county_seat = row["county_seat"]
        prefix = int(row["prefix"])
        counties[prefix] = (county, county_seat)

# Introduction to user
print("Do you want to learn about your Montana Counties?")
print("Sounds like SOOO much fun... right?")
print("If you have better things to do we understand")

# Ask user if they want to play
stillPlaying = True
while True:
    user_input = input("Ready to play? (type y/n): ").lower()
    if user_input not in ("y", "n"):
        print("Invalid input. Please type 'y' or 'n'.")
        continue
    elif user_input == "n":
        stillPlaying = False
        break
    elif user_input == "y":
        break

# Main loop: ask for prefix and display info
while stillPlaying:
    while True:
        # Prompt for license plate prefix
        user_input = input("Please enter a number (1-56) or type 'x' to exit: ").lower()

        # Exit condition
        if user_input == "x":
            stillPlaying = False
            break

        # Validate numeric input
        try:
            prefix = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'x' to exit.")
            continue

        # Validate range
        if prefix < 1 or prefix > 56:
            print("Enter a number between 1-56, there are only 56 counties!")
            continue

        # Valid prefix: look up county and seat
        county, seat = counties[prefix]

        # Ask user what info they want
        while True:
            choice = input("What information would you like? County ('c'), Seat ('s'), or Both ('b'): ").lower()
            if choice == "c":
                print(f'License plate prefix number {prefix}')
                print(f'County: {county}')
                break
            elif choice == "s":
                print(f'License plate prefix number {prefix}')
                print(f'County Seat: {seat}')
                break
            elif choice == "b":
                print(f'License plate prefix number {prefix}')
                print(f'County: {county} --- County Seat: {seat}')
                break
            else:
                print("Invalid choice. Please type 'c', 's', or 'b'.")

        # Exit inner loop to allow new prefix query
        break

# End of program
print("Thanks! Have a good day.")
