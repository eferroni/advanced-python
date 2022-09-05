from flat import Bill, Flatmate
from reports import PdfReport

# Create the bill
bill_amount = float(input("Hey user, enter the bill amount: "))
bill_year = int(input("Enter the bill year: "))
bill_month = int(input("Enter the bill month: "))
bill = Bill(bill_amount, bill_year, bill_month)

# Create the FIRST flatmate
flatmate1_name = input("Enter the name of the first flatmate: ")
flatmate1_days = int(input(f"How many days {flatmate1_name} stays at home? "))
flatmate1 = Flatmate(name=flatmate1_name)
flatmate1.add_days_in_house(bill_year, bill_month, flatmate1_days)

# Create the SECOND flatmate
flatmate2_name = input("Enter the name of the first flatmate: ")
flatmate2_days = int(input(f"How many days {flatmate2_name} stays at home? "))
flatmate2 = Flatmate(flatmate2_name)
flatmate2.add_days_in_house(bill_year, bill_month, flatmate2_days)

# Add Flatmates to the bill
bill.add_flatmate(flatmate1)
bill.add_flatmate(flatmate2)

# Calculate the Bill
bill.calculate_flatmate_bill()

# Generate the pdf report
pdf = PdfReport(f'bill_{bill.year}{str(bill.month).zfill(2)}.pdf')
pdf.generate(bill)
