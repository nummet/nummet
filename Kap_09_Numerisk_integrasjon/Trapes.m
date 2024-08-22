% Implementering av trapesmetoden for numerisk integrasjon.
% Integrasjonsgrensene a og b, oppdelinga n og integranden
% funk blir gitt heilt i toppen av skriptet.
% For å gi n brukar vi input-funksjonen.

% Integrasjonsgrenser
a=-1;
b=1;

% Integranden
funk=@(x) x^6;

% Oppdeling
n=input('Gi oppdelinga n: ');
h=(b-a)/n;                  % Steglengda

% Bidrag frå endane
T=h/2*(funk(a)+funk(b));

% Resten av bidraga
for i=1:(n-1)
    xi=a+i*h;
    T=T+h*funk(xi);
end

% Skriv svaret til skjerm
T