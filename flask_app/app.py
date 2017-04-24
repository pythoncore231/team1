import os.path

from datetime import datetime

from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm, GroupForm, ScheduleForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)


# ____________________________________________________________________________
# ________________________________ \\ Room // ________________________________
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    @staticmethod
    def get_room(id):
        room = None
        try:
            room = Room.query.get(id)
        except Exception, e:
            print e
        return room


# ---------------------------------\\ Room GET //-----------------------------
@app.route('/room', methods=['GET'])
def room_get():
    room_form = RoomForm(request.form)
    rooms = Room.query.all()
    return render_template('room.html', room_form=room_form, rooms=rooms)


# ---------------------------------\\ Room POST //----------------------------
@app.route('/room', methods=['POST'])
def room_post():
    room_f = RoomForm(request.form)
    if room_f.validate():
        room = Room(name=room_f.name.data, capacity=room_f.capacity.data)
        db.session.add(room)
        db.session.commit()
        return redirect('/room')
    return render_template('room.html', room_form=room_f)


# ---------------------------------\\ Room DELETE //--------------------------
@app.route('/room/<id>/delete', methods=['GET'])
def room_delete(id):
    try:
        room = Room.query.get(id)
        db.session.delete(room)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/room')


# ---------------------------------\\ Room UPDATE //--------------------------
@app.route('/room/<id>/update', methods=['GET', "POST"])
def room_update(id):
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


# ____________________________________________________________________________
# ________________________________ \\ User // ________________________________
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    @staticmethod
    def get_user(id):
        user = None
        try:
            user = User.query.get(id)
        except Exception, e:
            print e
        return user


# ---------------------------------\\ User GET //-----------------------------
@app.route('/user', methods=['GET'])
def user_get():
   user_f = UserForm(request.form)
   users = User.query.all()
   return render_template('user.html', user_form=user_f, users=users)


# ---------------------------------\\ User POST //-----------------------------
@app.route('/user', methods=['POST'])
def user_post():
    user_f = UserForm(request.form)
    if user_f.validate():
        user = User(firstname=user_f.firstname.data,
                    lastname=user_f.lastname.data,
                    age=user_f.age.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')
    return render_template('user.html', user_form=user_f)


# ---------------------------------\\ User DELETE //--------------------------
@app.route('/user/<id>/delete', methods=['GET'])
def user_delete(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/user')


# ---------------------------------\\ User UPDATE //--------------------------
@app.route('/user/<id>/update', methods=['GET', "POST"])
def user_update(id):
    user = User.get_user(id)
    if user:
        form = UserForm(request.form)
        if request.method == "POST" and form.validate():
            user.firstname = form.firstname.data
            user.lastname = form.lastname.data
            user.age = form.age.data
            db.session.commit()
            return redirect('/user')

        form.firstname.data = user.firstname
        form.lastname.data = user.lastname
        form.age.data = user.age
        return render_template('user_update.html', form=form)
    return redirect('/user')


# ____________________________________________________________________________
# ________________________________ \\ Lesson // ______________________________
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.Integer,nullable=False)

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def get_teacher(self):
        user = None
        try:
            user = User.query.get(self.teacher)
        except Exception, e:
            print e
        return user

    @staticmethod
    def get_lesson(id):
        lesson = None
        try:
            lesson = Lesson.query.get(id)
        except Exception, e:
            print e
        return lesson


# ---------------------------------\\ Lesson GET //---------------------------
@app.route('/lesson', methods=['GET'])
def lesson_get():
    lesson_f = LessonForm(request.form)
    users = User.query.all()
    lessons = Lesson.query.all()
    for lesson in lessons:
        lesson.teacher = lesson.get_teacher()
    return render_template('lesson.html', lesson_f=lesson_f, lessons=lessons, users=users)


# ---------------------------------\\ Lesson POST //--------------------------
@app.route('/lesson', methods=['POST'])
def lesson_post():
    form = LessonForm(request.form)
    if form.validate():
        teacher_id = User.get_user(form.teacher.data)
        if teacher_id:
            lesson = Lesson(name=form.name.data,
                            teacher=form.teacher.data)
            db.session.add(lesson)
            db.session.commit()
            return redirect('/lesson')
    return render_template('lesson.html', form=form)


# ---------------------------------\\ Lesson DELETE //--------------------------
@app.route('/lesson/<id>/delete', methods=['GET'])
def lesson_delete(id):
    try:
        lesson = Lesson.query.get(id)
        db.session.delete(lesson)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/lesson')


# ---------------------------------\\ Lesson UPDATE //--------------------------
@app.route('/lesson/<id>/update', methods=['GET', "POST"])
def lesson_update(id):
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


# ____________________________________________________________________________
# ________________________________ \\ Group // _______________________________
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    members = db.Column(db.String(10), unique=True, nullable=False)

    def get_members(self):
        members = []
        try:
            for member in self.members.split(','):
                user = User.query.get(int(member.strip()))
                members.append(user)
        except Exception, e:
            print e
        return members

    @staticmethod
    def get_group(id):
        group = None
        try:
            group = Group.query.get(id)
        except Exception, e:
            print e
        return group


# ---------------------------------\\ Group GET //----------------------------
@app.route('/group', methods=['GET'])
def group_get():
    group_f = GroupForm(request.form)
    users = User.query.all()
    groups = Group.query.all()
    for group in groups:
        group.members = group.get_members()
    return render_template('group.html', group_f=group_f, groups=groups, users=users)


# ---------------------------------\\ Group POST //---------------------------
@app.route('/group', methods=['POST'])
def group_post():
    group_f = GroupForm(request.form)
    if group_f.validate():
        group = Group(name=group_f.name.data, members=group_f.members.data)
        db.session.add(group)
        db.session.commit()
    return redirect('/group')


# ---------------------------------\\ Group DELETE //--------------------------
@app.route('/group/<id>/delete', methods=['GET'])
def group_delete(id):
    try:
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/group')


# ---------------------------------\\ Group UPDATE //--------------------------
@app.route('/group/<id>/update', methods=['GET', "POST"])
def group_update(id):
    group = Group.get_group(id)
    if group:
        form = GroupForm(request.form)
        if request.method == "POST" and form.validate():
            group.name = form.name.data
            group.members = form.members.data
            db.session.commit()
            return redirect('/group')

        form.name.data = group.name
        form.members.data = group.members
        return render_template('group_update.html', form=form)
    return redirect('/group')


# ____________________________________________________________________________
# ________________________________ \\ Schedule // ____________________________
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer, nullable=True)
    lesson = db.Column(db.Integer, nullable=True)
    group = db.Column(db.Integer, nullable=True)
    date = db.Column(db.String(10), nullable=True)
    para = db.Column(db.Integer, nullable=True)

    def __init__(self, room, lesson, group, date, para):
        self.room = room
        self.lesson = lesson
        self.group = group
        self.date = date
        self.para = para

    def get_room(self):
        room = None
        try:
            room = Room.query.get(self.room)
        except Exception, e:
            print e
        return room

    def get_lesson(self):
        lesson = None
        try:
            lesson = Lesson.query.get(self.lesson)
        except Exception, e:
            print e
        return lesson

    def get_group(self):
        group = None
        try:
            group = Group.query.get(self.group)
        except Exception, e:
            print e
        return group

    @staticmethod
    def get_schedule(id):
        schedule = None
        try:
            schedule = Schedule.query.get(id)
        except Exception, e:
            print e
        return schedule


