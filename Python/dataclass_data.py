# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from dataclasses import dataclass
from decimal import Decimal


"""Information entity"""


@dataclass
class Mail:
    mail: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Phone:
    phone: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Address:
    address: str
    zip_code: str
    city: str
    additional_address: str
    # Id is AUTO_INCREMENT
    id: int = None


"""Actors entity"""


@dataclass
class Actor:
    first_name: str
    last_name: str
    authentication_password: str
    # Foreign key attribute
    Email_id: Mail
    Phone_id: Phone
    Address_id: Address
    # Id is AUTO_INCREMENT
    id: int = None


"""Restaurants entity"""


@dataclass
class Status:
    status: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Restaurant:
    restaurant_name: str
    # Foreign key attribute
    Address_id: Address
    Phone_id: Phone
    Mail_id: Mail
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Employee:
    social_security_numb: str
    quality: str
    date_entry: str
    # Foreign key attribute
    Status_id: Status
    Restaurant_id: Restaurant

    Actor_id: Actor
    # L'id des employes est une FK qui pointe ver l'Id des acteurs, donc == à "Actors_id"?
    id: int


"""Billing entity"""


@dataclass
class Payment:
    payment_mode: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Order:
    product_type: str
    order_date: str
    # Foreign key attribute
    Status_id: Status
    Actor_id: Actor
    Restaurant_id: Restaurant
    Address_id: Address
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Invoice:
    invoice_date: str
    product_type: str
    product_price: Decimal
    product_tax: float

    payment_id: int # J'ai un doute sur cet attribut, qui n'est pas une clef ni clef etrangere ni id en auto increment

    # Foreign key attribute
    Address_id: Address
    Phone_id: Phone
    Actor_id: Actor
    Order_id: Order
    # Id is AUTO_INCREMENT
    id: int = None


"""Stock entity"""


@dataclass
class Ingredient:
    designation: str
    weight: float
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class ProductType:
    product_type: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Product:
    product_name: str
    product_price: Decimal
    # Id is not AUTO_INCREMENT
    id: int = int


"""Associate stock entity"""


@dataclass
class ProductStock:
    # Foreign key attribute
    Ingredient_id: Ingredient
    Restaurant_id: Restaurant
    # Attribute
    name_product: str
    weight: float
    conditioning: str
    quantity: float

@dataclass
class Composition:
    # Foreign key attribute
    Ingredient_id: Ingredient
    Product_id: Product
    # Attribute
    quantity: float

@dataclass
class ShoppingCart:
    # Foreign key attribute
    Order_id: Order
    Product_id: Product
    # Attribute
    article: str
    quantity: int
    price: Decimal
