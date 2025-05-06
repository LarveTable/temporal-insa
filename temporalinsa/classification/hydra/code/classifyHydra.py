from classification.hydra.code.hydra import Hydra, SparseScaler
import torch
import time
import numpy as np
from sklearn.metrics import f1_score
from classification.getClassifier import getClassifier

def classifyHydra(parameters, classifier, classifier_params, X_Train, X_Test, Y_Train, Y_Test):

    # Convert X_training to torch.FloatTensor, shape = (num_examples, 1, length)
    X_Train = torch.FloatTensor(X_Train).unsqueeze(1)

    # Convert X_test to torch.FloatTensor, shape = (num_examples, 1, length)
    X_Test = torch.FloatTensor(X_Test).unsqueeze(1)

    time_a = time.perf_counter()

    # Hydra run
    transform = Hydra(X_Train.shape[-1], k=int(parameters["k"]), g=int(parameters["g"]))
    scaler = SparseScaler()
    X_training_transform = transform(X_Train)
    X_training_transform = scaler.fit_transform(X_training_transform)
    X_test_transform = transform(X_Test)
    X_test_transform = scaler.transform(X_test_transform)

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