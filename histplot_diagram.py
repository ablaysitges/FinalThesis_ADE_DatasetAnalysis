import matplotlib.pyplot as plt
import seaborn as sns


def histplot_plot(numeric_data):
    plt.figure(figsize=(10, 6))

    sns.histplot(data=numeric_data, x="Achieve cost eficiencies", bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Cost Efficiency Improvements (%)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def histplot_plot_automation(numeric_data):
    plt.figure(figsize=(10, 6))

    sns.histplot(data=numeric_data, x="Increase automation in tasks, without reducing employment", bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Automation Increase (%)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))

    sns.histplot(data=numeric_data, x="Automate tasks to replace employees", bins=10,
                 color='skyblue', edgecolor='black')
    plt.xlabel('Automation Increase (%)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def histplot_plot_cross_analysis(numeric_data):
    sns.histplot(data=numeric_data, x="Accelerate development of creative content", hue="Achieve cost eficiencies")
    plt.show()

    sns.histplot(data=numeric_data, x="Increase automation in tasks, without reducing employment",
                 hue="Achieve cost eficiencies")
    plt.show()

    sns.histplot(data=numeric_data, x="Automate tasks to replace employees",
                 hue="Achieve cost eficiencies")
    plt.show()
    sns.histplot(data=numeric_data, x="Achieve cost eficiencies",
                 hue="Achieve cost eficiencies")
    plt.show()
