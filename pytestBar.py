
import os
import pandas
import matplotlib.pyplot as plt
import csv

DtTest = pandas.read_csv("example.csv")  #PowerBi Chart
#DtTest = dataset  #version for PowerBi



#fig, ax = plt.subplots()
print (DtTest)
DtTest['Duration'] = 0
DtTest['color'] = ""
colorvar = ""
for ind in DtTest.index:
    x = [DtTest['Start_Time'][ind], DtTest['EndTime'][ind]]
    duration = DtTest['EndTime'][ind] - DtTest['Start_Time'][ind]
    DtTest.loc[ind, 'Duration'] = duration
#    y = [1,1] #wil be replaced when using multiple machines
    machinename = DtTest['Machine'][ind]

    if DtTest["State"][ind] == 1:
        colorvar = "Yellow"
    elif DtTest["State"][ind] == 2:
        colorvar = "Green"
    elif DtTest["State"][ind] == 3:
        colorvar = "Purple"
    elif DtTest["State"][ind] == 4:
        colorvar = "Red"   
    else:
        colorvar = "Black"
        print (DtTest["State"][ind])
    DtTest.loc[ ind,'color'] = colorvar 

#ax

DtTest = DtTest.sort_values(by=['Machine'], ascending=False)
print (DtTest)
plt.barh(DtTest['Machine'], DtTest['Duration'], align='center', left = DtTest['Start_Time'], color=DtTest['color'] )



#plt.yticks([0,1,2,3,4,5,6], ["","Machine 4", "Machine 3 (2)", "Machine 3 (1)", "Machine 2", "Machine 1", ""])
plt.xlim( [0,max(DtTest['EndTime']) + 50] )
plt.title( "State Chart Test")
plt.xlabel("Time of Day")
plt.ylabel("Machine")
#plt.grid(True)


plt.show()
#plt.savefig("MachineStates.png")
print ("end code")