#!/usr/bin/env python3
"""
Jeu de la Vie de Conway - Moteur principal
"""

import time
import os
import sys
from typing import List, Tuple, Set


class GameOfLife:
    """Classe principale pour le jeu de la vie de Conway"""
    
    def __init__(self, width: int = 50, height: int = 30):
        """
        Initialise le jeu avec une grille de taille donnée
        
        Args:
            width: largeur de la grille
            height: hauteur de la grille
        """
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]
        self.generation = 0
    
    def clear_grid(self):
        """Vide la grille"""
        self.grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.generation = 0
    
    def set_cell(self, x: int, y: int, alive: bool = True):
        """
        Définit l'état d'une cellule
        
        Args:
            x: position x (colonne)
            y: position y (ligne)
            alive: état de la cellule (True = vivante, False = morte)
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = alive
    
    def get_cell(self, x: int, y: int) -> bool:
        """
        Récupère l'état d'une cellule
        
        Args:
            x: position x (colonne)
            y: position y (ligne)
            
        Returns:
            État de la cellule (True = vivante, False = morte)
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return False
    
    def count_neighbors(self, x: int, y: int) -> int:
        """
        Compte les voisins vivants d'une cellule
        
        Args:
            x: position x (colonne)
            y: position y (ligne)
            
        Returns:
            Nombre de voisins vivants
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if self.get_cell(nx, ny):
                    count += 1
        return count
    
    def next_generation(self):
        """Calcule la génération suivante selon les règles du jeu de la vie"""
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current_cell = self.grid[y][x]
                
                # Règles du jeu de la vie
                if current_cell:  # Cellule vivante
                    if neighbors == 2 or neighbors == 3:
                        new_grid[y][x] = True  # Survit
                    # Sinon meurt (sous-population ou surpopulation)
                else:  # Cellule morte
                    if neighbors == 3:
                        new_grid[y][x] = True  # Naît
        
        self.grid = new_grid
        self.generation += 1
    
    def display(self):
        """Affiche la grille dans le terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
        print(f"=== Jeu de la Vie - Génération {self.generation} ===")
        print("+" + "-" * self.width + "+")
        
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                line += "█" if self.grid[y][x] else " "
            line += "|"
            print(line)
        
        print("+" + "-" * self.width + "+")
        print("Appuyez sur Ctrl+C pour arrêter")
    
    def load_pattern(self, pattern: List[Tuple[int, int]], offset_x: int = 0, offset_y: int = 0):
        """
        Charge un pattern dans la grille
        
        Args:
            pattern: Liste de coordonnées (x, y) des cellules vivantes
            offset_x: décalage horizontal
            offset_y: décalage vertical
        """
        self.clear_grid()
        for x, y in pattern:
            self.set_cell(x + offset_x, y + offset_y, True)
    
    def run(self, delay: float = 0.1):
        """
        Lance la simulation
        
        Args:
            delay: délai entre les générations en secondes
        """
        try:
            while True:
                self.display()
                time.sleep(delay)
                self.next_generation()
        except KeyboardInterrupt:
            print("\nSimulation arrêtée.")
            sys.exit(0) 