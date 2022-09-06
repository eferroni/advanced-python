import json


class Bill:
    """
    Objetc that contains data about a bill, such as
    total amount and period of the bill
    """

    def __init__(self, amount: float, year: int, month: int):
        self.amount = amount
        self.year = year
        self.month = month
        self.flatmates = []

    def add_flatmate(self, flatmate):
        self.flatmates.append(flatmate)

    def calculate_flatmate_bill(self):
        # sum total of days
        total_days = 0
        for flatmate in self.flatmates:
            try:
                total_days += flatmate.days_in_house[self.year][self.month]['days']
            except Exception:
                pass

        # calculate the amount for each flatmates_bill
        for flatmate in self.flatmates:
            try:
                flatmate_amount = round(
                    (self.amount * (flatmate.days_in_house[self.year][self.month]['days'] / total_days)),
                    2
                )
                flatmate.days_in_house[self.year][self.month]['amount'] = flatmate_amount
            except Exception:
                pass


class Flatmate:
    """
    Object that contains data about a flatmates_bill person
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

    def __str__(self):
        return json.dumps(self.days_in_house)
