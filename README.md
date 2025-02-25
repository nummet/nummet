# Praktisk introduksjon til numeriske metodar
Kodebase for Praktisk introduksjon til numeriske metodar.

Her vil du finne all kode som har blitt utvikla i samband med læreboka _Praktisk introduksjon til numeriske metodar: Øvingsoppgåver til Python_.
Python-kode er gitt i mapper svarande til dei ulike kapittel i boka - med kjeldekode gitt både som ei samla notebook og som separate skript. Vi har også tatt med MATLAB/Octave-kode i notebook-format i eigne mapper innanfor kvart kapittel.

## Installering av conda, Jupyter Lab, Python og ting dei er avhengige av
(Sjå også Jupyter notebook Installasjon.ipynb.)

Gå til https://docs.conda.io/projects/conda/en/latest/user-guide/install, velg rett operativsystem og installer miniconda.

Køyr følgande kommandoar for å oppdatere conda og installere nødvendige avhengigheiter:
```
conda update -n base -c conda-forge conda 
conda create -n nummet -c conda-forge jupyterlab python matplotlib numpy sympy
```

Hvis du har MATLAB installert og ønsker å kunne køyre notebooks med MATLAB/Octave-kode i tillegg til dei med Python-kode, må du også installere ei MATLAB-kjerne for Jupyter:
```
conda activate nummet
python -m pip install jupyter-matlab-proxy
```
Du kan også finne MATLAB-kode som separate skript i dette repoet:
[https://github.com/Soelve/PraktiskIntroTilNumMet_MATLAB](url)

## Kodestil
Vi ønsker å følge PEP 8 – Style Guide for Python Code (https://peps.python.org/pep-0008/) og PEP 257 – Docstring Conventions (https://peps.python.org/pep-0257/).

## Linting av Python-kode
For å gjere automatisk sjekk av kode i notebooks kan du køyre følgende kommandoar:
```
conda install -c conda-forge pylint (skal kun køyrast éin gong)
cd <kapittel> 
jupyter nbconvert --to=script *.ipynb
pylint *.py
```
For reine skript droppar du linja "jupyter nbconvert --to=script *.ipynb"
