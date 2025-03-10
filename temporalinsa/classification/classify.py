from .rocket.code.classifyRocket import classifyRocket
from .minirocket.code.classifyMiniRocket import classifyMiniRocket
from .hydra.code.classifyHydra import classifyHydra
from .boss.classifyBoss import classifyBoss
from .LearningShapeletsmain.classifyLearningShapelets import classifyLearningShapelets

def requestClassifyRocket(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test):
    return classifyRocket(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test)

def requestClassifyMiniRocket(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test):
    return classifyMiniRocket(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test)

def requestClassifyHydra(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test):
    return classifyHydra(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test)

def requestClassifyBoss(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test):
    return classifyBoss(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test)

def requestClassifyLShapelets(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test):
    return classifyLearningShapelets(parameters, classifier, X_Train, X_Test, Y_Train, Y_Test)