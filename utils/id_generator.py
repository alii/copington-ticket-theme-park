from random import randint


def r(): return randint(0, 255)


def id_generator():
    return '%02X%02X%02X' % (r(), r(), r())
