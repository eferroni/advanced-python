import month


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
        pass


john = Flatmate(name="John")
john.add_days_in_house(2022, month.MARCH, 20)
mary = Flatmate(name="Mary")
mary.add_days_in_house(2022, month.MARCH, 25)

bill = Bill(120, 2022, month.MARCH, john, mary)
bill.calculate_flatmate_bill()


