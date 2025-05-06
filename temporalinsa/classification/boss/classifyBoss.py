from pyts.transformation import BOSS
import numpy as np
from sklearn.metrics import f1_score
from classification.getClassifier import getClassifier
import time

def classifyBoss(parameters, classifier, classifier_params, X_Train, X_Test, Y_Train, Y_Test):

    time_a = time.perf_counter()

    # BOSS run
    boss = BOSS(word_size=int(parameters["word_size"]), n_bins=int(parameters["n_bins"]), window_size=int(parameters["window_size"]), sparse=True)
    X_training_transform = boss.fit_transform(X_Train)
    X_test_transform = boss.transform(X_Test)

    time_b = time.perf_counter()

    # Classifier run
    classifier = getClassifier(classifier, classifier_params)
    classifier.fit(X_training_transform, Y_Train)
    accuracy = classifier.score(X_test_transform, Y_Test)
    f1 = f1_score(Y_Test, classifier.predict(X_test_transform), average='weighted')

    time_total = time_b - time_a

    dict = {
        "accuracy": accuracy,
        "f1_score": f1,
        "time": time_total,
    }

    return dict