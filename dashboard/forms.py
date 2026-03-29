from django import forms

from school.models import Classe
from .models import Note, Cours, Annonce


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['etudiant', 'cours', 'note']
        widgets = {
            'etudiant': forms.Select(attrs={'class': 'form-select'}),
            'cours': forms.Select(attrs={'class': 'form-select'}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '20'}),
        }

    def __init__(self, *args, **kwargs):
        # On récupère le professeur passé depuis la vue
        professeur = kwargs.pop('professeur', None)
        super(NoteForm, self).__init__(*args, **kwargs)
        if professeur:
            # On limite les choix aux cours donnés par ce prof précis
            self.fields['cours'].queryset = Cours.objects.filter(professeur=professeur)

class AnnonceForm(forms.ModelForm):
    class Meta:
        model = Annonce
        fields = ['title', 'content', 'classe']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'annonce'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Détails...'}),
            'classe': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        professeur = kwargs.pop('professeur', None)
        super(AnnonceForm, self).__init__(*args, **kwargs)
        if professeur:
            # Le prof ne peut envoyer des annonces qu'aux classes qu'il enseigne
            classes_ids = Cours.objects.filter(professeur=professeur).values_list('classe', flat=True)
            self.fields['classe'].queryset = Classe.objects.filter(id__in=classes_ids)
            # On ajoute une option vide pour "Toute l'école" si tu veux le permettre
            self.fields['classe'].empty_label = "Toute l'école (Général)"