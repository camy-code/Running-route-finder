import math

def calcLong(lat: float, distance: float):
    return (distance / (6371 * math.cos(math.radians(lat)))) * (180 / math.pi)

# Gets the perimeter coordinates, distance needs to be in km
def getBound(m_long: float, m_lat: float, distance: float):
    lat_change = distance / 111.19

    south = m_lat - lat_change
    north = m_lat + lat_change

    long_change = calcLong(m_lat, distance)

    west = m_long - long_change
    east = m_long + long_change

    return south, west, north, east