from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CalorieFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               calories_form=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)

        country = calories_form.country.data
        city = calories_form.city.data
        temperature = Temperature(country=country,
                                  city=city).get()

        weight = float(calories_form.weight.data)
        height = float(calories_form.height.data)
        age = int(calories_form.age.data)
        calories = Calorie(weight=weight,
                           height=height,
                           age=age,
                           temperature=temperature).calculate()

        return render_template('calories_form_page.html',
                               temperature=temperature,
                               calories=calories,
                               calories_form=calories_form,
                               result=True)


class CaloriesForm(Form):

    weight = StringField("Weight: ", default="87")
    height = StringField("Height: ", default="1.88")
    age = StringField("Age: ", default="36")
    country = StringField("Country: ", default="Brazil")
    city = StringField("City: ", default="Porto Alegre")
    button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories_form_page', view_func=CalorieFormPage.as_view('calories_form_page'))

app.run(debug=True)
