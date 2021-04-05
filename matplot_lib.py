import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
def main():
    # x and y data list
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # set plot style
    style.use('ggplot')
    # line plot example
    plt.plot(x, y, label="line plot example", linewidth=2)
    plt.legend()
    plt.grid(True,color="k")
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.title('Line Plot')
    plt.show()
    # bar chart vertical example
    plt.bar(x, y, label="bar chart vertical example", align='center')
    plt.legend()
    plt.grid(True,color="k")
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.title('Bar Chart Vertical')
    plt.show()
    # bar chart horizontal example
    plt.barh(x, y, label="bar chart horizontal example", align='center')
    plt.legend()
    plt.grid(True,color="k")
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.title('Bar Chart Horizontal')
    plt.show()
    # scatter plot example
    plt.scatter(x, y, label="scatter plot example")
    plt.legend()
    plt.grid(True,color="k")
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.title('Scatter Plot')
    plt.show()
    # histogram plot example
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    n, bins, patches = plt.hist(x, 50, density=1, facecolor='r', alpha=0.75,label="histogram plot example")
    plt.text(45, 0.028, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.legend()
    plt.grid(True,color="k")
    plt.xlabel("x")
    plt.ylabel("P(x)")
    plt.title("Histogram Plot")
    plt.show()
if __name__ == '__main__':
    main()