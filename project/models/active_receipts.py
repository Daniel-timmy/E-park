import uuid
from datetime import datetime

from flask_login import LoginManager
from mongoengine import StringField, ImageField, DateTimeField, EmbeddedDocument, IntField, EmailField, Document
from project import app

login_manager = LoginManager(app)


class ActiveReceipt(Document):
    uId = StringField(default=str(uuid.uuid4()))
    email = EmailField(required=False)
    status = StringField(required=True)
    lot = StringField(required=True)
    space = StringField(required=True)
    duration = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow(), required=False)
    start_time = DateTimeField(required=False)
    model = StringField(required=True)
    plate_number = StringField(required=True)
    reservation_type = StringField(required=True)
    amount = IntField(required=True)
    vehicle_picture = ImageField(required=False)
