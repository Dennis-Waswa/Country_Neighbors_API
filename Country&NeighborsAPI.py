# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:15:13 2020

@author: Dennis Waswa
"""

import re
import requests

country_code = input("Enter three-character country code: ")
if not re.match("^[A-Z]*$", country_code):
    print("Error! Only upper case letters A-Z allowed!")
elif len(country_code) > 3:
    print("Error! Only 3 characters allowed!")

level = int(input("Enter neighborhood level: "))


def get_direct_neighbors(country_cod):
    
    neighbors_list = []
    
    n = requests.get(f'http://restcountries.eu/rest/v2/alpha/{country_cod}')
    data = n.json()
    code = data['alpha3Code']
    name = data['name']
    borders = data['borders']
    neighbors_list.extend(borders)
    
    print(f"{name} has {len(neighbors_list)} 'level {level}' neighbors: {neighbors_list}")
    return neighbors_list, name, code


def get_n_level_neighbors(country_cod, x):
    neighbors_list = get_direct_neighbors(country_cod)[0]
    name = get_direct_neighbors(country_cod)[1]
    code = get_direct_neighbors(country_cod)[2]
    
    level_2 = []
    for country in neighbors_list:
        level_2.extend(get_direct_neighbors(country)[0])
        level_n = []
        for x in level_2:
            level_n = []
            k = get_direct_neighbors(x)[0]
            level_n.extend(k)
            level_n = set(level_n)
            level_n.remove(country_cod)
        print(f"{name} has {len(level_n)} 'level {level}' neighbors: {level_n}")
    print(code)
    level_2 = set(level_2)
    level_2.remove(code)
    print(f"{name} has {len(level_2)} 'level {level}' neighbors: {level_2}")
   
if level >= 1:
    if level == 1:
        get_direct_neighbors(country_code)
    elif level >= 2:
        get_n_level_neighbors(country_code, level)
    else:
        print("neighborhood level starts from 1")



