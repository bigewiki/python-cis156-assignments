#!/usr/bin/env python3

from datetime import date, datetime, timedelta
import re

def get_invoice_date():
    while True:
        # updated to use output expected 4 digit year
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")
        # match for the expected format
        if re.match(r'^\d\d\/\d\d\/\d\d\d\d$',invoice_date_str):
            # just in case they use an invalid date that matches the format
            try:
                # updated to use year with century (4 digit year)  
                invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y")
                return invoice_date.date()
            except:
                print("Invalid date, please try again with (MM/DD/YYYY) format")
        else:
            print('Invalid date format, please use (MM/DD/YYYY)')

def main():
    print("The Invoice Due Date program")
    print()

    while True:
        invoice_date = get_invoice_date()
        print()

        # moved current_date up higher since we can use it to check if the invoice date
        # is today or earlier
        current_date = datetime.now().date()

        if(invoice_date >= current_date):
            print('Invoice date must be earlier than today or earlier. Please try again. ')
            continue

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        days_overdue = (current_date - due_date).days

        # display results
        print("Invoice Date: " + invoice_date.strftime("%B %d, %Y"))
        print("Due Date:     " + due_date.strftime("%B %d, %Y"))
        print("Current Date: " + current_date.strftime("%B %d, %Y"))
        if days_overdue > 0:
            print("This invoice is", days_overdue, "day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print("This invoice is due in", days_due, "day(s).")
        print()

        # ask if user wants to continue
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break      

if __name__ == "__main__":
    main()
