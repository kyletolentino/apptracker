from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), nullable=False)
    job_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False, default=datetime.now().date())
    status = db.Column(db.String(50), nullable=False)

    def __init__(self, company, job_id, date, status):
        self.company = company
        self.job_id = job_id
        self.date = date
        self.status = status

@app.route('/')
def index():
    all_data = Tracker.query.all()

    return render_template("index.html", jobs = all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':

        company = request.form['company']
        job_id = request.form['job_id']

        entry = Tracker(company, job_id, date=datetime.now().date(),status='Applied')
        db.session.add(entry)
        db.session.commit()

        return redirect(url_for('index'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        entry = Tracker.query.get(request.form.get('id'))
        
        entry.company = request.form['company']
        entry.job_id = request.form['job_id']
        entry.status = request.form['status']

        # request.form['date'] is str type, must convert
        entry.date = datetime.strptime(request.form['date'], '%Y-%m-%d')

        db.session.commit()

        return redirect(url_for('index'))


@app.route('/delete', methods=['GET', 'POST'])
def delete():
     if request.method == 'POST':
        entry = Tracker.query.get(request.form.get('id'))

        db.session.delete(entry)
        db.session.commit()

        return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)