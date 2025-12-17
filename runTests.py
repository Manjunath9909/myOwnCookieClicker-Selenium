from testcases import countercheck, reset, buffcheck

import sys
import threading

def validateSetUp():
    #check to see in the given test setup string is all good
    return

def runSetup():
    #do the setup using the given commands in the setUp string
    for i in range(1, sys.argv.__len__()):
        threads[i-1] = buildThreads(sys.argv[i])
    startTest()
    return

def startTest():
    for i in range(0, sys.argv.__len__()-1):
        threads[i].start()
    for i in range(0, sys.argv.__len__()-1):
        threads[i].join()
    print("Started all the testcases")    

def buildThreads(arg):
    methodDict = {
        "-b": buffcheck,
        "-cc": countercheck,
        "-r" : reset
    }
    return threading.Thread(target=methodDict.get(arg, lambda: "unknown").run1(), args="manju", name="Threadx")

setupString = sys.argv[1]
threads = [None]*10
runSetup()