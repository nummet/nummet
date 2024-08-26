# Praktisk introduksjon til numeriske metodar
Kodebase for 2. utgave av Praktisk introduksjon til numeriske metodar.

## Installering av avhengigheter
> conda create -n nummet -c conda-forge jupyterlab python matplotlib numpy scipy sympy

Dersom du ønsker å kunne kjøre MATLAB-kode må du også installere en MATLAB-kjerne for Jupyter:
> conda activate jupyterlab
> python -m pip install jupyter-matlab-proxy

## Linting av Python-kode
> conda install -c conda-forge pylint (kjøres kun en gang)
> cd <kapittel> 
> jupyter nbconvert --to=script *Python.ipynb
> pylint *Python.py

## Kodestil
Vi etterstreber å følge PEP 8 og PEP 257.

PEP 8 – Style Guide for Python Code: https://peps.python.org/pep-0008/
PEP 257 – Docstring Conventions: https://peps.python.org/pep-0257/

## TODO
* arange -> linspace
* .2f -> .4f (eller .4e der det passer)
* "..." -> '...'
* Standardiserer på initialisering (til null) ved allokering av arrays
* Bruk """ """ i starten av skripter
* Ikke ta med "kjørekommandoer" for skripter
* Bruk "precision" for utskrift av matriser og vektorer
* Vi bruker arc* for trigonometriske funksjoner
* Konsekvent bruk av plt.show()
* Ta med import av biblioteker der det er fullstendige "skripter"
* Erstatt MATLAB-figurer (fra notebooks)
* Bruk hstack og vstack (eller append, hvis mulig), ikke c_ og r_ (Hva med concatenate().)

## 2. gjennomgang kapitler
("Les og revider" betyr at 1. gjennomgang ikke er gjort av MLS.)

* Søndag
    * ~~Les og revider 0--2~~
    * ~~Revider 3~~
* Mandag
    * ~~Les + revider 4~~
    * ~~Les + revider 5~~
    * ~~Les + revider 6~~
    * Les + revider 7
    * Les + revider 8
    * Revider 9
* Tirsdag
    * Les + revider 10
    * Revider 11
    * Les + revider 12
    * Revider 13
    * Revider 14 - separer ut gauss-funk (ikke ha den som en internfunksjon)! sigma/mu som input eller ei?
* Onsdag
    * Revider 15
    * Revider 16
    * Revider 17
    * Les og revider 18
    * Revider 19
    * Revider 20
    * Les og revider A og B
* Senere
    * Rydde nummet-repo
        * Oppdater Installasjon.ipynb
        * Oppdater README.md
        * Synke kode mellom notebooks, skripter og bokmanus
