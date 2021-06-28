# coding: utf-8
# creates table-like custom objects from the items in CSV files
# and connects path for CSV to be read or written to/from
import csv
from pathlib import Path

"""The purpose of this program is to analyze loan data and
determine the fair price of the loans to ensure loans are bought
at the best possible value.

This program is organized into five parts;
Part 1: Automation of Calculations
Part 2: Analysis of Loan Data
Part 3: Financial Calculations
Part 4: Conditionally filters lists of loans
Part 5: Save results to CSV file

"""


"""Part 1 - Automation of Calculations"""

# list of loan prices 
loan_costs = [500, 600, 200, 1000, 450]

# tells us how many loan prices are inside of the loan_costs list, then includes them in a statement
print("The number of loans is:", len(loan_costs))

# adds the values in the loan_costs list then includes them in a statement 
print("The total value of the loans:$",sum(loan_costs))

# averages the loan cost values from previous "loan_cost" list data then includes in a stament
print("The average loan amount is:$", (sum(loan_costs) / len(loan_costs)))



""" Part 2: Analysis of Loan Data


*** Using a dictionary of additional loan information, we can determine fair price using the following
formula;

Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

    @NOTE 
        ***Future value:  the amount of money the borrower must pay back upon maturity of the
        loan (also known as the face value).
        
        ***Remaining months: the remaining maturity (in months) before the loan needs to be fully repaid.
        
        ***Fair Value: the loan is worth at least the cost to buy it.
        
        *** Discount Rate- 20%  

"""


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


# print(present_value)- **kept as test tool

# determines present value using .get function which pulls data from loan_price list
# if the loan data is less than or equal to present value it prints a statement confirming
# its a good buy, otherwise it will say the loan is not a good buy

if present_value >= loan.get("loan_price"):
    print("The loan is worth at least the cost to buy it.")

else :
    print("The loan is too expensive and not worth the price")


""" Part 3: Financial Calculations - This function can be used with any newly uploaded loan data """


# new list of loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#   Using calculate_present_value as a calculating function we give paramaters of `future_value`, `remaining_months`,
#   and the `annual_discount_rate`

#   This function gives us the `present_value` for the loan. 

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    discount_rate = annual_discount_rate
    present_value = loan.get("future_value") / (1 + discount_rate/12) ** loan.get("remaining_months")
    return present_value


# This function recalculates the present value with new data using an annual discount rate of 20%

calculate_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),0.2)

# displays present value loan amount with rounding for two decimal places

print(f"The present value of the loan is:$ {round(present_value, 2)}")


"""Part 4: Conditionally filters lists of loans.

This is will filter your lists of loan prices/values based on your specifications and 
take the desired data and put it into a new list for clean reading.

"""
# list of dictionaries containing loan data
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

# empty list created to receive data that will be filtered
inexpensive_loans = []

# Loops through loan data in 'loans' list with condition of $500 or less, the 
# values which meet that condition will then be uploaded into a new list called 'inexpensive_loans'

for loan in loans:
    loanPrice = loan.get("loan_price")
    if loanPrice <= 500:
        inexpensive_loans.append(loan)

# shows newly generated list with filtered results

print("The following loans are considered inexpensive:",[inexpensive_loans])


"""Part 5: Save the results.

Saves(writes) newly generated data to a CSV file"""

# Sets the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Sets the output file path, added r for absolute file path raw, otherwise unicode error appears

output_path = Path(r"C:\Users\brien\Desktop\FinTech_Workspace\Challenges\loan_analyzer.csv")



# loop for CSV files to be written, using 'header' variable that was created and uploading
# it to out_path (where you would like the CSV saved)

with open(output_path,'w', newline='') as output_path:
    csvwriter = csv.writer(output_path)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
      csvwriter.writerow(row.values())

# You should now have a new CSV file saved in your specified folder (output_path)





