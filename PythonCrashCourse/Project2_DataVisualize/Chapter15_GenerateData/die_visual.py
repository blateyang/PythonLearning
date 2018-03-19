# ----------------------
# Author: blateyang
# Date: 2018/3/13
# ----------------------

"""Test die class and visualize it"""
from die import Die
import pygal  # pygal can generate scalable vector graph(svg)
import matplotlib.pyplot as plt
import pdb


def die_add(die1_sides, die2_sides):
    """Add the result of two die and visualize it"""
    die1 = Die(die1_sides)
    die2 = Die(die2_sides)
    # generate data
    results = []
    for i in range(1000):
        # pdb.set_trace()
        result = die1.roll() + die2.roll()
        results.append(result)
    # analyse results
    frequencies = []
    for i in range(2, die1.num_sides + die2.num_sides + 1):
        frequency = results.count(i)
        frequencies.append(frequency)

    # print(frequencies)

    # visualize results with pygal
    hist = pygal.Bar()

    hist.title = "Results of rolling two D6 1000 times"
    # hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_labels = [str(i) for i in range(2, 13)]
    hist.x_title = 'Result'
    hist.y_title = "Frequency of Result"

    hist.add('D6+D6', frequencies)
    hist.render_to_file('dice_visual.svg')


def die_product(die1_sides, die2_sides):
    """Product the result of two die and visualize it"""
    die1 = Die(die1_sides)
    die2 = Die(die2_sides)
    # generate data
    results = []
    for i in range(1000):
        # pdb.set_trace()
        result = die1.roll() * die2.roll()
        results.append(result)
    # analyse results
    frequencies = []
    max_result = die1.num_sides * die2.num_sides
    for i in range(1, max_result+1):
        frequency = results.count(i)
        frequencies.append(frequency)
    # visualize results with pygal
    hist = pygal.Bar()

    hist.title = "Results of rolling two D6 1000 times"
    hist.x_labels = [str(i) for i in range(1, max_result+1)]
    hist.x_title = 'Result'
    hist.y_title = "Frequency of Result"

    hist.add('D6*D6', frequencies)
    hist.render_to_file('dice_product_visual.svg')


def die_add_plt(die1_sides, die2_sides):
    """Add the result of two die and visualize it with matplotlib"""
    die1 = Die(die1_sides)
    die2 = Die(die2_sides)
    # generate data
    results = []
    for i in range(1000):
        # pdb.set_trace()
        result = die1.roll() + die2.roll()
        results.append(result)
    # analyse results
    frequencies = []
    max_result = die1.num_sides + die2.num_sides
    for i in range(2, max_result + 1):
        frequency = results.count(i)
        frequencies.append(frequency)
    # visualize result
    plt.bar(list(range(2, max_result+1)), frequencies)
    plt.xlabel('Result')
    plt.ylabel('Frequency of Result')
    plt.title('Results of rolling two D6 1000 times')
    plt.show()

# test
# die_product(6, 6)
die_add_plt(6, 6)
