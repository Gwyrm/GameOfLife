# Jeu de la Vie de Conway 🎮

Une implémentation complète du célèbre Jeu de la Vie de Conway en Python avec interface en ligne de commande.

## Description

Le Jeu de la Vie est un automate cellulaire inventé par le mathématicien John Conway en 1970. Il simule l'évolution de cellules sur une grille selon des règles simples mais qui peuvent produire des comportements complexes et fascinants.

### Règles du jeu

1. **Survie** : Une cellule vivante avec 2 ou 3 voisins vivants survit à la génération suivante
2. **Naissance** : Une cellule morte avec exactement 3 voisins vivants devient vivante
3. **Mort** : Dans tous les autres cas, la cellule meurt ou reste morte

## Installation

Aucune dépendance externe n'est requise. Le projet utilise uniquement la bibliothèque standard Python.

```bash
git clone <votre-repo>
cd GameOfLife
```

## Utilisation

### Utilisation basique

```bash
# Lancer avec un pattern spécifique
python main.py -p glider

# Lancer avec sélection interactive
python main.py

# Voir tous les patterns disponibles
python main.py --list
```

### Options de ligne de commande

```bash
python main.py [OPTIONS]

Options:
  -p, --pattern PATTERN   Choix du pattern initial
  -l, --list             Liste tous les patterns disponibles
  -w, --width WIDTH      Largeur de la grille (défaut: 80)
  -H, --height HEIGHT    Hauteur de la grille (défaut: 40)
  -s, --speed SPEED      Vitesse de simulation (défaut: 0.1 secondes)
  --help-detailed        Affiche l'aide détaillée
```

### Exemples d'utilisation

```bash
# Pattern glider classique
python main.py -p glider

# Canon à gliders sur grande grille
python main.py -p gosper_gun -w 100 -H 50

# Simulation rapide avec pattern aléatoire
python main.py -p random_medium -s 0.05

# Pattern complexe avec vitesse lente
python main.py -p pulsar -s 0.3
```

## Patterns disponibles

### 📂 Oscillateurs
- **blinker** - Oscillateur simple (période 2)
- **pentadecathlon** - Oscillateur complexe (période 15)
- **pulsar** - Oscillateur en forme d'étoile (période 3)

### 📂 Natures mortes
- **block** - Bloc statique 2x2
- **beehive** - Ruche hexagonale
- **loaf** - Pain
- **boat** - Bateau
- **tub** - Cuve

### 📂 Vaisseaux spatiaux
- **glider** - Vaisseau spatial se déplaçant en diagonal
- **lwss** - Vaisseau spatial léger (Light Weight Spaceship)

### 📂 Patterns spéciaux
- **gosper_gun** - Canon à gliders de Gosper
- **diehard** - Pattern qui meurt après 130 générations
- **acorn** - Pattern qui évolue pendant très longtemps

### 📂 Patterns aléatoires
- **random_small** - Pattern aléatoire petit (10x10)
- **random_medium** - Pattern aléatoire moyen (20x20)
- **random_large** - Pattern aléatoire grand (30x30)

## Structure du projet

```
GameOfLife/
├── main.py           # Interface principale avec arguments CLI
├── game_of_life.py   # Moteur du jeu et logique principale
├── patterns.py       # Collection de patterns prédéfinis
├── requirements.txt  # Dépendances (aucune pour ce projet)
└── README.md         # Cette documentation
```

## Fonctionnalités

- ✅ Simulation complète du Jeu de la Vie de Conway
- ✅ 16 patterns prédéfinis incluant les classiques
- ✅ Interface en ligne de commande intuitive
- ✅ Grille configurable (10x10 à 200x100)
- ✅ Vitesse de simulation ajustable
- ✅ Sélection interactive des patterns
- ✅ Affichage en temps réel dans le terminal
- ✅ Patterns aléatoires générés dynamiquement
- ✅ Centrage automatique des patterns

## Contrôles

- **Ctrl+C** : Arrêter la simulation
- **q** : Quitter lors de la sélection interactive

## Développement

Le code est structuré de manière modulaire :

- `GameOfLife` : Classe principale gérant la grille et l'évolution
- `Patterns` : Collection statique de tous les patterns
- `main()` : Interface CLI avec argparse

### Ajouter un nouveau pattern

Pour ajouter un nouveau pattern, modifiez le fichier `patterns.py` :

```python
@staticmethod
def mon_pattern() -> List[Tuple[int, int]]:
    """Description de mon pattern"""
    return [(0, 1), (1, 1), (2, 1)]  # Coordonnées des cellules vivantes
```

Puis ajoutez-le dans `get_all_patterns()` et `get_pattern_descriptions()`.

## Exemples de patterns intéressants

- **Glider** : Le pattern mobile le plus simple
- **Gosper Gun** : Premier pattern découvert qui génère des gliders à l'infini
- **Pentadecathlon** : Oscillateur avec une période de 15 générations
- **Diehard** : Pattern qui "meurt" après exactement 130 générations

## Licence

Ce projet est libre d'utilisation pour l'éducation et la recherche.

---

*Amusez-vous bien avec le Jeu de la Vie ! 🌟*
