# -*- PipEnv -*-
# -*- coding: Utf-8 -*-

import records

CATEGORIES = ['Entrée',
              'Pizza',
              'Dessert',
              'Boisson',
              'soda', 'Salade']

# ROYALE_PIZZA_ =  {'7610100514654': 1,'3038352876506': 90,'7613034232465': 120,'3333160002025': 89,'0060383195830': 120,'3076820002064': 5}

ROYALE_PIZZA =  ['7610100514654',
                 '3038352876506',
                 '7613034232465',
                 '3333160002025',
                 '3560070246571',
                 '3076820002064'
                 ]

db = records.Database("mysql+mysqlconnector://OCP6:OC_STUDENT@localhost/Oc_Pizza?charset=utf8mb4")


