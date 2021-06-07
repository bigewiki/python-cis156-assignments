#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon application")
print()

# choice must be "y" to continue - initializing here
choice = "y"

# our while statement controlled by the var choice
while choice.lower() == "y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))

    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        print()

        # calculate and display miles per gallon
        mpg = round((miles_driven / gallons_used), 2)
        print("Miles Per Gallon:        ", mpg)

        # calculate and display total gas cost
        total_gas_cost = round(gallons_used * cost_per_gallon, 1)
        print("Total Gas Cost:          ", total_gas_cost)

        # calculate and display cost per mile
        cost_per_mile = round(cost_per_gallon / mpg, 1)
        print("Cost Per Mile:           ", cost_per_mile)

        print()

        # prompt the user to continue or exit
        choice = input("Get entries for another trip (y/n)? ")

print()
print("Bye")
