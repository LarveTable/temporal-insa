# Was here before
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from result.requestExperiment import experimentRequestClassify
from webapp.models import ClassifierParameters, Experiment, Method, Parameters, Result

# Create your views here.
# Ici c'est la page d'acceuil
def index(request):
    return render(request, "webapp/home.html")

# Ici page de creation d'expérience
def new(request):
    return render(request, "webapp/new.html")

# Ici page de classification
def classify(request):
    return render(request, "webapp/classify.html")

# Ici page de documentation
def documentation(request):
    return render(request, "webapp/documentation.html")

# Ici page d'importation
def importation(request):
    return render(request, "webapp/importation.html")

# Ici page de visualisation des résultats
def result(request, experiment_id):
    experiment = get_object_or_404(Experiment, id=experiment_id)
    
    # Récupérer les méthodes utilisées dans cette expérience
    methods = Method.objects.filter(experiment=experiment)
    
    # Récupérer les résultats pour chaque méthode
    results = Result.objects.filter(experiment=experiment)
    
    # Récupérer les paramètres du classifieur si disponibles
    try:
        classifier_params = ClassifierParameters.objects.get(experiment=experiment).values
    except ClassifierParameters.DoesNotExist:
        classifier_params = {}
    
    # Créer un dictionnaire pour stocker toutes les informations de l'expérience
    experiment_data = {
        "id": experiment.id,
        "name": experiment.name if experiment.name else f"Experiment {experiment.id}",
        "type": experiment.type,
        "date": experiment.date.isoformat(),
        "datasets": experiment.datasets,  # Déjà un JSONField
        "classifier": experiment.classifier,
        "classifier_params": classifier_params,
        "methods": [],
        "results": []
    }
    
    # Ajouter les méthodes et leurs paramètres
    for method in methods:
        method_info = {"name": method.name}
        
        # Récupérer les paramètres de la méthode si disponibles
        try:
            params = Parameters.objects.get(method=method).values
            method_info["parameters"] = params
        except Parameters.DoesNotExist:
            method_info["parameters"] = {}
            
        experiment_data["methods"].append(method_info)
    
    # Ajouter les résultats
    for result in results:
        experiment_data["results"].append({
            "method": result.method.name,
            "values": result.values  # Déjà un JSONField
        })

    # Rendre le template avec les données
    return render(request, "webapp/result.html", {
        "experiment_data_json": json.dumps(experiment_data)
    })

# Requete de classification
@csrf_exempt
def classifyRequest(request):
    if request.method == 'POST':
        #try:
            data = json.loads(request.body)

            experiment_id = experimentRequestClassify(data)

            return JsonResponse({"status": "success", "experiment_id": experiment_id}, status=201)

        #except Exception as e:
         #   return JsonResponse({"status": "error", "error": str(e)}, status=400)

    return JsonResponse({"status": "error", "error": "Invalid request"}, status=400)