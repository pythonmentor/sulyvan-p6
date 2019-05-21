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
        keys = ['id',
                'product_name_fr',
                'main_category',
                'generic_name_fr']
        for product in all_products:
            if self.validate_the_data(keys, product):
                return product

    def connect_and_dowload_per_barcode(self):
        """ Use the configuration for the connecting interface """
        for barcode in ROYALE_PIZZA:
            bar_code = (f"https://fr.openfoodfacts.org/api/v0/produit/" 
                        f"{barcode}")
            config = {'tag_0': barcode}
            response = req.get(bar_code, params=config)
            products_section = response.json()
            products_barcode = products_section['product']
            return products_barcode

    def validate_the_data(self, keys, products_section):
        """ Validate the complete fields """
        for key in keys:
            if key not in products_section or not products_section[key]:
                return False
        return True

    def key_id(self, select=None):
        all_product = self.connect_and_dowload_per_category()
        id_product = self.format_final_response(all_product)
        id_barre_code = self.connect_and_dowload_per_barcode()
        if select == 1:
            return id_product['id']
        return id_barre_code['id']

    def key_name(self, select=None):
        all_product = self.connect_and_dowload_per_category()
        name_product = self.format_final_response(all_product)
        name_barre_code = self.connect_and_dowload_per_barcode()
        if select == 1:
            return name_product['product_name_fr']
        return name_barre_code['product_name_fr']

    def key_weight(self):
        weight_barre_code = self.connect_and_dowload_per_barcode()
        return weight_barre_code['quantity']

    def key_type(self):
        all_product = self.connect_and_dowload_per_category()
        name_product = self.format_final_response(all_product)
        return name_product['main_category']


def main():
    """ Initialize the data collect """
    downloader = ApiCollectingData()

    all_products = downloader.connect_and_dowload_per_category()
    # print(all_products)
    downloader.key_type()
    # downloader.format_final_response(all_products)


if __name__ == "__main__":
    main()
