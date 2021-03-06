# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from dataclasses import dataclass
from decimal import Decimal


"""Information entity"""


@dataclass
class Email:
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
    mail: Email
    phone: Phone
    address: Address
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
    address: Address
    phone: Phone
    email: Email
    # Id is AUTO_INCREMENT
    id: int = None


@dataclass
class Employee:
    social_security_numb: str
    quality: str
    date_entry: str
    # Foreign key attribute
    status_id: Status
    restaurant_id: Restaurant
    actor_id: Actor
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
    status_id: Status
    actor_id: Actor
    restaurant_id: Restaurant
    address_id: Address
    # Id is AUTO_INCREMENT
    id: int = None


@dataclass
class Invoice:
    invoice_date: str
    product_type: str
    product_price: Decimal
    product_tax: float

    payment_id: int

    # Foreign key attribute
    address_id: Address
    phone_id: Phone
    actor_id: Actor
    order_id: Order
    # Id is AUTO_INCREMENT
    id: int = None


"""Stock entity"""


@dataclass
class ProductType:
    product_type: str
    # Id is AUTO_INCREMENT
    id: int = None


@dataclass
class Product:
    product_name: str
    product_price: Decimal
    id: int

    # Foreign key attribute
    ProductType: ProductType
    # Id is not AUTO_INCREMENT


@dataclass
class Ingredient:
    product_name: str
    weight: float
    # Id is AUTO_INCREMENT
    id: int = None


"""Associate stock entity"""


@dataclass
class ProductStock:
    # Foreign key attribute
    ingredients_id: Ingredient
    restaurants_id: Restaurant
    # Attribute
    weight: float
    quantity: float


@dataclass
class Composition:
    # Foreign key attribute
    ingredients_id: Ingredient
    products_id: Product
    # Attribute
    quantity: float


@dataclass
class ShoppingCart:
    # Foreign key attribute
    orders_id: Order
    products_id: Product
    # Attribute
    article: str
    quantity: int
    price: Decimal
