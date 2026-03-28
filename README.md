# 🎓 PreSkool Academy - Système de Gestion Scolaire

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Django Version](https://img.shields.io/badge/django-4.0%2B-green)
![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey)

**PreSkool Academy** est une application web robuste de gestion d'établissement scolaire développée avec **Django**. Elle offre une plateforme centralisée pour les administrateurs, les enseignants, les étudiants et les parents, automatisant les processus académiques et administratifs.

---

## 🌟 Fonctionnalités Clés

### 🛠️ Espace Administration (Back-Office)
- **Gestion Complète (CRUD) :** Étudiants, Parents, Enseignants, Départements et Matières.
*   **Tableau de Bord Statistique :** Visualisation en temps réel des effectifs et des performances.
*   **Workflow d'Approbation :** Validation des demandes de cartes d'étudiant et de certificats officiels.

### 👨‍🏫 Espace Enseignant
- **Gestion de Classe :** Liste des étudiants affectés et suivi des cours.
- **Emploi du Temps :** Vue personnalisée des sessions et supervisions.
- **Profil Académique :** Détails sur le département et les matières enseignées.

### 🎓 Espace Étudiant & Parent
- **Profil Personnel :** Informations académiques et coordonnées.
- **Services Digitaux :** Demandes de cartes d'étudiant avec upload de photo et demandes de certificats (scolarité, réussite, relevés).
- **Consultation :** Suivi de la progression et de l'emploi du temps.

---

## 📊 Architecture Technique (UML)

### Diagramme de Classes
Voici la structure simplifiée des données du projet :

```mermaid
classDiagram
    class CustomUser {
        +String username
        +Boolean is_admin
        +Boolean is_teacher
        +Boolean is_student
    }
    class Student {
        +String student_id
        +String student_class
        +Image student_image
        +ForeignKey user
        +OneToOne parent
    }
    class Parent {
        +String father_name
        +String mother_name
        +String address
    }
    class Teacher {
        +String teacher_id
        +ForeignKey user
        +ForeignKey department
    }
    class Department {
        +String name
        +String year_started
    }
    class Subject {
        +String name
        +ForeignKey department
        +String grade
    }
    class CertificateRequest {
        +String type
        +String status
        +DateTime date_requested
    }

    CustomUser "1" -- "0..1" Student : roles
    CustomUser "1" -- "0..1" Teacher : roles
    Student "*" -- "1" Parent : liés
    Teacher "*" -- "1" Department : appartient
    Subject "*" -- "1" Department : liée
    CertificateRequest "*" -- "1" Student : demande
```

### Workflow de demande de document
```mermaid
sequenceDiagram
    participant E as Étudiant
    participant S as Système (Django)
    participant A as Administrateur

    E->>S: Soumet une demande (Carte/Certificat)
    S-->>A: Notifie la nouvelle demande
    A->>S: Valider la demande & Générer PDF
    S-->>E: Document disponible au téléchargement
```

---

## 📸 Galerie & Démonstration

| Tableau de Bord Admin | Carte Étudiant Digitale |
|:---:|:---:|
| ![Admin Dash](./capture_dashboard_admin.png) | ![Student Card](./capture_student_card.png) |

| Gestion des Enseignants | Demande de Certificats |
|:---:|:---:|
| ![Teachers](./capture_teachers_list.png) | ![Certificates](./capture_certificate_requests.png) |

---

## 🚀 Installation & Lancement

Suivez ces étapes pour installer le projet localement :

### 1. Cloner le dépôt
```bash
git clone https://github.com/votre-username/Application_Web_Systeme_De_Gestion_Scolaire.git
cd Application_Web_Systeme_De_Gestion_Scolaire/school
```

### 2. Configurer l'environnement virtuel
```bash
python -m venv monenv
# Windows
.\monenv\Scripts\activate
# Linux/Mac
source monenv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer les migrations & le serveur
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Accédez au portail sur : `http://127.0.0.1:8000/`

---

## 🛠️ Stack Technique
- **Backend :** Django 4.x (Python)
- **Frontend :** HTML5, CSS3 (Vanilla + Bootstrap), JavaScript
- **Base de données :** SQLite (Développement)
- **Librairies :** Pillow (Images), ReportLab/XHTML2PDF (Génération PDF)

---

## 📝 Licence
Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---
*Réalisé dans le cadre du Projet Fin de Module (PFM).*
