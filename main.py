#!/usr/bin/env python3
"""
Jeu de la Vie de Conway - Interface principale
"""

import argparse
import sys
from typing import Optional

from game_of_life import GameOfLife
from patterns import Patterns


def display_help():
    """Affiche l'aide détaillée du programme"""
    print("""
=== JEU DE LA VIE DE CONWAY ===

Le Jeu de la Vie est un automate cellulaire inventé par John Conway.
Il simule l'évolution de cellules selon des règles simples :

RÈGLES :
1. Une cellule vivante avec 2 ou 3 voisins survit
2. Une cellule morte avec exactement 3 voisins naît
3. Sinon, la cellule meurt ou reste morte

UTILISATION :
  python main.py [OPTIONS]

OPTIONS :
  -p, --pattern PATTERN   Choix du pattern initial
  -l, --list             Liste tous les patterns disponibles
  -w, --width WIDTH      Largeur de la grille (défaut: 80)
  -H, --height HEIGHT    Hauteur de la grille (défaut: 40)
  -s, --speed SPEED      Vitesse de simulation (défaut: 0.1 secondes)
  --help                 Affiche cette aide

EXEMPLES :
  python main.py -p glider
  python main.py -p gosper_gun -w 100 -H 50
  python main.py -p random_medium -s 0.05
  
CONTRÔLES :
  Ctrl+C : Arrêter la simulation
    """)


def list_patterns():
    """Affiche la liste des patterns disponibles"""
    patterns = Patterns.get_all_patterns()
    descriptions = Patterns.get_pattern_descriptions()
    
    print("\n=== PATTERNS DISPONIBLES ===\n")
    
    categories = {
        "Oscillateurs": ["blinker", "pentadecathlon", "pulsar"],
        "Natures mortes": ["block", "beehive", "loaf", "boat", "tub"],
        "Vaisseaux spatiaux": ["glider", "lwss"],
        "Patterns spéciaux": ["gosper_gun", "diehard", "acorn"],
        "Patterns aléatoires": ["random_small", "random_medium", "random_large"]
    }
    
    for category, pattern_list in categories.items():
        print(f"📂 {category}:")
        for pattern_name in pattern_list:
            if pattern_name in descriptions:
                print(f"   • {pattern_name:<15} - {descriptions[pattern_name]}")
        print()


def get_pattern_interactively() -> str:
    """Permet à l'utilisateur de choisir un pattern interactivement"""
    patterns = list(Patterns.get_all_patterns().keys())
    descriptions = Patterns.get_pattern_descriptions()
    
    print("\n=== SÉLECTION DE PATTERN ===\n")
    
    for i, pattern_name in enumerate(patterns, 1):
        desc = descriptions.get(pattern_name, "Aucune description")
        print(f"{i:2d}. {pattern_name:<15} - {desc}")
    
    while True:
        try:
            choice = input(f"\nChoisissez un pattern (1-{len(patterns)}) ou 'q' pour quitter: ").strip()
            
            if choice.lower() == 'q':
                print("Au revoir !")
                sys.exit(0)
            
            index = int(choice) - 1
            if 0 <= index < len(patterns):
                return patterns[index]
            else:
                print(f"Veuillez entrer un nombre entre 1 et {len(patterns)}")
                
        except ValueError:
            print("Veuillez entrer un nombre valide ou 'q' pour quitter")
        except KeyboardInterrupt:
            print("\nAu revoir !")
            sys.exit(0)


def main():
    """Fonction principale"""
    parser = argparse.ArgumentParser(
        description="Jeu de la Vie de Conway",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation:
  python main.py -p glider
  python main.py -p gosper_gun -w 100 -H 50 -s 0.05
  python main.py --list
        """
    )
    
    parser.add_argument('-p', '--pattern', 
                       help='Pattern à utiliser')
    parser.add_argument('-l', '--list', 
                       action='store_true', 
                       help='Liste tous les patterns disponibles')
    parser.add_argument('-w', '--width', 
                       type=int, 
                       default=80, 
                       help='Largeur de la grille (défaut: 80)')
    parser.add_argument('-H', '--height', 
                       type=int, 
                       default=40, 
                       help='Hauteur de la grille (défaut: 40)')
    parser.add_argument('-s', '--speed', 
                       type=float, 
                       default=0.1, 
                       help='Délai entre les générations en secondes (défaut: 0.1)')
    parser.add_argument('--help-detailed', 
                       action='store_true', 
                       help='Affiche l\'aide détaillée')
    
    # Gestion spéciale pour --help-detailed
    if '--help-detailed' in sys.argv:
        display_help()
        return
    
    args = parser.parse_args()
    
    # Afficher la liste des patterns si demandé
    if args.list:
        list_patterns()
        return
    
    # Validation des paramètres
    if args.width < 10 or args.width > 200:
        print("Erreur: La largeur doit être entre 10 et 200")
        sys.exit(1)
    
    if args.height < 10 or args.height > 100:
        print("Erreur: La hauteur doit être entre 10 et 100")
        sys.exit(1)
    
    if args.speed < 0.01 or args.speed > 5.0:
        print("Erreur: La vitesse doit être entre 0.01 et 5.0 secondes")
        sys.exit(1)
    
    # Choisir le pattern
    patterns = Patterns.get_all_patterns()
    
    if args.pattern:
        if args.pattern not in patterns:
            print(f"Erreur: Pattern '{args.pattern}' non trouvé.")
            print("Utilisez --list pour voir les patterns disponibles.")
            sys.exit(1)
        pattern_name = args.pattern
    else:
        pattern_name = get_pattern_interactively()
    
    # Initialiser le jeu
    print(f"\n🎮 Initialisation du Jeu de la Vie...")
    print(f"📐 Grille: {args.width}x{args.height}")
    print(f"🎨 Pattern: {pattern_name}")
    print(f"⚡ Vitesse: {args.speed}s par génération")
    
    game = GameOfLife(args.width, args.height)
    
    # Charger le pattern
    pattern = patterns[pattern_name]
    
    # Calculer le décalage pour centrer le pattern
    if pattern:
        max_x = max(x for x, y in pattern) if pattern else 0
        max_y = max(y for x, y in pattern) if pattern else 0
        offset_x = max(0, (args.width - max_x) // 2)
        offset_y = max(0, (args.height - max_y) // 2)
        
        game.load_pattern(pattern, offset_x, offset_y)
    
    print(f"\n🚀 Lancement de la simulation...")
    print("💡 Appuyez sur Ctrl+C pour arrêter\n")
    
    try:
        # Petite pause pour lire les informations
        import time
        time.sleep(2)
        
        # Lancer la simulation
        game.run(args.speed)
        
    except KeyboardInterrupt:
        print("\n✅ Simulation terminée. Merci d'avoir joué !")
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 