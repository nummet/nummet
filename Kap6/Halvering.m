% Implementering av halveringsmetoden for likninga
% sqrt(x)-cos(x)=0 med
% Grensene er gitt som a og b

% Grenser
a=0;
b=pi/2;

% Funksjonsverdiar
Fa=sqrt(a)-cos(a);
Fb=sqrt(b)-cos(b);

% Startar for-løkke som blir køyrd 10 gonger
for i=1:10
    c=(a+b)/2;       % Midtpunktet
  Fc=sqrt(c)-cos(c); % Funksjonsverdi i midtpunktet
  if Fa*Fc<0
    b=c;             % Set ny b til c
  else
    a=c;             % Set ny a til c
  end
end

% Reknar ut nytt midtpunkt og skriv svaret til skjerm
x=(a+b)/2
