% Skript som løyser likninga 
% \int_(mu-b)^(mu+b) f(x) dx = 1/2
% ved hjelp av Newtons metode. f(x) er ein Gauss-funksjon
% med middelverdi mu og standardavvik sigma.
% I tillegg har skriptet inputparametrane N og b0, der N
% er talet på punkt brukt i eit trapesestimat av
% integralet over, og b0 er startgjettinga for b.
% Skriptet brukar funksjonsfila IntGauss.m til å estimere
% integralet.

% Input-parametrar
mu=4;
sigma=2;
N=input('Talet på punkt i trapesintegrasjon: ');
b0=1;

% Fikserer presisjonen
Pres=1e-5;

% Set meir eller mindre tilfeldig verdi for bGml
bGml=10;
b=b0;

% Gauss-funksjonen
GaussFunk=@(x) 1/sigma/sqrt(2*pi).*exp(-(x-mu).^2/2/sigma^2);

% Itererer til vi får den presisjonen vi vil ha
while abs(b-bGml)>Pres
  bGml=b;
  G=IntGauss(mu,sigma,b,N);
  Nemnar=2*GaussFunk(mu+b);
  b=b-G/Nemnar;
end

% Skriv svaret til skjerm
b
