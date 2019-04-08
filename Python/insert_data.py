# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Python.data import FakeCollectingData
from Python.final_data import DataDowloader

import records as rec
from random import randint, sample


class InsertData:
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
         self.db = rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza_db?charset=utf8mb4")
         return self.db

    def insert_actor(self):
        """Table list / VALUES"""
        name = self.fake.first_name()
        last_name = self.fake.last_name()
        password = self.fake.random_password()

        self.db.query("""INSERT INTO acteur
              (nom, prenom, password)
              VALUES (:name, :last_name, :password)
              ; """,name=name, last_name=last_name, password=password)

    def insert_employe(self):
        list_qualite = 'Gerant', 'Pizzayolos','Hotesse', 'Livreur'
        num_ss_employe = self.fake.number_random(1, 99999999999999)
        quality = sample(list_qualite, 1)
        date = self.fake.fake_date()

        self.db.query("""INSERT INTO employe
              (num_ss_employe, qualite, date_entree)
              VALUES (:num_ss_employe, :quality, :date)
              ; """, num_ss_employe=num_ss_employe, quality=quality, date=date)

    def insert_status(self):
        list_status = ('En court de préparation',
                       'Commande terminé',
                       'Commande en cours de livraison',
                       'Commande livré')
        id =self.fake.number_random(1, 9999)
        status = sample(list_status, 1)

        self.db.query("""INSERT INTO statut
              (id, statut)
              VALUES (:id, :status)
              ; """, id=id, status=status)

    def insert_adress(self):
        adress = self.fake.adresse()
        zip = self.fake.adresse_zip()
        country = self.fake.adresse_country()
        adress2 = self.fake.adresse_complement()

        self.db.query("""INSERT INTO adresse
              (adresse, code_postal, ville, adresse_compl)
              VALUES (:adress, :zip, :country, :adress2)
              ; """, adress=adress, zip=zip, country=country, adress2=adress2)

    def insert_mail(self):
        mail = self.fake.fake_mail()
        self.db.query("""INSERT INTO mail
              (mail)
              VALUES (:mail)
              ; """, mail=mail)

    def insert_phone(self ):
        id = self.fake.number_random(1, 999)
        phone = self.fake.fake_telephone()

        self.db.query("""INSERT INTO telephone
           (id, telephone)
              VALUES (:id, :phone)
              ; """, id=id, phone=phone)

    def insert_restaurant(self):
        restaurant = self.fake.restaurant()
        self.db.query("""INSERT INTO restaurant
              (nom_restaurant)
              VALUES (:name)
              ; """, name=restaurant)

    def insert_commande(self):
        self.db.query("""INSERT INTO commande
              (type,_produit, date_commande)
              VALUES (
              WHERE );""", )

    def insert_facture(self):
            self.db.query("""INSERT INTO facture
              (date_facture, type_produit, prix, tva)
              VALUES (
              WHERE );""", )

    def insert_pay(self):
        self.db.query("""INSERT INTO paiement
              (mode)
              VALUES (
              WHERE); """, )

    def insert_ingredient(self):
        self.db.query("""INSERT INTO ingredient
              (designation, poids)
              VALUES (
              WHERE); """, )

    def insert_product(self):
        self.db.query("""INSERT INTO produit
              (nom, prix)
              VALUES (
              WHERE );""", )

    def insert_product_type(self):
        self.db.query("""INSERT INTO typeproduit
           (id, type_produit)
              VALUES (
              WHERE );""", )

    def insert_associate_table(self):

        # Single product, multiply the quantity
        self.db.query("""INSERT INTO stockProduit
              (nom, poids, conditionnement, quantite) 
              VALUES ( WHERE); """, )

        # insert composition
        self.db.query("""INSERT INTO composition
              (quantite)
              VALUES ( WHERE );""", )

        # insert basket line and multiply price
        self.db.query("""INSERT INTO pannier
              (article, quantite, prix)
              VALUES ( WHERE); """, )

    def insert_rows(self, finals):
        """ Completion the data row per row """
        for final in finals:
            self.insert_actor()
            self.insert_employe()
            self.insert_status()
            self.insert_adress()
            self.insert_mail()
            self.insert_phone()
            self.insert_restaurant()
        return True




def main():
    downloader = DataDowloader()
    finals = downloader.generate_data()
    print(finals)

    db = rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza_db?charset=utf8mb4")
    create = InsertData(db)

    create.insert_rows(finals)

if __name__ == "__main__":
    main()
