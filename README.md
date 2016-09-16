# ZipCracker -  Crack a Zip file by BruteForce.

ZipCracker est un outil en Python de crack qui utilise le bruteforce avec un dictionnaire.

### Prerequisities

* Python2.7
* zipfile
```
pip install zipfile
```

## Getting Started

```
$ python zipcracker.py

usage: zipcracker.py [-h] -f FILE -w WORD_LIST [-V]
```

Creation du fichier zip chiffré:

```
$ nano test.txt
  Voici un petit test.

$ zip --encrypt test.zip test.txt
  Enter password:
  Verify password:
     adding: test.txt (stored 0%)
$ ls
  test.txt  test.zip  zipcracker.py
```

Lancement du crack:

```
$ python zipcracker.py -f test.zip -w word_list
(2994 / 3107) |  96.00%

Password cracked: nirvana

Took 0.562439 seconds to crack the password. That is, 5325 attempts per second.
```

## Deployment

ZipCracker est compatible sur:

- Linux

## Authors

* **AneoPsy** - *Initial work*

## Acknowledgments

* Cryptographie
* Python
