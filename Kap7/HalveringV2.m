% Implementering av halveringsmetoden for likninga f(x)=0 der 
% f er kontinuerleg på [a,b] og f(a) og f(b) har ulike forteikn.

% Grenser
a=0;
b=pi/2;

% Gir funksjonen som skal vere null
NullFunk=@(x) sqrt(x)-cos(x);

% Funksjonsverdiar
Fa=NullFunk(a);
Fb=NullFunk(b);

% Initierer variabel som tel iterasjonane
Iterasjonar=0;

% Startar for-løkke som blir køyrd 10 gonger
while b-a>1e-3
  c=(a+b)/2;          % Midtpunktet
  Fc=NullFunk(c);     % Funksjonsverdi i midtpunktet
  if Fa*Fc<0
    b=c;              % Set ny b til c
  else
    a=c;              % Set ny a til c
  end
  Iterasjonar=Iterasjonar+1;  % Tel iterasjonane
end

% Reknar ut nytt midtpunkt og skriv svaret til skjerm
x=(a+b)/2
% Skriv talet på iterasjonar til skjerm
Iterasjonar