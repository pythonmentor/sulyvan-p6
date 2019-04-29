# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from faker import Faker
from random import randint, sample

fake = Faker("fr_FR")


class FakeCollectingData:
    """
    Creating the fake data or not Product
    """
    def __init__(self):
        """ The constructor is not used here """
        pass

# Adress attribute section:
    def fake_adress(self):
        numb = self.number_random(1, 9999)
        street = fake.street_name()
        return numb, street

    def fake_zip(self):
        code_postal = self.number_random(1, 9999)
        return code_postal

    def fake_city(self):
        city = fake.city()
        return city

    def fake_complement(self):
        random_num = str(self.number_random(1, 99))
        complement_list = ('',
                          'apartment ' + random_num,
                          'Floor ' + random_num,
                          'Bell ' + random_num,
                           '')
        complement = sample(complement_list, 1)
        return tuple(complement)

# Civility attribute section:
    def fake_first_name(self):
        first_name = fake.first_name()
        return first_name

    def fake_last_name(self):
        last_name = fake.last_name()
        return last_name

# Password attribute section:
    def fake__password(self):
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/*.:?!"
        password = ""
        for i in range(10):
            password = password + char[randint(0, len(char) - 4)]
        return password

# Mail attribute section:
    def fake_mail(self):
        mail = fake.email()
        return mail

# Phone attribute section:
    def fake_telephone(self):
        prefix = "+3356",  "+0176", "+0450"
        form = sample(prefix, 1)
        number = self.number_random(1, 999999)
        telephone = str(form) + number
        return telephone

# Restaurant attribute section:
    def fake_restaurant(self):
        list_name = ('Oc Pizza Lyon',
                     'Oc Pizza Paris',
                     'Oc Pizza Marseille',
                     'Oc Pizza Genéve')
        restaurant_name =sample(list_name, 1)
        key = restaurant_name
        return key

# Status attribute section:
    def fake_status(self):
        list_status = ('En court de préparation',
                       'Commande terminé',
                       'Commande en cours de livraison',
                       'Commande livré')
        id =self.number_random(1, 9999)
        status = sample(list_status, 1)
        key = id, status
        return tuple(key)

# Employee attribute section:
    def fake_quality(self):
        list_qualite = 'Gerant', 'Pizzaïolos','Hotesse', 'Livreur'
        quality = sample(list_qualite, 1)
        return tuple(quality)

    def fake_date(self):
        day = fake.day_of_month()
        month = fake.month_name()
        year = fake.year()
        key = day, month, year
        return key

# ' ' attribute section:

    def fake_price(self):
        price = str(self.number_random(1, 99)) + '.' + str(self.number_random(1, 99) + "€")
        return price

    def fake_payment(self):
        list_paiement = ('Espece',
                         'Carte bancaire',
                         'Cheque bancaire',
                         'Tiket restaurant')
        # id = (autoIncrement)
        mode = sample(list_paiement, 1)
        return tuple(mode)

    def number_random(self, count, count1):
        fake_number = randint(count, count1)
        return str(fake_number)


#     def key(self):
#
#         name = self.first_name()
#         last_name = self.last_name()
#         password = self.random_password()
#
#         num_ss_employe = self.number_random(1, 99999999999999)
#         quality = self.quality()
#         date = self.fake_date()
#
#         status_id =self.number_random(1, 999)
#         status = self.status()
#
#         adress = self.adresse()
#         zip = self.adresse_zip()
#         country = self.adresse_country()
#         adress2 = self.adresse_complement()
#
#         mail = self.fake_mail()
#
#         phone_id = self.number_random(1, 999)
#         phone = self.fake_telephone()
#
#         restaurant_name = self.restaurant()
#
#         actor = (name, last_name, password,
#                  adress, zip, country, adress2,
#                  mail,
#                  phone_id, phone)
#         employe = (name, last_name, password,
#                    adress, zip, country, adress2,
#                    mail,
#                    phone_id, phone,
#                    num_ss_employe, quality, date)
#         key = tuple(actor)
#         print(employe)
#         return  key

def main():
    """ Initialize the data collect """

    fake_data = FakeCollectingData()

if __name__ == "__main__":
    main()
