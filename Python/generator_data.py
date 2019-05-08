# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.faker_data import FakeCollectingData


class GeneratorData:
    """

    """

    def __init__(self):
        self.fake = FakeCollectingData()
#
    def test_fake(self):
        add = self.restaurant_address()
        zip = self.restaurant_zip()
        city = self.rastaurant_city()
        # mail = self.restaurant_mail()
        # phone = self.restaurant_phone()
        key = add, zip, city
        return key

# I. Generate the static data

    def restaurant_address(self, number=None):
        address =[]
        address_list = ("'10' 'rue Oc'",
                        "'12' 'rue Oc'")
        if number == 0:
            address.append({'address': address_list[0]})
            return address
        elif number == 1:
            address.append({'address_2': address_list[1]})
            return address
        address.append({'address': address_list[0],
                        'address_2':address_list[1]})
        return address

    def restaurant_zip(self, number=None):
        zip = []
        zip_list = ('75 000',
                    '75 001')
        if number == 0:
             zip.append({'zip_code': zip_list[0]})
             return zip
        elif number == 1:
            zip.append({'zip_code_2': zip_list[1]})
            return zip
        zip.append({'zip_code': zip_list[0],
                    'zip_code_2':zip_list[1]})
        return zip

    def rastaurant_city(self, number=None):
        city_list = ('Paris X em',
                     'Paris XII em')
        city = []
        if number == 0:
            city.append({'city': city_list[0]})
            return city
        elif number == 1:
            city.append({'city_2': city_list[1]})
            return city
        city.append({'city': city_list[0],
                    'city_2':city_list[1]})
        return city

    def restaurant_phone(self, number=None):
        phone = []
        phone_list = ('+0145486730',
                      '+0145486731')
        if number == 0:
            phone.append({'phone': phone_list[0]})
            return phone
        elif number == 1:
            phone.append({'phone_2': phone_list[1]})
            return phone
        phone.append({'phone': phone_list[0],
                      'phone_2':phone_list[1]})
        return phone

    def restaurant_mail(self, number=None):
        mail = []
        mail_list = ('Oc_Pizza_Paris_Xem@Oc_pizza.com',
                     'Oc_Pizza_Paris_Xem@Oc_pizza.com')
        if number == 0:
            mail.append({'mail': mail_list[0]})
            return mail
        elif number == 1:
            mail.append({'mail_2': mail_list[1]})
            return mail
        mail.append({'mail': mail_list[0],
                     'mail_2': mail_list[1]})
        return mail

# - status_list
    def gen_status_list(self):
        status_list = self.fake.fake_status(number=None)
        return status_list

# - product_type
    def gen_product_type(self):
        product_type = self.fake.fake_product_type(number=None)
        return product_type

# - paiement_list
    def gen_payment_list(self):
        payment_list = self.fake.fake_payment(number=None)
        return payment_list

# I. Generate Restaurant

# II. Generate Employee data

# III. Generate Actors data

# IV. Generate the Products and Products stock data

# V. Generate the Administrative data

    def generator_final(self):
        # print(self.test_fake())
        # print('1 :', self.gen_restaurant_list())
        # self.gen_status_list()
        # print('3 :', self.gen_quality_list())
        # print('4 :', self.gen_payment_list())

        # print(self.gen_address())
        # print(self.gen_aname_list())
        # print(self.gen_aname_list())
        # print(self.gen_aname_list())
        # print(self.gen_aname_list())
        pass


def main():
    """ Initialize the data collect """
    gen = GeneratorData()
    status = gen.test_fake()

    # status = [Status(**data) for data in fake.fake_status(number=None)]
    print(status)

if __name__ == "__main__":
    main()
