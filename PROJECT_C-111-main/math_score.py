import statistics
from numpy.lib.arraypad import pad
import csv
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics 

df = pd.read_csv("math-score.csv")
data = df["Math_score"].tolist()
dataset = []

#FUNCTION TO GET THE MEAN OF GIVEN DATA SAMPLE
def randomsetofmean(counter):
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    #FINDING MEAN,MEDIAN,MODE AND STANDARD DEVIATION OF SAMPLE DATA USING STATISTICS
    math_score_mean = statistics.mean(data)
    #math_score_median = statistics.median(data)
    #math_score_mode = statistics.mode(data)
    #math_score_std = statistics.stdev(data)

    return math_score_mean 
    

# FINDING MEAN, MEDIAN, MODE AND STD_DEVIATION OF THE SAMPLE
math_score_mean = statistics.mean(data)
mean_list = []
for i in range(0,1000):
    set_of_mean = randomsetofmean(100)
    mean_list.append(set_of_mean)
mean_list_std = statistics.stdev(data)
mean = statistics.mean(mean_list)

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values
first_std_deviation_start, first_std_deviation_end = math_score_mean-mean_list_std, math_score_mean+mean_list_std
second_std_deviation_start, second_std_deviation_end = math_score_mean-(2*mean_list_std), math_score_mean+(2*mean_list_std)
third_std_deviation_start, third_std_deviation_end = math_score_mean-(3*mean_list_std), math_score_mean+(3*mean_list_std)

# PRINTING ALL STANDARD DIVIATION
print(first_std_deviation_start, first_std_deviation_end)
print(second_std_deviation_start, second_std_deviation_end)
print(third_std_deviation_start, third_std_deviation_end)

#Plot a distribution graph(Remember:- Expectation is bell curve distribution)
fig = ff.create_distplot([mean_list], ["Math_score"], show_hist= False)
fig.add_trace(go.Scatter(x=[math_score_mean, math_score_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

#FINDING THE Z-SCORE USING THE FORMULA
z_score = (math_score_mean - mean)/mean_list_std
print("The z score is = ",z_score)
