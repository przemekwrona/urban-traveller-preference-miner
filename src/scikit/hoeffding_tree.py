import numpy as np
from skmultiflow.trees import HoeffdingTreeClassifier


def learn(x, y, header):
    n_samples = 0
    correct_cnt = 0

    classifier = HoeffdingTreeClassifier()

    for i in range(1, 2):
        for index, row in x.iterrows():
            y_pred = classifier.predict(np.array([row]))
            if y[index] == y_pred[0]:
                correct_cnt += 1

            classifier = classifier.partial_fit(np.array([row]), np.array([y[index]]))
            n_samples += 1

    print('{} samples for analysis.'.format(n_samples))
    print('accuracy: {}'.format(correct_cnt / n_samples))

    return classifier
