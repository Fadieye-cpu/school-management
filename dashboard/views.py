from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from dashboard.forms import NoteForm, AnnonceForm
from school.models import Departement, Classe, Matiere
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Annonce, Etudiant, Professeur, Note, Cours
from django.contrib.auth.decorators import user_passes_test


@login_required
def student_home(request):
    # Logique spécifique (ex: récupérer les notes de l'étudiant)
    return render(request, 'dashboard/studenthome.html')

@login_required
def prof_home(request):
    # Logique spécifique (ex: liste de ses cours)
    return render(request, 'dashboard/profhome.html')

@user_passes_test(lambda u: u.is_staff or u.role == 'ADMIN')
def admin_dashboard(request):
    context = {
        'nb_etudiants': Etudiant.objects.count(),
        'nb_professeurs': Professeur.objects.count(),
        'nb_classes': Classe.objects.count(),
        'departements': Departement.objects.all(),
    }
    return render(request, 'dashboard/adminhome.html', context)

@login_required
def student_dashboard(request):
    # 1. Récupérer le profil étudiant lié à l'utilisateur connecté
    try:
        etudiant = Etudiant.objects.get(user=request.user)
        # 2. Récupérer toutes les notes de cet étudiant
        notes = Note.objects.filter(etudiant=etudiant).select_related('cours')
        
        # Calculer la moyenne générale simple pour le dashboard
        if notes.exists():
            moyenne = sum(n.note for n in notes) / notes.count()
        else:
            moyenne = 0

        annonces = Annonce.objects.filter(
            Q(classe=etudiant.classe) | Q(classe__isnull=True)
        ).order_by('-date')[:5]
            
    except Etudiant.DoesNotExist:
        notes = []
        moyenne = 0
        etudiant = None
        annonces = Annonce.objects.filter(classe__isnull=True).order_by('-date')[:5]

    # 3. Récupérer les 5 dernières annonces
    annonces = Annonce.objects.all().order_by('-date')[:5]

    context = {
        'notes': notes,
        'annonces': annonces,
        'moyenne': round(moyenne, 2),
        'etudiant': etudiant,
    }
    return render(request, 'dashboard/studenthome.html', context)
    

@login_required
def professeur_dashboard(request):
    try:
        prof = Professeur.objects.get(user=request.user)
        ses_cours = Cours.objects.filter(professeur=prof)
        
        # Initialisation des formulaires
        form = NoteForm(professeur=prof)
        annonce_form = AnnonceForm(professeur=prof)

        if request.method == 'POST':
            # Si on ajoute une NOTE
            if 'submit_note' in request.POST:
                form = NoteForm(request.POST, professeur=prof)
                if form.is_valid():
                    form.save()
                    return redirect('dashboard:prof_home')
            
            # Si on ajoute une ANNONCE
            elif 'submit_annonce' in request.POST:
                annonce_form = AnnonceForm(request.POST, professeur=prof)
                if annonce_form.is_valid():
                    annonce_form.save()
                    return redirect('dashboard:prof_home')

        # On récupère aussi les annonces déjà postées (optionnel)
        mes_annonces = Annonce.objects.all().order_by('-date')[:5]

        return render(request, 'dashboard/profhome.html', {
            'prof': prof,
            'form': form,
            'annonce_form': annonce_form,
            'notes': Note.objects.filter(cours__in=ses_cours).order_by('-id')[:10],
            'mes_annonces': mes_annonces
        })

    except Professeur.DoesNotExist:
        return redirect('home')
    

@user_passes_test(lambda u: u.is_staff or u.role == 'ADMIN')
def admin_dashboard(request):
    context = {
        'nb_etudiants': Etudiant.objects.count(),
        'nb_professeurs': Professeur.objects.count(),
        'nb_classes': Classe.objects.count(),
        'nb_cours': Cours.objects.count(),
    }
    return render(request, 'dashboard/adminhome.html', context)