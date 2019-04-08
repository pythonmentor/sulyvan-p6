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

    def first_name(self):
        name = fake.first_name()
        return name

    def last_name(self):
        last_name = fake.last_name()
        return last_name

    def random_password(self):
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/*.:?!"
        password = ""
        for i in range(10):
            password = password + char[randint(0, len(char) - 4)]
        return password

    def fake_mail(self):
        mail = fake.email()
        return mail

    def fake_telephone(self):
        prefix = "+3356",  "+0176", "+0450"
        form = sample(prefix, 1)
        number = self.number_random(1, 999999)
        telephone = str(form ) + number
        return telephone

    def adresse(self):
        numb = self.number_random(1, 9999)
        street = fake.street_name()
        return numb, street

    def adresse_zip(self):
        code_postal = self.number_random(1, 9999)
        return code_postal

    def adresse_country(self):
        country = fake.city()
        return country

    def adresse_complement(self):
        random_num = str(self.number_random(1, 99))
        complement_list = ('',
                          'App ' + random_num,
                          'Etage ' + random_num,
                          'Sonette ' + random_num,
                           '')
        complement = sample(complement_list, 1)
        return complement

    def fake_date(self):
        day = fake.day_of_month()
        month = fake.month_name()
        year = fake.year()
        key = day, month, year
        return key

    def fake_price(self):
        price = str(self.number_random(1, 99)) + '.' + str(self.number_random(1, 99) + "€")
        return price

    def number_random(self, count, count1):
        fake_number = randint(count, count1)
        return str(fake_number)

    def restaurant(self):
        list_name = ('Oc Pizza Lyon',
                     'Oc Pizza Paris',
                     'Oc Pizza Marseille',
                     'Oc Pizza Genéve')
        # id = (autoIncrement)
        restaurant_name =sample(list_name, 1)
        key = restaurant_name
        return key

def main():
    """ Initialize the data collect """

    fake_data = FakeCollectingData()
    # fake_data.test()

if __name__ == "__main__":
    main()
