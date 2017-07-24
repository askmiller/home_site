from django.db import models

# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)

class Layer(models.Model):
    type = models.CharField(max_length=250)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

class Node(models.Model):
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    activation = models.CharField(max_length=1000)