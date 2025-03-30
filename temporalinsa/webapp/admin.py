from django.contrib import admin

from .models import Experiment, Method, Parameters, Result, ClassifierParameters

# Register your models here.
admin.site.register(Experiment)
admin.site.register(Method)
admin.site.register(Parameters)
admin.site.register(Result)
admin.site.register(ClassifierParameters)