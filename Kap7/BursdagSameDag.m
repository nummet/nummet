% Skript som reknar ut kor mange elevar det må vere i ein
% skuleklasse for at der mest sannsynleg vil vere minst to
% elevar med bursdag på same dag.
%
% P er sannsynet for at alle elevane har bursdagar
% på ulike datoar
% n er talet på elevar

% Initierer P og n
P=1;
n=0;

while P>1/2
  n=n+1;                   % Aukar elevtalet
  P=P*(365-n+1)/365;       % Oppdaterer sannsyn
end

% Skriv resultatet til skjerm
elevar=n
