# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records as rec


class InsertData:
    """
    The class insert the data in database Oc Pizza
    """

    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.db = db
        self.database = InsertData(self.db)


    def inseert_table(self):
        """Table list / VALUES"""

        self.db.query("""INSERT INTO acteur
              (nom, prenom, password)
              VALUES (
              WHERE); """, )

        self.db.query("""INSERT INTO adresse
              (adresse, code_postal, ville, adresse_compl)
              VALUES (
              WHERE);""", )

        self.db.query("""INSERT INTO commande
              (type,_produit, date_commande)
              VALUES (
              WHERE );""", )

        self.db.query("""INSERT INTO employe
              (id_ss_employe, qualite, date_entree)
              VALUES (
              WHERE); """, )

        self.db.query("""INSERT INTO facture
              (date_facture, type_produit, prix, tva)
              VALUES (
              WHERE );""", )

        self.db.query("""INSERT INTO ingredient
              (designation, poids)
              VALUES (
              WHERE); """, )

        self.db.query("""INSERT INTO mail
              (mail)
              VALUES (
              WHERE );""", )

        self.db.query("""INSERT INTO paiement
              (mode)
              VALUES (
              WHERE); """, )

        self.db.query("""INSERT INTO produit
              (nom, prix)
              VALUES (
              WHERE );""", )

        self.db.query("""INSERT INTO restaurant
              (nom_restaurant)
              VALUES (
              WHERE """, )

        self.db.query("""INSERT INTO statut
              (id, statut)
              VALUES (
              WHERE );""", )

        self.db.query("""INSERT INTO telephone
           (id, telephone)
              VALUES (
              WHERE); """, )

        self.db.query("""INSERT INTO typeproduit
           (id, type_produit)
              VALUES (
              WHERE );""", )

        # ASSOCIATE_TABLE #

        self.db.query("""INSERT INTO stockProduit
              (nom, poids, conditionnement, quantite)
              VALUES ( WHERE """, )

        self.db.query("""INSERT INTO composition
              (quantite)
              VALUES ( WHERE );""", )

        self.db.query("""INSERT INTO pannier
              (article, quantite, prix)
              VALUES ( WHERE); """, )

def main():
    db = rec.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza_db?charset=utf8mb4")

if __name__ == "__main__":
    main()
