# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Python.data import FakeCollectingData

import records as rec
from dataclasses import asdict, dataclass



class Repository:
    """
    The class insert the data in database Oc Pizza
    """

    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.fake = FakeCollectingData()
        self.db = db
        self.database = self.connect_mysql()

    def connect_mysql(self):
         """ Connecting in the database """
         self.db = rec.Database("mysql+mysqlconnector:/"
                                "/OCP6:OC_STUDENT@localhost/Oc_Pizza?charset=utf8mb4")
         return self.db

    def save(self, instance):
        pass

    def save_all(self, collection):
        for instance in collection:
            self.save(instance)


class StatusRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Statuses(status)
            VALUES (:status)
            """, **data )
        instance.id = self.db.query("""
            SELECT id FROM Statuses ORDER BY id DESC LIMIT 1
            """).all(asdict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Statuses
            """).all(asdict=True)
        return [Statuses(**data) for data in rows]


def main():

    downloader = FakeCollectingData()

    db = rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza?charset=utf8mb4")
    create = Repository(db)

if __name__ == "__main__":
    main()
