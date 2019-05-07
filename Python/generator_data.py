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
        key = self.fake.fake_telephone()
        return key


# I. Generate the static data
# - name_list = ('Oc Pizza Paris Xem', 'Oc Pizza Paris XIIem')
    def restaurant_address(self, number=None):
        address_list = []
        address = ("'10', 'rue Oc'", "'12', 'rue Oc'")
        zip = ('75 000', '75 001')
        city = ('Paris X em', 'Paris XII em')
        address_list.append({'address': address[number],
                             'zip_code': zip[number],
                             'city': city[number],
                             'additional_address': ''})
        return address_list


    def restaurant_phone(self, number=None):
        phone_list = []
        phone = ('+0145486730', '+0145486731')
        phone_list.append({'phone': phone[number]})
        return phone_list

    def restaurant_mail(self, number=None):
        mail_list = []
        mail = ('Oc_Pizza_Paris_Xem@Oc_pizza.com', 'Oc_Pizza_Paris_Xem@Oc_pizza.com')
        mail_list.append({'mail': mail[number]})
        return mail_list

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


    def gen_address(self):
        address = self.fake.fake_address()
        return address

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

    def gen_status(self):
        pass
        # status = [Status(**data) for data in fake_import.fake_status(number=None)]
        # return status



def main():
    """ Initialize the data collect """
    gen = GeneratorData()
    status = gen.restaurant_address( )

    # status = [Status(**data) for data in fake.fake_status(number=None)]
    print(status)

if __name__ == "__main__":
    main()
