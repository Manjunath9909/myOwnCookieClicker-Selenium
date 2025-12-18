# making a dictionary here so we can update the value for things like ID, CLASS once and it will be fetched through out the test suit
# boiler plate 


# add new elements here please/ update if you change them 

# We can also have other details here like text that should appear on elements 
# Which can then be used in the verification on the same 

elementDict = {
    "cookieButton" : {"id": "cookie", "class" : "bigCookie"},
    "x2buff" : {"id": "x2", "class" : "buffButton"},
    "x3buff" : {"id": "x3", "class" : "buffButton"},
    "x4buff" : {"id": "x4", "class" : "buffButton"},
    "x5buff" : {"id": "x5", "class" : "buffButton"},
    "x6buff" : {"id": "x6", "class" : "buffButton"},
    "reset" : {"id": "resetbutton", "class" : "resetbutton"}
}

def getElement(element):
    #print(elementDict.get(element)["id"])
    return elementDict.get(element) 