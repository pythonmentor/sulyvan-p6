# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python import data_api
from Python import data

import records as rec


class InsertData:
    """
    The class insert the data in database Oc Pizza
    """

    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.db = db
        self.database = InsertData(self.db)

    def insert_actor(self, name, last_name, password):
        """Table list / VALUES"""
        self.db.query("""INSERT INTO acteur
              (nom, prenom, password)
              VALUES (:name, :last_name, :password)
              ; """,name=name, last_name=last_name, password=password)

    def insert_employe(self, num_ss, quality, date):
        self.db.query("""INSERT INTO employe
              (id_ss_employe, qualite, date_entree)
              VALUES (:num_ss, :quality, :date)
              ; """, num_ss=num_ss, quality=quality, date=date)

    def insert_status(self, id, status):
        self.db.query("""INSERT INTO statut
              (id, statut)
              VALUES (:id, :status)
              ; """, id=id, status=status)

    def insert_adress(self, adress, zip, country, adress2):
        self.db.query("""INSERT INTO adresse
              (adresse, code_postal, ville, adresse_compl)
              VALUES (:adress, :zip, :country, :adress2)
              ; """, adress=adress, zip=zip, country=country, adress2=adress2)

    def insert_mail(self, mail):
        self.db.query("""INSERT INTO mail
              (mail)
              VALUES (:mail)
              ; """, mail=mail)

    def insert_phone(self, id, phone):
        self.db.query("""INSERT INTO telephone
           (id, telephone)
              VALUES (:id, :phone)
              ; """, id=id, phone=phone)

    def insert_restaurant(self, name):
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

    def insert_to_oreder(self):
        # organize the insert data in database
        pass


def main():

    rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza_db?charset=utf8mb4")


if __name__ == "__main__":
    main()
