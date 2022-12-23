from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///amdsmi.db'
db = SQLAlchemy(app)
app.app_context().push()


class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.Text(80), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f'MyTable({self.id}-{self.user_name}-{self.date})'


@app.route('/')
def my_name():
    my_table = MyTable.query.all()
    return render_template('home_page.html', my_table=my_table)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<user_id>')
def user(user_id):
    my_table = MyTable.query.get(user_id)
    return render_template('user.html', my_table=my_table)


if __name__ == "__main__":
    app.run(debug=True)
