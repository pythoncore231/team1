from wtforms import Form, StringField, IntegerField, validators

class RoomForm(Form):
    name = StringField('Name:', [validators.Length(min=1, max=10)])
    capacity = IntegerField('Capacity:') and StringField('Capacity:')

class UserForm(Form):
    firstname = StringField('First name:', [validators.Length(min=1, max=100)])
    lastname = StringField('Last name:', [validators.Length(min=1, max=15)])
    age = IntegerField('Age:')

class LessonForm(Form):
    name = StringField('Name:', [validators.Length(min=1, max=100)])
    teacher = IntegerField('teacher:')

class GroupForm(Form):
    name = StringField('Name:', [validators.Length(min=2, max=20)])
    members = StringField('Members:', [validators.Length(min=1, max=15)])