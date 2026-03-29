# School Management

Une application de gestion scolaire  pour l'EPT développée avec Django. Ce système permet de gérer les étudiants, les professeurs, les notes et les annonces via les dashboards.



---

# Fonctionnalités

Espace Professeur
- Saisie et consultation des notes pour ses propres cours.
- Publication d'annonces.
- Vue d'ensemble des cours assignés.

Espace Étudiant
- Consultation des notes personnelles en temps réel.
- Calcul automatique de la moyenne générale.
- Accès aux dernières annonces de l'établissement et de sa classe.

Administration
- Gestion complète via l'interface CRUD native de Django.
- Contrôle des accès et des rôles (Admin, Professeur, Étudiant).
- Lui seul est autorisé à créer les comptes Etudiants et Professeurs

---

# Aperçu des Dashboards

Interface Professeur
[Dashboard Professeur](screenshots/Dashboard_Prof.png)

Interface Étudiant
[Dashboard Étudiant](screenshots/Dashboard_etudiant.png)


---

#  Comptes de test

Pour tester les différentes interfaces sans créer de nouveaux comptes :

| Rôle | Login | Mot de passe |

| Administrateur| `administrateur` | `admin_ept` |
| Professeur | `michel` | `mysecret4` |
| Étudiant | `Aichatou` | `mysecret1` |

# Dépôt GitHub
https://github.com/Fadieye-cpu/school-management