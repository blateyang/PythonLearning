# ----------------------
# Author: blateyang
# Date: 2018/3/15
# ----------------------

"""Read and process population_data.json"""

import json
import csv
from pygal_maps_world.i18n import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle, LightColorizedStyle


def get_country_code(country_name):
    """Return  country code used by pygal according to country_name"""
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code
    return None


def get_dict_from_json(filename, year):
    """return related statistic dict indexed by country code of year"""
    with open(filename) as f:
        pop_data = json.load(f)
        pop_country_dict = {}
        # extract data of year
        for pop_dict in pop_data:
            if pop_dict['Year'] == year:
                code = get_country_code(pop_dict['Country Name'])
                if code:
                    # change 'Value'(str) into float
                    value = float(pop_dict['Value'])
                    pop_country_dict[code] = value
                else:
                    print('Error, can not find code to '+pop_dict['Country Name'])
    return pop_country_dict


def get_dict_from_csv(filename, year):
    """return related statistic dict indexed by country code of year"""
    with open(filename, encoding='UTF-8') as f:
        data = csv.reader(f)
        country_dict = {}
        header_row = next(data)
        # print(header_row)
        index2016 = header_row.index(str(year))
        for row in data:
            code = get_country_code(row[0])
            if code:
                try:
                    value = float(row[index2016])
                except ValueError:
                    print(row[index2016]+' can not convert to float')
                else:
                    country_dict[code] = value
            else:
                print('Error, can not find code to ' + row[0])
    return country_dict


# -------------plot world map and highlight America-----------------------
wm = World()
wm.title = 'North, Central, and South America'
# use add to display a district in same color
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('America.svg')

# ----------------plot world population map------------------------------
# group country according to population
pop_country_dict = get_dict_from_json('population_data.json', 2014)
g1_pop, g2_pop, g3_pop = {}, {}, {}
for code, value in pop_country_dict.items():
    if value < 10000000:  # population < 10 million
        g1_pop[code] = value
    elif value < 1000000000:  # population < 1 billion
        g2_pop[code] = value
    else:
        g3_pop[code] = value
print(len(g1_pop), len(g2_pop), len(g3_pop))

# plot world population map
wm2_style = RotateStyle('#336699', base_style=LightColorizedStyle)  # set color format(RGB)
wm2 = World(style=wm2_style)
wm2.title = 'World population distribution in 2014'
# wm2.add('2014', pop_country_dict)
wm2.add('0-10m', g1_pop)
wm2.add('10m-1bn', g2_pop)
wm2.add('>1bn', g3_pop)
wm2.render_to_file('world_population.svg')

# ---------------------plot world GDP map-------------------------------
gdp_country_dict = get_dict_from_json('gdp.json', 2016)
wm_gdp_style = RotateStyle('#336699')
wm_gdp = World(style=wm_gdp_style)
wm_gdp.title = 'World GDP in 2016'
wm_gdp.add('2016', gdp_country_dict)
wm_gdp.render_to_file('world_gdp.svg')

# ----------------plot world journel artical map------------------------
jas_country_dict = get_dict_from_csv('API_IP.JRN.ARTC.SC_DS2_en_csv_v2.csv', 2016)
style = RotateStyle('#336699')
wm_jas = World(style=style)
wm_jas.title = 'World journel articles of science in 2016'
wm_jas.add('2016', jas_country_dict)
wm_jas.render_to_file('world_journel_article.svg')