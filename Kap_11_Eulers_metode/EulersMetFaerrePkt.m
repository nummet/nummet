% Skript som implementerer Eulers metode.
% Input: Startkravet y(x0)=y0 og F(x,y),
% som definerer differensiallikninga ved
% y'=F(x,y).
% Skriptet brukar færre punkt til plotting 
% enn dei som blir rekna ut med Eulers metode.


% Startkrav og maksimal x-verdi
x0=0;
y0=1;
xMax=2;

% Differensiallikning
F=@(x,y) 3/2*sqrt(x)*y;

% Steglengda
N=input('Gi talet på steg: ');
h=(xMax-x0)/N;

% Initerar x og y
x=x0; y=y0;

% for-løkke som implementerer Eulers metode
xVektor(1)=x0;
yVektor(1)=y0;
indeks=1;
for n=1:N
  % Eulers framovermetode
  y=y+F(x,y)*h;
  if mod(n,10)==0
    % Oppdaterer vektor med x- og y-verdiar
    xVektor(indeks)=x;
    yVektor(indeks)=y;
    indeks=indeks+1;
  end
  % Oppdaterer x
  x=x+h;
end

% Plottar resultatet
plot(xVektor,yVektor,'b-','linewidth',1)
