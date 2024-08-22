% Skript som finn løysingane av andregradslikninga,
% a x^2 + b x + c = 0.
% Koeffisientane a, b og c blir lest inn frå skjerm.

% Koeffisientar
a=input('Gi verdien for a: ');
b=input('Gi verdien for b: ');
c=input('Gi verdien for c: ');

% Løysingar
x1=(-b-sqrt(b^2-4*a*c))/(2*a)
x2=(-b+sqrt(b^2-4*a*c))/(2*a)