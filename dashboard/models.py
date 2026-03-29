

from django.db import models
from authentification.models import User
from school.models import Departement, Classe, Matiere

# Create your models here.
class Professeur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    departement = models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    grade = models.CharField(max_length=50)

    def __str__(self):
        return self.user.get_full_name()
    
class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    matricule = models.CharField(max_length=20, unique=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()
    
class Cours(models.Model):
    professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    horaire = models.DateTimeField()

    def __str__(self):
        return f"{self.matiere.name} - {self.classe.name} - {self.professeur.user.get_full_name()}"
    
class Note(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    note = models.FloatField()

    def __str__(self):
        return f"{self.etudiant.user.get_full_name()} - {self.cours.matiere.name} : {self.note}"
    
class Document(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='documents/')

    def __str__(self):
        return f"{self.title} - {self.cours.matiere.name}"
    
class Annonce(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
            if self.classe:
                return f"[{self.classe.name}] {self.title}"
            return f"[TOUS] {self.title}"
    
