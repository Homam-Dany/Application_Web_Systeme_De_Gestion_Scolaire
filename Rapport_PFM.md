# Rapport : Projet de gestion d'école (PreSkool)

## Sommaire
1. [Introduction](#1-introduction)
2. [Partie 1 : Mise en place de l'environnement et du projet](#2-partie-1--mise-en-place-de-lenvironnement-et-du-projet)
3. [Partie 2 : Configuration du projet](#3-partie-2--configuration-du-projet)
4. [Partie 3 : Templates et Fichiers Statiques](#4-partie-3--templates-et-fichiers-statiques)
5. [Partie 4 : Création de l'application Student, Modèles et Migrations](#5-partie-4--création-de-lapplication-student-modèles-et-migrations)
6. [Partie 5 : Interface d'Administration Django](#6-partie-5--interface-dadministration-django)

---

## 1. Introduction
Ce rapport documente la construction pas à pas d'une application web de gestion d'école (PreSkool) avec le framework Django. Il trace l'ensemble des commandes exécutées ainsi que leurs objectifs afin de construire le projet final. Ce document sera mis à jour au fur et à mesure de l'avancement des parties.

## 2. Partie 1 : Mise en place de l'environnement et du projet

**1.1 Création de l'environnement virtuel et activation**
* L'environnement virtuel `monenv` a été créé et activé, isolant les dépendances du projet `school`.

**1.2 Installation de Django**
* **Commande :** `pip install django`
* **Objectif :** Installation du framework web Python Django.
* **Mise à jour supplémentaire :** `python.exe -m pip install --upgrade pip` pour la mise à jour de l'outil de gestion des paquets `pip`.

**1.3 Création du projet Django**
* **Commandes :** 
  ```bash
  django-admin startproject school
  cd school
  ```
* **Objectif :** Création de l'architecture de base du projet global nommé `school` et navigation dans son dossier principal.

**1.4 Création de la première application : faculty**
* **Commande :** `py manage.py startapp faculty`
* **Objectif :** Génération de la première application indépendante `faculty` au sein du projet `school`, contenant les fichiers nécessaires pour gérer ses vues, modèles, et son administration.

## 3. Partie 2 : Configuration du projet

**2.1 Enregistrement de l'application dans settings.py**
* **Action :** Ajout de `'faculty',` dans la liste `INSTALLED_APPS` du fichier `school/settings.py`.
* **Objectif :** Informer le projet Django de l'existence de la nouvelle application pour qu'il puisse prendre en compte ses modèles, vues, et templates.

**2.2 Création du fichier urls.py de l'application faculty**
* **Action :** Création du fichier `faculty/urls.py` avec la route de base `path('', views.index, name='index')`.
* **Objectif :** Définir les routes URL spécifiques à l'application `faculty`.

**2.3 Liaison avec les URLs du projet principal**
* **Action :** Ajout de `path('', include('faculty.urls'))` dans le fichier `school/urls.py`.
* **Objectif :** Déléguer la gestion des URL de la racine du site vers le fichier de routage de l'application `faculty`.

**2.4 Création de la vue index dans faculty**
* **Action :** Création de la fonction `index(request)` dans `faculty/views.py` qui retourne l'affichage de "First Test".
* **Objectif :** Traiter la requête HTTP entrante sur la route principale et renvoyer une réponse texte simple pour tester le bon fonctionnement de la configuration.

**2.5 Démarrage et vérification du serveur**
* **Commande :** `py manage.py runserver`
* **Objectif :** Lancement du serveur de développement local Django. L'application est alors accessible sur l'adresse locale `http://localhost:8000/`. L'affichage du message "First Test" confirme que les liens entre la vue, les URLs de l'application et les URLs natives du projet fonctionnent correctement.

*Aperçu du résultat dans le navigateur :*
![First Test Screenshot](./capture_first_test.png)

## 4. Partie 3 : Templates et Fichiers Statiques

**3.1 Création des dossiers static et templates**
* **Action :** Création des répertoires `static/` et `templates/` à la racine du projet `school`.
* **Objectif :** Organiser les fichiers statiques (CSS, JS, images) et les modèles HTML séparément du code Python.

**3.2 Configuration de settings.py pour les templates et les statiques**
* **Action :** Import de `os`, mise à jour du chemin `DIRS` dans la configuration `TEMPLATES`, et ajout des variables `STATIC_URL` et `STATICFILES_DIRS`.
* **Objectif :** Indiquer à Django où chercher les fichiers statiques et les templates HTML lors du rendu des pages.

**3.3 Import des assets Bootstrap**
* **Action :** Copie du dossier `assets/` (styles, scripts, images) contenant le thème PreSkool dans le répertoire `static/`.
* **Objectif :** Intégrer les styles visuels et la dynamique du tableau de bord.

**3.4 Intégration des templates HTML**
* **Action :** Création des fichiers `base.html` et `index.html` sous le répertoire `templates/Home/`. L'utilisation des balises `{% load static %}` permet de charger les ressources graphiques et `{% extends %}` d'hériter de la structure principale.
* **Objectif :** Structurer les pages du site avec le moteur de template dynamique de Django.

**3.5 Mise à jour de la vue pour utiliser un template**
* **Action :** Modification de `faculty/views.py` pour utiliser la fonction `render` et retourner le template `Home/index.html`.
* **Objectif :** Lier la logique de la vue à la nouvelle interface graphique HTML plutôt qu'à un simple texte. La vue est désormais testée et fonctionnelle.

*Aperçu du tableau de bord (Dashboard) intégré :*
![Dashboard Screenshot](./capture_dashboard.png)

## 5. Partie 4 : Création de l'application Student, Modèles et Migrations

**4.1 Création de l'application student**
* **Commande :** `py manage.py startapp student`
* **Objectif :** Créer un module distinct pour la gestion des étudiants et de leurs parents.

**4.2 Enregistrement de l'application student dans settings.py**
* **Action :** Ajout de `'student'` dans la liste `INSTALLED_APPS` du fichier `school/settings.py`.
* **Objectif :** Permettre à Django de détecter et d'intégrer l'application `student` dans le projet principal.

**4.3 Création de urls.py pour l'application student**
* **Action :** Définition des routes locales de l'application (`student_list` et `add_student`) et liaison de ces routes dans `school/urls.py` via `path('student/', include('student.urls'))`.
* **Objectif :** Structurer le routage des URL relatives aux étudiants. *(Note : des vues temporaires ont été créées conjointement dans `student/views.py` pour valider les routes et permettre la migration sans erreur).*

**4.4 Définition des modèles dans student/models.py**
* **Action :** Création des classes Python `Parent` et `Student` (héritant de `models.Model`), avec une relation `OneToOneField` entre l'étudiant et son parent.
* **Objectif :** Modéliser la structure de la base de données de l'application (champs de textes, dates, images, relations). *(Note : Une légère erreur de syntaxe `models.model` au lieu de `models.Model` a été corrigée).*

**4.5 Installation de Pillow pour ImageField**
* **Commande :** `python -m pip install Pillow`
* **Objectif :** Installer la bibliothèque requise pour gérer le champ d'upload d'image `student_image`.

**4.6 Création des fichiers de migration**
* **Commande :** `py manage.py makemigrations`
* **Objectif :** Générer les scripts Python reflétant la création des tables `Parent` et `Student`. 

**4.7 Application des migrations**
* **Commande :** `py manage.py migrate`
* **Objectif :** Exécuter les scripts de migration afin de créer concrètement toutes les tables requises (y compris celles par défaut de Django) dans la base de données SQLite.

*Aperçu de l'exécution des migrations :*
![Migrations Screenshot](./capture_migrations.png)

## 6. Partie 5 : Interface d'Administration Django

**5.1 Création d'un super-utilisateur (Superuser)**
* **Commande :** `py manage.py createsuperuser`
* **Identifiants créés :** Utilisateur `Houssam`, email `elhajiouihoussam@gmail.com`.
* **Objectif :** Créer un compte administrateur avec tous les privilèges pour accéder au panneau d'administration sécurisé de Django et gérer le contenu de la base de données.

**5.2 Enregistrement des modèles dans l'interface admin**
* **Action :** Mise à jour du fichier `student/admin.py` pour enregistrer les modèles `Parent` et `Student` en utilisant le décorateur `@admin.register()` avec des classes `ModelAdmin` personnalisées :
  * **ParentAdmin :** affichage des colonnes `father_name`, `mother_name`, `father_mobile`, `mother_mobile` ; recherche et filtrage par nom des parents.
  * **StudentAdmin :** affichage de toutes les informations clés (nom, prénom, ID, genre, date de naissance, classe, etc.) ; recherche par nom/ID/classe ; filtrage par genre, classe et section.
* **Objectif :** Rendre ces modèles visibles et gérables (opérations CRUD) directement depuis l'interface web d'administration de Django, avec une présentation optimisée.

**5.3 Vérification de l'interface d'administration**
* **Action :** Accès à `http://localhost:8000/admin/` avec les identifiants du super-utilisateur, ajout de données de test (un parent et un étudiant), et vérification de l'affichage.
* **Objectif :** Valider que les modèles sont correctement enregistrés et que les listes d'affichage, les filtres et la recherche fonctionnent comme prévu.

*Aperçu du panneau d'administration :*
![Admin Dashboard Screenshot](./capture_admin_dashboard.png)

*Liste des parents enregistrés :*
![Parents List Screenshot](./capture_admin_parents.png)

*Liste des étudiants enregistrés :*
![Students List Screenshot](./capture_admin_students.png)

## 7. Partie 6 : Vues CRUD pour la Gestion des Étudiants

**6.1 Mise à jour de student/views.py**
* **Action :** Création des fonctions de vues (CRUD) pour chaque opération : `student_list`, `add_student`, `edit_student`, `view_student`, `delete_student`.
* **Objectif :** Gérer les requêtes HTTP pour l'affichage, l'ajout, la consultation, la modification et la suppression d'étudiants.

**6.2 Mise à jour des routes dans student/urls.py**
* **Action :** Ajout des routes correspondant à chaque vue CRUD, en utilisant des paramètres tels que `<str:student_id>` pour identifier précisément quel étudiant ou parent est ciblé.
* **Objectif :** Associer les URLs appropriées (listes de données ou actions spécifiques) aux vues.

**6.3 Implémentation de la vue d'ajout d'un étudiant**
* **Action :** Développement de la logique POST dans `add_student` pour récupérer les données du formulaire HTML, créer d'abord un enregistrement `Parent`, puis l'instance `Student` liée au parent, et rediriger l'utilisateur vers la liste des étudiants avec un message de succès (via le module messages de Django).
* **Objectif :** Permettre l'enregistrement conjoint d'un parent et d'un étudiant de manière fluide et sécurisée dans la base de données.

**6.4 Liaison des menus aux routes**
* **Action :** Modification du fichier de template partagé `templates/Home/base.html` pour utiliser les balises locales `{% url 'nom_route' %}` comme `{% url 'student_list' %}` et `{% url 'add_student' %}` dans les attributs HTML `href` du menu de navigation.
* **Objectif :** Lier dynamiquement les liens du menu latéral du tableau de bord aux vues et URLs du projet, s'assurant ainsi que toute mise à jour de route côté backend est répercutée automatiquement côté front.

*Aperçu de la page listant les étudiants (Student List) :*
![Student List Screenshot](./capture_student_list.png)

*Aperçu du formulaire d'ajout d'étudiant (Add Student) :*
![Student Add Screenshot](./capture_student_add.png)
