# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

from Python.config import CATEGORIES, ROYALE_PIZZA

import requests as req
from pprint import pprint

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
                return product

    def connect_and_dowload_per_barcode(self):
        """ Use the configuration for the connecting interface """
        product_barcode = []
        for barcode in ROYALE_PIZZA:
            bar_code = f"https://fr.openfoodfacts.org/api/v0/produit/{barcode}"
            config = {'tag_0': barcode}
            response = req.get(bar_code, params=config)
            products_section = response.json()
            products_barcode = products_section['product']
            return products_barcode

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

    def generate_data(self):
        product_ctagorie = self.connect_and_dowload_per_category()
        product_barcode = self.connect_and_dowload_per_barcode()

        id = self.barcode(product_barcode)
        name = self.name(product_barcode)
        category = self.category_barcode(product_barcode)
        deisgnation = self.designation(product_barcode)
        weight = self.weight(product_barcode)
        key_barcode = (id, name, category, deisgnation, weight)

        key_category = (id, name, category, deisgnation)
        if self.validate_the_data(key_category, product_ctagorie):
            id = self.barcode(product_ctagorie)
            name = self.name(product_ctagorie)
            category = self.sub_category(product_ctagorie)
            deisgnation = self.designation(product_ctagorie)
            key_category = (id, name, category, deisgnation)
        print('\n',
                  key_barcode, '\n',
                  key_category)
        return key_barcode, key_category

def main():
    """ Initialize the data collect """

    downloader = ApiCollectingData()

    # step_category = downloader.connect_and_dowload_per_category()
    # downloader.format_final_response(step_category)

    # downloader.connect_and_dowload_per_barcode()
    # downloader.connect_and_dowload_per_category()
    downloader.generate_data()

if __name__ == "__main__":
    main()


