% Skript som implementerer Newtons metode

% Bestemmer x_0
x=1;

% Presisjon
Pres=1e-5;

% Talet på iterasjonar
Iterasjonar=0;

% Lagar ein variabel for "gamal" x-verdi (tilfeldig tal)
xGml=100;

while abs(x-xGml)>Pres
  % Kopierer den gamle x
  xGml=x;
  % Iterasjonsskjema
  x=x-(sqrt(x)-cos(x))/(1/(2*sqrt(x))+sin(x));
  % Tel iterasjonar
  Iterasjonar=Iterasjonar+1;
end

% Skriv svaret til skjerm
x
% Skriv talet på iterasjonar til skjerm
Iterasjonar
