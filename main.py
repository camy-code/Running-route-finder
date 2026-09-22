
from maps.fetch import *

def main():

    url = "https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400&date=2026-09-22"
    print("Hello worlds")
    res = getData(url)
    print(res)

if __name__ == "__main__":
    main()