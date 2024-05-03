import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def cluster_analysis():
    data = pd.read_csv('ValueCreatedByGenerativeAI_DataProofing.csv')

    data.replace('', pd.NA, inplace=True)
    data.dropna(inplace=True)

    # Exclude non-categorical columns
    data = data.drop(columns=["Value or potential value created by Generative AI 4"])
    data = data.drop(columns=["Classification"])

    data = data.apply(pd.to_numeric)



    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=4)
    clusters = kmeans.fit_predict(scaled_data)

    # Add cluster labels to the dataframe
    data['Cluster'] = clusters

    # Visualize the clusters
    sns.pairplot(data=data, hue='Cluster', palette='RdYlBu', diag_kind='kde')
    plt.show()
