# -------------------------
# Author: blateyang
# Date: 2018/3/9
# ------------------------

"""Store city and country name"""


def city_functions(city, country, population=None):
    """combine city and country with ','"""
    if population is None:
        return city.title()+', '+country.title()
    else:
        return city.title()+', '+country.title()+' - population '+str(population)
