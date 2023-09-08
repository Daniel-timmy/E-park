import uuid

from flask_login import UserMixin, LoginManager
from mongoengine import Document, StringField, EmailField, ImageField, DateTimeField, EmbeddedDocument, \
    EmbeddedDocumentField, ListField, IntField, BinaryField
from project import app

login_manager = LoginManager(app)


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


@login_manager.user_loader
def load_user(user_id):
    from project import db
    return db.get_obj(id=user_id)


class User(Document, UserMixin):
    uId = StringField(default=str(uuid.uuid4()))
    first_name = StringField(required=True)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    password_hash = StringField(required=False)
    vehicle_model = StringField(required=False)
    plate_number = StringField(required=False)
    vehicle_image = ImageField(required=False)
    receipts = ListField(EmbeddedDocumentField(Receipt))

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        from project import bcrypt
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, attempted_password):
        from project import bcrypt
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def get_id(self):
        return str(self.id)
