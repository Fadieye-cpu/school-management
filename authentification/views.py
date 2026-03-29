

# Create your views here.
from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = InscriptionForm()
    return render(request, 'authentification/register.html', {'form': form})


# 1. La page d'accueil (toujours accessible)
def accueil(request):
    return render(request, 'accueil.html') 

# 2. La vue "Aiguillage" (appelée juste après le login)
@login_required
def redirect_after_login(request):
    if request.user.role == 'STUDENT':
        return redirect('dashboard:student_home')
    elif request.user.role == 'PROF':
        return redirect('dashboard:prof_home')
    else:
        return redirect('admin:index')
    


def login_step1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        # Vérification des deux champs simultanément
        user_exists = User.objects.filter(username=username, email=email).exists()
        
        if user_exists:
            request.session['login_username'] = username
            return redirect('login2')
        else:
            messages.error(request, "Les informations saisies ne correspondent à aucun compte.")
            
    return render(request, 'authentification/login1.html')

def login_step2(request):
    username = request.session.get('login_username')
    
    if not username:
        return redirect('login1')

    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            del request.session['login_username'] # On nettoie la session
            return redirect('dashboard_redirect') # Ta redirection par rôle
        else:
            messages.error(request, "Mot de passe incorrect.")
            
    return render(request, 'authentification/login2.html', {'username': username})

def demo_accounts(request):
    return render(request, 'authentification/demo_accounts.html')