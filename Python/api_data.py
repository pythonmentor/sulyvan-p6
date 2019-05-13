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

            Ingredients_id = self.barcode(products_barcode)
            name_product = self.name(products_barcode)
            weight = self.weight(products_barcode)

            categories = self.category_barcode(products_barcode)
            designation = self.designation(products_barcode)

            key_barcode = (Ingredients_id,
                           name_product.upper(),
                           designation,
                           categories.upper(),
                           weight)
            formatting = key_barcode
            product_barcode.append(formatting)
            print('id_produit :', int(Ingredients_id), '\n',
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

if __name__ == "__main__":
    main()
