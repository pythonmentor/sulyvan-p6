# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


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

    def last_id(self):
        rows = self.db.query("""
            SELECT LAST_INSERT_ID() AS id
            """)
        for row in rows:
            return row['id']


"""Information SQL code"""


class EmailRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Email(id, mail)
            VALUES (:id, :mail)
            """, **data)

        instance.id = self.last_id()

    def get(self, id):
        rows = self.db.query("""
            SELECT * FROM Email WHERE id = :id
            """, id=id).as_dict()
        for row in rows:
            return self.table.Email(**row)

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Email
            """).all(as_dict=True)
        return [self.table.Email(**data) for data in rows]


class PhoneRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Phone(id, 
                              phone)
            VALUES (:id, 
                    :phone)
            """, **data)
        instance.id = self.db.query("""
            SELECT id FROM Phone 
            ORDER BY id DESC LIMIT 1
            """).all(as_dict=True)[0]['id']

        instance.id = self.last_id()

    def get(self, id):
        rows = self.db.query("""
            SELECT * FROM Phone WHERE id = :id
            """, id=id).as_dict()
        for row in rows:
            return self.table.Phone(**row)

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Phone
            """).all(as_dict=True)
        return [self.table.Phone(**data) for data in rows]


class AddressRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Address(id,
                                address, 
                                zip_code, 
                                city, 
                                additional_address)
            VALUES (:id,
                    :address, 
                    :zip_code, 
                    :city, 
                    :additional_address)
            """, **data)

        instance.id = self.last_id()

    def get(self, id):
        rows = self.db.query("""
                SELECT * FROM Address WHERE id = :id
                """, id=id).as_dict()
        for row in rows:
            return self.table.Email(**row)

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Address
            """).all(as_dict=True)
        return [self.table.Address(**data) for data in rows]


"""Actors SQL code"""


