import os.path

from flask import Flask, request, redirect,  render_template
from flask_sqlalchemy import SQLAlchemy

from form.forms import RoomForm, UserForm, LessonForm, GroupForm

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

#_______________________________________________________________________________________
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Room {} {}>'.format(self.name, self.capacity)


    @staticmethod
    def get_room(id):
        room = None
        try:    
            room = Room.query.get(id)
        except Exception, e:
            print e
        return room

    @staticmethod
    def create(name, capacity):
        room = Room(name=name,
                    capacity=capacity)
        db.session.add(room)
        db.session.commit()
        return room

#________________________________________________________________________________________________
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

#_______________________________________________________________________________________________
class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    teacher = db.Column(db.Integer,nullable=False)

    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
    def __repr__(self):
        return '<Teacher {} {} {}>'.format(self.id, self.name, self.teacher)

    @staticmethod
    def get_lesson(id):
        lesson = None
        try:    
            lesson = Lesson.query.get(id)
        except Exception, e:
            print e
        return lesson

    @staticmethod
    def create(name, teacher):
        lesson = Lesson(name=name,
                    teaxher=teacher)
        db.session.add(user)
        db.session.commit()
        return lesson


    def get_teacher(self):
        user = None
        try:    
            user = User.query.get(self.teacher)
        except Exception, e:
            print e
        return user

#__________________________________________________________________________________________
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    members = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return '<Group {} {}>'.format(self.id, self.name, self.members)

    @staticmethod
    def get_group(id):
        group = None
        try:    
            group = Group.query.get(id)
        except Exception, e:
            print e
        return group

    @staticmethod
    def create(name, members):
        group = Group(name=name,
                    members=members)
        db.session.add(list(user))
        db.session.commit()
        return group

    # def get_member(self):
    #     user = None
    #     try:    
    #         user = User.query.get(self.user)
    #     except Exception, e:
    #         print e
    #     return list(user)




    # Group
    #     name (str)
    #     members (list(user))
  
#________________________________________________________________ROOM___________________
     
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
        return render_template('room_update.html', f=form)
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

#______________________________________________________________USER______________________________________


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


#______________________________________________LESSON____________________________________

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



#__________________________________________________GROUP________________________________________________


@app.route('/group', methods=['GET', 'POST'])
def group():
    form = GroupForm(request.form)
    if request.method == 'POST' and form.validate():
        group = Group(name=form.name.data, members=form.members.data)
        db.session.add(group)
        db.session.commit()
        return redirect('/group')

    groups = Group.query.all()
    print groups
    return render_template('group.html', form=form, groups=groups)

@app.route('/group/<id>/update', methods=['GET', "POST"])
def group_put(id):
    group = Group.get_room(id)
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
