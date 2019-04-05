# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.data import FakeCollectingData
from Python.data_api import ApiCollectingData as Api

from random import randint, sample


class  JoinTheData:

    def __init__(self):
        self.fake = FakeCollectingData()
        api = Api()

    def actor(self):
        # id = (autoIncrement)
        name = self.fake.first_name()
        last_name = self.fake.last_name()
        password = self.fake.random_password()
        key = name, last_name, password
        return key

    def employee(self):
        list_qualite = ('Gerant', 'Pizzayolos',
                        'Hotesse', 'Livreur')
        num_ss_employe = self.fake.number_random(1, 99999999999999)
        quality = sample(list_qualite, 1)
        date = self.fake.fake_date()
        key = num_ss_employe, quality, date
        return key

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
        key = phone
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
        for g in range(10):
          actor =  self.actor()
          employe = self.employee()
          adress = self.adress()
          restaurant = self.restaurant()
          status = self.status()
          order = self.order()
          bill = self.bill()
          payment = self.payment()
          mail = self.mail()
          phone = self.phone()
          # ----------------
          type_product = self.type_product()
          product = self.product()
          stock_product = self.stock_product()
          composition = self.composition()
          basket = self.basket()
          # key = employe, actor, employe, adress, restaurant,
          key = employe, actor, adress, mail, phone
          print(key)
          return key

def main():
    """ Initialize the data collect """

    fake = JoinTheData()
    fake.generate_data()
    # api = ApiCollectingData()

    # join the data in the class

if __name__ == "__main__":
    main()