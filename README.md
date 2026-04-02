
=======

# 🎓 PRESKOOL - Système de Gestion Scolaire Intelligent (LMS/ERP) 🚀


>>>>>>> 

[![Django](https://img.shields.io/badge/Framework-Django%204.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![UI/UX](https://img.shields.io/badge/UI-Premium%20Glassmorphism-purple.svg)](#)
[![AI-Powered](https://img.shields.io/badge/AI-Chatbot%20Assistant-orange.svg)](#)
[![Security](https://img.shields.io/badge/Security-QR%20Code%20Attendance-blue.svg)](#)

**PreSkool** est une plateforme complète de gestion scolaire (ERP) et d'apprentissage en ligne (LMS) de nouvelle génération. Ce projet transforme l'expérience académique traditionnelle en un environnement numérique **Premium**, **Intelligent** et **Collaboratif**. 

> [!NOTE]
> *L'ensemble des visuels et captures d'écran de l'interface graphique est disponible en haute résolution dans notre [Dossier Drive du Projet](https://drive.google.com/drive/u/0/folders/1dMC407iPSG4S3uP4X1ZCLTAdBlkRav79).*

---

## ✨ Fonctionnalités Phares & Innovations

*   🤖 **Assistant IA (Chatbot)** : Un chatbot intelligent intégré pour accompagner et guider les utilisateurs au quotidien.
*   🌓 **Premium Dark/Light Mode** : Un design moderne, élégant et ergonomique, avec un support complet du mode sombre pour le confort visuel.
*   🌍 **Traduction Intégrée (i18n)** : Support multilingue instantané grâce à l'intégration de Google Translate.
*   📲 **Présence par QR Code Dynamique** : Un système de pointage innovant et ultra-sécurisé avec un QR Code qui s'actualise de façon périodique.
*   🪪 **Cartes Étudiantes Digitales** : Génération automatique de cartes d'identité numériques esthétiques, incluant la photo et le groupe sanguin de l'étudiant.
*   📄 **Générateur de Documents Officiels** : Création automatisée et export au format PDF d'attestations et de certificats de scolarité.
*   📊 **Tableaux de Bord Analytics** : Graphiques interactifs (via Chart.js) pour visualiser les performances, les présences et les statistiques globales.
*   🔍 **OmniSearch** : Un moteur de recherche global ultra-rapide pour naviguer facilement dans l'application.

---

## 👥 Espaces Utilisateurs et Fonctionnalités

### 👑 Espace Administrateur (Direction / HOD)
Un centre de contrôle complet pour piloter l'établissement de bout en bout.
*   **Tableau de Bord 360°** : Vue d'ensemble des effectifs, statistiques financières et académiques.
*   **Gestion des Utilisateurs** : Création et gestion complète des profils (Étudiants, Professeurs, Staff).
*   **Architecture Académique** : Gestion des classes, des matières, des sessions scolaires et des départements.
*   **Supervision des Présences** : Suivi global, génération de rapports et gestion des statistiques d'absence.
*   **Gestion des Congés** : Validation ou refus des demandes de congés du personnel et des étudiants.
*   **Import/Export de Données** : Synchronisation de masse (ex: emplois du temps) via des fichiers XML.
*   **Gestion des Résultats** : Supervision globale des notes, des rattrapages et des validations de semestres.

### 👩‍🏫 Espace Professeur (Staff)
Des outils pensés pour faciliter l'enseignement et le suivi des élèves.
*   **Tableau de Bord Pédagogique** : Statistiques de ses propres classes, taux de présence des élèves, etc.
*   **Gestion des Présences** : Appel numérique ultra-rapide via QR Code ou saisie manuelle traditionnelle.
*   **Évaluations & Notes** : Saisie sécurisée des notes, gestion des étudiants en rattrapage et publication des résultats.
*   **Ressources Pédagogiques** : Partage de supports de cours, de devoirs et de liens éducatifs (ex: dépôt GitHub).
*   **Communication** : Envoi de notifications ciblées aux étudiants.

### 🎓 Espace Étudiant
Un portail personnel intuitif pour suivre sa scolarité en toute autonomie.
*   **Dashboard Analytique** : Suivi global de la progression, statistiques de présence, et visualisation via un "Radar de Compétences".
*   **Dossier Scolaire** : Consultation sécurisée des notes, des statuts de validation (Validé, Non Validé, Rattrapage, Compensation) et de la moyenne générale.
*   **Emploi du Temps** : Accès direct au planning des cours.
*   **E-Learning** : Consultation et téléchargement des supports de cours et autres ressources partagées par les professeurs.
*   **Services Administratifs** : Soumission de demandes de congés, accès à la carte étudiante digitale et téléchargement direct de diverses attestations.

---

## 🛠️ Stack Technologique

**Backend**
*   Python 3.10+
*   Django 4.2+
*   SQLite (Base de données par défaut, facilement extensible vers PostgreSQL/MySQL)

**Frontend**
*   HTML5 / CSS3 / JavaScript (ES6+)
*   Bootstrap (Thème Premium avec éléments de Glassmorphism)
*   **Chart.js** (Visualisation de données et graphiques radar)
*   **Toastify.js** (Notifications et alertes non intrusives)

**Outils & Librairies**
*   **ReportLab** (Génération robuste de PDF)
*   **QRCode.js / qrcode** (Génération de QR codes pour l'Attendance)

---

## 🚀 Guide d'Installation

### 1. Prérequis
*   Python 3.8 ou supérieur installé sur votre machine.
*   Git.

### 2. Clonage du dépôt
```bash
git clone https://github.com/Homam-Dany/Application_Web_Systeme_De_Gestion_Scolaire.git
cd Application_Web_Systeme_De_Gestion_Scolaire
```

### 3. Configuration de l'Environnement Virtuel
Il est fortement recommandé d'utiliser un environnement virtuel pour isoler les dépendances.
```bash
# Création de l'environnement
python -m venv venv

# Activation (Windows)
.\venv\Scripts\activate

# Activation (macOS/Linux)
source venv/bin/activate
```

### 4. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 5. Base de données et Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Lancement du serveur
```bash
python manage.py runserver
```
📍 L'application sera accessible dans votre navigateur à l'adresse : `http://127.0.0.1:8000/`

---

## 💡 À Propos
Ce projet a été développé dans le cadre du module **PFM**, avec une attention toute particulière portée sur :
- L'**Expérience Utilisateur** (UX/UI de haute qualité).
- L'**Optimisation des processus administratifs** scolaires.
- L'intégration de **fonctionnalités modernes** offrant une réelle valeur ajoutée (Mode Sombre, Multilingue, IA, QR Code).
