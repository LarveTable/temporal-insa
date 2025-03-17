from webapp.models import Experiment, Method, Parameters, Result, ClassifierParameters
from main import ClassifyExperiment

def experimentRequestClassify(data):
    # Create an experiment with the given parameters, datasets is a list of dataset names as a json field
    experiment = Experiment.objects.create(name=data.get("name"), type=data.get("type"), 
                                           datasets=data.get("datasets"), 
                                           scaler=data.get("scaler"), 
                                           classifier=data.get("classifier"), 
                                           date=data.get("date"))
    
    # Save classifier parameters
    if data.get("classifier_parameters"):
        ClassifierParameters.objects.create(
            experiment=experiment,
            values=data["classifier_parameters"]
        )

    # Create Method entries
    for method_data in data.get("methods", []):
        method = Method.objects.create(
            experiment=experiment,
            name=method_data["name"]
        )

        # Save method parameters
        Parameters.objects.create(
            method=method,
            values=method_data["parameters"]
        )
    
    if checkParametersValidity(type, experiment):
        # create the experiment instance
        exp = ClassifyExperiment(experiment)
        # run and return the experiment id
        id = exp.run()
        return id
    else:
        experiment.delete()
        return None

def checkParametersValidity(type, experiment):
    # Check if the parameters are valid for the given experiment type
    #TODO
    return True