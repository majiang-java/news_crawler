import pymongo

class DBHelper(object):
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://118.24.3.198:27017/")
        self.mydb = self.myclient["databse"]
        self.mycol = self.mydb["bitcoin"]

    def insert(self,mydict):
        self.mycol.insert_one(mydict)
    
    def insert_many(self, mydicts):
        self.mycol.insert_many(mydicts)
