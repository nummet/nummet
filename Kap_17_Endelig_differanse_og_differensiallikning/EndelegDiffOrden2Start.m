% Skript som løyser startverdiproblemet
% a(x) y' + b(x) y = c(x), y(x_0)=y_0, y'(x_0)=yd.
% Skriptet brukar endeleg differanse-formlar for
% numeriske deriverte til å sette opp problemet
% som ei matriselikning.
% Input: 
%   1) Funksjonane a(x), b(x) og c(x)
%   2) Verdiane for x_0 og x_f, der x_f er maksimal x-verdi
%   3) Startkrava; y(x_0) og y'(x_0)
%   4) Talet på delintervall, N
% Til den siste variabelen brukar vi input-funksjonen. 
% Dei andre er hard-koda.

% Input-variable
x0=-2;
y0=2;
xF=2;
yD=-3;
% Gir oppdelinga av x-intervallet
N=input('Gi talet på delintervall: ');  

% Funksjonar
a=@(x) exp(x);
b=@(x) x;
c=@(x) -2*x.^0;
d=@(x) 2*exp(x)-x;

% Vektor med x-verdiar
h=(xF-x0)/N;
xVektor=(x0+h):h:(xF-h);

% Matriser og vektor for funksjonane;
Amat=diag(a(xVektor));
Bmat=diag(b(xVektor)); 
Cmat=diag(c(xVektor)); 
Cmat=[Cmat, zeros(N-1,1)];   % Utvidar Cmatrisa
Dvektor=d(xVektor).';

% Matriser for dei deriverte
% Brukar midpunktformelen for numerisk derivasjon
D1Mat=zeros(N-1,N);
D2Mat=zeros(N-1,N);
for ind=2:(N-2)
  D1Mat(ind,[ind-1 ind+1])=[-1 1]/(2*h);
  D2Mat(ind,(ind-1):(ind+1))=[1 -2 1]/h^2;
end
% Derivert i venstre ende
D1Mat(1,2)=1/(2*h);         
% Derivert i høgre ende
D1Mat(N-1,[N-2 N])=[-1 1]/(2*h);         
% Dobbelt-derivert i venstre ende
D2Mat(1,1:2)=[-2 1]/h^2;         
% Dobbelt-derivert i høgre ende
D2Mat(N-1,(N-2):N)=[1 -2 1]/h^2;         

% Set opp totalmatrisa
TotMat=[Amat*D2Mat+Bmat*D1Mat+Cmat, Dvektor];  
% Legg til startkravet på y(x_0)
TotMat(1,N+1)=TotMat(1,N+1)+y0*(-a(x0+h)/h^2+b(x0+h)/(2*h));
% Legg til startkravet på y'(x_0)
TotMat(N,:)=zeros(1,N+1);
TotMat(N,[1 2])=[4 -1]/(2*h);
TotMat(N,N+1)=yD+3/(2*h)*y0;

% Løyser likningssystemet
aux=rref(TotMat);           
yVektor=aux(:,N+1).';       
% Tar med utgangspunktet
yVektor=[y0, yVektor]; xVektor=[x0, xVektor, xF];

% Plottar løysinga
plot(xVektor,yVektor)