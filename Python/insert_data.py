# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.config import db
from Python.faker_data import FakeCollectingData
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

    def insert_restaurant_list(self, generate, fake):
        restaurant_address = []
        address_repo = AddressRepository(db)
        address = [Address(**data) for data in generate.restaurant_address(number=0)]
        zip_code = [Address(**data) for data in generate.restaurant_zip(number=0)]
        city = [Address(**data) for data in generate.rastaurant_city(number=0)]
        restaurant_address.append({'address': address,
                                   'zip_code': zip_code,
                                   'city': city,
                                   'additional_address': ''})
        address_repo.save_all(restaurant_address)
        # address_id = address_repo.last_id()

        # phone_repo = PhoneRepository(db)
        # phone = [Phone(**data) for data in generate.restaurant_phone(number=0)]
        # phone_repo.save_all(phone)
        # phone_id = phone_repo.last_id()

        # mail_repo = MailRepository(db)
        # mail = [Mail(**data) for data in generate.restaurant_mail(number=0)]
        # mail_repo.save_all(mail)
        # mail_id = mail_repo.last_id()

        # restaurant_repo = RestaurantRepository(db)
        # restaurant_name = [Restaurant(**data) for data in fake.fake_restaurant(number=0)]
        # restaurant.append({'restaurant_name': restaurant_name,
                           # 'Addresses_id': address_id,
                           # 'Phones_id': phone_id,
                           # 'Mail_id': mail_id})
        # restaurant_repo.save_all(restaurant)



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
    fake = FakeCollectingData()
    test = init.insert_restaurant_list(generate, fake)
    print(test)
if __name__ == "__main__":
    main()
