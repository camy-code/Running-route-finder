import math

def calcLong(lat:float,distance:float):
    return (distance/(6371 * math.cos(lat))) * (180.0/math.pi)


# Gets the perimeter coordinates, distance needs to be in km
def getBound(m_long:float,m_lat:float, distance:int):

    distance = float(distance)
    lat_change = distance / 111.19
    south = m_lat - lat_change
    north = m_lat + lat_change
    west = m_long - calcLong(south,distance)
    east = m_long + calcLong(north,distance)
    return south,west,north,east