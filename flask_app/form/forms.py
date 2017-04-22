from wtforms import Form, StringField, IntegerField, validators

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