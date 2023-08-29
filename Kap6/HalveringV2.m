% Implementering av halveringsmetoden for likninga f(x)=0
% der f er kontinuerleg på [a,b] og f(a) og f(b) har ulike
% forteikn.

% Grenser
a=0;
b=pi/2;

% Gir funksjonen som skal vere null
NullFunk=@(x) sqrt(x)-cos(x);

% Funksjonsverdiar
Fa=NullFunk(a);
Fb=NullFunk(b);

% Startar for-løkke som blir køyrd 10 gonger
for i=1:10
    c=(a+b)/2;        % Midtpunktet
  Fc=NullFunk(c);     % Funksjonsverdi i midtpunktet
  if Fa*Fc<0
    b=c;              % Set ny b til c
  else
    a=c;              % Set ny a til c
  end
end

% Reknar ut nytt midtpunkt og skriv svaret til skjerm
x=(a+b)/2
