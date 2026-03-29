from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/', views.register_view, name='register'),

    # Connexion (Utilise le template par défaut ou celui qu'on va créer)
    # Déconnexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', views.login_step1, name='login1'),
    path('login/password/', views.login_step2, name='login2'),
    path('demo/', views.demo_accounts, name='demo_accounts'),

    
    # Redirection après succès (facultatif si géré dans settings.py)
    # path('redirect/', views.redirect_by_role, name='role_redirect'),
]