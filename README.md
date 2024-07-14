# Création d'une API

## Auteurs
- **LECKOMBA Jude Luther**

Dans ce projet, nous allons développer une API qui permet à l'utilisateur de soumettre un ensemble de données via un fichier CSV et de recevoir les résultats dans un fichier JSON. La maîtrise d'AWS/Azure et des frameworks comme Flask ou Django sera un avantage.

## Table des matières

1. [Objectif](#objectif)
2. [Technologies utilisées](#technologies-utilisees)
3. [Mode opératoire](#mode-operatoire)
4. [Déploiement sur AWS](#deploiement-sur-aws)
5. [Références](#references)

<a name="objectif"></a>
## Objectif

Le but de ce projet est de créer une API qui permet :

- À l'utilisateur de téléverser un fichier CSV ou Excel contenant une série de données.
- À l'API de traiter ces données et de retourner les résultats sous forme de fichier JSON.
- De déployer cette API sur AWS (ou une plateforme similaire) pour une accessibilité globale.

<a name="technologies-utilisees"></a>
## Technologies utilisées

Pour ce projet, nous utiliserons les technologies suivantes :

- **Framework :** Flask (ou Django)
- **Cloud :** AWS (ou Azure)
- **Langage :** Python
- **Base de données :** PostgreSQL

La combinaison de Flask pour le backend et AWS pour le déploiement nous permettra de créer une API robuste et scalable.

<a name="mode-operatoire"></a>
## Mode opératoire

Voici comment l'API fonctionnera :

1. L'utilisateur soumet un fichier CSV via une requête HTTP POST à l'API.
2. L'API traite les données du fichier CSV.
3. Les résultats sont générés sous forme de fichier JSON.
4. En option, les résultats peuvent également être affichés dans une application frontend comme Flask.


<a name="deploiement-sur-aws"></a>
## Déploiement sur AWS

Pour déployer l'API sur AWS, suivez les étapes suivantes :

1. Configurer un compte AWS et créer un bucket S3 pour le stockage des fichiers CSV.
2. Utiliser AWS Elastic Beanstalk pour déployer l'application Flask.
3. Configurer un API Gateway pour gérer les requêtes HTTP et déployer l'API.

<a name="exemple-dutilisation"></a>
## Exemple d'utilisation

Voici un exemple simplifié de l'utilisation de l'API :

1. Télécharger le fichier CSV contenant les données à analyser.
2. Envoyer une requête POST à l'API avec le fichier CSV.
3. Recevoir le résultat au format JSON.

L'API peut être testée localement ou après déploiement sur AWS.

<a name="references"></a>
## Références

Pour des informations supplémentaires sur Flask, AWS, et la création d'APIs :

- Documentation Flask : [Flask Documentation](https://flask.palletsprojects.com/)
- Documentation AWS : [AWS Documentation](https://docs.aws.amazon.com/)


