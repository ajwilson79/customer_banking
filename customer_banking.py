# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account and check for valid input.
    while True:
        try:
            savings_balance = float(input('\nEnter your starting savings balance: '))
            if savings_balance < 0:
                raise ValueError("Balance cannot be negative.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input for balance: {e}. Please try again.")

    while True:
        try:
            savings_interest = float(input('Enter the APR for the savings account (as a percentage ex. enter 5 for 5%): '))
            if savings_interest < 0:
                raise ValueError("Interest rate cannot be negative.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input for interest: {e}. Please try again.")

    while True:
        try:
            savings_maturity = int(input('Enter the maturity period for the savings account (in months): '))
            if savings_maturity <= 0:
                raise ValueError("Maturity period must be a positive integer.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input for maturity: {e}. Please try again.")

    # Proceed with the program using the valid inputs

            
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'\nYou have earned: ${interest_earned:,.2f} in interest')
    print(f'Your updated savings balance is: ${updated_savings_balance:,.2f}.')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account and check for valid input.
    while True:
        try:
            cd_balance = float(input('\nEnter your starting cd balance: '))
            if cd_balance < 0:
                raise ValueError("Balance cannot be negative.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input for balance: {e}. Please try again.")

    while True:
        try:
            cd_interest = float(input('Enter the APR for the cd account (as a percentage ex. enter 5 for 5%): '))
            if cd_interest < 0:
                raise ValueError("Interest rate cannot be negative.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input for interest: {e}. Please try again.")

    while True:
        try:
            cd_maturity = int(input('Enter the maturity period for the cd account (in months): '))
            if cd_maturity <= 0:
                raise ValueError("Maturity period must be a positive integer.")
            break  # Exit loop if input is valid
        except ValueError as e:
            print(f"Invalid input for maturity: {e}. Please try again.")

    # Proceed with the program using the valid inputs

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'\nYou have earned: ${interest_earned:,.2f} in interest')
    print(f'Your updated CD balance is: ${updated_cd_balance:,.2f}.\n')

if __name__ == "__main__":
    # Call the main function.
    main()