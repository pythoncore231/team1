from wtforms import Form, StringField, IntegerField, validators
from wtforms.fields.html5 import DateField


class UserForm(Form):
    firstname = StringField('Firs tname:', [validators.Length(min=1, max=100)])
    lastname = StringField('Last name:', [validators.Length(min=1, max=15)])
    age = IntegerField('Age:')

class LessonForm(Form):
    name = StringField('Name:', [validators.Length(min=1, max=100)])
    teacher = IntegerField('Teacher:')

class GroupForm(Form):
    name = StringField('Name:', [validators.Length(min=1, max=15)])
    members = IntegerField('Members:')

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=15)])
    capacity = IntegerField('Capacity:')

class SchedulerForm(Form):
    room_id = IntegerField('room_id')
    lesson_id = IntegerField('lesson_id')
    group_id = IntegerField('group_id')
    date = DateField("date", format='%Y-%m-%d')
    para = IntegerField('group_id')

