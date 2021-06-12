import csv
import random
from numpy import average
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("data.csv")
data = df["data"].tolist()
dataset = []

#FUNCTION TO GET THE MEAN OF GIVEN DATA SAMPLE
def randomsetofmean(counter):
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    #FINDING MEAN,MEDIAN,MODE AND STANDARD DEVIATION OF SAMPLE DATA USING STATISTICS
    data_mean = statistics.mean(data)
    #data_median = statistics.mean(data)
    #data_mode = statistics.mean(data)

    return data_mean
#FUNCTION TO PLOT THE MEAN OF THE GRAPH
def showfig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["data"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = randomsetofmean(100)
        mean_list.append(set_of_mean)
    showfig(mean_list)
setup()

#data_std = statistics.stdev(data)
#PRINTING THE MEAN AND STD_DEVIATION
#print(data_mean, data_median, data_mode, data_std)

