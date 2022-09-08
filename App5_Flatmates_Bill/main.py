from flask.views import MethodView
from wtforms import Form, StringField, IntegerField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.flat import Bill, Flatmate

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)


class ResultPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)

        amount = float(bill_form.amount.data)
        year = int(bill_form.year.data)
        month = int(bill_form.month.data)
        the_bill = Bill(amount=amount, year=year, month=month)

        name1 = bill_form.name1.data
        days_in_house1 = int(bill_form.days_in_house1.data)
        flatmate1 = Flatmate(name=name1)
        flatmate1.add_days_in_house(year=year, month=month, days_in_house=days_in_house1)
        the_bill.add_flatmate(flatmate1)

        name2 = bill_form.name2.data
        days_in_house2 = int(bill_form.days_in_house2.data)
        flatmate2 = Flatmate(name=name2)
        flatmate2.add_days_in_house(year=year, month=month, days_in_house=days_in_house2)
        the_bill.add_flatmate(flatmate2)

        the_bill.calculate_flatmate_bill()

        return render_template(
            'results_page.html',
            name1=flatmate1.name,
            amount1=flatmate1.days_in_house[year][month]['amount'],
            name2=flatmate2.name,
            amount2=flatmate2.days_in_house[year][month]['amount']
        )

class BillForm(Form):
    amount = StringField("Bill Amount: ", default="100")
    year = IntegerField("Period Year: ", default=2022)
    month = IntegerField("Period Month: ", default=3)

    name1 = StringField("Name: ", default="Eduardo")
    days_in_house1 = IntegerField("Days in the House: ", default=10)

    name2 = StringField("Name: ", default="Bruna")
    days_in_house2 = IntegerField("Days in the House: ", default=10)

    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultPage.as_view('results_page'))

app.run(debug=True)
