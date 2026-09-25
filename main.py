
from maps.coordinateCalculator import *
from m_IO.fetch import * 

def main():
    m_lat = 51.1360705037541
    m_long = -114.18248881804557
    distance = 0.5

    url = "https://overpass-turbo.eu"
    print("--------")
    coor = getBound(m_lat=m_lat,m_long=m_long, distance=distance)
    print(coor)

    # 1. Get the JSON with the needed data and the bound
    # query =constructQuery(coor)
    # data = getData( coor=coor)
  
    # print(data)
    

    # 2. Parse this data into a list of nodes and weighted edges

    # 3. Make a graph with that data

    # 4. Run the path finding alg this should return subgraph of the one above

    # 5. Display the route on a map

if __name__ == "__main__":
    main()