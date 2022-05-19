import matplotlib.pyplot as plt
from sklearn import tree


def learn(x, y):
    # x = [[0, 0],
    #      [1, 1],
    #      [5, 2],
    #      [10, 10],
    #      [100, 100]]
    # y = [0, 1, 1, 2, 3]

    classifier = tree.DecisionTreeClassifier()
    classifier = classifier.fit(x, y)

    tree.plot_tree(classifier)
    plt.show()
