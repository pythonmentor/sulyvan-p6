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

    def number_random(self, count, count1):
        fake_number = randint(count, count1)
        return str(fake_number)

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
        random_num = str(self.number_random(1, 999))
        complement_list = ('', \
                          'App ' + random_num,
                          'Etage ' + random_num,
                          'Sonette ' + random_num, '')
        complement = sample(complement_list, 1)
        return complement

    def fake_date(self):
        day = fake.day_of_month()
        month = fake.month_name()
        year = fake.year()
        key = day, month, year
        return key


def main():
    """ Initialize the data collect """

    fake_data = FakeCollectingData()


if __name__ == "__main__":
    main()
