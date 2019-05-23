# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.config import db
from Python.faker_data import FakeCollectingData
from Python.generator_data import GeneratorData
from Python.dataclass_data import (Status, ProductType, Payment)
from Python.instance_data import (StatusRepository, ProductTypeRepository, PaymentRepository,
                                  RestaurantRepository, ActorRepository, ProductRepository)

class InsertData:
    """

    """

    def __init__(self):
        self.db = db

# I. Insert the static data

    def drop_and_create(self):
        self.db.query("""
            DROP TABLE `oc_pizza`.`actor`, `oc_pizza`.`address`,
            `oc_pizza`.`composition`, `oc_pizza`.`email`,
            `oc_pizza`.`employee`, `oc_pizza`.`ingredient`,
            `oc_pizza`.`invoice`, `oc_pizza`.`order`, `oc_pizza`.`payment`,
            `oc_pizza`.`phone`, `oc_pizza`.`product`, `oc_pizza`.`productstock`,
            `oc_pizza`.`producttype`, `oc_pizza`.`restaurant`,
            `oc_pizza`.`shoppingcart`, `oc_pizza`.`status`;
            """)


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
        restaurants = RestaurantRepository(db)
        restaurants.save_all(generate.restaurants())

    def insert_actor_list(self, generate):
        actors = ActorRepository(db)
        actors.save_all(generate.actors(20))

    def insert_product(self, generate):
        product = ProductRepository(db)
        product.save_all(generate.generate_product())


    def customer_insert(self):
        customer = ['restaurant_id',
                    'actor_attribute',
                    'address_attribute',
                    'mail_attribute',
                    'phone_attribute',
                    'shopping_cart_attribute',]
        pass

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

    # init.insert_product_type(generate)
    init.insert_product(generate)


if __name__ == "__main__":
    main()
