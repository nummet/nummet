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
* Bruk "precision" for utskrift av matriser og vektorer
* Konsekvent bruk av plt.show()
* Ta med import av biblioteker der det er fullstendige "skripter"
* Erstatt MATLAB-figurer (fra notebooks)
* Bruk "Bibliotek" overalt
* Skript?
* Fjern "fontsize"
* Rydde nummet-repo
  * Oppdater Installasjon.ipynb
  * Oppdater README.md
  * Synke kode mellom notebooks, skripter og bokmanus
