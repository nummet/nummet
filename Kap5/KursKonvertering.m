% Skript som reknar ut kva eit beløp i NOK tilsvarar i
% pund, euro og svenske kroner. Dei aktuelle kursane er
% fiksert i skriptet.

% Kursar
KursEuro=9;
KursPund=12.81;
KursSVK=95.3/100;

% Les inn beølp i NOK:
NOK=input('Beløp i norske kroner: ');

% Resultat
BelopEuro=NOK/KursEuro
BelopPund=NOK/KursPund
BelopSVK=NOK/KursSVK
