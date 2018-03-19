# coding:utf-8
# -------------------
# Author: blateyang
# Date: 2018/3/17
# 功能：查找某一演员或某一类型的电影，按评分排序并进行可视化（同时显示电影名、评分、
#       电影简介和链接）
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


def get_movie_info(movie_id):
    """Get summary and rating num of a certain movie"""
    movie_url = 'https://api.douban.com/v2/movie/'+movie_id
    r = requests.get(movie_url)
    if r.status_code == 200:
        movie_info = r.json()
        print(movie_info)
        return movie_info['summary']


def display_info(response_items):
    """display information of response"""
    print('部分搜索结果:')
    for i, item in enumerate(sorted(response_items, key=lambda d:d['rating']['average'], reverse=True)):
        print('条目id：', item['id'])
        print('中文名：', item['title'])
        print('原名：', item['original_title'])
        print('豆瓣链接：', item['alt'])
        print('平均评分：', item['rating']['average'])
        reviews_count, summary = get_movie_info(item['id'])
        print('评分人数：', reviews_count)
        print('简介：', summary)
        print('年份：', item['year'])
        print('条目分类：', item['subtype'])


def get_info_from_douban(actor=None, subtype=None):
    """Get data about actor or subtype from douban api"""
    url_head = 'https://api.douban.com/v2/movie/search'
    if (actor is None) and (subtype is None):
        print('You do not give any search information')
    elif actor is None:
        url = url_head+'?tag='+subtype+'20'
    elif subtype is None:
        url = url_head+'?q='+actor+'20'
    else:
        url = url_head+'?q='+actor+'20?tag='+subtype
    response = get_json(url)
    if response[0] == 200:
        response_items = sorted(response[1]['subjects'], key=lambda d:d['rating']['average'], reverse=True)
        names, plot_dicts = [], []
        for item in response_items:
            names.append(item['title'])
            summary = get_movie_info(item['id'])
            plot_dict={
                'value': item['rating']['average'],
                'label': summary,
                'xlink': item['alt']
            }
            plot_dicts.append(plot_dict)
        return names, plot_dicts


if __name__ == '__main__':
    # url = 'https://api.douban.com/v2/movie/search?q=周星驰20?tag=喜剧'
    # response = get_json(url)
    # if response[0] == 200:
    #     display_info(response[1]['subjects'][0:5])

    # visualization
    # self-define Pygal graph
    my_style = LS('#336699', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 10
    my_config.major_label_font_size = 18
    my_config.truncate_label = 10
    my_config.show_y_guides = False  # not show horizontal line
    my_config.width = 1000

    name = '豆瓣电影搜索排序'
    names, plot_dicts = get_info_from_douban('周星驰', '喜剧')
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = name+' 周星驰-喜剧'
    chart.x_labels = names
    chart.add('', plot_dicts)

    chart.render_to_file('douban_movie.svg')
