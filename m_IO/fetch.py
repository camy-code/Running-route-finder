import overpy

def constructQuery(coor: tuple):
    return f'''
    [out:json][timeout:60];

    way["highway"~"^(footway|path|pedestrian|cycleway)$"]
            ["surface"!~"^(dirt|earth|ground|mud|sand|gravel|fine_gravel|grass)$"]
        ({coor[0]},{coor[1]},{coor[2]},{coor[3]});

    out geom;
    '''

def getFetchData(coor: tuple):
    api = overpy.Overpass(
        url="https://overpass-api.de/api/interpreter"
    )
    query = constructQuery(coor)
    print(query)
    return api.query(query)


def getStubData():
    with open ("stubJSON.txt", "r") as file:
        content = file.read()
        return content

def writeData(content:str):
    with open("stubJSON.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a second line.")
    
    
def getData(coor:tuple, isStub:bool, isWrite:bool):
    content = ""
    if isStub:
        content = getStubData()
    else:
        content = getFetchData(coor=coor)

    if isWrite:
        writeData(content=content)
    
    return content

    