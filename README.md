# ☕ Cafeteria Django

<p align="center">
  <img src="https://img.shields.io/badge/Django-Application%20web-success?style=for-the-badge&logo=django" alt="Django">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap" alt="Bootstrap">
  <img src="https://img.shields.io/badge/GitHub-Versionning-black?style=for-the-badge&logo=github" alt="GitHub">
</p>

<p align="center">
  <strong>Projet de TP Django : gestion complète d’une cafétéria scolaire</strong><br>
  Gestion des étudiants, des crédits, des produits, du stock et des transactions dans une interface moderne.
</p>

---

## 📌 Présentation du projet

Dans ce TP, nous avons développé une application web Django dédiée à la **gestion d’une cafétéria d’école**.  
L’idée est simple : chaque étudiant possède un **crédit personnel** qu’il peut utiliser pour acheter des produits disponibles à la vente.

L’application permet de gérer :

- les **étudiants**
- leur **crédit**
- les **produits**
- le **stock disponible**
- les **transactions d’achat**
- une **interface claire et moderne avec Bootstrap**
- une **base de données structurée**
- un **versionnement propre avec Git et GitHub**

Ce projet nous a permis de mettre en pratique les bases essentielles du développement web avec Django, tout en respectant une architecture propre et des bonnes pratiques de développement.

---

## 🎯 Objectifs pédagogiques

Ce TP avait pour but de nous faire travailler sur plusieurs compétences importantes :

- découvrir le framework **Django**
- comprendre l’architecture **MVT** : Model / View / Template
- créer des **modèles** pour structurer les données
- afficher dynamiquement les données avec des **views** et des **templates**
- styliser l’interface avec **CSS / Bootstrap / JavaScript**
- réfléchir à la **conception de la base de données**
- utiliser **dbdiagram.io** pour modéliser les relations
- comprendre la différence entre **IP / LAN / localhost / accès réseau**
- créer un environnement Python isolé avec **venv**
- sauvegarder le projet avec **Git / GitHub**
- manipuler les opérations **CRUD**
- comprendre l’usage de **GET** et **POST**

---

# 🛠️ Stack technique

## Technologies utilisées

- **Python 3**
- **Django**
- **Bootstrap 5**
- **HTML5 / CSS3**
- **SQLite** (base de données par défaut de Django)
- **Git**
- **GitHub**
- **dbdiagram.io**

---

# 📁 Structure du projet

Voici l’organisation générale du projet :

```bash
cafeteria-django/
│
├── cafeteria/                # Configuration principale du projet Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── cafeteria_app/            # Application principale
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── product_list.html
│   │   └── ...
│   └── ...
│
├── venv/                     # Environnement virtuel (ignoré par Git)
├── manage.py
├── README.md
└── .gitignore
