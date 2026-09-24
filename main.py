
from maps.fetch import *
from maps.coordinateCalculator import *

def main():

    url = "https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400&date=2026-09-22"
    print("--------")
    print(getBound(m_lat=51.136258,m_long=-114.182517, distance=0.5))

    # 1. Get the JSON with the needed data and the bound

    # 2. Parse this data into a list of nodes and weighted edges

    # 3. Make a graph with that data

    # 4. Run the path finding alg this should return subgraph of the one above

    # 5. Display the route on a map

if __name__ == "__main__":
    main()