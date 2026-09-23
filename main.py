
from maps.fetch import *
from maps.coordinateCalculator import *

def main():

    url = "https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400&date=2026-09-22"
    print("--------")
    print(getBound(m_lat=51.136258,m_long=-114.182517, distance=5))

if __name__ == "__main__":
    main()