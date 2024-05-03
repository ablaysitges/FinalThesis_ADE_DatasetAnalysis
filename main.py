# This is a sample Python script.
import pandas as pd

from boxplot_analysis import boxplot_plot
from cluster_analysis import cluster_analysis
from correlation_matrix import correlation_matrix_plot
from descriptive_analysis import descriptive_analysis
from histplot_diagram import histplot_plot_cross_analysis, histplot_plot, histplot_plot_automation


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def data_cleansing():
    data = pd.read_csv('ValueCreatedByGenerativeAI_DataProofing.csv', sep=',')

    data.isna().sum()

    data_clean = data.dropna()

    data_numeric = data_clean.copy()
    data_numeric.drop('Value or potential value created by Generative AI 4', inplace=True, axis=1)
    data_numeric.drop('Classification', inplace=True, axis=1)

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    return data_clean, data_numeric


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_clean, data_numeric = data_cleansing()
    descriptive_analysis(data_numeric)
    histplot_plot(data_numeric)
    histplot_plot_automation(data_numeric)
    #histplot_plot_cross_analysis(data_numeric)
    correlation_matrix_plot(data_numeric)
    #cluster_analysis()
    #boxplot_plot(data_clean)