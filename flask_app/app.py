import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import date

from form.forms import RoomForm, UserForm, LessonForm, GroupForm, SchedulerForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

###  ROOM   ###
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)

    @staticmethod ###get info about room (id)
    def get_room(id):
        room = None
        try:    
            room = Room.query.get(id)
        except Exception, e:
            print e
        return room

    @staticmethod ###create inputed room and commit db
    def create(name, capacity):
        room = Room(name=name,
                    capacity=capacity)
        db.session.add(room)
        db.session.commit()
        return room

@app.route('/room', methods=['GET']) ###show list of rooms on screen
def room_get():
   room_f = RoomForm(request.form)
   rooms = Room.query.all()
   return render_template('room.html', room_form=room_f, rooms=rooms)

@app.route('/room', methods=['POST']) ###send created room to db
def room_post():
    room_f = RoomForm(request.form)
    if room_f.validate():
        Room.create(name=room_f.name.data,
                    capacity=room_f.capacity.data)
        return redirect('/room')
    return render_template('room.html', room_form=room_f)

@app.route('/room/<id>/update', methods=['GET', "POST"]) ###edit existed room
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

@app.route('/room/<id>/delete', methods=['GET']) ###delete existed room
def room_delete(id):
    try:
        room = Room.query.get(id)
        db.session.delete(room)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/room')

### USER    ###
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.firstname)

    @staticmethod ###get info about user (id)
    def get_user(id):
        user = None
        try:    
            user = User.query.get(id)
        except Exception, e:
            print e
        return user

    @staticmethod ###create inputed user and commit db
    def create(firstname, lastname, age):
        user = User(lastname=lastname,
                    firstname=firstname,
                    age=age)
        db.session.add(user)
        db.session.commit()
        return user

@app.route('/user', methods=['GET']) ###show list of users on screen
def user_get():
   user_f = UserForm(request.form)
   users = User.query.all()
   return render_template('user.html', user_form=user_f, users=users)


@app.route('/user', methods=['POST'])  ###create room on page
def user_post():
    user_f = UserForm(request.form)
    if user_f.validate():
        User.create(lastname=user_f.lastname.data,
                    firstname=user_f.firstname.data,
                    age=user_f.age.data)
        return redirect('/user')
    return render_template('user.html', user_form=user_f)

@app.route('/user/<id>/update', methods=['GET', "POST"]) ###edit
def user_put(id):
    user = User.get_user(id)
    if user:
        form = UserForm(request.form)
        if request.method == "POST" and form.validate():
            user.lastname = form.lastname.data
            user.firstname = form.firstname.data
            user.age = form.age.data

            db.session.commit()
            return redirect('/user')

        form.lastname.data = user.lastname
        form.firstname.data = user.firstname
        form.age.data = user.age
        return render_template('user_update.html', form=form)
    return redirect('/user') 
   
@app.route('/user/<id>/delete', methods=['GET']) ###delete
def user_delete(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/user')

###   LESSON    ###
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.Integer,nullable=False)

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def __repr__(self):
        return '<Teacher {} {} {}>'.format(self.id, self.name, self.teacher)

    def get_teacher(self):
        user = None
        try:    
            user = User.query.get(self.teacher)
        except Exception, e:
            print e
        return user

    @staticmethod ###geting info about lesson (id)
    def get_lesson(id):
        lesson = None
        try:    
            lesson = Lesson.query.get(id)
        except Exception, e:
            print e
        return lesson

@app.route('/lesson', methods=['GET'])
def lesson_get():
    form = LessonForm(request.form)
    users = User.query.all()
    
    lessons = Lesson.query.all()
    for lesson in lessons:
        lesson.teacher = lesson.get_teacher()
        print lesson
    return render_template('lesson.html', form=form, lessons=lessons, users=users)

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

@app.route('/lesson/<id>/update', methods=['GET', "POST"]) ###edit existed lesson
def lesson_put(id):
    users = User.query.all()
    lessons = Lesson.query.all()
    
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
        return render_template('lesson_update.html', form=form, users=users, lessons=lessons)
    return redirect('/lesson') 

@app.route('/lesson/<id>/delete', methods=['GET']) ###delete existed lesson
def lesson_delete(id):
    try:
        lesson = Lesson.query.get(id)
        db.session.delete(lesson)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/lesson')

