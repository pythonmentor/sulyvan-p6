# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Python.final_data import JoinTheData

import records as rec


class InsertData:
    """
    The class insert the data in database Oc Pizza
    """


    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.db = db
        self.database = self.connect_mysql()



    def connect_mysql(self):
         """ Connecting in the database """
         self.db = rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza_db?charset=utf8mb4")
         return self.db


    def insert_actor(self, name, last_name, password, *args):
        """Table list / VALUES"""
        self.db.query("""INSERT INTO acteur
              (nom, prenom, password)
              VALUES (:name, :last_name, :password)
              ; """,name=name, last_name=last_name, password=password)

    def insert_employe(self, num_ss, quality, date, *args):
        self.db.query("""INSERT INTO employe
              (id_ss_employe, qualite, date_entree)
              VALUES (:num_ss, :quality, :date)
              ; """, num_ss=num_ss, quality=quality, date=date)

    def insert_status(self, id, status, *args):
        self.db.query("""INSERT INTO statut
              (id, statut)
              VALUES (:id, :status)
              ; """, id=id, status=status)

    def insert_adress(self, adress, zip, country, adress2, *args):
        self.db.query("""INSERT INTO adresse
              (adresse, code_postal, ville, adresse_compl)
              VALUES (:adress, :zip, :country, :adress2)
              ; """, adress=adress, zip=zip, country=country, adress2=adress2)

    def insert_mail(self, mail, *args):
        self.db.query("""INSERT INTO mail
              (mail)
              VALUES (:mail)
              ; """, mail=mail)

    def insert_phone(self, id, phone, *args):
        self.db.query("""INSERT INTO telephone
           (id, telephone)
              VALUES (:id, :phone)
              ; """, id=id, phone=phone)

    def insert_restaurant(self, name, *args):
        self.db.query("""INSERT INTO restaurant
              (nom_restaurant)
              VALUES (:name)
              ; """, name=name)

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
            self.insert_actor(*final)
            self.insert_employe(*final)
            self.insert_status(*final)
            self.insert_adress(*final)
            self.insert_mail(*final)
            self.insert_phone(*final)
            self.insert_restaurant(*final)
        return True


def main():

    downloader = JoinTheData()
    finals = downloader.generate_data()

    print(finals)
    db = rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza_db?charset=utf8mb4")
    create = InsertData(db)

    create.insert_rows(finals)

if __name__ == "__main__":
    main()
