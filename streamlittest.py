import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.header('Example Sim Data Report')
st.write("""
Hello World! \n
This is a demo of the streamlit technology, hosting data from a simulation into a web interface. it uses matplotlib, pandas, and numpy to manage data. 

""")

DtTest = pd.read_csv("example.csv")
#st.line_chart(dttest)

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
dt2 = DtTest.filter(items=['Machine', 'Duration', 'State'], )
dt3 = dt2[dt2['State']==2]

fig, ax = plt.subplots()
ax.barh(DtTest['Machine'], DtTest['Duration'], align='center', left = DtTest['Start_Time'], color=DtTest['color'] )
#plt.show()
# 

st.subheader('Machine States')
st.pyplot(fig)


#st.bar_chart()
if st.checkbox('Show Raw Data'):
    DtTest

st.subheader('Machine Cycle Times')
hist_values = np.histogram(dt3['Duration'], bins=30, )[0] #range=(0,24)

machineref = st.radio(
        "Pick A Machine for Display options:", 
        ('all','Machine001(1)', 'Machine002(1)','Machine003(1)','Machine003(2)','Machine004(1)',)
)
if machineref == 'all':
    dt3 = dt2[dt2['State']==2]
else:
    dt3 = dt3[dt3['Machine']==machineref]
hist_values = np.histogram(dt3['Duration'], bins=30, )[0] #range=(0,24)

st.bar_chart(hist_values)
#

if st.checkbox('Show Raw Cycletime Data'):
    dt3
st.write ("""
end
""")