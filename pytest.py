import os
import pandas
import matplotlib.pyplot as plt
import csv

DtTest = pandas.read_csv("example.csv")

for ind in DtTest.index:
    x = [DtTest['Start_Time'][ind], DtTest['EndTime'][ind]]
    
#    y = [1,1] #wil be replaced when using multiple machines
    machinename = DtTest['Machine'][ind]
    if machinename == "Machine001(1)":
       y = [5,5]
    elif machinename == "Machine002(1)":
        y = [4,4]
    elif machinename == "Machine003(1)":
        y = [3,3]
    elif machinename == "Machine003(2)":
        y = [2,2]   
    elif machinename == "Machine004(1)":
        y = [1,1]   
    else:
        #else it'll equal a different "row"
        y = [0,0]
    
    
    if DtTest["State"][ind] == 1:
        colorvar = "Yellow"
    elif DtTest["State"][ind] == 2:
        colorvar = "Green"
    elif DtTest["State"][ind] == 3:
        colorvar = "Purple"
    elif DtTest["State"][ind] == 4:
        colorvar = "Red"   
    
    #print (x,y,colorvar)
    # looks like x = [1,10], y = [1,1], green etc.
    plt.plot(x,y, colorvar, linewidth=25)

plt.yticks([0,1,2,3,4,5,6], ["","Machine 4", "Machine 3 (2)", "Machine 3 (1)", "Machine 2", "Machine 1", ""])
#plt.yticks(["Machine 1", "Machine 2", "Machine 3", "Machine 4"])
plt.title( "State Chart Test")
plt.xlabel("Time of Day")
plt.ylabel("Machine")
#plt.grid(True)


plt.show()
plt.savefig("savename.png")

print ("end code")