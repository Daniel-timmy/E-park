from dotenv import load_dotenv, find_dotenv
from mongoengine import connect
import os
from project.models.user import User
from project.models.admin import Admin
from project.models.parking_lot import Lot

from pymongo import MongoClient

classes = {'User': User, 'Lot': Lot}


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
        print('saved')

    def get_one(self, email=None, cls=None):
        """"""
        if email is not None and cls is not None:
            if cls in classes.values():
                obj = cls.objects.get(email=email)
                return obj
            else:
                return None

    def get_obj(self, id):
        """"""
        # if cls not in classes.values():
        #     return None

        all_cls = db.get_all(User)
        for value in all_cls.values():
            if value.uId == id:
                return value
        return None

    def get_lot(self, name):
        """"""
        # if cls not in classes.values():
        #     return None

        all_cls = db.get_all(Lot)
        for value in all_cls.values():
            if value.lot_name == name:
                return value
        return None

    def get_all(self, cls=None):
        """"""
        o_dict = {}
        b_dict = {}
        if cls in classes.values():
            objs = cls.objects()
            for obj in objs:
                o_dict[obj.uId] = obj
            b_dict.update(o_dict)
            for key, value in b_dict.items():
                print(f'Key: {key}, Value: {value}')

            return b_dict


    def update_space_status(self,uLot, cUser, sStatus, rStatus, time_left):
        """"""
        uLot.update(push__status=sStatus)
        print('lot update succesfull')
        cUser.update(push__status=rStatus)
        print('receipt update succesfull')
        uLot.update(push__time_left=time_left)




    def update_user_receipt(self, uId, receipts):
        """"""
        obj = User.objects.get(uId=uId)
        obj.update(push__receipts=receipts)
        print("success")

    def delete(self):
        """"""


db = DB()
user = User(first_name='timmy455')
res = db.get_one(cls=User)
db.insert(user)
res = db.get_one(cls=User)
print(res)
