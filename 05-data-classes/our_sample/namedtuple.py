
from collections import namedtuple


if __name__ == "__main__":
    Coordinate = namedtuple('Coordinate', 'x y z' , defaults=[20,30])
    #1-Useful Representation
    moscow = Coordinate(50)#Coordinate(20,10,30)
    print(Coordinate)
    print(moscow)
    print(type(moscow))
    #moscow.x = 40.45
    print(moscow) 
    #2- Meaningful __eq__
    result = (moscow== Coordinate(x=20,y=10,z=30))
    print(result)
    result_01 = issubclass(Coordinate , tuple)
    print(result_01)
