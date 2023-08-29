from mongoengine import Document, StringField, EmailField, ImageField, DateTimeField, EmbeddedDocument, \
    EmbeddedDocumentField, ListField, IntField
import bcrypt


class Receipt(EmbeddedDocument):
    status = StringField(required=True)
    lot = StringField(required=True)
    space = StringField(required=True)
    duration = DateTimeField(required=True)
    date = DateTimeField(required=False)
    model = StringField(required=True)
    plate_number = StringField(required=True)
    tType = StringField(required=True)
    amount = IntField(required=True)


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    password_hash = StringField(required=True)
    vehicle_model = StringField(required=True)
    plate_number = StringField(required=True)
    vehicle_image = ImageField(required=False)
    receipt = ListField(EmbeddedDocumentField(Receipt))

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
