import webbrowser

import month
from fpdf import FPDF
import calendar

class Bill:
    """
    Objetc that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount: float, year: int, month: int, *flatmates):
        self.amount = amount
        self.year = year
        self.month = month
        self.flatmates = flatmates

    def calculate_flatmate_bill(self):
        # sum total of days
        total_days = 0
        for flatmate in self.flatmates:
            try:
                total_days += flatmate.days_in_house[self.year][self.month]['days']
            except Exception:
                pass

        # calculate the amount for each flatmate
        for flatmate in self.flatmates:
            try:
                flatmate_amount = round(
                    (self.amount * (flatmate.days_in_house[self.year][self.month]['days'] / total_days)),
                    2
                )
                flatmate.days_in_house[self.year][self.month]['amount'] = flatmate_amount
                print(f"{flatmate.name} = {flatmate_amount}")
            except Exception:
                pass


class Flatmate:
    """
    Object that contains data about a flatmate person
    who lives in the house and pays share of the bill
    """

    def __init__(self, name):
        self.name = name
        self.days_in_house = {}

    def add_days_in_house(self, year, month, days_in_house):
        self.days_in_house[year] = {
            month: {
                'days': days_in_house,
                'amount': 0
            }
        }


class PdfReport:
    """
    Create a pdf file that contains data abput
    the flatmates such as their names, their amount
    and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill: Bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=1, align='C', ln=1)

        # Insert Period label and value
        pdf.set_font('Times', size=14, style='B')
        pdf.cell(
            w=300,
            h=40,
            txt=f'Period: {calendar.month_name[bill.month]}/{bill.year}',
            border=0,
        )
        pdf.cell(
            w=250,
            h=40,
            txt=f'Total Amount: $ {bill.amount}',
            border=0,
            ln=1
        )

        # Labels
        pdf.set_font(family="Times", size=12, style='B')
        pdf.cell(w=150, h=25, txt="Name")
        pdf.cell(w=150, h=25, txt="Days in House")
        pdf.cell(w=150, h=25, txt="Pay", ln=1)

        # Insert Flatmates
        pdf.set_font(family="Times", size=12)
        for flatmate in bill.flatmates:
            pdf.cell(
                w=150,
                h=25,
                txt=flatmate.name,
                border=0,
            )
            pdf.cell(
                w=150,
                h=25,
                txt=str(flatmate.days_in_house[bill.year][bill.month]["days"]),
                border=0,
            )
            pdf.cell(
                w=150,
                h=25,
                txt=f'$ {flatmate.days_in_house[bill.year][bill.month]["amount"]}',
                border=0,
                ln=1
            )

        pdf.output(self.filename)


john = Flatmate(name="John")
john.add_days_in_house(2022, month.MARCH, 20)
mary = Flatmate(name="Mary")
mary.add_days_in_house(2022, month.MARCH, 25)

bill = Bill(120, 2022, month.MARCH, john, mary)
bill.calculate_flatmate_bill()

pdf = PdfReport('bill.pdf')
pdf.generate(bill)

