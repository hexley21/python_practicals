import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(64))
    semester = db.Column(db.Integer)
    gpa = db.Column(db.Integer)

def __repr__(self):
    return f"Student('{self.id}', '{self.name}', '{self.semester}', '{self.gpa}'"

@app.route("/")
def main():
    students = []
    student = db.session.query(Student).all()
    for stud in student:
        students.append((stud.id, stud.name, stud.semester, stud.gpa))
    return str(students)

@app.route("/add/<identification>_<nam>_<smstr>_<gp>")
def add(identification, nam, smstr, gp):
    new_student = Student(id=int(identification), name=str(nam), semester=int(smstr), gpa=int(gp))
    db.session.add(new_student)
    db.session.commit()
    return f"added - Student({identification}, {nam}, {smstr}, {gp},)"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5005)
