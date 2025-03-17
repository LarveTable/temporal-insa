from django.urls import path

from . import views

app_name = "webapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("classify/", views.classify, name="classify"),
    path('result/<int:experiment_id>/', views.result, name='result'),
]