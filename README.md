# Logiciel console gestion de tournoi d'échecs

## Description
Ce projet est un logiciel console qui permet de gérer des tournois d'échecs selon le système Suisse et de gérer une base de joueurs

### Fonctionnement
Lorsqu'on crée un tournoi
On doit inscrire au minimum 8 joueurs au tournoi.
On doit terminer celui-ci avant de pouvoir en créer un nouveau.
Le tournoi sera considéré comme terminé lorsque tous les rounds seront terminés.
Un round est terminé lorsqu'on aura saisi les scores des matchs.
Toutes les données sont stockées dans des fichiers JSON.
Un pour la base de données Joueurs et un pour les tournois.


### Menu des fonctionnalités disponibles :
- gestion des joueurs
  - Consultation de la liste des joueurs
  - Inscription de joueurs
  - Modification de joueurs

- Gestion des tournois
  - Consultation de la liste des tournois
  - Création de tournois
  - Gestion du dernier tournoi créé
    - Inscription de joueurs
    - Consultation des joueurs inscrits
    - Gestion des rounds
      - Démarrage des rounds
      - Consultation des matchs
      - Saisie des scores

- Consultation des rapports
  - Consultation des joueurs enregistrés
  - Consultation des tournois enregistrés
  - Consultation du nom et les dates d'un tournoi
  - Consultation des joueurs d'un tournoi
  - Consultation de tous les matchs / Round d'un tournoi

## Installation

1. Ouvrer un terminal
2. Aller dans le dossier où vous souhaitez stocker le projet
3. Cloner le projet avec la commande : git clone https://github.com/wilodorico/python_p4_logiciel_tournoi_echecs.git

## Créer et activer l'environnement virtuel
1. Placer vous sur le projet
2. Créer l'environnement virtuel avec la commande : `python -m venv venv`
3. Activer l'environnement virtuel :
- Pour Windows : `venv\Scripts\activate`
- Pour MacOS et linux :  `source venv/bin/activate`

## Installation des packages
Une fois que vous avez activé l'environnement virtuel, installez les packages à l'aide du fichier `requirements.txt` 
Exécuter la commande : `pip install -r requirements.txt`

## Comment lancer le logiciel
1. S'assurer d'être dans le bon répertoire du projet via le terminal
2. Exécuter le logiciel `main.py` avec la commande : `python main.py`

## Comment Générer un rapport flake8
1. S'assurer d'être dans le bon répertoire du projet via le terminal
2. Exécuter la commande : `flake8`
3. Le rapport est généré dans le dossier `flake8_rapport`