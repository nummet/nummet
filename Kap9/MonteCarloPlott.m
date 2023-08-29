% Skript som estimerer eit integral ved Monte Carlo-metoden
% Sjølve integralet, og den analytiske løysninga av det, er
% spesifisert i starten av skriptet - i tillegg til
% det maksimale talet på trekk.

% Integrasjonsgrenser
a=-1;
b=3;

% Integrand
funk=@(x) x*sin(x^2);

% Kjent analytisk svar:
Fasit=(cos(1)-cos(9))/2;

% Maksimalt tal på trekk:
Nmax=1000;

% Initierer summen
MCsum=0;

% Lagar klart plott for estimata - saman med eksakt svar
plot([1 Nmax],Fasit*[1 1],'k--')
hold on

% Vi utfører uttrekka og legg til summen for kvar gong
for n=1:Nmax
  x=a+(b-a)*rand;
  MCsum=MCsum+funk(x);
  Estimat=(b-a)*MCsum/n;          % Integral-estimat
  plot(n,Estimat,'b.')            % Plottar estimat
end
hold off
axis([0 Nmax -1 2])

% Skriv svaret til skjerm
Estimat
