% Skript som implementerer Eulers midtpunktsmetode for 
% ei differensiallikning av andre orden.
% Input: Startkravet y(x0)=y0, y'(x0)=u0 og F(x,y),
% som definerer differensiallikninga ved
% Y'=F(x,Y), der Y=[y, u]^T.
% Merk at skriptet skil mellom "Y", som er ein vektor i R^2,
% og skalaren "y".
% Skriptet tar talet på steg N som input.

% Startkrav og maksimal x-verdi
x0=0;
y0=.15;
u0=0;
xMax=50;

% Differensiallikning
F=@(x,Y) [Y(2); -5*sin(Y(1))];

% Steglengda
N=input('Gi talet på steg: ');
h=(xMax-x0)/N;

% Lagar vektorar
xVektor=x0:h:xMax;
yVektor=zeros(1,N+1);
yVektor(:,1)=y0;

% Initerar x og Y
x=x0;
Y=[y0; u0];

% for-løkke som implementerer Eulers metode
for indeks=1:N
% Eulers midtpunktsmetode
  xHatt=x+h/2;
  YHatt=Y+F(x,Y)*h/2;
  Y=Y+F(xHatt,YHatt)*h;
% Oppdaterer vektor med y-verdiar
  yVektor(indeks+1)=Y(1);
% Oppdaterer x
  x=x+h;
end



% Plottar resultatet
plot(xVektor,yVektor,'linewidth',1)
