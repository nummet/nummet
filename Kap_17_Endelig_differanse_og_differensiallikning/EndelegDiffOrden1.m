% Skript som løyser startverdiproblemet
% a(x) y' + b(x) y = c(x), y(x_0)=y_0.
% Skriptet brukar endeleg differanse-formlar for
% numeriske deriverte til å sette opp problemet
% som ei matriselikning.
% Input:
%   1) Funksjonane a(x), b(x) og c(x)
%   2) Startkravet, x0 og y0
%   3) Maksimalverdi for x, xF
%   4) Talet på delintervall, N
% Til den siste variabelen brukar vi input-funksjonen.
% Dei andre er hardkoda.

% Inputvariablar
x0=0;
y0=0;
xF=10;
% Gir oppdelinga av x-intervallet
N=input('Gi talet på delintervall: ');

% Funksjonar
a=@(x) log(x+1);
b=@(x) exp(-x);
c=@(x) sin(x.^2/5);

% Vektor med x-verdiar
h=(xF-x0)/N;
xVektor=(x0+h):h:xF;

% Matriser og vektor for funksjonane;
Amat=diag(a(xVektor));
Bmat=diag(b(xVektor));
Cvektor=c(xVektor).';

% Matrise for den deriverte
% Brukar midtpunktsformelen for numerisk derivasjon
D1Mat=zeros(N,N);
for ind=2:(N-1)
  D1Mat(ind,[ind-1 ind+1])=[-1 1]/(2*h);
end
% Derivert i venstre ende
D1Mat(1,2)=1/(2*h);
% Derivert i høgre ende
D1Mat(N,(N-2):N)=[1 -4 3]/(2*h);

% Set opp totalmatrisa
TotMat=[Amat*D1Mat+Bmat, Cvektor];
% Legg til startkravet
TotMat(1,N+1)=TotMat(1,N+1)+a(x0+h)*y0/(2*h);

% Løyser likningssystemet
aux=rref(TotMat);
yVektor=aux(:,N+1).';
% Tar med utgangspunktet
yVektor=[y0, yVektor]; xVektor=[x0, xVektor];

% Plottar løysinga
plot(xVektor,yVektor)
