import os.path
from datetime import datetime, date

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm, GroupForm, SchedulerForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

#-----------Classes------------#

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)

    @staticmethod
    def create(name, capacity):
        room = Room(name=name, capacity=capacity)
        db.session.add(room)
        db.session.commit()
        return room

    @staticmethod
    def get_room(id):
        room = None
        try:
            room = Room.query.get(id)
        except Exception, e:
            print e
        return room

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    id_group = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.firstname)

    @staticmethod
    def create(firstname, lastname, age, id_group):
        user = User(lastname=lastname,
                    firstname=firstname,
                    age=age,
                    id_group=id_group)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def get_user(id):
        user = None
        try:
            user = User.query.get(id)
        except Exception, e:
            print e
        return user

    @staticmethod
    def get_users_in_group(id_group):
        string = ''
        try:
            users = User.query.filter(User.id_group == id_group)
            string = ', '.join([i.firstname + " " + i.lastname for i in users])
        except Exception, e:
            print e
        return string

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.Integer, nullable=False)

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __repr__(self):
        return '<Teacher {} {} {}>'.format(self.id, self.name, self.teacher)

    @staticmethod
    def create(name, teacher):
        lesson = Lesson(name=name, teacher=teacher)
        db.session.add(lesson)
        db.session.commit()
        return lesson

    @staticmethod
    def get_lesson(id):
        lesson = None
        try:
            lesson = Lesson.query.get(id)
        except Exception, e:
            print e
        return lesson

    def get_teacher(self):
        user = None
        try:
            user = User.query.get(self.teacher)
        except Exception, e:
            print e
        return user

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)

    @staticmethod
    def create(name):
        group = Group(name=name)
        db.session.add(group)
        db.session.commit()
        return group

    @staticmethod
    def get_group(id):
        group = None
        try:
            group = Group.query.get(id)
        except Exception, e:
            print e
        return group

class Scheduler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, nullable=False)
    lesson_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    para = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Lesson {} {} {}>'.format(self.id, self.name, self.teacher)

    @staticmethod
    def create(room_id, lesson_id, group_id, date, para):
        scheduler = Scheduler(room_id=room_id, lesson_id=lesson_id,
                              group_id=group_id, date=date, para=para)
        db.session.add(scheduler)
        db.session.commit()
        return scheduler

    @staticmethod
    def get_scheduler(id):
        scheduler = None
        try:
            scheduler = Scheduler.query.get(id)
        except Exception, e:
            print e
        return scheduler

    def to_dict(self):
        data = {}
        data["id"] = self.id
        data["room"] = Room.get_room(self.room_id).name
        data["lesson"] = Lesson.get_lesson(self.lesson_id).name
        data["group"] = Group.get_group(self.group_id).name
        data["date"] = self.date
        data["para"] = self.para
        return data

#-----------Routes------------#

@app.route('/')
def main():
    schedulers = [s.to_dict() for s in Scheduler.query.filter(Scheduler.date >= datetime.now().strftime('%Y-%m-%d'))]
    return render_template('main.html', s=schedulers, date = datetime.now().strftime('%Y-%m-%d'))

###room###

@app.route('/room', methods=['GET', 'POST'])
def room():
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        Room.create(name=form.name.data, capacity=form.capacity.data)
        return redirect('/room')

    rooms = Room.query.all()
    return render_template('room.html', f=form, r=rooms)

@app.route('/room/<id>/update', methods=['GET', "POST"])
def room_put(id):
    room = Room.get_room(id)
    if room:
        form = RoomForm(request.form)
        if request.method == "POST" and form.validate():
            room.name = form.name.data
            room.capacity = form.capacity.data
            db.session.commit()
            return redirect('/room')

        form.name.data = room.name
        form.capacity.data = room.capacity
        return render_template('room_update.html', form=form)
    return redirect('/room')

@app.route('/room/<id>/delete', methods=['GET'])
def room_delete(id):
    try:
        room = Room.query.get(id)
        db.session.delete(room)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/room')

###user###

@app.route('/user', methods=['GET', "POST"])
def user():
    user_f = UserForm(request.form)
    if request.method == 'POST' and user_f.validate():
        User.create(lastname=user_f.lastname.data,
                        firstname=user_f.firstname.data,
                        age=user_f.age.data,
                        id_group=user_f.id_group.data)
        return redirect('/user')

    groups = Group.query.all()
    users = User.query.all()
    return render_template('user.html', user_form=user_f, users=users, groups=groups)

