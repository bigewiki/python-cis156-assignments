#!/usr/bin/env python3

# Step 4: import csv module
import csv

def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))                    
        if miles_driven > 0:       
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
    
def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))                    
        if gallons_used > 0:       
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue
        
def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    # Step 3: add the entries into 2-dimensional list
    # initialize the list
    mpg_values = []

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        # Step 3: append to list
        mpg_values.append([miles_driven, gallons_used, mpg])
        print("Miles Per Gallon:\t" + str(mpg))
        print()
        
        more = input("More entries? (y or n): ")
    # Step 4: write to csv file
    with open("trips.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(mpg_values)
    print("Bye")

if __name__ == "__main__":
    main()

