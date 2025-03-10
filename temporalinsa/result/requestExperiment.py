from ..webapp.models import Experiment, Method, Parameters, Result
from ..main import ClassifyExperiment

def experimentRequestClassify(name, type, datasets, methods, parameters):
    # Create an experiment with the given parameters, datasets is a list of dataset names as a json field
    experiment = Experiment.objects.create(name=name, type=type, datasets=datasets)
    # Methods is a list of method names
    for method in methods:
        method = Method.objects.create(experiment=experiment, name=method)
        # Parameters is a list of parameter values as a json field with method name and associated parameters
        for parameter in parameters:
            Parameters.objects.create(method=method, values=parameter)
    
    if checkParametersValidity(type, experiment):
        # create the experiment instance
        exp = ClassifyExperiment(experiment)
        # run and return the experiment
        return exp.run()
    else:
        experiment.delete()
        return None

def checkParametersValidity(type, experiment):
    # Check if the parameters are valid for the given experiment type
    return True