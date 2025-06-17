#!/usr/bin/env python3
"""
Script de test pour vérifier que tous les patterns fonctionnent
"""

from game_of_life import GameOfLife
from patterns import Patterns


def test_all_patterns():
    """Teste le chargement de tous les patterns"""
    print("🧪 Test de tous les patterns...\n")
    
    patterns = Patterns.get_all_patterns()
    descriptions = Patterns.get_pattern_descriptions()
    
    game = GameOfLife(50, 30)
    
    for pattern_name, pattern_coords in patterns.items():
        try:
            # Test de chargement du pattern
            game.load_pattern(pattern_coords, 10, 10)
            
            # Vérifier qu'il y a au moins une cellule vivante
            alive_count = sum(sum(row) for row in game.grid)
            
            description = descriptions.get(pattern_name, "Aucune description")
            status = "✅ OK" if alive_count > 0 else "⚠️  Vide"
            
            print(f"{status} {pattern_name:<15} - {alive_count:3d} cellules - {description}")
            
        except Exception as e:
            print(f"❌ {pattern_name:<15} - ERREUR: {e}")
    
    print(f"\n✅ Test terminé - {len(patterns)} patterns vérifiés")


def test_game_logic():
    """Teste la logique du jeu avec un pattern simple"""
    print("\n🧪 Test de la logique du jeu...\n")
    
    game = GameOfLife(10, 10)
    
    # Test avec le blinker (oscillateur simple)
    blinker = [(4, 3), (4, 4), (4, 5)]
    game.load_pattern(blinker)
    
    print("Génération 0:")
    for y in range(10):
        line = ""
        for x in range(10):
            line += "█" if game.grid[y][x] else "."
        print(line)
    
    # Evolution de 2 générations
    game.next_generation()
    print(f"\nGénération 1 - {game.generation}:")
    for y in range(10):
        line = ""
        for x in range(10):
            line += "█" if game.grid[y][x] else "."
        print(line)
    
    game.next_generation()
    print(f"\nGénération 2 - {game.generation}:")
    for y in range(10):
        line = ""
        for x in range(10):
            line += "█" if game.grid[y][x] else "."
        print(line)
    
    print("\n✅ Le blinker devrait être revenu à sa forme initiale (oscillateur période 2)")


if __name__ == "__main__":
    print("=== TESTS DU JEU DE LA VIE ===\n")
    test_all_patterns()
    test_game_logic()
    print("\n🎉 Tous les tests sont terminés !") 