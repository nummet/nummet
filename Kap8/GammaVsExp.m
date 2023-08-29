% Skript som bestemmer skjæringspunktet mellom
% eksponentialfunksjonen og gammafunksjonen.
% Til det brukar vi Newtons metode og numerisk derivasjon.
% Skriptet plottar konvergensen av svaret mot h-verdien
% som blir brukt i derivasjonen.

% Gir presisjon og h-verdiane
Pres=1e-5;
hVektor=[2:-.1:.1];
% Startverdi
x0=8;

indeks=1;
% Bestemmer x ved Newtons metode for kvar av h-verdiane
for h=hVektor
  x=x0;
  xGml=10;
  while abs(x-xGml)>Pres
    xGml=x;
    % Den deriverte av gamma
    Derivert=(gamma(x+h)-gamma(x-h))/(2*h);
    % Iterasjonsformel (Newtons metode)
    x=x-(gamma(x)-exp(x))/(Derivert-exp(x));
  end
  Svar(indeks)=x;
  indeks=indeks+1;
end

% Plottar løysingane som funksjon av h
plot(hVektor,Svar,'kx-','linewidth',2)
