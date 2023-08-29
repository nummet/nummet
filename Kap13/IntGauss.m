function G=IntGauss(mu,sigma,b,N)

% Funksjon som estimerer int_(mu-b)^(mu+b) f(x) dx - 1/2
% for Gauss-funksjonen
% f(x)=1/(2*sqrt(2*pi))*exp(-(x-mu)^2/(2*sigma^2)).
% Integralet blir estimert ved trapesintegrasjon,
% inputvariabelen N gir talet på punkt brukt i estimatet.

% Gauss-funksjonen
GaussFunk=@(x) 1/sigma/sqrt(2*pi).*exp(-(x-mu).^2/2/sigma^2);

% Bestemmer steglengda
h=2*b/(N-1);
% Startverdi for x
x=mu-b;
%Endepunkt:
Int=(GaussFunk(mu-b)+GaussFunk(mu+b))/2;
% for-løkke som går over alle "indre" punkt
for ind=2:(N-1)
  x=x+h;
  Int=Int+GaussFunk(x);
end
% Gangar summen med steglengda h for å få integralet
Int=Int*h;

% Bestemmer funksjonen G
G=Int-1/2;
