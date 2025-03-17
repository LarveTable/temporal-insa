# available classifiers
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import RidgeClassifierCV
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier

def getClassifier(classifier, classifier_params):
    # return the classifier object
    match classifier:
        case "SVC":
            return SVC()
        case "RidgeClassifierCV":
            return RidgeClassifierCV()
        case "RandomForestClassifier":
            return RandomForestClassifier()
        case "LogisticRegression":
            return LogisticRegression()
        case "SGDClassifier":
            return SGDClassifier()
        case "KNeighborsClassifier":
            return KNeighborsClassifier()
        case "GaussianNB":
            return GaussianNB()
        case "DecisionTreeClassifier":
            return DecisionTreeClassifier()
        case "AdaBoostClassifier":
            return AdaBoostClassifier()
        case "GradientBoostingClassifier":
            return GradientBoostingClassifier()
        case "ExtraTreesClassifier":
            return ExtraTreesClassifier()
        case "BaggingClassifier":
            return BaggingClassifier()
        case _:
            raise ValueError("Invalid classifier")