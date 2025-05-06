from classification.minirocket.code.minirocket import transform, fit
from classification.getClassifier import getClassifier
from sklearn.metrics import f1_score
import time
import traceback
import numpy as np

def classifyMiniRocket(parameters, classifier, classifier_params, X_Train, X_Test, Y_Train, Y_Test):

    time_a = time.perf_counter()

    # Data conversion
    X_Train = X_Train.astype(np.float32)
    X_Test = X_Test.astype(np.float32)

    # MiniRocket run
    param = fit(X_Train, num_features=int(parameters["num_features"]), max_dilations_per_kernel=int(parameters["max_dilations"]))
    X_training_transform = transform(X_Train, param)
    X_test_transform = transform(X_Test, param)

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