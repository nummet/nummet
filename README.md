# Praktisk introduksjon til numeriske metodar
Kodebase for 2. utgave av Praktisk introduksjon til numeriske metodar.

## Installering av avhengigheter
>> conda create -n nummet -c conda-forge jupyterlab python matplotlib numpy scipy sympy

TODO: Legg til MATLAB - sjekk notebook i kapittel 6 (?)

## Linting av Python-kode
(en gang) >> conda install -c conda-forge pylint
>> cd <kapittel> 
>> jupyter nbconvert --to=script *Python.ipynb
>> pylint *Python.py


