# Créez une API sécurisée RESTful en utilisant Django REST


Projet n°10 de la formation développeur d'Application Python.

:lock: ## Introduction : 

SoftDesk, une société d'édition de logiciels de développement et de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques (issue tracking system). Cette solution s’adresse à des entreprises clientes, en B2B. 

Cahier des charges:

Une application de suivi des problèmes pour les trois plateformes (site web, applications Android et iOS).
L'application permettra essentiellement aux utilisateurs de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.
Les trois applications exploiteront les points de terminaison d'API qui serviront les données.
Principales fonctionnalités de l'application :
A voir sur la page projet.


:pushpin: ## Utilisation : Voici la liste des outils utilisées pour ce projet :

#### Outils : 

* Django Rest Framwork 
* JWT Token

### Librairies Python :

asgiref==3.6.0
Django==4.2
djangorestframework==3.14.0
djangorestframework-simplejwt==5.2.2
drf-nested-routers==0.93.4
PyJWT==2.6.0
pytz==2023.3
sqlparse==0.4.4
tzdata==2023.3


:pushpin: ## Installation du projet : 



:computer: ### Python
Vous devez avoir Python, version 3.9 minimum, installé sur votre ordinateur (si ce n'est pas le cas vous pouvez le télécharger [ici - Python](https://www.python.org/downloads/))


:mag: Ensuite téléchargez le repo version zip sur github  :


:point_right: Créez un nouveau dossier sur votre bureau avec le nom que vous souhaitez par exemple le nom du projet : SoftDesk_P10



:point_right: Dé-zippez le contenu du dossier zip dans ce nouveau dossier : SoftDesk_P10



Une fois cela fait ouvrez le terminal de commande (Invite de commande) :



:point_right: Une fois le terminal ouvert nous allons rejoindre notre bureau dans un premier temps
```
cd desktop
```
:point_right: Ensuite nous allons rejoindre notre nouveau dossier sur le bureau
```
cd SoftDesk_P10
```
:point_right: Une fois là nous allons créer notre environnement virtuel ( exemple : envVirtuel ) sur python avec cette commande
```
python -m venv envVirtuel
```
:point_right: Une fois l'environnement créé nous allons nous rendre dans le dossier de l'environnement virtuel afin de l'activer:


Pour cela il nous faut récupérer le chemin du dossier:


* Rendez-vous sur votre bureau
* Allez dans le dossier "SoftDesk_P10"
* Maj + Clic Droit sur le dossier "envVirtuel"
* Faire : "Copier en tant que chemin d'accès"



:point_right: Une fois cela fait, retournez sur le terminal copiez votre chemin d'accès en rajoutant "\Scripts\activate" à la fin :
```
C:\Users\wolf\Desktop\SoftDesk_P10\envVirtuel\Scripts\activate
```
:point_right: Si tout va bien vous devez voir apparaître un (env) à côté de votre chemin d'accès, comme ceci
```
(env) C:\Users\wolf\Desktop\SoftDesk_P10>
```
:point_right: Déplacez-vous dans le dossier source du projet qui se nomme SoftDesk, comme ceci
```
(env) C:\Users\wolf\Desktop\SoftDesk_P10> cd SoftDesk
```
:point_right: Maintenant nous allons télécharger les librairies associés au projet nécessaire, pour cela tapez
```
pip install -r requirements.txt
```


:computer: ### Tout est fin prêt, pour lancer votre projet Django  DRF sur un navigateur !



:point_right: Pour lancer le serveur tapez la commande suivante :
```
python manage.py runserver
``` 


Afin de tester les différentes fonctionalités du site, 3 comptes utilisateurs ont été créés : 

*redmoon@gmail.com
*password

*yumi@gmail.com
*lyoko

*ulrich@gmail.com
*lyoko


:mag: Il ne vous reste plus qu'à parcourir la documentation de SoftDesk afin d'essayer toutes ces points de terminaison d'API.


:point_right: Pour lancer le serveur tapez la commande suivante : [ici - Documentation Postman](https://documenter.getpostman.com/view/17892890/2s93m62hvQ)


<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>




