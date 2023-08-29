% Skript som bestemmer kor lang tid det å tømme ein tank.
% Profilen til tanken er gitt ved R(x) under.
% Vi tar utgangspunkt i Torricellis lov, V'(t) = -k sqrt(h).

% Startkrav:
t0=0;
h0=60;
t=t0; h=h0;

% Parametrar
Vtot=2.0547e+04;
k=2*Vtot/(3*sqrt(h0));

% Profilfunksjon
R=@(x) 5+4./(1+exp((35-x)/1.5)).*(sqrt(x)-sqrt(30)).^2;
% Høgresida i differensiallikninga
F=@(x) -k*sqrt(x)./(pi*R(x).^2);

% Steglengde
dt=input('Steglengda i tid: ');

while h>0
  h=h+F(h)*dt;       % Eulers metode
  t=t+dt;
end

% Skriv slutttida til skjerm
t
