from dataclasses import dataclass
@dataclass #(frozen=True)
class Coordinate():
    let : float
    lon : float

    def __str__(self) -> str:
        ne = 'N' if self.let >= 0 else 'S'
        we = 'E' if self.lon >=0 else 'W'
        return f'{abs(self.let):.0f}{ne} ,{abs(self.lon)}{we}'
    

if __name__ == '__main__':
    moscow = Coordinate(55.70,66.77)
    print(moscow)    
    moscow.let = 40.45
    print(moscow) 