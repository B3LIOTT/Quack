# Quack

## Prerequis

```bash
pip install requests
pip install rich
```

## Utilisation

```bash
quack -h
usage: quack [-h] {new,get} ...

🦆 Quack - Gestionnaire d'alias DuckDuckGo

positional arguments:
  {new,get}   Commandes disponibles
    new       Génère un nouvel alias email
    get       Affiche les alias existants

options:
  -h, --help  show this help message and exit
```

```bash
quack get -h
usage: quack get [-h] target

positional arguments:
  target      'all' (tout), 'mails' (sans mdp), ou l'email recherché

options:
  -h, --help  show this help message and exit
```
