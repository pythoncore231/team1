from wtforms import Form, StringField, IntegerField, validators

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=10)])
    capacity = IntegerField('Capacity')

class UserForm(Form):
    firstname = StringField('First name', [validators.Length(min=1, max=100)])
    lastname = StringField('Last name', [validators.Length(min=1, max=15)])
    age = IntegerField('Age')

class LessonForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=15)])
    teacher = StringField('Teacher', [validators.Length(min=1, max=100)])

class GroupForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=15)])
    members = StringField('Members', [validators.Length(min=1, max=100)])