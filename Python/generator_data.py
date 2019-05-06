# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.faker_data import FakeCollectingData
from Python.dataclass_data import Status
from Python.instance_data import StatusRepository

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
    def gen_restaurant_list(self):
        restaurant_list = self.fake.fake_restaurant()
        name_1 = restaurant_list[-1]
        address_1 = '12', 'rue Oc',
        zip_1 = '75 000'
        city_1 = 'Paris X em'
        mail_1 = 'Oc_Pizza_Paris_Xem@Oc_pizza.com'
        phone_1 = '+0145486730'
        name_2 = restaurant_list[0]
        address_2 = '14', 'rue Oc'
        zip_2 = '75 001'
        city_2 = 'Paris XII em'
        mail_2 = 'Oc_Pizza_Paris_Xem@Oc_pizza.com'
        phone_2 = '+0145486731'
        oc_1 = ('X :',
                name_1,
                address_1, zip_1, city_1,
                mail_1, phone_1)
        oc_2 = ('XII :',
                name_2,
                address_2, zip_2, city_2,
                mail_2, phone_2)
        return (name_1, address_1, zip_1, city_1, mail_1, phone_1,
                name_2, address_2, zip_2, city_2, mail_2, phone_2)

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
    status = gen.gen_product_type()

    # status = [Status(**data) for data in fake.fake_status(number=None)]
    print(status)

if __name__ == "__main__":
    main()
