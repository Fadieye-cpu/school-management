# authentification/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User
from dashboard.models import Etudiant, Professeur
from school.models import Classe, Departement

class InscriptionForm(UserCreationForm):
    role = forms.ChoiceField(choices=User.ROLE_CHOICES, widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_role'}))
    
    # Champs Étudiant (id unique pour le JS)
    matricule = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'group': 'student-field'}))
    classe = forms.ModelChoiceField(queryset=Classe.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select', 'group': 'student-field'}))
    date_naissance = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'group': 'student-field'}))
    lieu_naissance = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'group': 'student-field'}))
    
    # Champs Professeur
    departement = forms.ModelChoiceField(queryset=Departement.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-select', 'group': 'prof-field'}))
    grade = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'group': 'prof-field'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "role")

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data.get('role')
        if commit:
            user.save()
            if user.role == 'STUDENT':
                Etudiant.objects.create(
                    user=user,
                    matricule=self.cleaned_data.get('matricule'),
                    classe=self.cleaned_data.get('classe'),
                    date_naissance=self.cleaned_data.get('date_naissance'),
                    lieu_naissance=self.cleaned_data.get('lieu_naissance')
                )
            elif user.role == 'PROF':
                Professeur.objects.create(
                    user=user,
                    departement=self.cleaned_data.get('departement'),
                    grade=self.cleaned_data.get('grade')
                )
        return user