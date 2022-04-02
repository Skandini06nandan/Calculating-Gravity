import csv
import pandas as pd
import plotly.express as pe

stars=[]
with open("final_data.csv", "r") as f:
    csvreader =csv.reader(f)
    for row in csvreader:
        stars.append(row)

headers =stars [0]
planetdata = stars[1:]
headers[0] ='Row Number'

print(headers)
print(planetdata[0])

data = pd.read_csv('star_with_gravity.csv')

mass = data["Mass"].tolist()
radius = data["Radius"].tolist()

mass.pop(0)
radius.pop(0)
kg=[]

for i in mass:
    kg = i*(1.98855e+30)
print("kilo",kg)

for i in radius:
    meters=i*(1.496e+11)
print("meters",meters)

starmass = []
starradius = []
starname = []
for i in planetdata:
    starmass.append(i[3])
    starradius.append(i[4])
    starname.append(i[1])

planetgravity = []

for index, name in enumerate(starname):
    #6371000= Earth radius in meters
    #5.972e24= Earth mass in kg
    planetgravity.append(6.67e-11*(float(starmass[index])*5.972e+24)/(float(starradius[index])**2)*6371000*6371000)

scatter = pe.scatter(x=starradius, y=starmass, size=planetgravity, title='Star Gravity by Name', hover_data=[starname])
scatter.show()

        