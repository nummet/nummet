% Enkel implementering av Eulers metode
% for startverdiproblemet y'=x+y, y(0)=1.
% Skriptet allokerar vektoren med y-verdiar.

x0=0;                           % Startkrav
y0=1;
xMax=10;

N=1e8;                          % Oppdeling
h=(xMax-x0)/N;
xVektor=x0:h:xMax;              % Vektor med x-verdiar
yVektor=zeros(1,N+1);

x=x0; y=y0;
yVektor(1)=y0;
tic                             % Startar klokka
for i=1:N
  y=y+(x+y)*h;                  % Oppdaterer y
  yVektor(i+1)=y;               % Skriv y-verdien til vektor
  x=x+h;                        % Oppdaterer x
end
toc                             % Stoppar klokka
