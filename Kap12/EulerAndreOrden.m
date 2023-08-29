% Skript som implementerer Eulers framovermetode for 
% ei differensiallikning av andre orden.
% Input: Startkravet y(x0)=y0, y'(x0)=u0 og F(x,y),
% som definerer differensiallikninga ved
% Y'=F(x,Y), der Y=[y, u]^T.
% Merk at skriptet skil mellom "Y", som er ein vektor i R^2,
% og skalaren "y".
% Skriptet tar talet på steg, N, som input.

% Startkrav og maksimal x-verdi
x0=0;
y0=2;
u0=-1;
xMax=2;

% Differensiallikning
F=@(x,Y) [Y(2); -Y(2)+2*Y(1)+2*x+1];

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
% Eulers framovermetode
  Y=Y+F(x,Y)*h;
% Oppdaterer vektor med y-verdiar
  yVektor(indeks+1)=Y(1);
% Oppdaterer x
  x=x+h;
end

% Plottar resultatet
plot(xVektor,yVektor,'b-','linewidth',1.5)
