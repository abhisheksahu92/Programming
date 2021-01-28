from abc import ABC,abstractmethod,abstractproperty

class Polygon(ABC):

    @abstractproperty
    def shape(self):
        print('Parent class')

    def rk(self):
        print('This is a concreate method')

    @abstractmethod
    def noofsides(self):
        return

class Triangle(Polygon):

    @property
    def shape(self):
        super().shape
        print('Child Class')

    def noofsides(self):
        print('It has three sides')
    
    def rk(self):
        super().rk()
        print('This is a subclass')


class Rectangle(Polygon):
    @property
    def shape(self):
        print(super().shape)
        print('Child Class')

    def noofsides(self):
        print('It has four sides')

t = Triangle()
t.noofsides()
t.rk()
t.shape

r = Rectangle()
r.noofsides()