@app.route('/user/<id>/update', methods=['GET', "POST"])
def user_put(id):
    user = User.get_user(id)
    if user:
        form = UserForm(request.form)
        if request.method == "POST" and form.validate():
            user.lastname = form.lastname.data
            user.firstname = form.firstname.data
            user.age = form.age.data
            user.id_group = form.id_group.data

            db.session.commit()
            return redirect('/user')

        form.lastname.data = user.lastname
        form.firstname.data = user.firstname
        form.age.data = user.age
        form.id_group.data = user.id_group
        return render_template('user_update.html', form=form)
    return redirect('/user')

@app.route('/user/<id>/delete', methods=['GET'])
def user_delete(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/user')

###lesson###

@app.route('/lesson', methods=['GET', "POST"])
def lesson():
    form = LessonForm(request.form)
    if request.method == 'POST' and form.validate():
        teacher_id = User.get_user(form.teacher.data)
        if teacher_id:
            Lesson.create(name=form.name.data, teacher=form.teacher.data)
            return redirect('/lesson')

    users = User.query.all()
    lessons = Lesson.query.all()
    for lesson in lessons:
        lesson.teacher = lesson.get_teacher()
    return render_template('lesson.html', form=form, lessons=lessons, users=users)

@app.route('/lesson/<id>/update', methods=['GET', "POST"])
def lesson_put(id):
    lesson = Lesson.get_lesson(id)
    if lesson:
        form = LessonForm(request.form)
        if request.method == "POST" and form.validate():
            lesson.name = form.name.data
            lesson.teacher = form.teacher.data
            db.session.commit()
            return redirect('/lesson')

        form.name.data = lesson.name
        form.teacher.data = lesson.teacher
        return render_template('lesson_update.html', form=form)
    return redirect('/lesson')

@app.route('/lesson/<id>/delete', methods=['GET'])
def lesson_delete(id):
    try:
        lesson = Lesson.query.get(id)
        db.session.delete(lesson)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/lesson')

###group###

@app.route('/group', methods=['GET', 'POST'])
def group():
    form = GroupForm(request.form)
    if request.method == 'POST' and form.validate():
        Group.create(name=form.name.data)
        return redirect('/group')

    groups = Group.query.all()
    groups = [(groups[i], User.get_users_in_group(groups[i].id)) for i in range(len(groups))]
    return render_template('group.html', f=form, groups=groups)

@app.route('/group/<id>/update', methods=['GET', "POST"])
def group_put(id):
    group = Group.get_group(id)
    if group:
        form = GroupForm(request.form)
        if request.method == "POST" and form.validate():
            group.name = form.name.data
            db.session.commit()
            return redirect('/group')

        form.name.data = group.name
        return render_template('group_update.html', form=form)
    return redirect('/group')

@app.route('/group/<id>/delete', methods=['GET'])
def group_delete(id):
    try:
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/group')

###scheduler###

@app.route('/scheduler', methods=['GET', 'POST'])
def scheduler():
    form = SchedulerForm(request.form)
    if request.method == 'POST' and form.validate() and 1 <= form.para.data <= 7:
        room_id = Room.get_room(form.room_id.data)
        lesson_id = Lesson.get_lesson(form.lesson_id.data)
        group_id = Group.get_group(form.group_id.data)
        if room_id and lesson_id and group_id:
            Scheduler.create(room_id=form.room_id.data,
                             lesson_id=form.lesson_id.data,
                             group_id=form.group_id.data,
                             date=form.date.data,
                             para=form.para.data)
            return redirect('/scheduler')

    rooms = Room.query.all()
    lessons = Lesson.query.all()
    groups = Group.query.all()
    schedulers = [s.to_dict() for s in Scheduler.query.all()]
    return render_template('scheduler.html', form=form, s=schedulers, r=rooms, l=lessons, g=groups)

@app.route('/scheduler/<id>/update', methods=['GET', "POST"])
def scheduler_put(id):
    scheduler = Scheduler.get_scheduler(id)
    if scheduler:
        form = SchedulerForm(request.form)
        if request.method == "POST" and form.validate():
            scheduler.room_id = form.room_id.data
            scheduler.lesson_id = form.lesson_id.data
            scheduler.group_id = form.group_id.data
            scheduler.date = form.date.data
            scheduler.para = form.para.data
            db.session.commit()
            return redirect('/scheduler')

        form.room_id.data = scheduler.room_id
        form.lesson_id.data = scheduler.lesson_id
        form.group_id.data = scheduler.group_id
        form.date.data = scheduler.date
        form.para.data = scheduler.para
        return render_template('scheduler_update.html', form=form)
    return redirect('/scheduler')

@app.route('/scheduler/<id>/delete', methods=['GET'])
def scheduler_delete(id):
    try:
        scheduler = Scheduler.query.get(id)
        db.session.delete(scheduler)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/scheduler')


if __name__ == "__main__":
    db.create_all()
    app.run()