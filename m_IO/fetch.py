import requests

def constructQuery(coor:tuple):
    query = f''''
    [out:json][timeout:25][bbox:{coor[0]}, {coor[1]}, {coor[2]}, {coor[3]}];
    way["highway"~"^(footway|path|pedestrian|cycleway)$"]
    ["surface"!~"^(dirt|earth|ground|mud|sand|gravel|fine_gravel|grass)$"];
    out geom;
    '''


    return query

def getData(url:str, query:str ="", writeOutput=False,useStub = False):
    response = requests.get(url=url, params={'data':query})

    if response.status_code == 200:
        data = response.json()
        return data
        
    else:
        return {}

