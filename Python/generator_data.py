# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.faker_data import FakeCollectingData
from Python.dataclass_data import Restaurant, Address, Phone, Email, Actor

class GeneratorData:
    """

    """

    def __init__(self):
        self.fake = FakeCollectingData()

    # - status_list
    def gen_status_list(self):
        status_list = self.fake.fake_status(number=None)
        return status_list

    # - product_type
    def gen_product_type(self):
        product_type = self.fake.fake_product_type(number=None)
        return product_type

    # - payment_list
    def gen_payment_list(self):
        payment_list = self.fake.fake_payment(number=None)
        return payment_list

    def gen_restaurants(self, number=None):
        restaurant_address = [
            Restaurant(
                restaurant_name="OC Pizza Paris X",
                address=Address(
                    address="10 rue Oc",
                    zip_code="75 000",
                    city="Paris X em",
                    additional_address="",),
                phone=Phone(
                    phone="+0145486730",),
                email=Email(
                    mail="Oc_Pizza_Paris_Xem@Oc_pizza.com",)),

            Restaurant(
                restaurant_name="OC Pizza Paris XII",
                address=Address(
                    address="12 rue Oc",
                    zip_code="75 001",
                    city="Paris XII em",
                    additional_address="",),
                phone=Phone(
                    phone="+0145486731",),
                email=Email(
                    mail="Oc_Pizza_Paris_XIIem@Oc_pizza.com",))]

        if number is None or number >= len(restaurant_address):
            return restaurant_address
        return restaurant_address[number]


"""
Product: 
        product_name:
        product_price:
        ProductType_id:
        
Ingredient: 
        designation:
        weight:
 
 
ProductStock:
        Ingredients_id:
        Restaurants_id:
        name_product:
        weight:
        conditioning:
        quantity:

composition:
        Ingredients_id
        Products_id:
        quantity:

ShoppingCart:
        Orders_id:
        Products_id:
        article:
        quantity:
        price:
        
"""

#     def actors(self, number=1):
#         return [
#             Actor(
#                  restaurant_name="OC Pizza Paris X",
#                 #                 address=Address(
#                 #                     address="10 rue Oc",
#                 #                     zip_code="75 000",
#                 #                     city="Paris X em",
#                 #                     additional_address="",
#                 #                 ),
#                 #                 phone=Phone(
#                 #                     phone="+0145486730",
#                 #                 ),
#                 #                 email=Email(
#                 #                     mail="Oc_Pizza_Paris_Xem@Oc_pizza.com",
#                 #                 )),
#                 first_name=self.fake.fake_first_name(),
#                 last_name=self.fake.fake_last_name(),
#                 authentication_password=self.fake.fake_password(),
#
#                 address_id=Address(*self.fake.fake_address()),
#                 phone_id=Phone(
#                     phone=self.fake.fake_phone(),
#                 ),
#                 mail_id=Email(
#                     mail=self.fake.fake_mail(),
#                 )
#             )
#             for _ in range(number)
#         ]

def main():
    """ Initialize the data collect """
    gen = GeneratorData()

    # status = [Status(**data) for data in fake.fake_status(number=None)]

if __name__ == "__main__":
    main()