# ---------------------------------\\ Schedule GET //-----------------------------
@app.route('/schedule', methods=['GET'])
def schedule_get():
    schedule_f = ScheduleForm(request.form)
    rooms = Room.query.all()
    lessons = Lesson.query.all()
    groups = Group.query.all()
    schedules = Schedule.query.all()
    for schedule in schedules:
        schedule.room = schedule.get_room()
        schedule.lesson = schedule.get_lesson()
        schedule.group = schedule.get_group()
        print schedule
    return render_template('schedule.html', schedule_f=schedule_f,
                           rooms=rooms, lessons=lessons, groups=groups, schedules=schedules)


# ---------------------------------\\ Schedule POST //-----------------------------
@app.route('/schedule', methods=['POST'])
def schedule_post():
    schedule_f = ScheduleForm(request.form)
    if schedule_f.validate():
        schedule = Schedule(room=schedule_f.room.data,
                            lesson=schedule_f.lesson.data,
                            group=schedule_f.group.data,
                            date=schedule_f.date.data,
                            para=schedule_f.para.data)
        db.session.add(schedule)
        db.session.commit()
        return redirect('/schedule')
    return render_template('schedule.html', schedule_form=schedule_f)


# ---------------------------------\\ Schedule DELETE //--------------------------
@app.route('/schedule/<id>/delete', methods=['GET'])
def schedule_delete(id):
    try:
        schedule = Schedule.query.get(id)
        db.session.delete(schedule)
        db.session.commit()
    except Exception, e:
        print e
    return redirect('/schedule')


# ---------------------------------\\ Schedule UPDATE //--------------------------
@app.route('/schedule/<id>/update', methods=['GET', "POST"])
def schedule_update(id):
    schedule = Schedule.get_schedule(id)
    if schedule:
        form = ScheduleForm(request.form)
        if request.method == "POST" and form.validate():
            schedule.room = form.room.data
            schedule.lesson = form.lesson.data
            schedule.group = form.group.data
            schedule.date = form.date.data
            schedule.para = form.para.data
            db.session.commit()
            return redirect('/schedule')

        form.room.data = schedule.room
        form.lesson.data = schedule.lesson
        form.group.data = schedule.group
        form.date.data = schedule.date
        form.para.data = schedule.para
        return render_template('schedule_update.html', form=form)
    return redirect('/schedule')


# ____________________________________________________________________________
# ________________________________ \\ Starter // ____________________________
@app.route('/')
def starter():
    # day of a week
    today = datetime.today().strftime("%A")
    print today
    check_day = Schedule.query.filter(Schedule.date == today)
    return render_template('starter.html', schedules=check_day)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
