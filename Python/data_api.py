# -*- PipEnv -*-
# -*- coding: Utf-8 -*-


import requests as req
from pprint import pprint


class ApiCollectingData:
    """
        This class has the responsibility of collecting a certain number
        of products, in selected categories, thus to give a valid
        structure for the insertion in the database
    """
    CATEGORIES = ['Sodas',
                  'Eaux',
                  'Salade',
                  'Pizza',
                  'Glaces']

    def __init__(self):
        """ The constructor is not used here """
        pass

    def connect_and_harvest(self):
        """ Use the configuration for the connecting interface """
        all_products = []
        # Address OpenFooFact.org the API FR locating
        api = "https://fr.openfoodfacts.org/cgi/search.pl"
        for category in self.CATEGORIES:
            # This config for  for connecting API
            config = {"action": "process",
                      # Get the result by category
                      "tagtype_0": "categories",
                      # the tag represents the article search
                      'tag_0': category,
                      "tag_contains_0": "contains",
                      # Number of articles per page
                      # Min content 20, Max content 1000
                      "page_size": 5,
                      # The API response in JSON
                      "json": 1}
            # Uses the configuration for the connection
            response = req.get(api, params=config)
            # Return the response in JSON
            results = response.json()
            # Finally result of API
            products_section = results['products']
            for product in products_section:
                product['main_category'] = category
            all_products.extend(products_section)
        return all_products

    def format_final_response(self, all_products):
        """ Formatted the response just harvest the categories selected """
        product_final = []
        keys = ['id', 'product_name_fr', 'nutrition_grade_fr',
                'url', 'categories', 'main_category', 'stores']
        print(len(all_products))
        for product in all_products:
            if self.validate_the_data(keys, product):
                barcode = product['id']
                name = product['product_name_fr']
                sub_category = product['main_category'].upper()
                designation = product['generic_name_fr']
                poids = product['quantity']
                key = (barcode, name, sub_category, poids)
                formatting = key
                product_final.append(formatting)
                ###############################
                """ PRINT RESULTS FUNCTION """
                ###############################
                # Print type results the stores and category count
                print(' produit: ', name.upper(), '\n',
                      ' id_produit: ', int(barcode),
                      ' designation: ', designation.upper(),
                      ' poids: ', poids,
                      'présent dans: ', [sub_category], [len(sub_category)],
                      f"Nous avons récupéré {len(product_final)} produits", '\n'*2)
                # Print type results final form
                pprint(product_final)
                ###############################
        return product_final

    def validate_the_data(self, keys, products_section):
        """ Validate the complete fields """
        for key in keys:
            if key not in products_section or not products_section[key]:
                return False
        return True


def main():
    """ Initialize the data collect """

    downloader = ApiCollectingData()
    connect = downloader.connect_and_harvest()
    downloader.format_final_response(connect)

if __name__ == "__main__":
    main()
