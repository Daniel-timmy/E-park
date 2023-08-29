import os
from pymongo import MongoClient
from mongoengine import connect, StringField, IntField, Document
from dotenv import load_dotenv, find_dotenv


class User(Document):
    name = StringField()
    age = IntField()


class DB:

    def __init__(self):
        load_dotenv(find_dotenv())
        password = os.environ.get('PWD')
        connection_string = f'mongodb+srv://timmy:{password}@clustere.s3vbyer.mongodb.net/test?retryWrites=true&w=majority'
        self.client = MongoClient(connection_string)
        self.db = self.client.get_database('test_mongoengine')  # Replace with your desired database name

        connect(db='test_mongoengine', host=connection_string)

    def insert_data(self, data):
        user = User(**data)
        user.save()

    def find_data(self, query):
        return User.objects(**query)

    # Add other CRUD methods as needed


# Example usage
if __name__ == "__main__":
    db_instance = DB()

    # data_to_insert = {"name": "Alice", "age": 28}
    # db_instance.insert_data(data_to_insert)

    query = {"age__gt": 25}
    result = db_instance.find_data(query)
    for user in result:
        print(user.name, type(user.age), type(str(user.id)))
