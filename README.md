# Differential Fault Analysis Attack sur le chiffrement DES

[![SchoolProject](https://img.shields.io/badge/School-project-83BD75?labelColor=B4E197&style=for-the-badge)]()
[![forthebadge made-with-python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

Ce projet vise à expliquer et mettre en pratique une méthodologie d'**attaque par injections de fautes** sur le **chiffrement DES**.

## Scénario d'attaque

On suppose qu'on a obtenu, par injection de fautes sur une carte à puce, 32 chiffrés fautés. On dispose en outre du message en clair et du chiffré correct de ce message (voir *utils.py*). L'objectif de l'attaquant est alors de récupérer la clé secrète utilisée par la carte.

Je décris la méthodologie de l'attaque dans le fichier *DFA_ON_DES.pdf*.

## Utilisation du script

Les valeurs des chiffrés fautés, du message en clair et du chiffré correct sont à fournir au début du fichier *utils.py*. Des valeurs d'exemple sont déjà fournies.

```sh
$ python3 K_recovery.py
```

**Attention :** Pour fonctionner, le script nécessite une connexion Internet : il fait des appels sur une calculette DES en ligne (https://emvlab.org/descalc/) pour les parties de brute-force.