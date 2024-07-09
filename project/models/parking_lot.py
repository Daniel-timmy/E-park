import uuid

from mongoengine import EmbeddedDocument, EmbeddedDocumentField, IntField, Document, StringField, ListField


class Space(EmbeddedDocument):
    uId = StringField(default=str(uuid.uuid4()))
    space_name = StringField(required=True)
    time_left = IntField(required=True)  # in minutes
    status = StringField(required=True)  # reserved, occupied, empty
    # reserved_time_slot = ListField()  [[start_hour, end_hour]]
    reserved_day_slot = ListField()  # [[start_day, end_day]]


class Lot(Document):
    uId = StringField(default=str(uuid.uuid4()))
    lot_name = StringField(required=True)
    space = ListField(EmbeddedDocumentField(Space))


