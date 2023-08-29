from mongoengine import EmbeddedDocument, EmbeddedDocumentField, IntField, Document, StringField, DateTimeField, \
    ImageField, ListField


class Space(EmbeddedDocument):
    space = StringField(required=True)
    time_left = IntField(required=True)
    status = StringField(required=True)  # reserved, occupied, empty


class Lot(Document):
    lot_name = StringField(required=True)
    space = ListField(EmbeddedDocumentField(Space))
