import uuid

from mongoengine import DictField, EmailField, DateTimeField, EmbeddedDocument, EmbeddedDocumentField, IntField, \
    Document, StringField, ListField


class Space(EmbeddedDocument):
    uId = StringField(default=str(uuid.uuid4()))
    space_name = StringField(required=True)
    time_left = IntField(required=True)  # in minutes
    status = StringField(required=True)  # reserved, occupied, empty
    # reserved_time_slot = ListField()  [[start_hour, end_hour]]
    reserved_day_slot = DictField()  # {'receipt_id': [start_days,end_days, email], ...]
    start_time = DateTimeField(required=False)
    days_filled = ListField(StringField(), default=[])  # ['mon', 'tue']
    email = EmailField(required=False)
    duration = IntField(required=False)  # in days


class Lot(Document):
    uId = StringField(default=str(uuid.uuid4()))
    lot_name = StringField(required=True)
    space = ListField(EmbeddedDocumentField(Space))
