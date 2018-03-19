# -------------------
# Author: blateyang
# Date: 2018/3/16
# -------------------


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


def get_json(url):
    """Get status and data from json which response by url"""
    r = requests.get(url)
    response_dict = r.json()
    return r.status_code, response_dict


def get_api_request_limit(url_limit):
    """Return the total times and reamining times you can use to request"""
    r_limit = requests.get(url_limit)
    limit_dict = r_limit.json()
    print(limit_dict)
    total = limit_dict['resources']['search']['limit']
    remaining = limit_dict['resources']['search']['remaining']
    return total, remaining


def display_info(response_items):
    """display information of items"""
    for i, repos_dict in enumerate(response_items):
        print('Information about repos', i+1)
        print('Name: ', repos_dict['name'])
        print('Full_name: ', repos_dict['full_name'])
        print('Owner: ', repos_dict['owner']['login'])
        print('Stars: ', repos_dict['stargazers_count'])
        print('Repository: ', repos_dict['html_url'])
        print('Created: ', repos_dict['created_at'])
        print('Updated: ', repos_dict['updated_at'])
        print('Description: ', repos_dict['description'])


def get_info_from_github(name):
    """Use web API of github to search repositories about python"""
    # execute api call and store response
    url = 'https://api.github.com/search/repositories?q=language:'+name+'&sort=stars'
    url_limit = 'https://api.github.com/rate_limit'

    status_code, response_dict = get_json(url)
    total, remaining = get_api_request_limit(url_limit)
    # print outline info of response_dict
    print('Response dict keys: ', response_dict.keys())
    print('Repositories returned: ', len(response_dict['items']))
    print('Your request limit times: ', total)
    print('Your request remaining times: ', remaining)
    # display_info(response_dict['items'])

    names, plot_dicts = [], []
    for repos_dict in response_dict['items']:
        names.append(repos_dict['name'])
        repos_description = repos_dict['description']
        if repos_description is None:  # if repos_dict has no description
            repos_description = 'No description'
        plot_dict = {
            'value': repos_dict['stargazers_count'],
            'label': repos_description,
            'xlink': repos_dict['html_url']
        }
        plot_dicts.append(plot_dict)

    return names, plot_dicts


if __name__ == '__main__':
    # visualization
    # self-define Pygal graph
    my_style = LS('#336699', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False  # not show horizontal line
    my_config.width = 1000

    name = 'C++' # if name is C++， need to rename it when render to file
    names, plot_dicts = get_info_from_github(name)
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = name+' Projects'
    chart.x_labels = names
    chart.add('', plot_dicts)

    chart.render_to_file('Cplusplus_projects.svg')
