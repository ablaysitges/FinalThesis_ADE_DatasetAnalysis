import matplotlib.pyplot as plt
import seaborn as sns


def boxplot_plot(data_clean):
    fig, axes = plt.subplots(2, 4, figsize=(60, 20))
    sns.boxplot(data=data_clean, x="Accelerate development of creative content", y="Classification", ax=axes[0, 0])
    sns.boxplot(data=data_clean, x="Increase automation in tasks, without reducing employment", y="Classification", ax=axes[0, 1])
    sns.boxplot(data=data_clean, x="Automate tasks to replace employees", y="Classification", ax=axes[1, 0])
    sns.boxplot(data=data_clean, x="Achieve cost eficiencies", y="Classification", ax=axes[1, 1])
    sns.boxplot(data=data_clean, x="Improve client or customer experience", y="Classification", ax=axes[0, 2])
    sns.boxplot(data=data_clean, x="Drive data-driven decision making", y="Classification", ax=axes[1, 2])
    sns.boxplot(data=data_clean, x="Minimize workorce recruitment and retention challenges", y="Classification", ax=axes[1, 3])
    sns.boxplot(data=data_clean, x="Value or potential value created by Generative AI, other", y="Classification", ax=axes[0, 3])

    plt.tight_layout()
    plt.show()
