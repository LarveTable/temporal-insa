from classification.rocket.code.rocket_functions import generate_kernels, apply_kernels
from classification.getClassifier import getClassifier

def classifyRocket(parameters, classifier, classifier_params, X_Train, X_Test, Y_Train, Y_Test):
    
    # Rocket run
    input_length = X_Train.shape[-1]
    kernels = generate_kernels(input_length, parameters["num_kernels"])
    X_training_transform = apply_kernels(X_Train, kernels)
    X_test_transform = apply_kernels(X_Test, kernels)

    # Classifier run
    classifier = getClassifier(classifier, classifier_params)
    classifier.fit(X_training_transform, Y_Train)
    accuracy = classifier.score(X_test_transform, Y_Test)

    return accuracy