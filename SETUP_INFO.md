# Configuration rapide de l'environnement 🚀

## Utilisation simple

1. **Configuration automatique** (recommandée) :
   ```bash
   python setup.py
   ```

2. **Activation de l'environnement** :
   - Mac/Linux : `source venv/bin/activate`
   - Windows : `venv\Scripts\activate.bat`

3. **Lancement du jeu** :
   ```bash
   python main.py
   ```

## Scripts disponibles

| Script | OS | Description |
|--------|----|-----------| 
| `setup.py` | Tous | Script universel qui détecte l'OS automatiquement |
| `setup_env.sh` | Mac/Linux | Script shell pour systèmes Unix |
| `setup_env.bat` | Windows | Script batch pour Windows |

## Que font ces scripts ?

✅ Vérifient que Python est installé  
✅ Créent un environnement virtuel `venv`  
✅ Activent l'environnement virtuel  
✅ Mettent à jour pip  
✅ Installent les dépendances depuis `requirements.txt`  

## Première utilisation

```bash
# 1. Configurer l'environnement
python setup.py

# 2. Activer l'environnement (si besoin)
source venv/bin/activate    # Mac/Linux
# ou
venv\Scripts\activate.bat   # Windows

# 3. Lancer le jeu
python main.py -p glider
```

---

💡 **Astuce** : Une fois l'environnement configuré, vous n'avez qu'à l'activer pour travailler sur le projet ! 