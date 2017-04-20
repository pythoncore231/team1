import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy

from form.room import RoomForm
from form.lesson import LessonForm
from form.forms import UserForm, GroupForm


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

#=============================== Classes ====================================

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(10), nullable=False)
    lastname = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    def __repr__(self):
        return '<User {} {}>'.format(self.id, self.firstname)

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=False, nullable=False)
    teacher = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Lesson {} {}>'.format(self.name, self.teacher)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), unique=True, nullable=False)
    members = db.Column(db.String(100), nullable=False)
#============================================================================


#=============================== Routes ====================================
@app.route('/')
def hello_world():
    '''
    Hello world route!
    '''
    return 'Hello, World!'

@app.route('/room', methods=['GET', 'POST'])
def room():
    '''
    Room route!
    '''
    form = RoomForm(request.form)
    if request.method == 'POST' and form.validate():
        room = Room(name=form.name.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        return redirect('/room')

    rooms = Room.query.all()
    return render_template('room.html', form=form, rooms=rooms)

@app.route('/room/<id>/delete', methods=['GET'])
def room_delete(id):
    try:
        room = Room.query.get(id)
        db.session.delete(room)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/room')

@app.route('/user', methods=['GET'])
def user_get():
   '''
    User route!
    ''' 
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
    return render_template('user.html', user_form=user_f)

@app.route('/user/<id>/delete', methods=['GET'])
def user_delete(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/user')

@app.route('/user/<id>/edit', methods=['GET'])
def user_edit(id):
    try:
        user = User.query.get(id)
        db.session.add(user)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/user')

@app.route('/lesson', methods=['GET', 'POST'])
def lesson():
    '''
    Lesson route!
    '''
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

@app.route('/lesson/<id>/delete', methods=['GET'])
def lesson_delete(id):
    try:
        lesson = Lesson.query.get(id)
        db.session.delete(lesson)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/lesson')

@app.route('/group', methods=['GET', 'POST'])
def group():
    '''
    Group route!
    '''
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

@app.route('/group/<id>/delete', methods=['GET'])
def group_delete(id):
    try:
        group = Group.query.get(id)
        db.session.delete(group)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/group')


if __name__ == "__main__":
    db.create_all()
    app.run()
