from django.contrib import admin

from .models import Experiment, Method, Parameters

# Register your models here.
admin.site.register(Experiment)
admin.site.register(Method)
admin.site.register(Parameters)