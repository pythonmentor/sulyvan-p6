# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Python.faker_data import FakeCollectingData
from Python import dataclass_data as table

from dataclasses import asdict
import records as rec


class Repository:
    """
    The class insert the data in database Oc Pizza
    """

    def __init__(self, db):
        """ Connect to Mysql database from the class DataBaseUser() """
        self.db = db
        self.table = table

    def save(self, instance):
        pass

    def save_all(self, collection):
        for instance in collection:
            self.save(instance)


"""Information SQL code"""


class MailRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Mail(mail)
            VALUES (:mail)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Mail 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Mail
            """).all(as_dict=True)
        return [self.table.Mail(**data) for data in rows]


class PhoneRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Phone(phone)
            VALUES (:phone)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Phone 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Phone
            """).all(as_dict=True)
        return [self.table.Phone(**data) for data in rows]


class AddressRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Address(address, 
                                zip_code, 
                                city, 
                                additional_address)
            VALUES (:address, 
                    :zip_code, 
                    :city, 
                    :additional_address)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Address 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Address
            """).all(as_dict=True)
        return [self.table.Address(**data) for data in rows]


"""Actors SQL code"""


class ActorRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Mail_id'] = instance.Mail.id
        data['Phone_id'] = instance.Phone.id
        data['Address_id'] = instance.Address.id
        self.db.query("""
            INSERT INTO Actor(first_name, 
                               last_name, 
                               authentication_password,
                               Mail_id, 
                               Phone_id,
                               Address_id)
            VALUES (:first_name, 
                    :last_name, 
                    :authentication_password,
                    :Mail_id, 
                    :Phone_id,
                    :Address_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Actor 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Actor
            """).all(as_dict=True)
        return [self.table.Actor(**data) for data in rows]


"""Restaurants SQL code"""


class StatusRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Status(status)
            VALUES (:status)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Status 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Status
            """).all(as_dict=True)
        return [self.table.Status(**data) for data in rows]


class RestaurantRepository(Repository):
    def save(self, instance):
        data = asdict(instance)
        data['Address_id'] = instance.Address.id
        data['Phone_id'] = instance.Phone.id
        data['Mail_id'] = instance.Mail.id
        self.db.query("""
            INSERT INTO Restaurant(restaurant_name, 
                                   Address_id,
                                   Phone_id,
                                   Mail_id)
            VALUES (:restaurant_name, 
                    :Address_id,
                    :Phone_id,
                    :Mail_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Restaurant 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Restaurant
            """).all(as_dict=True)
        return [self.table.Restaurant(**data) for data in rows]


class EmployeeRepository(Repository):
    def save(self, instance):
        data = asdict(instance)
        data['Status_id'] = instance.Status.id
        data['Restaurant_id'] = instance.Restaurant.id
        data['Actor_id'] = instance.Actor.id
        self.db.query("""
            INSERT INTO Employee(social_security_numb, 
                                 quality, 
                                 date_entry,
                                 Status_id,
                                 Restaurant_id,
                                 Actor_id)
            VALUES (:social_security_numb, 
                    :quality, 
                    :date_entry,
                    :Status_id,
                    :Restaurant_id,
                    :Actor_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Employee 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Employee
            """).all(as_dict=True)
        return [self.table.Employee(**data) for data in rows]


"""Billing SQL code"""


class PaymentRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Payment(payment_mode)
            VALUES (:payment_mode)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Payment 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Payment
            """).all(as_dict=True)
        return [self.table.Payment(**data) for data in rows]


class OrderRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Status_id'] = instance.Status.id
        data['Actor_id'] = instance.Actor.id
        data['Restaurant_id'] = instance.Restaurant.id
        data['Address_id'] = instance.Address.id
        self.db.query("""
            INSERT INTO Order(product_type, 
                              order_date,
                              Status_id,
                              Actor_id,
                              Restaurant_id,
                              Address_id)
            VALUES (:product_type, 
                    :order_date,
                    :Status_id,
                    :Actor_id,
                    :Restaurant_id,
                    :Address_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Order 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Order
            """).all(as_dict=True)
        return [self.table.Order(**data) for data in rows]


class InvoiceRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Address_id'] = instance.Address.id
        data['Phone_id'] = instance.Phone.id
        data['Actor_id'] = instance.Actor.id
        data['Order_id'] = instance.Order_.d
        self.db.query("""
            INSERT INTO Invoice(invoice_date, 
                                product_type, 
                                product_price, 
                                product_tax,
                                Address_id,
                                Phone_id,
                                Actor_id,
                                Order_id)
            VALUES (:invoice_date, 
                    :product_type, 
                    :product_price, 
                    :product_tax,
                    :Address_id,
                    :Phone_id,
                    :Actor_id,
                    :Order_id)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Invoice 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Invoice
            """).all(as_dict=True)
        return [self.table.Invoice(**data) for data in rows]


"""Stock SQL code"""


class IngredientRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Ingredient(designation, 
                                   weight)
            VALUES (:designation, 
                    :weight)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Ingredient
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Ingredient
            """).all(as_dict=True)
        return [self.table.Ingredient(**data) for data in rows]


class ProductTypeRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO ProductType(product_type)
            VALUES (:product_type)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM ProductType
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM ProductType
            """).all(as_dict=True)
        return [self.table.ProductType(**data) for data in rows]


class ProductRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Product(product_name, 
                                product_price)
            VALUES (:product_name, 
                    :product_price)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Product
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Product
            """).all(as_dict=True)
        return [self.table.Product(**data) for data in rows]


"""Associate SQL code"""


class ProductStockRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Ingredient_id'] = instance.Ingredient.id
        data['Restaurant_id'] = instance.Restaurant.id
        self.db.query("""
            INSERT INTO ProductStock(Ingredient_id,
                                     Restaurant_id,
                                     name_product, 
                                     weight, 
                                     conditioning, 
                                     quantity)
            VALUES (:Ingredient_id,
                    :Restaurant_id,
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
        return [self.table.ProductStock(**data) for data in rows]


class CompositionRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Ingredient_id'] = instance.Ingredient.id
        data['Product_id'] = instance.Product.id
        self.db.query("""
            INSERT INTO Composition(Ingredient_id,
                                    Product_id,
                                    quantity)
            VALUES (:Ingredient_id,
                    :Product_id,
                    :quantity)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Composition 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Composition
            """).all(as_dict=True)
        return [self.table.Composition(**data) for data in rows]


class ShoppingCartRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Order_id'] = instance.Order.id
        data['Product_id'] = instance.Product.id
        self.db.query("""
            INSERT INTO ShoppingCart(Order_id,
                                     Product_id,
                                     article, 
                                     quantity, 
                                     price)
            VALUES (:Order_id,
                    :Product_id,
                    :article, 
                    :quantity, 
                    :price)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM ShoppingCart 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM ShoppingCart
            """).all(as_dict=True)
        return [self.table.ShoppingCart(**data) for data in rows]


def main():

    # db = \
    rec.Database("mysql+mysqlconnector://"
                 "OCP6:OC_STUDENT@localhost/"
                 "Oc_Pizza?charset=utf8mb4")
    # create = Repository(db)


if __name__ == "__main__":
    main()
