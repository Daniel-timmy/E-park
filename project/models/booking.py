import uuid

from mongoengine import Document, StringField, DateTimeField, ImageField


class Booking(Document):
    uId = StringField(default=str(uuid.uuid4()))
    lot = StringField(required=True)
    space = StringField(required=True)
    duration = DateTimeField(required=True)
    start_time = DateTimeField(required=False)
    model = StringField(required=True)
    plate_number = StringField(required=True)
    reservation_type = StringField(required=True)
    vehicle_picture = ImageField(required=False)
