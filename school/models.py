from django.db import models

# Create your models here.

class Departement(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Classe (models.Model):
    name = models.CharField(max_length=10) 
    level = models.IntegerField() 
    department = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Matiere (models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return self.name