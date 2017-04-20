import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)


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

    @staticmethod
    def get_user(id):
        user = None
        try:    
            user = User.query.get(id)
        except Exception, e:
            print e
        return user

    @staticmethod
    def create(firstname, lastname, age):
        user = User(lastname=lastname,
                    firstname=firstname,
                    age=age)
        db.session.add(user)
        db.session.commit()
        return user


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
    print rooms
    return render_template('room.html', f=form, r=rooms, data="dfasdas")

@app.route('/user', methods=['GET'])
def user_get():
   user_f = UserForm(request.form)
   users = User.query.all()
   return render_template('user.html', user_form=user_f, users=users)


@app.route('/user', methods=['POST'])
def user_post():
    user_f = UserForm(request.form)
    if user_f.validate():
        User.create(lastname=user_f.lastname.data,
                    firstname=user_f.firstname.data,
                    age=user_f.age.data)
        return redirect('/user')
    return render_template('user.html', user_form=user_f)

@app.route('/user/<id>/update', methods=['GET', "POST"])
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
   
@app.route('/user/<id>/delete', methods=['GET'])
def user_delete(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
    except Exception, e:
        print e

    return redirect('/user')

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

if __name__ == "__main__":
    db.create_all()
    app.run()
