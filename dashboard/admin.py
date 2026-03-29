from django.contrib import admin

# Register your models here.
from .models import Professeur, Etudiant, Cours, Note

admin.site.register(Professeur)
admin.site.register(Etudiant)
admin.site.register(Cours)
admin.site.register(Note)