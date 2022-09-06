from flask.views import MethodView
from wtforms import Form


class HomePage(MethodView):
    pass


class BillFormPage(MethodView):
    pass


class ResultPage(MethodView):
    pass


class BillForm(Form):
    pass