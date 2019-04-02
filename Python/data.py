# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from faker import Faker
from random import randint, sample

fake = Faker("fr_FR")


class CreatingFakeData:
    """
    Creating the fake data or not Product
    """
    def __init__(self):
        """ The constructor is not used here """
        pass

    def first_name(self):
        name = fake.first_name()
        return name

    def last_name(self):
        last_name = fake.last_name()
        return last_name

    def fake_mail(self):
        mail = fake.email()
        return mail

    def telephone(self):
        telephone = fake.telephone()
        return telephone

    def number_random(self, count, count1):
        fake_number = randint(0, count1)
        return fake_number

    def adress(self):
        random_num = str(self.number_random(1, 999))
        complement_list = 'App ' + random_num, \
                          'Etage ' + random_num, \
                          'Sonette ' + random_num
        numb = self.number_random(1, 9999)
        street = fake.street_name()
        code_postal = self.number_random(1, 9999)
        country = fake.city()
        complement = sample(complement_list, 1)
        key = numb, street, code_postal, country, complement
        return key

    def fake_date(self):
        day = fake.day_of_month()
        month = fake.month_name()
        year = fake.year()
        key = day, month, year
        return key

    def generate(self):
        list_qualite = 'Gerant', 'Pizzayolos', 'Hotesse', 'Livreur'
        list_statut = 'En court de préparation', 'Commande terminé', \
                      'Commande en cours de livraison', 'Commande livré'
        list_paiement = 'Espece', 'Carte bancaire',\
                        'Cheque bancaire', 'Tiket restaurant'
        for a in range(20):
            date = (self.fake_date())
            acteur = 'name :', self.first_name(), \
                     'last_name :', self.last_name(), \
                     'password :', str(self.number_random(1, 99099))
            adresse = self.adress()
            mail = 'mail :', self.fake_mail()
            telephone = 'telephone :', str(self.number_random(1, 99999999999))
            employe = acteur, \
                      'qualité :', sample(list_qualite, 1), \
                      date, mail, telephone, adresse,
            restaurant = 'nom_restaurant :', "Oc_Pizza", \
                         adresse, telephone, mail
            statut = sample(list_statut, 1)
            paiement = sample(list_paiement, 1)
            prix = str(self.number_random(1, 99)) +'.'+ str(self.number_random(1, 99))
            key = (telephone)
            print(key)
            return key


def main():
    """ Initialize the data collect """

    fake_data = CreatingFakeData()
    fake_data.generate()


if __name__ == "__main__":
    main()
