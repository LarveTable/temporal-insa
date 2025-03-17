from django.db import models

# Create your models here.
class Experiment(models.Model):
    # id of the experiment
    id = models.IntegerField("ID", primary_key=True)
    # name of the experiment
    name = models.CharField("Name", max_length=20, null=True)
    # type of the experiment
    type = models.CharField("Type", max_length=4)
    # date of creation
    date = models.DateTimeField("Date created")
    # names of datasets
    datasets = models.JSONField("Datasets")
    # scaler for the experiment
    scaler = models.CharField("Scaler", max_length=20, null=True)
    # classifier for the experiment
    classifier = models.CharField("Classifier", max_length=20, null=True)

    # string representation of the object
    def __str__(self):
        return f"{self.id} - {self.type} - {self.date}"

class Method(models.Model):
    # attached experiment
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    # name of the method
    name = models.CharField("Name", max_length=20)

    # string representation of the object
    def __str__(self):
        return f"{self.experiment} - {self.name}"

class Parameters(models.Model):
    # attached method
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    # values of the parameters
    values = models.JSONField("Values")

    # string representation of the object
    def __str__(self):
        return f"{self.method} - {self.values}"
    
class Result(models.Model):
    # attached experiment
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    # attached method
    method = models.ForeignKey(Method, on_delete=models.CASCADE)
    # values of the results
    values = models.JSONField("Values")

    # string representation of the object
    def __str__(self):
        return f"{self.experiment} - {self.method} - {self.values}"
    
class ClassifierParameters(models.Model):
    # attached experiment
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    # values of the parameters
    values = models.JSONField("Values")

    # string representation of the object
    def __str__(self):
        return f"{self.method} - {self.values}"