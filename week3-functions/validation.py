#!/usr/bin/env python3

def get_float(prompt, low_val, high_val):
    # Function will loop until it returns a valid float
    while True:
        prompt_input = float(input(prompt))
        if prompt_input > low_val and prompt_input <= high_val:
            return prompt_input
        else:
            print(
                f'Entry must be greater than {low_val} and less than or equal to {high_val}')


def get_int(prompt, low_val, high_val):
    # Function will loop until it returns a valid integer
    while True:
        prompt_input = int(input(prompt))
        if prompt_input > low_val and prompt_input <= high_val:
            return prompt_input
        else:
            print(
                f'Entry must be greater than {low_val} and less than or equal to {high_val}')


def main():
    choice = "y"
    while choice.lower() == "y":
        # testing
        get_float("Enter a float: ", 0, 100)
        get_int("Enter an integer: ", 0, 100)
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
