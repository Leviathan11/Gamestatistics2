import math
# Report functions


def get_most_played(filename):
    sells = 0
    title = ""
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        if float(game.split('\t')[1]) > sells:
            sells = int(game.split('\t')[1])
            title = game.split('\t')[0]
    return title


def sum_sold(filename):
    sells = 0
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        sells += float(game.split('\t')[1])
    return sells


def get_selling_avg(filename):
    sum_sold = 0
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        sum_sold += float(game.split('\t')[1])
    return math.ceil(sum_sold/len(content))


def count_longest_title(filename):
    length = 0
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        if len(game.split('\t')[0]) > length:
            length = len(game.split('\t')[0])
    return length


def get_date_avg(filename):
    sum_date = 0
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        sum_date += int(game.split('\t')[2])
    return math.ceil(sum_date/len(content))


def get_game(filename, title):
    with open(filename) as f:
        content = f.readlines()
    for game in content:
        if game.split('\t')[0] == title:
            properties = game.split('\t')
            properties[1] = float(properties[1])
            properties[2] = int(properties[2])
            properties[4] = properties[4][:-1]
            return properties
    raise ValueError("There is no such game!")
