import os.path

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm, GroupForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=True)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    teacher = db.Column(db.Integer, nullable=False)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    members = db.Column(db.String(100), nullable=False)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/room', methods=['GET', 'POST'])
def room():
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        room = Room(name=form.name.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        return redirect('/room')

    rooms = Room.query.all()
    return render_template('room.html', form=form, rooms=rooms)


@app.route('/user', methods=['GET', 'POST'])
def user():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, age=form.age.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')

    users = User.query.all()
    return render_template('user.html', form=form, users=users)


@app.route('/lesson', methods=['GET', 'POST'])
def lesson():
    form = LessonForm(request.form)
    if request.method == 'POST' and form.validate():
        users = User.query.all()
        teacher = ""
        for user in users:
            if form.teacher.data == user.firstname + " " + user.lastname:
                teacher = user
        if not teacher:
            firstn, lastn = form.teacher.data.split()
            teacher = User(firstname=firstn, lastname=lastn)
            db.session.add(teacher)
            db.session.commit()
        lesson = Lesson(name=form.name.data, teacher=teacher.id)
        db.session.add(lesson)
        db.session.commit()
        return redirect('/lesson')

    lessons = Lesson.query.all()
    return render_template('lesson.html', form=form, lessons=lessons)


@app.route('/group', methods=['GET', 'POST'])
def group():
    form = GroupForm(request.form)
    if request.method == 'POST' and form.validate():

        users = User.query.all()
        members = []
        members_str_in = form.members.data.split(',')
        for member in members_str_in:
            teacher = ""
            for user in users:
                if member.strip() == user.firstname + " " + user.lastname:
                    teacher = user
            if not teacher:
                firstn, lastn = member.split()
                teacher = User(firstname=firstn, lastname=lastn)
                db.session.add(teacher)
                db.session.commit()
            members.append(unicode(teacher.id))

        group = Group(name=form.name.data, members=', '.join(members))
        db.session.add(group)
        db.session.commit()
        return redirect('/group')

    groups = Group.query.all()
    return render_template('group.html', form=form, groups=groups)


if __name__ == "__main__":
    db.create_all()
    app.run()