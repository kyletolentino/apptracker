from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Tracker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    # job_id = db.Colum(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # status = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Tracker %r>' % self.name


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        entry = Tracker(name=name)

        try:
            db.session.add(entry)
            db.session.commit()
            return redirect('/')
        except:
            return "Uh-oh, we can't add it."
    
    else:
        names = Tracker.query.order_by(Tracker.date).all()
        return render_template('index.html', names=names)


@app.route('/delete/<int:id>')
def delete(id):
    company = Tracker.query.get_or_404(id)

    try:
        db.session.delete(company)
        db.session.commit()
        return redirect('/')
    except:
        return "We couldn't delete that entry."


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    company = Tracker.query.get_or_404(id)

    if request.method == 'POST':
        company.name == request.form['name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "We couldn't update that entry."
    

    else:
        title = "Update Entry"
        return render_template('update.html', title=title, company=company)


if __name__ == "__main__":
    app.run(debug=True)