# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


from Python.config import CATEGORIES, ROYALE_PIZZA

import requests as req


class ApiCollectingData:
    """
        This class has the responsibility of collecting a certain number
        of products, in selected categories, thus to give a valid
        structure for the insertion in the database
    """

    def __init__(self):
        """ The constructor is not used here """
        pass

    def connect_and_dowload_per_category(self):
        """ Use the configuration for the connecting interface """
        product_categories = []
        # Address OpenFooFact.org the API FR locating
        api = "https://fr.openfoodfacts.org/cgi/search.pl"
        for category in CATEGORIES:
            # This config for  for connecting API
            config = {"action": "process",
                      "tagtype_0": "categories",
                      'tag_0': category,
                      "tag_contains_0": "contains",
                      "page_size": 5,
                      "json": 1}
            response = req.get(api, params=config)
            results = response.json()
            products_section = results['products']
            for product in products_section:
                product['main_category'] = category
                product_categories.extend(products_section)
            # pprint(product_categories)
        return product_categories

    def format_final_response(self, all_products):
        """ Formatted the response just harvest the categories selected """
        product_final = []
        keys = ['id',
                'product_name_fr',
                'main_category',
                'generic_name_fr']
        for product in all_products:
            if self.validate_the_data(keys, product):

                id = self.barcode(product)
                product_name = self.name(product)
                product_type = self.sub_category(product)
                designation = self.designation(product)

                key = (id,
                       product_name,
                       product_type,
                       designation)
                formatting = key
                product_final.append(formatting)
                print('id :', int(id), '\n',
                      'product_name :', product_name.upper(), '\n',
                      'product_type :', product_type, '\n',
                      'designation :', designation.upper(), '\n',
                      f"Nous avons récupéré "
                      f"{len(product_final)} "
                      f"produits", '\n'*2)
        return product_final

    def connect_and_dowload_per_barcode(self):
        """ Use the configuration for the connecting interface """
        product_barcode = []
        for barcode in ROYALE_PIZZA:
            bar_code = (f"https://fr.openfoodfacts.org/api/v0/produit/" 
                        f"{barcode}")
            config = {'tag_0': barcode}
            response = req.get(bar_code, params=config)
            products_section = response.json()
            products_barcode = products_section['product']

            ingredients_id = self.barcode(products_barcode)
            name_product = self.name(products_barcode)
            weight = self.weight(products_barcode)

            categories = self.category_barcode(products_barcode)
            designation = self.designation(products_barcode)

            key_barcode = (ingredients_id,
                           name_product.upper(),
                           designation,
                           categories.upper(),
                           weight)
            formatting = key_barcode
            product_barcode.append(formatting)
            print('id_produit :', int(ingredients_id), '\n',
                  'name_product :', name_product.upper(), '\n',
                  # 'présent dans :', categories, '\n',
                  'designation :', designation.upper(), '\n',
                  'weight : ', weight, '\n',
                  f"Nous avons récupéré {len(product_barcode)} produits", '\n' * 2)
        return product_barcode

    def barcode(self, attribute):
        barcode = attribute['id']
        return barcode

    def name(self, attribute):
        name = attribute['product_name_fr']
        return name

    def sub_category(self, attribute):
        sub_category = attribute['main_category']
        return sub_category

    def category_barcode(self, attribute):
        sub_category = attribute['categories']
        return sub_category

    def designation(self, attribute):
        designation = attribute['generic_name_fr']
        return designation

    def weight(self, attribute):
        weight = attribute['quantity']
        return weight

    def validate_the_data(self, keys, products_section):
        """ Validate the complete fields """
        for key in keys:
            if key not in products_section or not products_section[key]:
                return False
        return True


def main():
    """ Initialize the data collect """
    downloader = ApiCollectingData()

    all_products = downloader.connect_and_dowload_per_barcode()
    # downloader.format_final_response(all_products)
    downloader.name(['product_name_fr'])


if __name__ == "__main__":
    main()

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
"""
    type, id, name, poids, 
    SCHEMA TON GENERATE DATA FOR INSERT:
    I. class ProductType:
        product_type: str
        # Id is AUTO_INCREMENT

    II. class Product:
        product_name: str
        product_price: Decimal
        # Foreign key attribute
        ProductType_id = ProductType
        # Id is not AUTO_INCREMENT
        id: int = int

    III. class Ingredient:
        product_name: str
        weight: float
        # Id is AUTO_INCREMENT

    IV. class ProductStock:
        # Foreign key attribute
        ingredients_id: Ingredient
        restaurants_id: Restaurant
        # Attribute
        name_product: str
        weight: float
        OR
        quantity: float

    V. class Composition:
        # Foreign key attribute
        ingredients_id: Ingredient
        products_id: Product
        # Attribute
        quantity: float

    VI. class ShoppingCart:
        # Foreign key attribute
        orders_id: Order
        products_id: Product
        # Attribute
        article: str
        quantity: int
        price: Decimal
"""

