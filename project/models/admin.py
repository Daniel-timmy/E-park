import uuid
from datetime import datetime

from mongoengine import Document, StringField, DateTimeField, EmailField, IntField

# from project import login_manager
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     from project import db
#     return db.get_obj(id=user_id)


class Admin(Document):
    uId = StringField(default=str(uuid.uuid4()))
    first_name = StringField(required=True)
    last_name = StringField(required=False)
    email = EmailField(required=False)
    admin_code = IntField(required=True)
    created_at = DateTimeField(default=datetime.utcnow(), required=False)
    password_hash = StringField(required=False)

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
        return str(self.uId)
