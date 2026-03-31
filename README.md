<p align="center">
<h1>TP Django — Gestion de la cafétéria</h1>
</p>

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

## Sommaire

- [1. Contexte du projet](#1-contexte-du-projet)
- [2. Choix techniques globaux](#2-choix-techniques-globaux)
- [3. Mise en place du projet](#3-mise-en-place-du-projet)
- [4. Versionnement et GitHub](#4-versionnement-et-github)
- [5. Architecture du projet Django](#5-architecture-du-projet-django)
- [6. Modélisation avec Django](#6-modélisation-avec-django)
- [7. Interface d’administration](#7-interface-dadministration)
- [8. Architecture MVT](#8-architecture-mvt)
- [9. Gestion des vues et des URLs](#9-gestion-des-vues-et-des-urls)
- [10. Templates et intégration des données](#10-templates-et-intégration-des-données)
- [11. CRUD et gestion des formulaires](#11-crud-et-gestion-des-formulaires)
- [12. Mise en forme et choix visuels](#12-mise-en-forme-et-choix-visuels)
- [13. Gestion des fichiers statiques](#13-gestion-des-fichiers-statiques)
- [14. Authentification et plugins Django](#14-authentification-et-plugins-django)
- [15. Réseau : IP, LAN, localhost](#15-réseau--ip-lan-localhost)
- [16. Difficultés rencontrées](#16-difficultés-rencontrées)
- [17. Conclusion](#17-conclusion)

---

## 1. Contexte du projet

### 1.1 Présentation générale

***

### 1.2 Problématique

***

### 1.3 Besoin auquel répond l’application

***

---

## 2. Choix techniques globaux

### 2.1 Choix de Django comme framework principal

***

### 2.2 Choix de Bootstrap pour l’interface

***

### 2.3 Pourquoi nous avons conservé une structure simple et claire

***

### 2.4 Pourquoi nous avons privilégié des solutions natives de Django

***

---

## 3. Mise en place du projet

### 3.1 Création du repository

***

### 3.2 Initialisation du projet Django

***

### 3.3 Création de l’application principale

***

### 3.4 Premiers tests de lancement

***

### 3.5 Choix faits dès le démarrage du projet

***

---

## 4. Versionnement et GitHub

### 4.1 Création du dépôt GitHub

***

### 4.2 Utilisation de Git au fil du projet

***

### 4.3 Sauvegardes régulières

***

### 4.4 Travail sur plusieurs machines

***

### 4.5 Utilisation de SSH

***

### 4.6 Pourquoi nous avons versionné de cette manière

***

---

## 5. Architecture du projet Django

### 5.1 Arborescence générale

***

### 5.2 Rôle du dossier principal du projet

***

### 5.3 Rôle de l’application Django

***

### 5.4 Pourquoi nous avons séparé le projet et l’application

***

### 5.5 Structure des fichiers retenue

***

~~~bash
cafeteria-django/
├── cafeteria/
├── cafeteria_app/
├── static/
├── templates/
├── manage.py
├── README.md
└── .gitignore
~~~

---

## 6. Modélisation avec Django

### 6.1 Traduction du diagramme en modèles Django

***

### 6.2 Modèle `Student`

***

### 6.3 Modèle `Product`

***

### 6.4 Modèle `Transaction`

***

### 6.5 Pourquoi nous avons choisi ces champs

***

### 6.6 Pourquoi nous avons ajouté certaines contraintes ou valeurs par défaut

***

### 6.7 Extrait de `models.py`

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

## 7. Interface d’administration

### 7.1 Mise en place de l’admin Django

***

### 7.2 Enregistrement des modèles

***

### 7.3 Utilité de l’interface admin dans notre projet

***

### 7.4 Pourquoi nous avons utilisé l’admin pour les premiers tests

***

~~~python
from django.contrib import admin
from .models import Student, Product, Transaction

admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Transaction)
~~~

---

## 8. Architecture MVT

### 8.1 Compréhension du pattern MVT

***

### 8.2 Rôle du Model

***

### 8.3 Rôle de la View

***

### 8.4 Rôle du Template

***

### 8.5 Pourquoi cette architecture nous a aidés à mieux organiser le projet

***

---

## 9. Gestion des vues et des URLs

### 9.1 Première vue réalisée

***

### 9.2 Liste des produits disponibles

***

### 9.3 Configuration des routes

***

### 9.4 Pourquoi nous avons choisi cette logique de navigation

***

### 9.5 Pourquoi nous avons nommé les URLs de cette manière

***

~~~python
from django.urls import path
from cafeteria_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
]
~~~

---

## 10. Templates et intégration des données

### 10.1 Principe des templates Django

***

### 10.2 Passage des données depuis la view

***

### 10.3 Affichage dynamique avec les balises Django

***

### 10.4 Utilisation des boucles, conditions et variables

***

### 10.5 Pourquoi nous avons utilisé un template de base `base.html`

***

### 10.6 Pourquoi cette structure rend le projet plus maintenable

***

~~~html
{% extends 'base.html' %}

{% block content %}
***
{% endblock %}
~~~

---

## 11. CRUD et gestion des formulaires

### 11.1 Mise en place des opérations CRUD

***

### 11.2 Ajout d’un étudiant

***

### 11.3 Modification d’un étudiant

***

### 11.4 Suppression d’un étudiant

***

### 11.5 Gestion des produits et transactions

***

### 11.6 Utilisation de `ModelForm`

***

### 11.7 Pourquoi nous avons utilisé `ModelForm` plutôt qu’un formulaire HTML manuel

***

### 11.8 Exemple de structure

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

## 12. Mise en forme et choix visuels

### 12.1 Choix du style général

***

### 12.2 Intégration de Bootstrap

***

### 12.3 Organisation de l’interface

***

### 12.4 Lisibilité et expérience utilisateur

***

### 12.5 Responsive design

***

### 12.6 Pourquoi nous avons fait cette mise en forme

***

### 12.7 Pourquoi nous avons privilégié la clarté plutôt que la complexité visuelle

***

---

## 13. Gestion des fichiers statiques

### 13.1 Organisation des fichiers CSS, JS et images

***

### 13.2 Utilisation du dossier `static/`

***

### 13.3 Ajout éventuel d’images et d’un logo

***

### 13.4 Pourquoi nous avons séparé les fichiers statiques du reste du projet

***

### 13.5 Comment cette organisation facilite la maintenance du projet

***

~~~html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<script src="{% static 'js/script.js' %}"></script>
~~~

---

## 14. Authentification et plugins Django

### 14.1 Système d’authentification Django

***

### 14.2 Protection des vues

***

### 14.3 Intégration possible du CAS ENSEA

***

### 14.4 Plugin `django-cas-ng`

***

### 14.5 Plugin `django-import-export`

***

### 14.6 Intérêt de ces plugins dans le cadre du projet

***

### 14.7 Ce que nous avons choisi d’intégrer ou non, et pourquoi

***

---

## 15. Réseau : IP, LAN, localhost

### 15.1 Compréhension de `localhost`

***

### 15.2 Adresse `127.0.0.1`

***

### 15.3 Notion de LAN

***

### 15.4 Accès local vs accès réseau

***

### 15.5 En quoi ces notions nous ont aidés à mieux comprendre le fonctionnement du projet

***

---

## 16. Difficultés rencontrées

### 16.1 Problèmes techniques rencontrés

***

### 16.2 Difficultés de compréhension

***

### 16.3 Solutions apportées

***

### 16.4 Ce que nous aurions pu améliorer

***

---

## 17. Conclusion

### 17.1 Bilan général

***

### 17.2 Ce que ce projet nous a apporté

***

### 17.3 Perspectives d’amélioration

***

---

## Annexes

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
