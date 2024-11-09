# Praktisk introduksjon til numeriske metodar
Kodebase for Praktisk introduksjon til numeriske metodar.

## Installering av conda, Jupyter Lab, Python og avhengigheter
Gå til https://docs.conda.io/projects/conda/en/latest/user-guide/install, velg korrekt OS og installer miniconda.

Kjør følgende kommandoer for å oppdatere conda og installere nødvendige avhengigheter:
```
> conda update -n base -c conda-forge conda 
> conda create -n nummet -c conda-forge jupyterlab python matplotlib numpy sympy
```

Hvis du har MATLAB installert og ønsker å kunne kjøre notebooks med MATLAB-kode i tillegg til de med Python-kode, så må du også installere en MATLAB-kjerne for Jupyter:
> conda activate nummet
> python -m pip install jupyter-matlab-proxy

## Kodestil
Vi etterstreber å følge PEP 8 – Style Guide for Python Code (https://peps.python.org/pep-0008/) og PEP 257 – Docstring Conventions (https://peps.python.org/pep-0257/).

## Linting av Python-kode
For å gjøre automatisk sjekk av kode i notebooks kan du kjøre følgende kommandoer:
> conda install -c conda-forge pylint (kjøres kun en gang)
> cd <kapittel> 
> jupyter nbconvert --to=script *.ipynb
> pylint *.py
