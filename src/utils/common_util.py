
def cook_element(element: tuple, *custom):
    _, ele = element
    return ele.format(*custom)