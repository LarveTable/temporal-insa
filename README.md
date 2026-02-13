
# Temporal'INSA ⏳

> Une plateforme web pour la classification et l'analyse de séries temporelles.

**Projet de 4ème année - Département Informatique - INSA Rennes**

Temporal'INSA est une suite logicielle permettant aux chercheurs et data scientists de lancer facilement des expérimentations de classification sur des jeux de données de séries temporelles (Time Series). L'objectif est de comparer les performances de différents algorithmes de l'état de l'art dans des contextes variés.

## Objectif du projet

La classification de séries temporelles est complexe en raison de la nature séquentielle des données. Ce projet vise à simplifier cette tâche en offrant une interface unifiée pour :
1.  **Configurer** des expérimentations.
2.  **Lancer** des algorithmes de classification robustes.
3.  **Visualiser** et comparer les résultats de performance.

## Fonctionnalités

* **Algorithmes supportés :** utilisation de 5 méthodes majeures :
    * Rocket
    * MiniRocket
    * ~~Learning Shapelets~~
    * Hydra
    * BOSS
* **Gestion des Datasets :** Support du format standard UCR.
* **Pré-traitement automatique :** Scaling (ex: MinMaxScaler).
* **Interface Web complète :** 
	* Création de nouvelles expériences.
    * Chargement de configurations existantes.
    * Tableau de bord des résultats (métriques de précision, etc.).
* **Extensibilité :** Architecture conçue pour ajouter facilement de nouveaux algorithmes ou datasets.

## Stack Technique

Nous avons fait le choix d'une architecture unifiée pour faciliter la maintenance et la cohérence des données.

* **Langage :** Python
* **Framework Web :** Django (Backend & Frontend unifiés)
* **Base de données :** SQL (Structure relationnelle pour la gestion des expérimentations)

## Aperçu



## Choix de conception

Initialement prévu avec une séparation Angular/Python et une base MongoDB, le projet a évolué vers une stack **Full-Django** et **SQL**.
Ce choix stratégique nous a permis de :
1.  Fiabiliser la communication entre l'interface et les algorithmes de calcul.
2.  Garantir l'intégrité des données grâce au schéma relationnel.
3.  Concentrer nos efforts sur l'utilisation unifiée et l'adaptation des algorithmes de classification plutôt que sur la complexité d'architecture.

## Auteurs

Projet réalisé en 2024-2025 par :
* **Yorick Charlery**
* **Mengxin Yuan**

**Superviseure :** Laurence Rozé (INSA Rennes)

---
*Ce projet a été développé dans le cadre du cursus ingénieur de l'INSA Rennes.*