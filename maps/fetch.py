import requests


def getData(url:str):
    response = requests.get(url=url)

    if response.status_code == 200:
        data = response.json()
        return data
        
    else:
        return {}