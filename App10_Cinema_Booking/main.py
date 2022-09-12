from uuid import uuid4
import sqlite3
from fpdf import FPDF


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        seat.occupy()
        card.process_sale(seat.price)
        ticket = Ticket(user=self, seat=seat)
        ticket.to_pdf('ticket.pdf')


class Seat:

    database = 'cinema.db'

    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.price = 0
        self.availability = False

    @classmethod
    def clear(cls):
        connection = sqlite3.connect(cls.database)
        connection.execute("""
        UPDATE Seat SET "taken" = 0
        """)
        connection.commit()
        connection.close()

    def get_details(self) -> bool:
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "price", "taken" FROM Seat WHERE seat_id=?
        """, [self.seat_id])
        record = cursor.fetchone()
        if record is not None:
            price, taken = record
            self.price = price
            self.availability = not taken

            seat_found = True
        else:
            print('Sorry we could not find this seat')
            seat_found = False
        cursor.close()
        connection.close()

        return seat_found

    def is_free(self) -> bool:
        if not self.availability:
            print("Sorry, this seat is not available")
        return self.availability

    def occupy(self):
        connection = sqlite3.connect(self.database)
        connection.execute("""
        UPDATE Seat SET "taken" = 1 WHERE seat_id=?
        """, [self.seat_id])
        connection.commit()
        connection.close()


class Card:

    database = 'banking.db'

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder
        self.balance = None

    def validate(self, price):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()
        cursor.execute("""
        SELECT "balance" FROM Card
        WHERE type=?
        AND number=?
        AND cvc=?
        AND holder=?
        """, [self.type, self.number, self.cvc, self.holder])
        record = cursor.fetchone()
        if record is not None:
            self.balance = record[0]
            if self.balance >= price:
                validation = True
            else:
                print("This card doesnt have balance!")
                validation = False
        else:
            print('Sorry we could not find this card')
            validation = False
        cursor.close()
        connection.close()

        return validation

    def process_sale(self, price):
        self.balance -= price
        connection = sqlite3.connect(self.database)
        connection.execute("""
        UPDATE Card SET "balance"=?
        WHERE type=?
        AND number=?
        AND cvc=?
        AND holder=?
        """, [self.balance, self.type, self.number, self.cvc, self.holder])
        connection.commit()
        connection.close()


class Ticket:
    def __init__(self, user, seat):
        self.id = str(uuid4())
        self.user = user
        self.seat = seat

    def to_pdf(self, path: str):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', style='B', size=24)
        pdf.cell(w=0, h=80, txt="Your digital Ticket", border=1, ln=1, align='C')

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Name", border=1)
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=0, h=25, txt=self.user.name, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Ticket ID", border=1)
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=0, h=25, txt=self.id, border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Price", border=1)
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat.price), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt="Seat Number", border=1)
        pdf.set_font(family='Times', style='B', size=12)
        pdf.cell(w=0, h=25, txt=str(self.seat.seat_id), border=1, ln=1)
        pdf.cell(w=0, h=5, txt="", border=0, ln=1)

        pdf.output(path)

Seat.clear()

name = input("What is your name? ")
user = User(name=name)

while True:
    seat_number = input("Whats is the seat number? press q to exit ")
    if seat_number == 'q':
        print("Have a great day!")
        exit()
    seat = Seat(seat_number)
    found = seat.get_details()
    if found:
        if seat.is_free():
            break

while True:
    card_type = input("Card type: press q to exit ")
    if card_type == 'q':
        print("Have a great day!")
        exit()
    card_number = input("Card number: ")
    card_cvc = input("Card CVC: ")
    card_holder = input("Card Holder: ")
    card = Card(card_type, card_number, card_cvc, card_holder)
    print('SEAT PRICE: ', seat.price)
    if card.validate(seat.price):
        break

user.buy(seat, card)
