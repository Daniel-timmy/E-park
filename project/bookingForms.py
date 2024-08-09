import time
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SelectField, IntegerField, SubmitField, RadioField
from wtforms.validators import InputRequired

today = ''
def dayHourChoices(unit):
    """ Populates the start_day choices arguments 
    """
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    hours = hours = [[i for i in range(0, 24)]] * 6

    timestamp = time.time()
    current_date = time.ctime(timestamp)
    current_date = current_date.split(' ')
    day = list(current_date)
    
    hour = day[4].split(':')[0]
    global today
    today = day[0] 

    idx = days.index(day[0])
    idx =  (idx) % len(days)
    days[:] = days[idx:] + days[:idx]

    if unit == 'hours':
        hours[0] = [i for i in range(int(hour), 24)]
        return hours
    elif unit == 'days':
        return days
    else:
        []

class BookingForm(FlaskForm):
    lot = SelectField(label='Lot', choices=['EDU', 'FET', 'LSC', 'PHY', 'LAW', 'MGT', 'SCS', 'CLS', 'CIS', 'AGR', 'MDS'],
                      validators=[InputRequired('Choose a parking lot.')])
    space = StringField(label="Spaces",
                        validators=[InputRequired('Choose a parking space')])
    duration = SelectField(label="How many days", validators=[InputRequired()], 
                           choices=['1', '2', '3', '4', '5', '6', '7'])
    # start_hour = SelectField(label="Start hour", choices=dayHourChoices(unit='hours'))  # dynamic
    start_day = SelectField(label="Start day", choices=dayHourChoices(unit='days'), default=today)
    model = StringField(label="Vehicle Model", validators=[InputRequired()])
    # time_unit = SelectField(label="Days or Hours"
    #                         choices=['hours', 'days'],
    #                         validators=[InputRequired()])
    plate_number = StringField(label="Plate number", validators=[InputRequired()])
    reservation_type = SelectField(label="Reservation?", choices=['Reservation', 'On spot'])
    vehicle_image = FileField(label='Vehicle Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField(label='Make payment')

    # Based on the lot and space chosen a message will be displayed 
    # to alert the user if the particular space is available and which days are still free





