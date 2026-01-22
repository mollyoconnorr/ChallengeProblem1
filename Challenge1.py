import csv

# Use a dictionary
# - fast look up times O(1)
# - Ensures prefixes are unique, no duplicates
# - Scales well for future use with potentially bigger datasets
counties = {}

with open("MontanaCounties.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        county = row["county"]
        county_seat = row["county_seat"]
        prefix = int(row["prefix"])

        counties[prefix] = (county, county_seat)

print("Do you want to learn about your Montana Counties?")
print("Sounds like SOOO much fun... right?")
print("If you have better things to do we understand")

stillPlaying = True

while True:
    user_input = input("Ready to play? (type y/n): ").lower()
    if user_input != "y" and user_input != "n":
        print("Invalid input. Please try again.")
        continue
    elif user_input == "n":
        stillPlaying = False
        break
    elif user_input == "y":
        break

while stillPlaying:
    while True:
        just_county = False
        just_seat = False
        user_input = input("Please enter a number (1-56) or type 'x' to be done: ").lower()
        if user_input == "x":
            stillPlaying = False
            break
        try:
            prefix = int(user_input)
        except ValueError:
            print("Not a valid string.")
            continue

        if prefix < 1 or prefix > 56:
            print("Enter a number between 1-56, there are only 56 counties!")
            continue

        elif 0 < prefix < 57:
            county, seat = counties[prefix]
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
                    print(f'County: {county}, County Seat: {seat}')
                    break
                else:
                    print("Invalid choice. Please type 'c', 's', or 'b'")

            break
        else:
            print("Invalid input, please try again!")
            break

print("Thanks! Have a good day.")
