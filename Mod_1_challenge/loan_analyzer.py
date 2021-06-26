# coding: utf-8
import csv
from pathlib import Path

"""The purpose of this program is to analyze loan data and
determine the fair price of the loans.
"""


"""Automation of Calculations"""

#list of loan prices 
loan_costs = [500, 600, 200, 1000, 450]

#tells us how many loan prices are inside of the loan_costs list, then includes them in a statement
print("The number of loans is:", len(loan_costs))

#adds the values in the loan_costs list then includes them in a statement 
print("The total value of the loans:$",sum(loan_costs))

# averages the loan cost values from previous "loan_cost" list data then includes in a stament
print("The average loan amount is:$", (sum(loan_costs) / len(loan_costs)))



"""Analysis of Loan Data"""

"""

**Using a dictionary of additional loan information, we can determine fair price using the following
formula;

Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

    @NOTE 
        ***Future value:  the amount of money the borrower must pay back upon maturity of the
        loan (also known as the face value).
        
        ***Remaining months: the remaining maturity (in months) before the loan needs to be fully repaid.
        
        ***Fair Value: the loan is worth at least the cost to buy it.
        
        *** Discount Rate- 20%  """



# dictionary of loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# uses get() function to extract the Future Value on the loan
print("Future Value:$", loan.get("future_value"))

# uses get() function to extract the remaining amount of months on the loan
print("Remaining Months:", loan.get("remaining_months"))


# Calculates fair value using **monthly** present value formula with 20% discount rate value

discount_rate = 0.2

present_value = loan.get("future_value") / (1 + discount_rate/12) ** loan.get("remaining_months")


#print(present_value)- kept as test tool

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

#determines present value using .get function using loan list data to 
if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")

else :
    print("The loan is too expensive and not worth the price")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    discount_rate = annual_discount_rate
    present_value = loan.get("future_value") / (1 + discount_rate/12) ** loan.get("remaining_months")
    return present_value


# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

calculate_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),0.2)

print(f"The present value of the loan is:$ {round(present_value, 2)}")


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!

for loan in loans:
    loanPrice = loan.get("loan_price")
    if loanPrice <= 500:
        inexpensive_loans.append(loan)

# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

print("The following loans are considered inexpensive:",[inexpensive_loans])

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""



# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path

output_path = Path(r"C:\Users\brien\Desktop\FinTech_Workspace\Challenges\loan_analyzer.csv")


# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!


import csv 
from pathlib import Path
with open(output_path,'w', newline='') as output_path:
    csvwriter = csv.writer(output_path)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
      csvwriter.writerow(row.values())






