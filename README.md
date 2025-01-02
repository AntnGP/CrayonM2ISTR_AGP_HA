# PROJET DE TP M2ISTR DE CONCEPTION ORIENTEE OBJET

Projet par Ayman et Antoine

## Niveau d'avancement
Toute partie python et serveur fonctionnel.
Partie C++ non fonctionnelle et partiellement finie.
Toutes les parties ont ete abordées mais pas mises en oeuvres complètement. La partie lowlevel et le C++ n'ont pas ete terminé, notament aucune fonction n'a ete mise en oeuvre ci ce n'est faire un simple affichage des données. Deplus, le transfert de toutes les classes entre le python et le C++ n'est pas entierment implementé non plus.

## Contexte

Projet d'étude dans le cadre de notre ensignement de Master.
Le projet pour but de lier un exercice de conception d'objets à une interface web au travers de Django afin de modelisezr une usine de crayon de facon tres simple.


## Installer le projet :
En considerant que vous ayez un systeme d'exploitation fonctionnel, avec pip, python et venv installés 
**Recuperer les fichiers sources**
```
git clone https://github.com/AntnGP/CrayonM2ISTR_AGP_HA
```
**Configurer l'environnement**
```
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install django
```

**Installer Pre-commit si besoin de modifier le projet (optionel)**
```
wget https://gitlab.laas.fr/gsaurel/teach/raw/main/.pre-commit-config.yaml
pip install pre-commit
pre-commit install
pre-commit run -a
```
le precommit sera lancé de facon automatique lors d'une tentative de commit

**Pour verifier la syntaxe des fichiers (optionel)**
```
pre-commit run -a
```

## Fonctionnement du Projet
Ce projet est destiné dans un premier temps à faire fonctionner sur un serveur hebergé sur la machine en local, les données d'une usine fictive.
**Pour lancer ce serveur :**
Aller dans le dossier ./crayon
(optionel) Si c'est la 1er fois lancé ou si un edit a ete fait sur les fichiers
(super used conseillé : Admin, mdp : Admin)
```
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
```
Lancer le serveur
Pour acceder au serveur :
```
./manage.py runserver
```


Puis acceder au lien : http://localhost:8000/admin pour voir l'interface

Pour acceder a un des elements : http://localhost:8000/ville/2 par exemple
lien au format http://localhost:8000/CLASSE/ID , avec CLASSE visibles dans low_level/lowlevel.ccp ou high_level/urls.py. Les ID sont les eneiemes instansation de chaque classe.

Pour instancier de nouvelles classes, passer par l'interface administrateur



