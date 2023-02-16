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
df[df["Vict Sex"] == "F"].shape

# number of male victims 
df[df["Vict Sex"] == "M"].shape

# we want to count the number of incidences of violent crime for each year starting with 2020 and ending with 2023
# note that at this current time, we are in February 2023
# df[df["DATE OCC"] == "01/01/2020 12:00:00 AM"]
sample = ["01/01/2020 12:00:00 AM"]
df[df["DATE OCC"].isin(sample)] 
# df2 = df[df["DATE OCC"].dt.strftime('%Y') == "2020"]
# df2 = df.loc[(df["DATE OCC"] >= "01/01/2020") & (df["DATE OCC"] <= "12/31/2020")]
df2 = df.loc[(df["DATE OCC"] >= "01/01/2021")]
df2.head()