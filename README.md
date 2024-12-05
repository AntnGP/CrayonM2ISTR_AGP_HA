# PROJET DE TP M2ISTR DE CONCEPTION ORIENTEE OBJET

Projet d'étude pour introduire au git dans le cadre de notre ensignement de Master.
Projet ayant pour but de lier un exercice de conception d'objets à une interface web au travers de Django.

Mot de passe et identifiant admin de Django :
Admin Admin


## Installer le projet :
*Installer les fichiers sources*
```
git clone https://github.com/AntnGP/CrayonM2ISTR_AGP_HA
```
*Configurer l'environnement*
```
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install django
```

*Installer Pre-commit si besoin de modifier (optionel)*
```
wget https://gitlab.laas.fr/gsaurel/teach/raw/main/.pre-commit-config.yaml
pip install pre-commit
pre-commit install
pre-commit run -a 
```
-#le precommit sera lancé de facon automatique lors d'une tentative de commit
*Pour verifier la syntaxe des fichiers*
```
pre-commit run -a
```

## Fonctionnement du Projet
Ce projet est destiné dans un premier temps à faire fonctionner sur un serveur hebergé sur la machine en local, les données d'une usine fictive.
Pour lancer ce serveur :
```

```
Pour acceder au serveur :
```

```
