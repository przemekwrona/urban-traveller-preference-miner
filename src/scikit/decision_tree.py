import matplotlib.pyplot as plt
# import graphviz
from sklearn import tree
from sklearn.tree import export_text


def learn(x, y, headers):
    classifier = tree.DecisionTreeClassifier(max_leaf_nodes=8)
    classifier = classifier.fit(x, y)

    tree.plot_tree(classifier)
    plt.show()

    tree.plot_tree(classifier)

    # print(export_text(classifier))

    return classifier
