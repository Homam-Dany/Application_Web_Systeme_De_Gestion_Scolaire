# 🎓 PreSkool - Système de Gestion Scolaire Intelligent (LMS/ERP) 🚀

[![Django](https://img.shields.io/badge/Framework-Django%204.2%2B-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![UI/UX](https://img.shields.io/badge/UI-Premium%20Glassmorphism-purple.svg)](#)
[![AI-Powered](https://img.shields.io/badge/AI-Chatbot%20Assistant-orange.svg)](#)
[![Security](https://img.shields.io/badge/Security-QR%20Code%20Attendance-blue.svg)](#)

**PreSkool** est une plateforme complète d'apprentissage en ligne (LMS) et de gestion scolaire (ERP) de nouvelle génération. Ce projet transforme l'expérience académique traditionnelle en un environnement numérique **Premium**, **Intelligent** et **Collaboratif**.

> [!NOTE]
> *L'ensemble des visuels et captures d'écran de l'interface graphique est disponible en haute résolution dans notre [Dossier Drive Principale du Projet](https://drive.google.com/drive/u/0/folders/1dMC407iPSG4S3uP4X1ZCLTAdBlkRav79).*

---

## 🎥 Démonstration Vidéo

Découvrez l'application en action à travers notre vidéo de démonstration complète, présentant l'interface utilisateur, le parcours étudiant, le parcours professeur et l'interface administrateur :

▶️ **[Voir la vidéo de présentation (Lien Google Drive)](https://drive.google.com/drive/folders/1fB2lloK0bYfbs3QJr7CCFwb-uTgFxcIs?usp=drive_link)**

---

## ✨ Fonctionnalités Phares & Innovations

*   🤖 **Assistant IA (Chatbot)** : Un chatbot intelligent intégré pour accompagner et guider les utilisateurs au quotidien.
*   🌓 **Premium Dark/Light Mode** : Un design moderne, élégant et ergonomique, avec un support complet du mode sombre pour un confort visuel optimal.
*   🌍 **Traduction Intégrée (i18n)** : Support multilingue instantané grâce à l'intégration de traduction automatique.
*   📲 **Présence par QR Code Dynamique** : Système de pointage innovant et ultra-sécurisé via un QR Code éphémère qui s'actualise périodiquement.
*   🪪 **Cartes Étudiantes Digitales** : Génération automatique de cartes d'identité numériques esthétiques, formatées pour l'impression.
*   📄 **Générateur de Documents Officiels** : Création automatisée et export au format PDF pour les attestations de réussite et certificats de scolarité.
*   📊 **Tableaux de Bord Analytics** : Graphiques avancés et interactifs (via Chart.js) pour visualiser les indicateurs de performance, l'absentéisme et les données démographiques.
*   🔍 **OmniSearch** : Un moteur de recherche global ultra-rapide pour naviguer instantanément au sein de l'application.

---

## 👥 Espaces Utilisateurs et Fonctionnalités

### 👑 Espace Administrateur (Direction / HOD)
*   **Tableau de Bord 360°** : Vue d'ensemble des effectifs, statistiques et performances globales de l'établissement.
*   **Gestion des Identités** : Création, validation et administration complète des profils.
*   **Architecture Académique** : Modélisation des classes, matières, sessions scolaires et départements.
*   **Supervision des Présences** : Suivi global de l'assiduité, génération de rapports et alertes.
*   **Gestion des Flux Administratifs** : Approbation des demandes de cartes étudiantes, attestations, et réservations de salles.
*   **Validation des Notes** : Supervision sécurisée des procès-verbaux, traitement des rattrapages, et publication officielle des résultats semestriels.

### 👩‍🏫 Espace Professeur
*   **Tableau de Bord Pédagogique** : Accès rapide aux cours de la journée, suivi statistique et alertes.
*   **Appel Numérique (Web & Mobile)** : Pointage innovant via session QR Code dynamique ou pointage matriciel classique.
*   **Évaluations & Notes** : Saisie sécurisée et centralisée des résultats d'examens avec propositions de modification post-publication.
*   **Ressources Pédagogiques** : Espace Cloud pour partager les supports de cours, TP, TD et liens éducatifs.
*   **Communication Directe** : Interface d'envoi de notifications ciblées aux étudiants d'une classe ou d'une promotion.

### 🎓 Espace Étudiant
*   **Dashboard Analytique** : Suivi de progression, statistiques individuelles de présence, et rendu graphique des compétences acquises.
*   **Dossier Scolaire & Notes** : Consultation des moyennes, calcul en temps réel des validations de modules (Validé, Non Validé, Rattrapage).
*   **Planning & Cours** : Emploi du temps numérique avec les modifications de salles en temps réel.
*   **E-Learning Actif** : Téléchargement instantané des supports de cours déposés par l'équipe pédagogique.
*   **Guichet Administratif Numérique** : Soumission en 1-clic de demandes officielles (carte étudiante, attestations de scolarité).

---

## 🛠️ Stack Technologique

**Backend**
*   **Python 3.10+**
*   **Django 4.2+** / ORM Django
*   SQLite (Base de données locale par défaut - Migrable vers PostgreSQL)

**Frontend**
*   HTML5 / CSS3 / JavaScript (ES6+)
*   Conception UI sur-mesure (Thème Premium avec composants *Glassmorphism*)
*   **Chart.js** (Visualisation analytique)
*   **Toastify.js** (Notifications asynchrones et non bloquantes)

**Outils Spécialisés**
*   **ReportLab** (Génération PDF complexe)
*   **QRCode.js** (Rendu cryptographique pour les sessions d'appel)

---

## 🚀 Guide d'Installation

### 1. Prérequis
*   Python 3.10 ou supérieur installé (Assurez-vous qu'il est ajouté au PATH).
*   Git installé.

### 2. Clonage du dépôt
```bash
git clone https://github.com/Homam-Dany/Application_Web_Systeme_De_Gestion_Scolaire.git
cd Application_Web_Systeme_De_Gestion_Scolaire
cd school
```

### 3. Configuration de l'Environnement Virtuel (Recommandé)
```bash
# Création de l'environnement virtuel
python -m venv venv

# Activation (Sous Windows)
.\venv\Scripts\activate

# Activation (Sous macOS/Linux)
source venv/bin/activate
```

### 4. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 5. Préparation de la base de données
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Lancement du serveur local
```bash
python manage.py runserver
```
📍 L'application sera accessible depuis votre navigateur à l'adresse suivante : **`http://127.0.0.1:8000/`**

---

## 💡 À Propos

Projet développé dans le cadre de notre **Projet de Fin de Module (PFM)**. Ce développement place au cœur de ses préoccupations l'ergonomie (UX/UI), la digitalisation éco-responsable des processus administratifs, et l'intégration de solutions modernes adaptées à l'éducation 2.0.
