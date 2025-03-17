# Was here before
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from result.requestExperiment import experimentRequestClassify
from webapp.models import Experiment, Result

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

def result(request, experiment_id):
    # Retrieve the experiment
    experiment = get_object_or_404(Experiment, id=experiment_id)

    # Retrieve the results for every method of the experiment
    results = Result.objects.filter(experiment=experiment)

    return render(request, "webapp/result.html", {"experiment": experiment, "results": results})

# Requete de classification
@csrf_exempt
def classifyRequest(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            experiment_id = experimentRequestClassify(data)

            return JsonResponse({"status": "success", "experiment_id": experiment_id}, status=201)

        except Exception as e:
            return JsonResponse({"status": "error", "error": str(e)}, status=400)

    return JsonResponse({"status": "error", "error": "Invalid request"}, status=400)