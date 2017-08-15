# _*_ coding:utf-8 _*_
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        i = 0
        ret = []
        try:
            if not self.dimension == v.dimension:
                raise ValueError
            len = self.dimension
            while i < len:
                ret.append(self.coordinates[i] + v.coordinates[i])
                i += 1
        except ValueError:
            raise ValueError('The dimension must be  the same')
        return ret

if __name__ == '__main__':
    mvector = Vector([1,2,3])
    nvector = Vector([4,5,6])
    print mvector + nvector