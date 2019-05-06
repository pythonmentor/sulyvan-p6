# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Python.config import db
# from Python.dataclass_data import Status
from Python.generator_data import GeneratorData
from Python.dataclass_data import (Status, ProductType, Payment,
                                   Restaurant, Address,
                                   Mail, Phone)
from Python.instance_data import (StatusRepository, ProductTypeRepository, PaymentRepository,
                                  RestaurantRepository, AddressRepository,
                                  MailRepository, PhoneRepository)

class InsertData:
    """

    """

    def __init__(self):
        self.db = db

# I. Insert the static data

    def insert_status_list(self, generate):
        status_repo = StatusRepository(db)
        status = [Status(**data) for data in generate.gen_status_list()]
        status_repo.save_all(status)

    def insert_product_type(self, generate):
        repo =ProductTypeRepository(db)
        product_type = [ProductType(**data) for data in generate.gen_product_type()]
        repo.save_all(product_type)

    def insert_payment_list(self, generate):
        payment_repo = PaymentRepository(db)
        payment = [Payment(**data) for data in generate.gen_payment_list()]
        payment_repo.save_all(payment)

    def insert_restaurant_list(self, generate):
        name_repo = RestaurantRepository(db)
        restaurant = [Restaurant(**data) for data in generate.gen_restaurant_list()]
        name_repo.save_all(restaurant)

        address_repo = AddressRepository(db)
        address = [Address(**data) for data in generate.gen_restaurant_list()]
        address_repo.save_all(address)

        mail_repo = MailRepository(db)
        mail = [Mail(**data) for data in generate.gen_restaurant_list()]
        mail_repo.save_all(mail)

        phone_repo = PhoneRepository(db)
        phone = [Phone(**data) for data in generate.gen_restaurant_list()]
        phone_repo.save_all(phone)

# II. Insert Employee data
# -

# III. Insert Actors data
# -

# IV. Insert the Products and Products stock data
# -

# V. Insert the Administrative data
# -


def main():
    """ Initialize the data collect """
    init = InsertData()
    generate = GeneratorData()

    init.insert_restaurant_list(generate)

if __name__ == "__main__":
    main()
