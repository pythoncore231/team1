from wtforms import Form, StringField, DateField, IntegerField, validators


class RoomForm(Form):
    name = StringField('Name:', [validators.Length(min=4, max=10)])
    capacity = IntegerField('Capacity:')


class UserForm(Form):
    firstname = StringField('First name:', [validators.Length(min=1, max=100)])
    lastname = StringField('Last name:', [validators.Length(min=1, max=15)])
    age = IntegerField('Age:')
    id_group = IntegerField('Group:')


class LessonForm(Form):
    name = StringField('Name:', [validators.Length(min=1, max=100)])
    teacher = IntegerField('Teacher:')


class GroupForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=15)])


class SchedulerForm(Form):
    room_id = IntegerField('Room ID')
    lesson_id = IntegerField('Lesson ID')
    group_id = IntegerField('Group ID')
    date = DateField("Date", format='%Y-%m-%d')
    para = IntegerField('Para')