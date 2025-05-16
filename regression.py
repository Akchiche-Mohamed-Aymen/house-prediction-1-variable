import numpy

def regress_price(surface):
    try:
        surface = float(surface)
        surfaces = numpy.random.uniform(0, 500.0, size=100)
        #9.750 is average price for m*m in USA
        prices = 9.750 * surfaces
        linear = numpy.polyfit(surfaces , prices , 1)
        price = round(numpy.polyval(linear , [surface] )[0] , 2)
        return price
    except ValueError:
        raise ValueError("String can't be changed into integer")
