import numpy

def regress_price(surface):
    try:
        surface = float(surface)
        surfaces = numpy.random.uniform(0, 500.0, size=100)
        prices = numpy.random.uniform(0, 500.0, size=100)
        linear = numpy.polyfit(surfaces , prices , 1)
        price = round(numpy.polyval(linear , [surface] )[0] , 2)
        return price
    except ValueError:
        raise ValueError("String can't be changed into integer")
