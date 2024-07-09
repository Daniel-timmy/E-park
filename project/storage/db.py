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
        try:
            obj.save()
        except:
            raise

    def get_one(self, email=None, cls=None):
        """"""
        if email is not None and cls is not None:
            if cls in classes.values():
                obj = cls.objects.get(email=email)
                return obj
            else:
                return None

    def get_obj(self, id):
        """Get User object by the provided id

        """
        user = User.objects(uId=id)
        return user[0]


    def get_lot(self, name):
        """"""
        requested_lot = Lot.objects(lot_name=name)
        return requested_lot

        # all_cls = db.get_all(Lot)
        # for value in all_cls.values():
        #     if value.lot_name == name:
        #         return value
        # return None

    def get_all(self, cls=None):
        """"""
        o_dict = {}
        b_dict = {}

        if cls in classes.values():
            objs = cls.objects()
            for obj in objs:
                o_dict[obj.uId] = obj
            b_dict.update(o_dict)
            return b_dict
        else:
            return None
    def get_empty_space_count(self):
        """Gets the total number of empty 
        spaces per parking lot"""
        pipeline = [
            {"$unwind": "$space"},
            {"$match": {"space.status": "empty"}},
            {"$count": "empty_spaces_count"}
        ]

        count = Lot.objects.aggregate(*pipeline)
        empty_spaces = 0
        for cnt in count:
            return cnt["empty_spaces_count"]

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
