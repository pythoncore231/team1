import os.path

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm, GroupForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# ---------------------------------\\ Room //---------------------------------
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)


@app.route('/room', methods=['GET'])
def room_get():
    room_form = RoomForm(request.form)
    rooms = Room.query.all()
    return render_template('room.html', room_form=room_form, rooms=rooms)


@app.route('/room', methods=['POST'])
def room_post():
    room_f = RoomForm(request.form)
    if room_f.validate():
        room = Room(name=room_f.name.data, capacity=room_f.capacity.data)
        db.session.add(room)
        db.session.commit()
    return redirect('/room')


# ---------------------------------\\ User //---------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=True)


@app.route('/user', methods=['GET'])
def user_get():
    user_f = UserForm(request.form)
    users = User.query.all()
    return render_template('user.html', user_form=user_f, users=users)


@app.route('/user', methods=['POST'])
def user_post():
    user_f = UserForm(request.form)
    if user_f.validate():
        user = User(lastname=user_f.lastname.data,
                    firstname=user_f.firstname.data,
                    age=user_f.age.data)
        db.session.add(user)
        db.session.commit()
    return redirect('/user')


# ---------------------------------\\ Lesson //---------------------------------
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    teacher = db.Column(db.String(10), unique=True, nullable=False)


@app.route('/lesson', methods=['GET'])
def lesson_get():
    lesson_f = LessonForm(request.form)
    lessons = Lesson.query.all()
    return render_template('lesson.html', lesson_form=lesson_f, lessons=lessons)


@app.route('/lesson', methods=['POST'])
def lesson_post():
    lesson_f = LessonForm(request.form)
    if lesson_f.validate():
        lesson = Lesson(name=lesson_f.name.data, teacher=lesson_f.teacher.data)
        db.session.add(lesson)
        db.session.commit()
    return redirect('/lesson')


# ---------------------------------\\ Group //---------------------------------
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    members = db.Column(db.String(10), unique=True, nullable=False)


@app.route('/group', methods=['GET'])
def group_get():
    group_f = GroupForm(request.form)
    groups = Group.query.all()
    return render_template('group.html', group_form=group_f, groups=groups)


@app.route('/group', methods=['POST'])
def group_post():
    group_f = GroupForm(request.form)
    if group_f.validate():
        group = Group(name=group_f.name.data, members=group_f.members.data)
        db.session.add(group)
        db.session.commit()
    return redirect('/group')


if __name__ == "__main__":
    db.create_all()
    app.run()
