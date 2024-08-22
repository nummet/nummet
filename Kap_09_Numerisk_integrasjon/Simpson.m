% Implementering av Simpsons metode.
% Integrasjonsgrensene a og b, oppdelinga n og integranden
% funk blir gitt heilt i toppen av skriptet.
% For å gi oppdelinga n brukar vi input-funksjonen

% Integrasjonsgrensene
a=0;
b=1;

% Integranden
funk=@(x) cos(pi*x);

% Oppdeling (kontrollerer at n er eit partal)
n=input('Gi oppdelinga n: ');
if round(n/2) ~= n/2
    disp('n må vere eit partal')
    return
end
h=(b-a)/n;                  % Steglengda

% Bidrag frå endane
S=h/3*(funk(a)+funk(b));

% Oddetalsbidrag:
for i=1:2:(n-1);
    xi=a+i*h;
    S=S+h/3*4*funk(xi);
end

% Partalsbidrag
for i=2:2:(n-2)
    xi=a+i*h;
    S=S+h/3*2*funk(xi);
end

% Skriv svaret til skjerm
S
