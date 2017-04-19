from wtforms import Form, StringField, IntegerField, validators

class RoomForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=10)])
    capacity = IntegerField('Capacity')
