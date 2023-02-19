#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sms

# read data in and visualize it initially 
df = pd.read_csv("crime.csv")
df.columns

df.shape

# number of female victims
numberOfFemaleVict = df[df["Vict Sex"] == "F"].shape

# number of male victims 
numberOfMaleVict = df[df["Vict Sex"] == "M"].shape

# making a pie chart of male to female victims
dataForPieChart = np.array([numberOfFemaleVict, numberOfMaleVict])
myLabels = ["Female Victims", "Male Victims"]
myColors = ["pink", "blue"]
plt.pie(dataForPieChart, labels = myLabels, colors = myColors)
plt.legend(title = "Total victims By Sex", loc = "upper left")
plt.show()