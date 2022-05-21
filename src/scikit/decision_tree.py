import matplotlib.pyplot as plt
import graphviz
from sklearn import tree
from sklearn.tree import export_text


def learn(x, y, headers, class_names):
    classifier = tree.DecisionTreeClassifier(max_leaf_nodes=12, max_depth=5)
    classifier = classifier.fit(x, y)

    tree.plot_tree(classifier)
    # plt.show()

    # tree.plot_tree(classifier, feature_names=headers, filled=True)

    dot_data = tree.export_graphviz(classifier, out_file=None,
                                    feature_names=headers,
                                    class_names=class_names,
                                    filled=True)
    graph = graphviz.Source(dot_data, format="png")
    graph.render("decision_tree", view=True)

    print(export_text(classifier))

    return classifier
