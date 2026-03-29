from django.contrib import admin

from school.models import Classe, Departement, Matiere

# Register your models here.
admin.site.register(Departement)
admin.site.register(Classe)
admin.site.register(Matiere)