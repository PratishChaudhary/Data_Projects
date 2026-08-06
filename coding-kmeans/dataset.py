import matplotlib.pyplot as plt
import pandas as pd
from kmeans import KMeans
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Iris.csv')
X = df.iloc[:,:4]
y = df.iloc[:,5]
encoder = LabelEncoder()
y = encoder.fit_transform(y)

