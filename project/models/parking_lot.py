import uuid

from mongoengine import EmbeddedDocument, EmbeddedDocumentField, IntField, Document, StringField, DateTimeField, \
    ImageField, ListField


class Space(EmbeddedDocument):
    uId = StringField(default=str(uuid.uuid4()))
    space = StringField(required=True)
    time_left = IntField(required=True)  # in minutes
    status = StringField(required=True)  # reserved, occupied, empty


class Lot(Document):
    uId = StringField(default=str(uuid.uuid4()))
    lot_name = StringField(required=True)
    space = ListField(EmbeddedDocumentField(Space))
