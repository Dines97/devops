from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./employee.db'
db = SQLAlchemy(app)


class Employee(db.Model):
    emp_no = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(14), nullable=False)
    last_name = db.Column(db.VARCHAR(16), nullable=False)
    gender = db.Column(db.Enum('M', 'F'), nullable=True)


@app.route('/', methods=['GET'])
def home():
    arg = request.headers.get('bootcamp')

    if arg == 'devops':
        return "Hosgeldin DevOps"

    employee = Employee.query.all()

    result = ''

    for i in employee:
        result += str(i.emp_no) + ' ' + i.first_name + ' ' + i.last_name + ' ' + i.gender + '<br>'

    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
