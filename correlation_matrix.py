import matplotlib.pyplot as plt
import seaborn as sns


def correlation_matrix_plot(numeric_data):
    plt.figure(figsize=(10, 8))
    numeric_data.drop('Value or potential value created by Generative AI, other', inplace=True, axis=1)

    sns.heatmap(numeric_data.corr(), annot=True, cmap="RdYlBu")

    plt.tight_layout()
    plt.show()
