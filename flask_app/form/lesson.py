from wtforms import Form, StringField, IntegerField, validators

class LessonForm(Form):
    name = StringField('Name:', [validators.Length(min=4, max=10)])
    teacher = StringField('Teacher:')
