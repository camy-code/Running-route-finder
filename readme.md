## The Goal

The goal of this project is to create a way for me to find new running routes in my neighborhood as well as to help others do the same. In the final version of my project I want to be able to ask my application for:

- An Xkm route that has Y meters of elevation gain that starts at longitude a and lattitude b where my tolerance for distance is T and my tolerance for elevation is P.

- Tolerance is how much a measurement can be off by plus **or** minus.

- It is also important to note that we hope to do our run in a loop so that we return to X Y at the end.

And so the final program would run something like:
``` 
python main.py a b X Y T P
```

Inherently this problem is a graph problem that I think is in NP but for now we do not concern ourselves with this as we need to figure out how to get the street data of my neighborhood into our program.

## Using Overpass API to access open street map
There is open source data for maps called open street map and we can use an API called Overpass API to query this information.