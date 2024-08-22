function [M leiar]=Trappesteg(A,m)

% Funksjon som omstrukturerer første søyle i ei matrise
% slik at dette blir første steg mot å få matrisa på
% trappeform. Input er matrisa som skal rekkereduserast
% og talet på rekker i denne. Output er den 
% modifiserte matrisa og ein indeks som er 1 dersom
% søyla har leiande tal og 0 viss ikkje.
% Input:
% A - Matrisa som skal rekkereduserast
% m - talet på rekker i matrisa

% Kopierer matrisa
M=A;

% Leitar etter eit tal ulik null i søyle 1
indeks=1;
while indeks<=m & abs(A(indeks,1))<1e-14
  indeks=indeks+1;
end

% Viss det er ei rein nullsøyle
if indeks==m+1
 leiar=0;        % Set at søyla ikkje har leiande tal
 return          % Går ut av funksjonsfila
end

% Set at søyla har eit leiande tal
leiar=1;

% Sørger for å ha tal ulik null oppe til venstre
if indeks>1
  M=ByteRekker(M,1,indeks);
end

% Gjer alle tala under det leiande talet til null
m11=M(1,1);
for indeks=2:m
  % Finn talet vi skal gonge med
  k=-M(indeks,1)/m11;
  % Legg til slik at vi får null
  M=LeggeTilMult(M,k,1,indeks);
end
