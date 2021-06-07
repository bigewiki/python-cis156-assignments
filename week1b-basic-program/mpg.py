#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon:\t\t"))

# calculate miles per gallon
mpg = round(miles_driven / gallons_used, 1)
# mpg = round(mpg, 1)

# calculate total cost of gas
total_cost = round(float(cost_per_gallon * gallons_used), 1)

#calculate cost per mile
cost_per_mile = round(float(cost_per_gallon / mpg), 1)
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print("Total Gas Cost:\t\t\t" + str(total_cost))
print("Cost Per Mile:\t\t\t" + str(cost_per_mile))
print()
print("Bye")


