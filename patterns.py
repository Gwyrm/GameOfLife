#!/usr/bin/env python3
"""
Patterns prédéfinis pour le Jeu de la Vie
"""

from typing import List, Tuple, Dict


class Patterns:
    """Collection de patterns classiques du jeu de la vie"""
    
    @staticmethod
    def get_all_patterns() -> Dict[str, List[Tuple[int, int]]]:
        """Retourne tous les patterns disponibles"""
        return {
            "blinker": Patterns.blinker(),
            "block": Patterns.block(),
            "beehive": Patterns.beehive(),
            "loaf": Patterns.loaf(),
            "boat": Patterns.boat(),
            "tub": Patterns.tub(),
            "glider": Patterns.glider(),
            "lwss": Patterns.lwss(),
            "pentadecathlon": Patterns.pentadecathlon(),
            "pulsar": Patterns.pulsar(),
            "gosper_gun": Patterns.gosper_gun(),
            "diehard": Patterns.diehard(),
            "acorn": Patterns.acorn(),
            "random_small": Patterns.random_small(),
            "random_medium": Patterns.random_medium(),
            "random_large": Patterns.random_large()
        }
    
    @staticmethod
    def get_pattern_descriptions() -> Dict[str, str]:
        """Retourne les descriptions des patterns"""
        return {
            "blinker": "Oscillateur simple (période 2)",
            "block": "Nature morte - bloc statique",
            "beehive": "Nature morte - ruche",
            "loaf": "Nature morte - pain",
            "boat": "Nature morte - bateau",
            "tub": "Nature morte - cuve",
            "glider": "Vaisseau spatial se déplaçant en diagonal",
            "lwss": "Vaisseau spatial léger (Light Weight Spaceship)",
            "pentadecathlon": "Oscillateur complexe (période 15)",
            "pulsar": "Oscillateur en forme d'étoile (période 3)",
            "gosper_gun": "Canon à gliders de Gosper",
            "diehard": "Pattern qui meurt après 130 générations",
            "acorn": "Pattern qui évolue pendant longtemps",
            "random_small": "Pattern aléatoire petit (10x10)",
            "random_medium": "Pattern aléatoire moyen (20x20)",
            "random_large": "Pattern aléatoire grand (30x30)"
        }
    
    # Oscillateurs
    @staticmethod
    def blinker() -> List[Tuple[int, int]]:
        """Oscillateur simple - barre qui clignote"""
        return [(1, 0), (1, 1), (1, 2)]
    
    @staticmethod
    def pentadecathlon() -> List[Tuple[int, int]]:
        """Oscillateur complexe avec période 15"""
        return [
            (5, 1), (6, 1), (7, 1),
            (4, 2), (8, 2),
            (4, 3), (8, 3),
            (4, 4), (8, 4),
            (5, 5), (6, 5), (7, 5),
            (5, 7), (6, 7), (7, 7),
            (4, 8), (8, 8),
            (4, 9), (8, 9),
            (4, 10), (8, 10),
            (5, 11), (6, 11), (7, 11)
        ]
    
    @staticmethod
    def pulsar() -> List[Tuple[int, int]]:
        """Oscillateur en forme d'étoile"""
        pattern = []
        
        # Motif de base (un quart)
        base = [
            (2, 0), (3, 0), (4, 0),
            (0, 2), (5, 2),
            (0, 3), (5, 3),
            (0, 4), (5, 4),
            (2, 5), (3, 5), (4, 5)
        ]
        
        # Ajouter les 4 quarts par symétrie
        for x, y in base:
            # Quart 1 (haut-droite)
            pattern.extend([(x + 6, y + 2), (x + 6, 12 - y), 
                           (12 - x, y + 2), (12 - x, 12 - y)])
        
        return pattern
    
    # Natures mortes
    @staticmethod
    def block() -> List[Tuple[int, int]]:
        """Bloc 2x2 statique"""
        return [(0, 0), (1, 0), (0, 1), (1, 1)]
    
    @staticmethod
    def beehive() -> List[Tuple[int, int]]:
        """Ruche hexagonale"""
        return [(1, 0), (2, 0), (0, 1), (3, 1), (1, 2), (2, 2)]
    
    @staticmethod
    def loaf() -> List[Tuple[int, int]]:
        """Pain"""
        return [
            (1, 0), (2, 0),
            (0, 1), (3, 1),
            (1, 2), (3, 2),
            (2, 3)
        ]
    
    @staticmethod
    def boat() -> List[Tuple[int, int]]:
        """Bateau"""
        return [(0, 0), (1, 0), (0, 1), (2, 1), (1, 2)]
    
    @staticmethod
    def tub() -> List[Tuple[int, int]]:
        """Cuve"""
        return [(1, 0), (0, 1), (2, 1), (1, 2)]
    
    # Vaisseaux spatiaux
    @staticmethod
    def glider() -> List[Tuple[int, int]]:
        """Glider classique"""
        return [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    
    @staticmethod
    def lwss() -> List[Tuple[int, int]]:
        """Light Weight Spaceship"""
        return [
            (0, 0), (3, 0),
            (4, 1),
            (0, 2), (4, 2),
            (1, 3), (2, 3), (3, 3), (4, 3)
        ]
    
    # Patterns spéciaux
    @staticmethod
    def gosper_gun() -> List[Tuple[int, int]]:
        """Canon à gliders de Gosper"""
        return [
            # Bloc de gauche
            (0, 4), (0, 5), (1, 4), (1, 5),
            
            # Émetteur principal
            (10, 4), (10, 5), (10, 6), (11, 3), (11, 7),
            (12, 2), (12, 8), (13, 2), (13, 8),
            (14, 5), (15, 3), (15, 7), (16, 4), (16, 5), (16, 6),
            (17, 5),
            
            # Structure de droite
            (20, 2), (20, 3), (20, 4), (21, 2), (21, 3), (21, 4),
            (22, 1), (22, 5), (24, 0), (24, 1), (24, 5), (24, 6),
            
            # Bloc de droite
            (34, 2), (34, 3), (35, 2), (35, 3)
        ]
    
    @staticmethod
    def diehard() -> List[Tuple[int, int]]:
        """Pattern qui meurt après 130 générations"""
        return [
            (6, 0),
            (0, 1), (1, 1),
            (1, 2), (5, 2), (6, 2), (7, 2)
        ]
    
    @staticmethod
    def acorn() -> List[Tuple[int, int]]:
        """Pattern qui évolue très longtemps"""
        return [
            (1, 0),
            (3, 1),
            (0, 2), (1, 2), (4, 2), (5, 2), (6, 2)
        ]
    
    # Patterns aléatoires
    @staticmethod
    def random_small() -> List[Tuple[int, int]]:
        """Génère un pattern aléatoire petit"""
        import random
        pattern = []
        for x in range(10):
            for y in range(10):
                if random.random() < 0.3:  # 30% de chance d'être vivant
                    pattern.append((x, y))
        return pattern
    
    @staticmethod
    def random_medium() -> List[Tuple[int, int]]:
        """Génère un pattern aléatoire moyen"""
        import random
        pattern = []
        for x in range(20):
            for y in range(20):
                if random.random() < 0.25:  # 25% de chance d'être vivant
                    pattern.append((x, y))
        return pattern
    
    @staticmethod
    def random_large() -> List[Tuple[int, int]]:
        """Génère un pattern aléatoire grand"""
        import random
        pattern = []
        for x in range(30):
            for y in range(30):
                if random.random() < 0.2:  # 20% de chance d'être vivant
                    pattern.append((x, y))
        return pattern 