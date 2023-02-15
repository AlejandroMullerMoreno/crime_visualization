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