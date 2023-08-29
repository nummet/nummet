% Skript som løyser randverdiproblemet
% a(x) y'' + b(x) y' + c(x) y = d(x) med
% y(x_0)=y_0 og y(x_f)=y_f.
% Skriptet brukar endeleg differanse-formlar for
% numeriske deriverte til å sette opp problemet
% som ei matriselikning.
% Input:
%   1) Funksjonane a(x), b(x), c(x) og d(x)
%   2) Verdiane for x_0 og x_f
%   3) Randkrava; y(x_0) og y(x_f)
%   4) Talet på delintervall, N
% Til den siste variabelen brukar vi input-funksjonen.
% Dei andre er hardkoda.

% Inputvariablar
x0=-2;
y0=2;
xF=5;
yF=-5;
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
Dvektor=d(xVektor).';

% Matriser for dei deriverte
D1Mat=zeros(N-1,N-1);
D2Mat=zeros(N-1,N-1);
for ind=2:(N-2)
  D1Mat(ind,[ind-1 ind+1])=[-1 1]/(2*h);
  D2Mat(ind,(ind-1):(ind+1))=[1 -2 1]/h^2;
end
% Derivert i venstre ende
D1Mat(1,2)=1/(2*h);
% Derivert i høgre ende
D1Mat(N-1,N-2)=-1/(2*h);
% Dobbeltderivert i venstre ende
D2Mat(1,1:2)=[-2 1]/h^2;
% Dobbeltderivert i høgre ende
D2Mat(N-1,(N-2):(N-1))=[1 -2]/h^2;

% Set opp totalmatrisa
TotMat=[Amat*D2Mat+Bmat*D1Mat+Cmat, Dvektor];
% Legg til randkrava
TotMat(1,N)=TotMat(1,N)+y0*(-a(x0+h)/h^2+b(x0+h)/(2*h));
TotMat(N-1,N)=TotMat(N-1,N)-yF*(a(xF-h)/h^2+b(xF-h)/(2*h));

% Løyser likningssystemet
aux=rref(TotMat);
yVektor=aux(:,N).';
% Tar med randpunkta
yVektor=[y0, yVektor, yF]; xVektor=[x0, xVektor, xF];

% Plottar løysinga
plot(xVektor,yVektor)
