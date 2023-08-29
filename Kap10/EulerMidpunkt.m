% Skript som implementerer Eulers midtpunktsmetode.
% Input: Startkravet y(x0)=y0 og F(x,y),
% som definerer differensiallikninga ved
% y'=F(x,y)

% Startkrav og maksimal x-verdi
x0=0;
y0=1;
xMax=2;

% Differensiallikning
F=@(x,y) 3/2*sqrt(x)*y;

% Steglengda
N=input('Gi talet på steg: ');
h=(xMax-x0)/N;

% Vektor med x-verdiar
xVektor=x0:h:xMax;

% Initerar x og y
x=x0; y=y0;

% for-løkke som implementerer Eulers metode
yVektor(1)=y0;
for indeks=1:N
  % Eulers midtpunktsmetode
  xHatt=x+h/2;
  yHatt=y+F(x,y)*h/2;
  y=y+F(xHatt,yHatt)*h;  % Oppdaterer vektor med y-verdiar
  yVektor(indeks+1)=y;
  % Oppdaterer x
  x=x+h;
end

% Plottar resultatet
plot(xVektor,yVektor,'b-','linewidth',1)
