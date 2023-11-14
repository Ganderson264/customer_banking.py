
class Account:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

class SavingsAccount(Account):
    def __init__(self, balance, interest):
        super().__init__(balance, interest)

def create_savings_account(balance, interest, maturity):
    """This function calculates the interest earned on the savings account balance for the given months.
    It returns the updated savings account balance and interest earned.
    """
    # Calculate the interest earned on the savings account balance for the given months.
    interest_rate = interest / 100
    monthly_interest_rate = interest_rate / 12
    interest_earned = balance * monthly_interest_rate * maturity

    # Update the savings account balance with interest earned.
    updated_balance = balance + interest_earned

    # Return the updated savings account balance and interest earned.
    return updated_balance, interest_earned

def create_cd_account(balance, interest, maturity):
    """This function calculates the interest earned on the CD account balance for the given months.
    It returns the updated CD account balance and interest earned.
    """
    # Calculate the interest earned on the CD account balance for the given months.
    interest_rate = interest / 100
    interest_earned = balance * interest_rate * maturity

    # Update the CD account balance with interest earned.
    updated_balance = balance + interest_earned

    # Return the updated CD account balance and interest earned.
    return updated_balance, interest_earned

def main(): 
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account interest rate: "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Interest earned on savings account: {interest_earned:.2f}")
    print(f"Updated savings account balance: {updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate: "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned on CD account: {cd_interest_earned:.2f}")
    print(f"Updated CD account balance: {updated_cd_balance:.2f}")
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account interest rate: "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Interest earned on CD account: {interest_earned:.2f}")
    print(f"Updated CD account balance: {updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
