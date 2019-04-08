# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.data import FakeCollectingData
from Python.data_api import ApiCollectingData as Api

from random import randint, sample


class  DataDowloader:

    def __init__(self):
        self.fake = FakeCollectingData()
        api = Api()

    def restaurant(self):
        list_name = ('Oc Pizza Lyon',
                     'Oc Pizza Paris',
                     'Oc Pizza Marseille',
                     'Oc Pizza Genéve')
        # id = (autoIncrement)
        restaurant_name =sample(list_name, 1)
        key = restaurant_name
        return key

    def status(self):
        list_status = ('En court de préparation',
                       'Commande terminé',
                       'Commande en cours de livraison',
                       'Commande livré')
        id =self.fake.number_random(1, 9999)
        status = sample(list_status, 1)
        key = id, status
        return key

    def order(self):
        # id = (autoIncrement)
        product_type = ()
        date_order = ()
        key = product_type, date_order
        return key

    def bill(self):
        #id =(FK)
        date =self.fake.fake_date()
        product_type =()
        price = self.fake.number_random(1, 99)
        taxe_rate =()
        key = date, product_type, price, taxe_rate
        return key

    def payment(self):
        list_paiement = ('Espece',
                         'Carte bancaire',
                         'Cheque bancaire',
                         'Tiket restaurant')
        # id = (autoIncrement)
        mode = sample(list_paiement, 1)
        return mode

    def mail(self):
        # id = (autoIncrement)
        mail = self.fake.fake_mail()
        return mail

    def phone(self):
        id = (self.fake.number_random(1, 999))
        phone = self.fake.fake_telephone()
        key = id, phone
        return id, key

    def adress(self):
        # id = (autoIncrement)
        adress = (self.fake.adresse())
        zip =(self.fake.adresse_zip())
        country =(self.fake.adresse_country())
        complement = (self.fake.adresse_complement())

        key = adress, zip, country, complement
        return key

    def ingredient(self):
        # id = (autoIncrement)
        designation = ()
        weight = ()
        return None

    def type_product(self):
        id = (self.fake.number_random(1, 999))
        product_type = ()
        return None

    def product(self):
        # id = (autoIncrement)
        name = ()
        price = ()
        return None

    # Associate table

    def stock_product(self):
        name = ()
        weight = ()
        conditioning = ()
        quantity = ()
        return None

    def composition(self):
        quantity = ()
        return None

    def basket(self):
        # id = (autoIncrement)
        name = ()
        price = ()
        return None

    def generate_data(self):
        list_qualite = 'Gerant', 'Pizzaïolos','Hotesse', 'Livreur'
        for g in range(10):
            name = self.fake.first_name()
            last_name = self.fake.last_name()
            password = self.fake.random_password()
            adress = self.fake.adresse()
            zip = self.fake.adresse_zip()
            country = self.fake.adresse_country()
            complement = self.fake.adresse_complement()
            num_ss_employe = self.fake.number_random(1, 99999999999999)
            quality = sample(list_qualite, 1)
            date = self.fake.fake_date()
            status = self.status()
            mail = self.fake.fake_mail()
            id = self.fake.number_random(1, 999)
            phone = self.fake.fake_telephone()
            restaurant = self.fake.restaurant()
            key = (name, last_name, password,               # Actor_table
                   num_ss_employe, quality, date,    # Employe_table
                   id, status,                              # Status_table
                   adress, zip, country, complement,        # Adresse_table
                   mail,                                    # Mail_table
                   id, phone,                                # Phone_table
                   restaurant)                              # Restaurant_table
            return key

def main():
    """ Initialize the data collect """

    fake = DataDowloader()
    fake.generate_data()

    # api = ApiCollectingData()

    # join the data in the class

if __name__ == "__main__":
    main()