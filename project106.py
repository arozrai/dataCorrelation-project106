import plotly.express as px 
import csv 
import numpy as np 

def getDataSource(data_path): 
    coffeeIntake = [] 
    HoursSlept = [] 
    with open(data_path) as csv_file: 
        csv_reader = csv.DictReader(csv_file) 
        for row in csv_reader: 
            coffeeIntake.append(float(row["Coffee in ml"])) 
            HoursSlept.append(float(row["sleep in hours"])) 
    return {"x": coffeeIntake , "y": HoursSlept} 

def findCorrelation(datasource): 
    correlation = np.corrcoef(datasource["x"], datasource["y"]) 
    print(correlation) 
    print("Correlation between Coffee Intake vs Hours Slept :- \n--->",correlation[0,1]) 
    fig = px.scatter(x=datasource["x"], y=datasource["y"])
    fig.show()

def setup(): 
    data_path = "coffeIntakeVsHoursSlept.csv" 
    datasource = getDataSource(data_path) 
    findCorrelation(datasource) 

setup()