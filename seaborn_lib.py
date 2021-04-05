import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
def main():
    iris_data = sns.load_dataset(name="iris")
    # print(iris_data)
    style.use('ggplot')
    # swarm plot example
    sns.swarmplot(x="species", y="petal_length", data=iris_data)
    plt.text(40, 7, "abc")
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()
    # factor plot example
    g = sns.factorplot("species", "petal_length", data=iris_data, kind="bar",palette="muted", legend=False)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()
    # box plot example
    sns.boxplot(x="species", y="petal_length", data=iris_data)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.title("Species vs. Petal Length")
    plt.show()
    # pair plot example
    sns.pairplot(iris_data, hue="species", size=2)
    plt.ylabel("petal length, cm")
    plt.xlabel("species")
    plt.show()
if __name__ == '__main__':
    main()