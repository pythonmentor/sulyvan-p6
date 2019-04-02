# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from faker import Faker
from random import randint, sample
fake = Faker("fr_FR")

class CreatingData:
    """
    Creating the fake data or not Product
    """

def first_name():
    name = fake.first_name()
    return name

def last_name():
    last_name = fake.last_name()
    return last_name

def fake_mail():
    mail = fake.email()
    return mail

def telephone():
    telephone = fake.telephone()
    return telephone

def number_random(count, count1):
    fake_number = randint(0, count1)
    return fake_number

def adress():
    random_num = str(number_random(1, 999))
    complement_list = 'App ' + random_num, 'Etage ' + random_num, 'Sonette ' + random_num
    numb = number_random(1, 9999)
    street = fake.street_name()
    code_postal = number_random(1, 9999)
    country = fake.city()
    complement = sample(complement_list, 1)
    key = numb, street, code_postal, country, complement
    return key

def fake_date():
    day = fake.day_of_month()
    month = fake.month_name()
    year = fake.year()
    key = day, month, year
    return key

def generate():
    list_qualite = 'Gerant', 'Pizzayolos', 'Hotesse', 'Livreur'
    list_statut = 'En court de préparation', 'Commande terminé', 'Commande en cours de livraison', 'Commande livré'
    list_paiement = 'Espece', 'Carte bancaire','Cheque bancaire', 'Tiket restaurant'
    for a in range(20):
        date = (fake_date())
        acteur = 'name :', first_name(), 'last_name :', last_name(), 'password :', str(number_random(1, 99099))
        adresse = adress()
        mail = 'mail :', fake_mail()
        telephone = 'telephone :', str(number_random(1, 99999999999))
        employe = acteur, 'qualité :', sample(list_qualite, 1), date, mail, telephone, adresse,
        restaurant = 'nom_restaurant :', "Oc_Pizza", adresse, telephone, mail
        statut = sample(list_statut, 1)
        paiement = sample(list_paiement, 1)
        prix = str(number_random(1, 99)) +'.'+ str(number_random(1, 99))
        key = ()
        print(key)
generate()



