function M=Bakoverfase(A,LeiarVektor)

% Denne funksjonen tar utgangspunkt i ei matrise på
% trappeform og ein vektor med søylenummera til alle
% leiande tal. Den sørger for at alle leiande tal blir
% éin og alle tal over desse blir null.
% Input: 
% A - matrise på trappeform
% LeiarVektor - vektor med nummeret på leiande søyler
% Elementa i LeiarVektor må komme i stigande rekkefølge.

% Kopierer matrisa og finn formatet
M=A;
[m n]=size(A);

% Bestemmer talet på leiande tal
l=length(LeiarVektor);

% Går gjennom dei leiande tala - nedanfrå
for rekke=l:-1:1  
  soeyle=LeiarVektor(rekke);             % Den aktuelle søyla
  Blokk=M(1:rekke,soeyle:n);             % Hentar ut blokk
  kInv=Blokk(rekke,1);                   % Det leiande talet
  Blokk=GongeRekke(Blokk,1/kInv,rekke);  % Set dette til 1
  % Gjer tala over det leiande talet til null
  for p=1:(rekke-1)
    k=-Blokk(p,1);                       
    Blokk=LeggeTilMult(Blokk,k,rekke,p);
  end
  M(1:rekke,soeyle:n)=Blokk;             % Oppdaterer matrisa    
end
