# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

def create_savings_account(balance, interest_rate, months):
        interest_earned = balance * (interest_rate / 100) * (months / 12)
        updated_balance = balance + interest_earned
        return updated_balance, interest_earned

def create_cd_account(balance, interest_rate, months):
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    return updated_balance, interest_earned
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    balance = float(input("Enter the initial savings account balance: "))
    interest_rate = float(input("Enter the interest rate for the savings account: "))
    months = int(input("Enter the lengt of months to calculate the amount of interest: "))
    interest_earned = balance * (interest_rate/100 * months/12)
    updated_balance = balance + interest_earned
    # Call the create_savings_account function and pass the variables from the user.
    create_savings_account = (balance, interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Interest earned on the savings account:", interest_earned)
    print("Updated balance on the savings account:", updated_balance)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    
    cd_balance = float(input("Enter the initial CD account balance: "))
    cd_interest_rate = float(input("Enter the interest rate for the CD account: "))
    cd_months = int(input("Enter the lenght of the month to calculate the amount of interest for the CD account: "))
    cd_interest_earned = cd_balance * (cd_interest_rate/100 * cd_months/12)
    cd_updated_balance = cd_balance + cd_interest_earned
    # Call the create_cd_account function and pass the variables from the user.
    create_cd_account = (cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print("Interest earned on CD account:", cd_interest_earned)
    print("Updated balance on CD account", cd_updated_balance)
    
    # Call the main function.
    while True:
    
        choice = input("Do you want to continue? (y/n): ")
        if choice.lower() != 'y':
            break
if __name__ == "__main__":
    main()
