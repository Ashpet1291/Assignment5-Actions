def firstrun():
    return "success"


def circleArea(input):
    PI = 3.14
    radius = input
    area = PI * radius * radius
    return area


def firstNLastList(list):
    listItems = list
    res = [ listItems[0], listItems[-1]]
    return str(res)
