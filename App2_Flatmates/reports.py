import calendar

from fpdf import FPDF

from flat import Bill


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
        pdf.image("files/house.png", w=30, h=30)

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

        pdf.output(f"files/{self.filename}")
