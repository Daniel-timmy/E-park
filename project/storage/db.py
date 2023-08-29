from dotenv import load_dotenv, find_dotenv
from mongoengine import connect
import os
from project.models.user import User
from project.models.booking import Booking
from project.models.parking_lot import Lot

from pymongo import MongoClient

classes = {'User': User, 'Booking': Booking, 'Lot': Lot}


class DB:

    def __init__(self):
        load_dotenv(find_dotenv())
        password = os.environ.get('PWD')
        connection_string = f'mongodb+srv://timmy:{password}@clustere.s3vbyer.mongodb.net/?retryWrites=true&w=majority'
        self.client = MongoClient(connection_string)
        self.db = self.client.get_database('E-park')
        connect(db='E-park', host=connection_string)
        print('successful connection')

    def insert(self, obj):
        """"""
        obj.save()

    def get_one(self, id=None, cls=None):
        """"""
        if id is not None:
            if cls in classes.values():
                obj = cls.objects(id=id)
                return obj
            else:
                return None

    def get_all(self, cls=None):
        """"""
        o_dict = {}
        if cls in classes.values():
            objs = cls.objects()
            for obj in objs:
                o_dict[str(obj.id)] = obj
            return o_dict
        else:
            return None

    def update_booking_status(self):
        """"""

    def update_user_profile(self):
        """"""

    def delete(self):
        """"""


db = DB()
user = User(first_name='dan')
res = db.get_one(cls=User)
db.insert(user)
print(res)
