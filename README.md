# Dashboard

Tableau de bord web interactif permettant de visualiser et explorer des les courbes des signaux grâce à **D3.js**.

Ce projet transforme des séries temporelles issues de simulations industrielles en une interface graphique modulaire, interactive et fidèle aux valeurs originales.

---

## Objectifs du projet

- Transformer les sorties Dymola en courbe
- Architecture modulaire et maintenable
- Chargement dynamique des données JSON
- Navigation temporelle exacte (sans interpolation)
- Visualisation multi-signaux temps réel

---

## Structure du projet

Dashboard/
│
├── public/
│ ├── index.html
│ └── data/
│ └── ACDC_timeseries.json
│
├── src/
│ ├── app.js
│ ├── ui.js
│ └── components/
│ └── Graph.js
│
├── style.css
└── README.md

---

## Principe de fonctionnement

1. Les données sont exportées depuis **Dymola** en JSON
2. Les signaux sont automatiquement groupés par composant
3. L’interface détecte dynamiquement tous les composants électriques
4. L’utilisateur sélectionne un composant et un signal
5. Un curseur temporel permet de parcourir **exactement** les instants simulés
6. Les valeurs affichées correspondent fidèlement aux données originales

---

## Lancer l’application

Depuis la racine du projet :

```bash
cd Dashboard
python -m http.server 8000
Puis ouvrir dans le navigateur :

http://localhost:8000/public/index.html
Interface utilisateur:
Élément	                    Fonction
Sélecteur composant:	Choix du composant électrique
Sélecteur signal:	Choix du signal du composant
Curseur temporel:	Navigation dans le temps simulé
Graphique:	        Courbe D3 avec point courant

Architecture:
Fichier	            Rôle
app.js	        Chargement et orchestration
ui.js	        Logique de l’interface
Graph.js	Moteur de rendu D3
index.html	Structure HTML
style.css	Style cockpit

Garanties techniques:
Aucune interpolation
Valeurs strictement identiques aux sorties Dymola
Compatible gros volumes (80 Mo+)

Évolutions prévues:
Superposition multi-courbes
Alertes de dépassement
Vue synoptique animée
Simulation temps réel
Panneaux avioniques
```
