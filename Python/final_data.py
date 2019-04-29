# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from dataclasses import dataclass

"""Voici les dataclass qui correspond parfaitement au modéle physique de donnèes
   est-il possible de faire une class "Entity" pour les dataclass?"""

"""Informations entity"""
@dataclass
class Emails:
    mail: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Phones:
    phone: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Adresses:
    address: str
    zip_code: str
    city: str
    additional_address : str
    # Id is AUTO_INCREMENT
    id: int = None


"""Actors entity"""
@dataclass
class Actors:
    first_name: str
    last_name: str
    authentication_password: str
    # Foreign key attribute
    Emails_id: Emails
    Phones_id: Phones
    Adresses_id: Adresses
    # Id is AUTO_INCREMENT
    id: int = None


"""Restaurants entity"""
@dataclass
class Statuses:
    status: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Restaurants:
    restaurant_name: str
    # Foreign key attribute
    Addresses_id: Adresses
    Phones_id: Phones
    Mails_id: Emails
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Employees:
    social_security_numb: str
    quality: str
    date_entry: str
    # Foreign key attribute
    Status_id: Statuses
    Restaurants_id: Restaurants

    Actors_id: Actors
    # Lid des employes est une FK qui pointe ver l'Id des acteurs, donc == à "Actors_id"?
    id: int = Actors_id


"""Billing entity"""
@dataclass
class Payments:
    payment_mode: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Orders:
    product_type: str
    order_date: str
    # Foreign key attribute
    Status_id: Statuses
    Actors_id: Actors
    Restaurants_id: Restaurants
    Adresses_id: Adresses
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Invoices:
    invoices_date: str
    product_type: str
    product_price: float
    product_taxe: float

    payments_id: int # J'ai un doute sur cet attribut, qui n'est pas une clef ni clef etrangere ni id en auto increment

    # Foreign key attribute
    Adresses_id: Adresses
    Phones_id: Phones
    Actors_id: Actors
    Orders_id: Orders
    # Id is AUTO_INCREMENT
    id: int = None


"""Stock entity"""
@dataclass
class Ingredients:
    designation: str
    weight: float
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class ProductTypes:
    product_type: str
    # Id is AUTO_INCREMENT
    id: int = None

@dataclass
class Products:
    product_name: str
    product_price: float
    # Id is not AUTO_INCREMENT
    id: int = int


"""Associate stock entity"""
@dataclass
class Product_Stock:
    # Foreign key attribute
    Ingredients_id: Ingredients
    Restaurants_id: Restaurants
    # Attribute
    name_product: str
    weight: float
    conditioning: str
    quantity: float

@dataclass
class Compositions:
    # Foreign key attribute
    Ingredients_id: Ingredients
    Products_id: Products
    # Attribute
    quantity: float

@dataclass
class Shopping_Cart:
    # Foreign key attribute
    Orders_id: Orders
    Products_id: Products
    # Attribute
    article: str
    quantity: int
    price: float

