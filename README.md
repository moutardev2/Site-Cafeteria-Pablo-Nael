# TP Django — Gestion de la cafétéria

<p align="center">
  <img src="https://img.shields.io/badge/Django-MVT-0C4B33?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
  <img src="https://img.shields.io/badge/Projet-Binôme-informational?style=for-the-badge" alt="Binôme">
</p>

<p align="center">
  <strong>Compte rendu de projet</strong><br>
  <em>Application web de gestion d’une cafétéria scolaire avec Django</em>
</p>

---

## Binôme

- **Étudiant 1** : **Naël**
- **Étudiant 2** : **Pablo**

---

## Sommaire

- [1. Contexte du projet](#1-contexte-du-projet)
- [3. Organisation du travail en binôme](#3-organisation-du-travail-en-binôme)
- [4. Choix techniques globaux](#4-choix-techniques-globaux)
- [5. Mise en place de l’environnement](#5-mise-en-place-de-lenvironnement)
- [6. Versionnement et GitHub](#6-versionnement-et-github)
- [7. Architecture du projet Django](#7-architecture-du-projet-django)
- [9. Modélisation avec Django](#9-modélisation-avec-django)
- [10. Interface d’administration](#10-interface-dadministration)
- [11. Architecture MVT](#11-architecture-mvt)
- [12. Gestion des vues et des URLs](#12-gestion-des-vues-et-des-urls)
- [13. Templates et intégration des données](#13-templates-et-intégration-des-données)
- [14. CRUD et gestion des formulaires](#14-crud-et-gestion-des-formulaires)
- [16. Mise en forme et choix visuels](#16-mise-en-forme-et-choix-visuels)
- [17. Gestion des fichiers statiques](#17-gestion-des-fichiers-statiques)
- [18. Authentification et plugins Django](#18-authentification-et-plugins-django)
- [19. Réseau : IP, LAN, localhost](#19-réseau--ip-lan-localhost)
- [20. Difficultés rencontrées](#20-difficultés-rencontrées)
- [22. Conclusion](#22-conclusion)

---

## 1. Contexte du projet

### 1.1 Présentation générale
***

### 1.2 Problématique
***

### 1.3 Besoin auquel répond l’application
***

---

## 2. Objectifs pédagogiques

### 2.1 Compétences techniques visées
***

### 2.2 Objectifs liés à Django
***

### 2.3 Objectifs liés au travail de développement
***

---

## 3. Organisation du travail en binôme

### 3.1 Répartition des tâches
***

### 3.2 Méthode de travail avec Pablo
***

### 3.3 Coordination et communication
***

### 3.4 Pourquoi nous avons choisi cette organisation
***

---

## 4. Choix techniques globaux

### 4.1 Pourquoi nous avons choisi Django
***

### 4.2 Pourquoi nous avons utilisé Bootstrap
***

### 4.3 Pourquoi nous avons conservé une structure simple et claire
***

### 4.4 Pourquoi nous avons privilégié des solutions natives de Django
***

---

## 5. Mise en place de l’environnement

### 5.1 Création du repository
***

### 5.2 Environnement virtuel Python
***

### 5.3 Installation de Django
***

### 5.4 Initialisation du projet
***

### 5.5 Pourquoi nous avons isolé l’environnement avec `venv`
***

### 5.6 Pourquoi cette étape était importante dès le départ
***

---

## 6. Versionnement et GitHub

### 6.1 Création du dépôt GitHub
***

### 6.2 Utilisation de Git au fil du projet
***

### 6.3 Sauvegardes régulières
***

### 6.4 Travail sur plusieurs machines
***

### 6.5 Utilisation de SSH
***

### 6.6 Pourquoi nous avons versionné de cette manière
***

---

## 7. Architecture du projet Django

### 7.1 Arborescence générale
***

### 7.2 Rôle du dossier principal du projet
***

### 7.3 Rôle de l’application Django
***

### 7.4 Pourquoi nous avons séparé le projet et l’application
***

### 7.5 Structure des fichiers retenue
***

```bash
cafeteria-django/
├── cafeteria/
├── cafeteria_app/
├── static/
├── templates/
├── manage.py
├── README.md
└── .gitignore
```
## 8. Modélisation avec Django

### 8.1 Traduction du diagramme en modèles Django

***

### 8.2 Modèle `Student`

***

### 8.3 Modèle `Product`

***

### 8.4 Modèle `Transaction`

***

### 8.5 Pourquoi nous avons choisi ces champs

***

### 8.6 Pourquoi nous avons ajouté certaines contraintes ou valeurs par défaut

***

### 8.7 Extrait de `models.py`

***

~~~python
from django.db import models

class Student(models.Model):
    pass

class Product(models.Model):
    pass

class Transaction(models.Model):
    pass
~~~

---

## 9. Interface d’administration

### 9.1 Mise en place de l’admin Django

***

### 9.2 Enregistrement des modèles

***

### 9.3 Utilité de l’interface admin dans notre projet

***

### 9.4 Pourquoi nous avons utilisé l’admin pour les premiers tests

***

~~~python
from django.contrib import admin
from .models import Student, Product, Transaction

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Transaction)
~~~

---

## 10. Architecture MVT

### 10.1 Compréhension du pattern MVT

***

### 10.2 Rôle du Model

***

### 10.3 Rôle de la View

***

### 10.4 Rôle du Template

***

### 10.5 Pourquoi cette architecture nous a aidés à mieux organiser le projet

***

---

## 11. Gestion des vues et des URLs

### 11.1 Première vue réalisée

***

### 11.2 Liste des produits disponibles

***

### 11.3 Configuration des routes

***

### 11.4 Pourquoi nous avons choisi cette logique de navigation

***

### 11.5 Pourquoi nous avons nommé les URLs de cette manière

***

~~~pyhon
from django.urls import path
from cafeteria_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
]
~~~

---

## 12. Templates et intégration des données

### 12.1 Principe des templates Django

***

### 12.2 Passage des données depuis la view

***

### 12.3 Affichage dynamique avec les balises Django

***

### 12.4 Utilisation des boucles, conditions et variables

***

### 12.5 Pourquoi nous avons utilisé un template de base `base.html`

***

### 12.6 Pourquoi cette structure rend le projet plus maintenable

***

~~~html
{% extends 'base.html' %}

{% block content %}
***
{% endblock %}
~~~

---

## 13. CRUD et gestion des formulaires

### 13.1 Mise en place des opérations CRUD

***

### 13.2 Ajout d’un étudiant

***

### 13.3 Modification d’un étudiant

***

### 13.4 Suppression d’un étudiant

***

### 13.5 Gestion des produits et transactions

***

### 13.6 Utilisation de `ModelForm`

***

### 13.7 Pourquoi nous avons utilisé `ModelForm` plutôt qu’un formulaire HTML manuel

***

### 13.8 Exemple de structure

***

~~~python
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'credit']
~~~

---

## 14. Mise en forme et choix visuels

### 14.1 Choix du style général

***

### 14.2 Intégration de Bootstrap

***

### 14.3 Organisation de l’interface

***

### 14.4 Lisibilité et expérience utilisateur

***

### 14.5 Responsive design

***

### 14.6 Pourquoi nous avons fait cette mise en forme

***

### 14.7 Pourquoi nous avons privilégié la clarté plutôt que la complexité visuelle

***

---

## 15. Gestion des fichiers statiques

### 15.1 Organisation des fichiers CSS, JS et images

***

### 15.2 Utilisation du dossier `static/`

***

### 15.3 Ajout éventuel d’images et d’un logo

***

### 15.4 Pourquoi nous avons séparé les fichiers statiques du reste du projet

***

### 15.5 Pourquoi cette organisation est importante en développement et en production

***

~~~html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/script.js' %}"></script>
~~~

---

## 16. Authentification et plugins Django

### 16.1 Système d’authentification Django

***

### 16.2 Protection des vues

***

### 16.3 Intégration possible du CAS ENSEA

***

### 16.4 Plugin `django-cas-ng`

***

### 16.5 Plugin `django-import-export`

***

### 16.6 Pourquoi ces plugins sont pertinents dans le cadre du projet

***

### 16.7 Pourquoi nous avons choisi de rester cohérents avec les consignes du TP

***

---

## 17. Réseau : IP, LAN, localhost

### 17.1 Compréhension de `localhost`

***

### 17.2 Adresse `127.0.0.1`

***

### 17.3 Notion de LAN

***

### 17.4 Accès local vs accès réseau

***

### 17.5 Pourquoi ces notions sont importantes pour un projet web Django

***

---

## 18. Difficultés rencontrées

### 18.1 Problèmes techniques rencontrés

***

### 18.2 Difficultés de compréhension

***

### 18.3 Solutions apportées

***

### 18.4 Ce que nous aurions pu améliorer

***

---

## 19. Conclusion

### 19.1 Bilan général

***

### 19.2 Ce que ce projet nous a apporté

***

### 19.3 Perspectives d’amélioration

***

---

##  Annexes

### A. Commandes utiles

***

~~~bash
python3 -m venv venv
source venv/bin/activate
pip install django
django-admin startproject cafeteria .
python manage.py startapp cafeteria_app
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
python manage.py createsuperuser
git add .
git commit -m "..."
git push
~~~

### B. Extraits de code importants

***

### C. Captures d’écran

***

### D. Liens utiles

***
