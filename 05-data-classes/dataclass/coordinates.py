"""
``Coordinate``: simple class decorated with ``dataclass`` and a custom ``__str__``::

    >>> moscow = Coordinate(55.756, 37.617)
    >>> print(moscow)
    55.8°N, 37.6°E

"""

# tag::COORDINATE[]

from dataclasses import dataclass
from dataclasses import asdict
@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        print(type(ns))
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
# end::COORDINATE[]


if __name__ == "__main__":
    moscow = Coordinate(55.756, 37.617)
    print(moscow)
    print(type(moscow))
    dic = asdict(moscow)
    print(dict)

