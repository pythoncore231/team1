from wtforms import Form, StringField, IntegerField, validators, DateTimeField

class RoomForm(Form):
    name = StringField('Name:', [validators.Length(min=3, max=10)])
    capacity = IntegerField('Capacity:')

class UserForm(Form):
    firstname = StringField('First name:', [validators.Length(min=1, max=10)])
    lastname = StringField('Last name:', [validators.Length(min=1, max=10)])
    age = IntegerField('Age:')

class LessonForm(Form):
    name = StringField('Name:', [validators.Length(min=1, max=10)])
    teacher = IntegerField('Teacher:')

class GroupForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=10)])
    members = StringField('Members', [validators.Length(min=1, max=30)])

class SchedulerForm(Form):
    room = IntegerField('Room')
    lesson = IntegerField('Lesson')
    group = IntegerField('Group')
    date = DateTimeField('Date', format='%d/%m/%Y')
    para = IntegerField('Para', [validators.number_range(min=1, max=7)])