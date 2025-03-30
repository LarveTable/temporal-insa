from webapp.models import Experiment, Method, Parameters, Result, ClassifierParameters
from preprocess.process_dataset import Processing
from classification.classify import requestClassifyRocket, requestClassifyMiniRocket, requestClassifyHydra, requestClassifyBoss, requestClassifyLShapelets

class ClassifyExperiment:
    def __init__(self, experiment):
        # id of the experiment object stored in the database
        self.id = experiment.id
        # matching list of methods corresponding to the experiment
        self.methods = Method.objects.filter(experiment=self.id)
        # matching dictionnaire of parameters corresponding to the methods
        self.parameters = {}
        for method in self.methods:
            self.parameters[method.name] = Parameters.objects.get(method=method.id)
        # datasets of the experiment
        self.datasets = experiment.datasets
        # scaler of the experiment
        self.scaler = experiment.scaler
        # classifier of the experiment
        self.classifier = experiment.classifier
        # parameters of the classifier
        self.classifier_params = ClassifierParameters.objects.filter(experiment=self.id)

    def run(self):
        # loop on datasets
        for dataset in self.datasets:
            # preprocess the dataset
            processer = Processing(dataset)
            X_Train, X_Test, Y_Train, Y_Test = processer.scale(self.scaler)
            # loop on methods
            for method in self.methods:
                # returning results of the classification (accuracy, f1-score, etc.)
                match method.name:
                    case "Rocket":
                        result = requestClassifyRocket(self.parameters[method.name].values, self.classifier, self.classifier_params, X_Train, X_Test, Y_Train, Y_Test)
                    case "MiniRocket":
                        result = requestClassifyMiniRocket(self.parameters[method.name].values, self.classifier, self.classifier_params, X_Train, X_Test, Y_Train, Y_Test)
                    case "Hydra":
                        result = requestClassifyHydra(self.parameters[method.name].values, self.classifier, self.classifier_params, X_Train, X_Test, Y_Train, Y_Test)
                    case "Boss":
                        result = requestClassifyBoss(self.parameters[method.name].values, self.classifier, self.classifier_params, X_Train, X_Test, Y_Train, Y_Test)
                    case "L-Shapelets":
                        result = requestClassifyLShapelets(self.parameters[method.name].values, self.classifier, self.classifier_params, X_Train, X_Test, Y_Train, Y_Test)
                    case _:
                        raise ValueError("Invalid method")
                    
                # save the results
                exp = Experiment.objects.get(id=self.id)
                method = Method.objects.get(id=method.id)
                Result.objects.create(experiment=exp, method=method, values=result)
        return self.id