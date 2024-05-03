import matplotlib
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns


def descriptive_analysis(data_descriptive):

    descriptive = data_descriptive.describe()
    print(descriptive)
    plt.show()


    #sns.displot(data=data_descriptive, x="Achieve cost eficiencies")
    #sns.pairplot(data=data_descriptive, palette='Dark2', diag_kind='kde')
    #plt.show()

    #plt.sho(data=data_descriptive, x="Accelerate development of creative content")

