function [M LeiarVektor]=Trappeform(A)

% Funksjon som reduserer ei matrise til ei trappeform.
% Funksjonen lagar også ein vektor med søylenummera
% til søylene med leiande tal.

% Finn formatet på matrisa
[m n]=size(A);

% Kopierer matrisa
M=A;

% Initierer vektoren med søylenummera for dei leiande tala
LeiarVektor=[];
% Set rekkenummeret til éin
rekke=1;
% Går gjennom kvar søyle i matrisa og rekkereduserer for
% kvar undermatrise
for soeyle=1:n
  % Hentar ut relevant underblokk av matrisa
  Blokk=M(rekke:m,soeyle:n);
  % Rekkeopererer på blokka slik at første søyle får
  % rett struktur
  % Undersøker også om søyla har leiande tal
  [Blokk leiar]=Trappesteg(Blokk,m-rekke+1);
  % Oppdaterer dersom søyla har leiande tal
  if leiar==1
    % Oppdaterer vektor med leiande tal
    LeiarVektor=[LeiarVektor, soeyle];
    % Oppdaterer den store matrisa
    M(rekke:m,soeyle:n)=Blokk;
    % Oppdaterer rekketalet
    rekke=rekke+1;
  end
end
