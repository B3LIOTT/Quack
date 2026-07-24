# Quack

## Prerequis

### Duck Email Privacy

S'inscrire sur Duck Email Privacy [ici](https://duckduckgo.com/email/signup).

Aller sur le dashboard [ici](https://duckduckgo.com/email/settings/autofill).

Ouvrir le devtool, cliquer sur Generate Private Duck Address, et identifer la requête POST. Le token API est dans le auth header.

Ajouter le token récupéré dans le `.env` du projet.

### Dépendances

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

## Tip

Pour quacker partout :

```bash
chmod +x quack
sudo ln -s /absolute/path/to/Quack/quack /usr/local/bin/quack
```
