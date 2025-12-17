from testcases import countercheck, reset, buffcheck

import sys
import threading

#globals
setupString = sys.argv[1]
#add new valid args to this list
validArgs = ["-cc", "-b", "-r"]
threads = [None]*10

def validateSetUp():
    #check to see in the given test setup string is all good
    for i in range(1, sys.argv.__len__()):
        if isValidArg(sys.argv[i]):
            continue
        else:
            print("Invalid arguement : " + sys.argv[i])
            print("Valid arguements are : " + str(validArgs))
            exit(0)
    runSetup()
    return

def runSetup():
    #do the setup using the given commands in the setUp string
    for i in range(1, sys.argv.__len__()):
        buildThreads(sys.argv[i], i-1)
    startTest()
    return

def startTest():

    for i in range(0, sys.argv.__len__()-1):
        threads[i].start()
    for i in range(0, sys.argv.__len__()-1):
        threads[i].join() 

#the function targetted by all threads
def threadFunc(arg, index):
    methodDict = {
        "-b": buffcheck,
        "-cc": countercheck,
        "-r" : reset
    }
    thisWindowPosition = getPositionData(index)
    methodDict.get(arg, lambda: "unknown").run(thisWindowPosition, 210)

def buildThreads(arg, index):
    threads[index] = threading.Thread(target=threadFunc, args=(arg,index,))

def isValidArg(arg):
    if arg in validArgs:
        return True

def getPositionData(windowCount):
    snapNum = 450 * windowCount
    nextWindowPosition = [300,600,snapNum,0]
    return nextWindowPosition

#flow starts here
validateSetUp()