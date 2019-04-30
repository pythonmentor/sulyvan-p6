# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.faker_data import FakeCollectingData
from Python.dataclass_data import *

import records as rec
from dataclasses import asdict


class Repository:
    """
    The class insert the data in database Oc Pizza
    """

    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.fake = FakeCollectingData()
        self.db = db
        self.database = self.connect_mysql()

    def connect_mysql(self):
        """ Connecting in the database """
        self.db = rec.Database("mysql+mysqlconnector://"
                               "OCP6:OC_STUDENT@localhost/"
                               "Oc_Pizza?charset=utf8mb4")
        return self.db

    def save(self, instance):
        pass

    def save_all(self, collection):
        for instance in collection:
            self.save(instance)


"""Informations SQL code"""


class EmailsRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Emails(mail)
            VALUES (:mail)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Emails 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Emails
            """).all(as_dict=True)
        return [Emails(**data) for data in rows]


class PhonesRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Phones(phone)
            VALUES (:phone)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Phones 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Phones
            """).all(as_dict=True)
        return [Phones(**data) for data in rows]


class AdressesRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Adresses(address, 
                                zip_code, 
                                city, 
                                additional_address)
            VALUES (:address, 
                    :zip_code, 
                    :city, 
                    :additional_address)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Adresses 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Adresses
            """).all(as_dict=True)
        return [Adresses(**data) for data in rows]


"""Actors SQL code"""


class ActorsRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Emails_id'] = instance.Emails.id
        data['Phones_id'] = instance.Phones.id
        data['Adresses_id'] = instance.Adresses.id
        self.db.query("""
            INSERT INTO Actors(first_name, 
                               last_name, 
                               authentication_password,
                               Emails_id, 
                               Phones_id,
                               Adresses_id)
            VALUES (:first_name, 
                    :last_name, 
                    :authentication_password,
                    :Emails_id, 
                    :Phones_id,
                    :Adresses_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Actors 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Actors
            """).all(as_dict=True)
        return [Actors(**data) for data in rows]


"""Restaurants SQL code"""


class StatusRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Statuses(status)
            VALUES (:status)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Statuses 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Statuses
            """).all(as_dict=True)
        return [Statuses(**data) for data in rows]


class RestaurantsRepository(Repository):
    def save(self, instance):
        data = asdict(instance)
        data['Addresses_id'] = instance.Addresses.id
        data['Phones_id'] = instance.Phones.id
        data['Mails_id'] = instance.Mails.id
        self.db.query("""
            INSERT INTO Restaurants(restaurant_name, 
                                    Addresses_id,
                                    Phones_id,
                                    Mails_id)
            VALUES (:restaurant_name, 
                    :Addresses_id,
                    :Phones_id,
                    :Mails_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Restaurants 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Restaurants
            """).all(as_dict=True)
        return [Restaurants(**data) for data in rows]


class EmployeesRepository(Repository):
    def save(self, instance):
        data = asdict(instance)
        data['Status_id'] = instance.Status.id
        data['Restaurants_id'] = instance.Restaurants.id

        data['Actors_id'] = instance.Actors.id
        self.db.query("""
            INSERT INTO Employees(social_security_numb, 
                                  quality, 
                                  date_entry,
                                  Status_id,
                                  Restaurants_id,
                                  
                                  Actors_id)
            VALUES (:social_security_numb, 
                    :quality, 
                    :date_entry,
                    Status_id,
                    Restaurants_id,
                    
                    Actors_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Employees 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Employees
            """).all(as_dict=True)
        return [Employees(**data) for data in rows]


"""Billing SQL code"""


class PaymentsRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Payments(payment_mode)
            VALUES (:payment_mode)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Payments 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Payments
            """).all(as_dict=True)
        return [Payments(**data) for data in rows]


class OrdersRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Status_id'] = instance.Status.id
        data['Actors_id'] = instance.Actors.id
        data['Restaurants_id'] = instance.Restaurants.id
        data['Adresses_id'] = instance.Adresses.id
        self.db.query("""
            INSERT INTO Orders(product_type, 
                               order_date,
                               Status_id,
                               Actors_id,
                               Restaurants_id,
                               Adresses_id)
            VALUES (:product_type, 
                    :order_date,
                    :Status_id,
                    :Actors_id,
                    :Restaurants_id,
                    :Adresses_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Orders 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Orders
            """).all(as_dict=True)
        return [Orders(**data) for data in rows]


class InvoicesRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Adresses_id'] = instance.Adresses.id
        data['Phones_id'] = instance.Phones.id
        data['Actors_id'] = instance.Actors.id
        data['Orders_id'] = instance.Orders_.d
        self.db.query("""
            INSERT INTO Invoices(invoices_date, 
                                 product_type, 
                                 product_price, 
                                 product_tax,
                                 Adresses_id,
                                 Phones_id,
                                 Actors_id,
                                 Orders_id)
            VALUES (:invoices_date, 
                    :product_type, 
                    :product_price, 
                    :product_tax,
                    :Adresses_id,
                    :Phones_id,
                    :Actors_id,
                    :Orders_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Invoices 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Invoices
            """).all(as_dict=True)
        return [Invoices(**data) for data in rows]


"""Stock SQL code"""


class IngredientsRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Ingredients(designation, 
                                    weight)
            VALUES (:designation, 
                    :weight)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Ingredients 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Ingredients
            """).all(as_dict=True)
        return [Ingredients(**data) for data in rows]


class ProductTypesRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO ProductTypes(product_type)
            VALUES (:product_type)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM ProductTypes 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM ProductTypes
            """).all(as_dict=True)
        return [ProductTypes(**data) for data in rows]


class ProductsRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Products(product_name, 
                                product_price)
            VALUES (:product_name, 
                    :product_price)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Products 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Products
            """).all(as_dict=True)
        return [Products(**data) for data in rows]


"""Associate SQL code"""


class ProductStockRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Ingredients_id'] = instance.Ingredients.id
        data['Restaurants_id'] = instance.Restaurants.id
        self.db.query("""
            INSERT INTO ProductStock(Ingredients_id,
                                     Restaurants_id,
                                     name_product, 
                                     weight, 
                                     conditioning, 
                                     quantity)
            VALUES (:Ingredients_id,
                    :Restaurants_id,
                    :name_product, 
                    :weight, 
                    :conditioning, 
                    :quantity)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM ProductStock 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM ProductStock
            """).all(as_dict=True)
        return [ProductStock(**data) for data in rows]


class CompositionsRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Ingredients_id'] = instance.Ingredients.id
        data['Products_id'] = instance.Product.id
        self.db.query("""
            INSERT INTO Compositions(Ingredients_id,
                                     Products_id,
                                     quantity)
            VALUES (:Ingredients_id,
                    :Products_id,
                    :quantity)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Compositions 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Compositions
            """).all(as_dict=True)
        return [Compositions(**data) for data in rows]


class ShoppingCartRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Orders_id'] = instance.Orders.id
        data['Products_id'] = instance.Product.id
        self.db.query("""
            INSERT INTO ShoppingCart(Orders_id,
                                     Products_id,
                                     article, 
                                     quantity, 
                                     price)
            VALUES (:Orders_id,
                    :Products_id,
                    :article, 
                    :quantity, 
                    :price)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Shopping_Cart 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Shopping_Cart
            """).all(as_dict=True)
        return [ShoppingCart(**data) for data in rows]


def main():

    # db = \
    rec.Database("mysql+mysqlconnector://"
                 "OCP6:OC_STUDENT@localhost/"
                 "Oc_Pizza?charset=utf8mb4")
    # create = Repository(db)


if __name__ == "__main__":
    main()
