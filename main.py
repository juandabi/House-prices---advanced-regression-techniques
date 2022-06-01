#!/anaconda3/bin/python

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/train.csv')

print(df.head())


sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')

df.shape()
