Projet Platinum - Application de location de voitures

Description :

Bienvenue sur le projet Platinium, une application web dédiée à la gestion de la location de véhicules. Ce système repose sur une architecture en microservices, avec un backend, une interface utilisateur et une base de données. Le tout est conteneurisé et orchestré grâce à Docker.

L'objectif principal est de fournir une plateforme performante pour gérer les opérations de location de voitures.

Fonctionnalités :

Backend (API REST) :

- POST : Ajouter une voiture.
- GET : Afficher les voitures disponibles.
- POST : Réserver une voiture.

Frontend :

- Affichage des voitures disponibles.
- Ajout de nouvelles voitures via un formulaire.
- Interaction avec l’API backend pour gérer les données.

Base de données :

Stockage des informations sur les utilisateurs, les voitures, et les réservations.

Technologies utilisées :

- Backend : Flask (Python)
- Base de données : MySQL
- Frontend : HTML, CSS, JavaScript
- Conteneurisation : Docker
- Orchestration : Docker Compose

Structure des dossiers :

Voici comment est organisé la structure du projet : 

platinium/
├── backend/               # Backend Flask pour gestion des API REST
│   ├── app/
│   │   ├── __init__.py    # Initialisation du module Flask
│   │   ├── main.py        # Point d'entrée du backend
│   │   ├── models.py      # Modèles de la base de données
│   │   ├── routes.py      # Gestion des routes API
│   │   └── config.py      # Configuration de l'application Flask
│   ├── requirements.txt   # Liste des dépendances Python
│   └── Dockerfile         # Dockerfile pour conteneuriser le backend
├── database/              # Scripts et config debase de données MySQL
│   ├── init.sql           # Script SQL d'initialisation des tables
│   └── Dockerfile         # Dockerfile pour la base de données MySQL
├── frontend/              # Interface user sur HTML/CSS/JavaScript
│   ├── src/
│   │   ├── index.html     # Page principale de l'application
│   │   ├── style.css      # Feuille de styles pour le frontend
│   │   └── app.js         # Scripts pour les interactions avec l'API
│   └── Dockerfile         # Dockerfile pour conteneuriser le frontend
├── docker-compose.yml     # Orchestration de tous les services
└── README.md              # Documentation du projet

Prérequis :

- Docker
- Docker Compose
- Docker Desktop
- MySQL

Étapes pour faire fonctionner l'application (commande linux) :

1. Cloner le projet :

git clone <URL-DU-DEPOT>
cd platinium

2. Construire les images Docker :

docker-compose build

3. Lancer l'application :

docker-compose up

4. Accéder à l'application :

- Frontend : http://localhost:8080
- Backend (API) : http://localhost:5000

Endpoints de l'API :

1. Afficher toutes les voitures :

- GET /cars
- Réponse : Liste des voitures disponibles.

2. Ajouter une voiture :

- POST /cars
- Requête :

{
  "model": "Tesla Model 3",
  "price_per_day": 100.0
}

3. Réserver une voiture :

- POST /bookings
- Corps de la requête :

{
  "user_id": 1,
  "car_id": 1
}

Auteur :

Rémi Brisset
Je rend ce travail seul car je n'ai pas trouvé de camarade pour faire ce projet...