class ActorRepository(Repository):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.address = AddressRepository(self.db)
        self.phones = PhoneRepository(self.db)
        self.emails = EmailRepository(self.db)

    def save(self, instance):
        self.address.save(instance.address)
        self.phones.save(instance.phone)
        self.emails.save(instance.mail)
        data = asdict(instance)
        data['Emails_id'] = instance.mail.id
        data['Phones_id'] = instance.phone.id
        data['Addresses_id'] = instance.address.id
        self.db.query("""
            INSERT INTO Actor(first_name, 
                              last_name, 
                              authentication_password,
                              Emails_id, 
                              Phones_id,
                              Addresses_id)
            VALUES (:first_name, 
                    :last_name, 
                    :authentication_password,
                    :Emails_id, 
                    :Phones_id,
                    :Addresses_id)
            """, **data)

        instance.id = self.last_id()

    def get(self, id):
        rows = self.db.query("""
            SELECT * FROM Actor WHERE id = :id
            """, id=id).as_dict()

        for actor in rows:
            self._get_foreign_objects(actor)
            return self.table.Restaurant(**actor)

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Actor
            """).all(as_dict=True)
        for actor in rows:
            self._get_foreign_objects(actor)
        return [self.table.Actor(**data) for data in rows]

    def _get_foreign_objects(self, actor):
        actor['address'] = self.address.get(actor['Addresses_id'])
        del actor['Addresses_id']
        actor['phone'] = self.phones.get(actor['Phones_id'])
        del actor['Phones_id']
        actor['email'] = self.emails.get(actor['Emails_id'])
        del actor['Emails_id']


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.addresses = AddressRepository(self.db)
        self.phones = PhoneRepository(self.db)
        self.emails = EmailRepository(self.db)

    def save(self, instance):
        self.addresses.save(instance.address)
        self.phones.save(instance.phone)
        self.emails.save(instance.email)

        data = asdict(instance)
        data['Addresses_id'] = instance.address.id
        data['Phones_id'] = instance.phone.id
        data['Emails_id'] = instance.email.id
        self.db.query("""
            INSERT INTO Restaurant(restaurant_name, 
                                   Addresses_id,
                                   Phones_id,
                                   Emails_id)
            VALUES (:restaurant_name, 
                    :Addresses_id,
                    :Phones_id,
                    :Emails_id)
            """, **data)

        instance.id = self.last_id()

    def get(self, id):

        rows = self.db.query("""
                SELECT * FROM Restaurant WHERE id = :id
                """, id=id).as_dict()

        for restaurant in rows:
            self._get_foreign_objects(restaurant)
            return self.table.Restaurant(**restaurant)

    def get_all(self):

        rows = self.db.query("""
            SELECT * FROM Restaurant
            """).all(as_dict=True)

        for restaurant in rows:
            self._get_foreign_objects(restaurant)
        return [self.table.Restaurant(**data) for data in rows]

    def _get_foreign_objects(self, restaurant):
        restaurant['address'] = self.addresses.get(restaurant['Addresses_id'])
        del restaurant['Addresses_id']
        restaurant['phone'] = self.phones.get(restaurant['Phones_id'])
        del restaurant['Phones_id']
        restaurant['email'] = self.emails.get(restaurant['Emails_id'])
        del restaurant['Emails_id']


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


"""Stock SQL code"""


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

    def get(self, type_product_id):
        rows =  self.db.query("""
            SELECT * FROM ProductType 
            WHERE id = :type_product
            """, type_product=type_product_id).all(as_dict=True)
        return [self.table.ProductType(**data) for data in rows][0]

    def get_by_name(self, product_type):
        rows =  self.db.query("""
            SELECT * FROM ProductType 
            WHERE product_type = :product_type
            """, product_type=product_type).all(as_dict=True)
        return [self.table.ProductType(**data) for data in rows][0]


class ProductRepository(Repository):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_types = ProductTypeRepository(self.db)

    def save(self, instance):
        self.product_types.save(instance.ProductType)
        data = asdict(instance)
        data['ProductType_id'] = instance.ProductType.id

        self.db.query("""
            INSERT INTO Product(id,
                                product_name, 
                                product_price,
                                ProductType_id)
            VALUES (:id,
                    :product_name, 
                    :product_price,
                    :ProductType_id)
            """, **data)

    def get(self, id):
        rows = self.db.query("""
            SELECT * FROM ProductType WHERE id = :id
            """, id=id).as_dict()
        for row in rows:
            self._get_foreign_objects(row)
            return self.table.Product(**row)

    def get_all(self):
        rows = self.db.query("""
            SELECT * FROM Product
            """).all(as_dict=True)
        return [self.table.Product(**data) for data in rows]

    def _get_foreign_objects(self, product):
        product['ProductType'] = self.product_types.get(product['ProductType_id'])
        del product['ProductType_id']


class test_insert(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Product(id,
                                product_name, 
                                product_price,
                                ProductType_id)
            VALUES (:id,
                    :product_name, 
                    :product_price,
                    :ProductType_id);
            """, **data)

    def pop_id_product_type(self, tag):
        return self.db.query("""
            SELECT id FROM producttype
            WHERE product_type = :tag;
            """, tag=tag).all(as_dict=True)


class IngredientRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        self.db.query("""
            INSERT INTO Ingredient(product_name, 
                                   weight)
            VALUES (:product_name, 
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


"""Associate SQL code"""


class ProductStockRepository(Repository):

    def save(self, instance):
        data = asdict(instance)
        data['Ingredient_id'] = instance.Ingredient.id
        data['Restaurant_id'] = instance.Restaurant.id
        self.db.query("""
            INSERT INTO ProductStock(Ingredient_id,
                                     Restaurant_id,
                                     weight, 
                                     quantity)
            VALUES (:Ingredient_id,
                    :Restaurant_id,
                    :weight, 
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
        data['Order_id'] = instance.Order.id
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


def main():

    db = rec.Database("mysql+mysqlconnector://"
                      "OCP6:OC_STUDENT@localhost/"
                      "Oc_Pizza?charset=utf8mb4")
    EmailRepository(db)    # create = Repository(db) pop_id_product_type

    test = test_insert(db)
    print(test.pop_id_product_type('Boisson'))

if __name__ == "__main__":
    main()
