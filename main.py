from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField, URLField
from wtforms.validators import DataRequired, URL
import csv

FLASK_KEY = os.urandom(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_KEY
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Location URL', validators=[DataRequired(),URL()])
    open_time = TimeField("Opening time", validators=[DataRequired()])
    close_time = TimeField("Closing time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee rating", choices=["✘", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"], validators=[DataRequired()])
    wifi_rating = SelectField("WIFI strength rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField("Power outlet rating", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open("cafe-data.csv", "a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},{form.location.data},{form.open_time.data},{form.close_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_rating.data}")
        return render_template("add.html", form=form)
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
