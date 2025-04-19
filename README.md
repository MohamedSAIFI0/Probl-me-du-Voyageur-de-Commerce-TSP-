# Visualisation de la probabilité d'acceptation du recuit simulé

## Description
Ce projet propose une visualisation interactive de la fonction de probabilité d'acceptation utilisée dans l'algorithme du recuit simulé (Simulated Annealing). Il illustre comment la température influence l'acceptation de solutions sous-optimales pendant le processus d'optimisation.

## Contexte théorique
Dans le recuit simulé, la probabilité d'accepter une solution moins bonne est calculée par la formule :

```
P = exp(-Δ/T)
```

Où :
- `Δ` (delta) est la différence de coût entre la nouvelle solution et la solution actuelle (Δ = C(S') - C(S))
- `T` est la température actuelle du système

Cette probabilité permet à l'algorithme d'échapper aux optima locaux, surtout au début du processus quand la température est élevée.

## Fonctionnalités
Le code propose deux visualisations :

1. **Visualisation statique** :
   - Affiche la courbe de probabilité d'acceptation en fonction de la température
   - Met en évidence des points spécifiques (T=5, 10, 20, 50, 100)
   - Montre la valeur exacte de la probabilité à ces points
   - Inclut une légende explicative du concept

2. **Visualisation interactive** :
   - Permet de modifier la valeur de delta (différence de coût) via un slider
   - Met à jour la courbe en temps réel pour montrer l'impact de delta
   - Facilite la compréhension intuitive du comportement de l'algorithme

## Prérequis
- Python 3.x
- NumPy
- Matplotlib

## Installation
```bash
pip install numpy matplotlib
```

## Utilisation
Exécutez simplement le script Python :
```bash
python simulated_annealing_visualization.py
```

## Interprétation des résultats
- **Haute température** (début du recuit) : Même des solutions significativement moins bonnes (grand Δ) ont une probabilité élevée d'être acceptées, permettant une large exploration de l'espace des solutions.
- **Basse température** (fin du recuit) : Seules les solutions meilleures ou légèrement moins bonnes sont acceptées, favorisant la convergence vers un optimum local prometteur.

## Application au problème du voyageur de commerce (TSP)
Cette visualisation aide à comprendre le mécanisme par lequel le recuit simulé:
1. Évite de rester piégé dans des optima locaux
2. Équilibre l'exploration et l'exploitation
3. Converge progressivement vers des solutions de qualité

Ces principes sont essentiels pour résoudre efficacement des problèmes combinatoires comme le TSP.

## Extension possible
Le code peut être facilement adapté pour visualiser d'autres aspects du recuit simulé:
- L'évolution de la température au fil des itérations
- La comparaison entre différentes stratégies de refroidissement
- L'évolution de la qualité des solutions acceptées

## Auteur
Mohamed SAIFI