###     GROUP   ###
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    members = db.Column(db.String(30), nullable=False)

    def __init__(self, name, members):
            self.name = name
            self.members = members

    def __repr__(self):
        return '<Group {} {} {}>'.format(self.id, self.name, self.members)

    def get_members(self):
        members = []
        try:
            for member in self.members.split(','):
                user = User.query.get(int(member.strip()))
                members.append(user)
        except Exception, e:
            print e
        return members

    @staticmethod ###geting info about group (id)
    def get_group(id):
        group = None
        try:    
            group = Group.query.get(id)
        except Exception, e:
            print e
        return group

@app.route('/group', methods=['GET'])
def group_get():
    form = GroupForm(request.form)
    users = User.query.all()
    
    groups = Group.query.all()
    for group in groups:
        group.members = group.get_members()
        # print members
    return render_template('group.html', form=form, groups=groups, users=users)

@app.route('/group', methods=['POST'])
def group_post():
    form = GroupForm(request.form)
    if form.validate():
        group = Group(name=form.name.data,
                            members=form.members.data)
        db.session.add(group)
        db.session.commit()
        return redirect('/group')
    return render_template('group.html', form=form)

@app.route('/group/<id>/update', methods=['GET', "POST"]) ###edit existed group
def group_put(id):
    users = User.query.all()
    groups = Group.query.all()
    
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
        return render_template('group_update.html', form=form, users=users, groups=groups)
    return redirect('/lesson') 

@app.route('/group/<id>/delete', methods=['GET']) ###delete existed group
def group_delete(id):
    try:
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/group')


### SCHEDULER  ###
class Scheduler(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.Integer, nullable=False)
    lesson = db.Column(db.Integer, nullable=False)
    group = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    para = db.Column(db.Integer, nullable=False)

    def __init__(self, room, lesson, group, date, para):
            self.room = room
            self.lesson = lesson
            self.group = group
            self.date = date
            self.para = para

    def __repr__(self):
        return '<Scheduler {} {} {} {}>'.format(self.id, self.lesson, self.date, self.para)

    @staticmethod ###geting info about scheduler (id)
    def get_scheduler(id):
        scheduler = None
        try:    
            scheduler = Scheduler.query.get(id)
        except Exception, e:
            print e
        return scheduler

@app.route('/scheduler', methods=['GET'])
def scheduler_get():
    form = SchedulerForm(request.form)
    lessons = Lesson.query.all()
    rooms = Room.query.all()
    groups = Group.query.all()
    schedulers=Scheduler.query.all()
    return render_template('scheduler.html', schedulers=schedulers, form=form, groups=groups, lessons=lessons, rooms=rooms)

@app.route('/scheduler', methods=['POST'])
def scheduler_post():
    form = SchedulerForm(request.form)
    if form.validate():
        scheduler = Scheduler(room=form.room.data,
                            lesson=form.lesson.data,
                            group=form.group.data,
                            date=form.date.data,
                            para=form.para.data)
        db.session.add(scheduler)
        db.session.commit()
        return redirect('/scheduler')
    lessons = Lesson.query.all()
    rooms = Room.query.all()
    groups = Group.query.all()
    schedulers=Scheduler.query.all()
    return render_template('scheduler.html', schedulers=schedulers, form=form, groups=groups, lessons=lessons, rooms=rooms)

@app.route('/scheduler/<id>/delete', methods=['GET']) ###delete existed scheduler
def scheduler_delete(id):
    try:
        scheduler = Scheduler.query.get(id)
        db.session.delete(scheduler)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/scheduler')

@app.route('/scheduler/<id>/update', methods=['GET', "POST"])
def scheduler_put(id):
    lessons = Lesson.query.all()
    rooms = Room.query.all()
    groups = Group.query.all()
    schedulers=Scheduler.query.all()
    
    scheduler = Scheduler.get_scheduler(id)
    if scheduler:
        form = SchedulerForm(request.form)
        if request.method == "POST" and form.validate():
            scheduler.room = form.room.data
            scheduler.lesson = form.lesson.data
            scheduler.group = form.group.data
            scheduler.date = form.date.data
            scheduler.para = form.para.data

            db.session.commit()
            return redirect('/scheduler')

        form.room.data = scheduler.room
        form.lesson.data = scheduler.lesson
        form.group.data = scheduler.group
        form.date.data = scheduler.date
        form.para.data = scheduler.para
        return render_template('scheduler_update.html', schedulers=schedulers, form=form, groups=groups, lessons=lessons, rooms=rooms)
    return redirect('/scheduler') 

@app.route('/')
def hello_world():
    onday = Scheduler.query.filter(Scheduler.date == date.today())
    print onday
    return render_template('main.html', schedulers=onday)

if __name__ == "__main__":
    db.create_all()
    app.run()